#!/usr/bin/env python3
"""
Telegram daemon for *What Rain Feels Like*.

Subcommands:
  get-chat-id   Print your Telegram chat ID (run once, then paste into .env)
  daemon        Poll for incoming messages and append them to reader_notes.md
  send          Send text or a chapter file as a message (text) or document (file)
"""

import json
import os
import sys
import time
import datetime
import argparse
import string
import random
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent.parent
ENV_FILE = ROOT / ".env"
READER_NOTES = ROOT / "reader_notes.md"


# ---------------------------------------------------------------------------
# .env loader (stdlib only)
# ---------------------------------------------------------------------------

def load_env(path: Path) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip().strip('"').strip("'")
    return env


# ---------------------------------------------------------------------------
# Telegram API helpers
# ---------------------------------------------------------------------------

def api_call(token: str, method: str, payload: dict | None = None) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload or {}).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise RuntimeError(f"Telegram API error {e.code}: {body}") from e


def split_at_paragraphs(text: str, limit: int = 4096) -> list:
    """Split text at paragraph boundaries, never mid-word. Falls back to word boundaries."""
    if len(text) <= limit:
        return [text]
    chunks = []
    current = ""
    for paragraph in text.split("\n\n"):
        block = paragraph + "\n\n"
        if len(current) + len(block) <= limit:
            current += block
        else:
            if current:
                chunks.append(current.rstrip())
            if len(block) > limit:
                # Single paragraph too long — split at word boundary
                words = block.split(" ")
                current = ""
                for word in words:
                    candidate = (current + " " + word) if current else word
                    if len(candidate) <= limit:
                        current = candidate
                    else:
                        chunks.append(current)
                        current = word
            else:
                current = block
    if current.strip():
        chunks.append(current.rstrip())
    return chunks


def send_text(token: str, chat_id: str, text: str, markdown: bool = False) -> None:
    payload_base = {"chat_id": chat_id}
    if markdown:
        payload_base["parse_mode"] = "Markdown"
    for chunk in split_at_paragraphs(text):
        api_call(token, "sendMessage", {**payload_base, "text": chunk})


def send_document(token: str, chat_id: str, file_path: str) -> None:
    path = Path(file_path)
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    boundary = "".join(random.choices(string.ascii_letters + string.digits, k=28))
    file_data = path.read_bytes()

    def field(name: str, value: str) -> bytes:
        return (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
            f"{value}\r\n"
        ).encode()

    body = (
        field("chat_id", chat_id)
        + (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="document"; filename="{path.name}"\r\n'
            f"Content-Type: text/markdown\r\n\r\n"
        ).encode()
        + file_data
        + f"\r\n--{boundary}--\r\n".encode()
    )

    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            result = json.loads(resp.read())
            if not result.get("ok"):
                raise RuntimeError(f"Telegram API error: {result}")
    except urllib.error.HTTPError as e:
        body_err = e.read().decode()
        raise RuntimeError(f"Telegram API error {e.code}: {body_err}") from e


# ---------------------------------------------------------------------------
# Subcommand: get-chat-id
# ---------------------------------------------------------------------------

def cmd_get_chat_id(token: str) -> None:
    print("Waiting for you to send a message to @kucoinmasterbot on Telegram…")
    print("(Open Telegram, find the bot, send any message — even just 'hi')\n")
    offset = None
    while True:
        payload: dict = {"timeout": 30, "allowed_updates": ["message"]}
        if offset is not None:
            payload["offset"] = offset
        result = api_call(token, "getUpdates", payload)
        for update in result.get("result", []):
            offset = update["update_id"] + 1
            msg = update.get("message")
            if msg:
                chat = msg["chat"]
                chat_id = chat["id"]
                name = " ".join(filter(None, [
                    chat.get("first_name"), chat.get("last_name")
                ]))
                username = chat.get("username", "")
                print(f"Chat detected!")
                print(f"  Name    : {name}")
                print(f"  Username: @{username}" if username else "  Username: (none)")
                print(f"  Chat ID : {chat_id}")
                print(f"\nAdd this line to your .env file:")
                print(f"  TELEGRAM_CHAT_ID={chat_id}")
                return


# ---------------------------------------------------------------------------
# Subcommand: daemon
# ---------------------------------------------------------------------------

def append_note(text: str) -> None:
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n---\n**{ts}**\n\n{text}\n"
    with open(READER_NOTES, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[{ts}] Note appended ({len(text)} chars)")


def cmd_daemon(token: str, chat_id: str) -> None:
    print(f"Daemon running. Listening for messages from chat {chat_id}.")
    print(f"Notes will be appended to: {READER_NOTES}")
    print("Ctrl-C to stop.\n")
    offset = None
    while True:
        try:
            payload: dict = {"timeout": 30, "allowed_updates": ["message"]}
            if offset is not None:
                payload["offset"] = offset
            result = api_call(token, "getUpdates", payload)
            for update in result.get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message", {})
                text = msg.get("text", "").strip()
                from_id = str(msg.get("chat", {}).get("id", ""))
                if text and from_id == str(chat_id):
                    append_note(text)
        except KeyboardInterrupt:
            print("\nDaemon stopped.")
            sys.exit(0)
        except Exception as exc:
            print(f"[error] {exc} — retrying in 10s")
            time.sleep(10)


# ---------------------------------------------------------------------------
# Subcommand: send
# ---------------------------------------------------------------------------

def cmd_send(token: str, chat_id: str, text: str | None, file_path: str | None, as_document: bool = False) -> None:
    if file_path:
        if as_document:
            send_document(token, chat_id, file_path)
            print(f"Sent as document: {file_path}")
        else:
            content = Path(file_path).read_text(encoding="utf-8")
            filename = Path(file_path).name
            header = f"— {filename} —\n\n"
            send_text(token, chat_id, header + content)
            print(f"Sent file: {file_path} ({len(content)} chars)")
    elif text:
        send_text(token, chat_id, text)
        print(f"Sent ({len(text)} chars)")
    else:
        content = sys.stdin.read()
        send_text(token, chat_id, content)
        print(f"Sent stdin ({len(content)} chars)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Telegram daemon for What Rain Feels Like",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("get-chat-id", help="Print your chat ID after you send the bot a message")
    sub.add_parser("daemon", help="Poll and append incoming messages to reader_notes.md")

    send_p = sub.add_parser("send", help="Send a message or chapter file")
    grp = send_p.add_mutually_exclusive_group()
    grp.add_argument("text", nargs="?", help="Text to send")
    grp.add_argument("--file", metavar="PATH", help="Path to a chapter file to send as text")
    send_p.add_argument("--document", action="store_true", help="Send --file as a downloadable document instead of text")

    args = parser.parse_args()

    env = load_env(ENV_FILE)
    token = env.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = env.get("TELEGRAM_CHAT_ID", "")

    if not token:
        print("Error: TELEGRAM_BOT_TOKEN missing from .env")
        sys.exit(1)

    if args.cmd == "get-chat-id":
        cmd_get_chat_id(token)

    elif args.cmd == "daemon":
        if not chat_id:
            print("Error: TELEGRAM_CHAT_ID not set. Run: python3 tools/telegram_daemon.py get-chat-id")
            sys.exit(1)
        cmd_daemon(token, chat_id)

    elif args.cmd == "send":
        if not chat_id:
            print("Error: TELEGRAM_CHAT_ID not set. Run: python3 tools/telegram_daemon.py get-chat-id")
            sys.exit(1)
        cmd_send(token, chat_id, args.text, args.file, as_document=args.document)


if __name__ == "__main__":
    main()
