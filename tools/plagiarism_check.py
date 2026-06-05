#!/usr/bin/env python3
"""
Plagiarism check for What Rain Feels Like.

Extracts distinctive 7-word phrases from every chapter and searches for
exact matches online using DuckDuckGo (no API key required, text never
stored anywhere). Skips the project's own GitHub repo in results.

Usage:
    pip install duckduckgo-search
    python3 tools/plagiarism_check.py
"""

import re
import sys
import time
import random
from pathlib import Path


# ── Configuration ────────────────────────────────────────────────────────────

CHAPTERS_DIR = Path(__file__).parent.parent / "chapters"
NGRAM_SIZE   = 7       # words per phrase — distinctive without being too rigid
SAMPLE_EVERY = 8       # take one phrase every N sentences (controls total requests)
DELAY_MIN    = 2.0     # seconds between searches (respect rate limits)
DELAY_MAX    = 4.0
OWN_REPO     = "horiaboc"   # filter our own GitHub from results


# ── Text extraction ───────────────────────────────────────────────────────────

def extract_prose(md_text: str) -> str:
    """Strip markdown structure; return clean prose only."""
    lines = []
    for line in md_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):        # headings
            continue
        if stripped == "---":               # section breaks
            continue
        if stripped.startswith(">"):        # epigraphs / blockquotes
            continue
        if re.match(r"^—\s", stripped):     # attribution lines
            continue
        lines.append(stripped)
    return " ".join(lines)


def split_sentences(text: str) -> list[str]:
    """Rough sentence splitter — good enough for phrase extraction."""
    # Split on . ! ? followed by whitespace or end
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.split()) >= NGRAM_SIZE]


def phrase_from_sentence(sentence: str) -> str | None:
    """Return a 7-word phrase from the middle of a sentence."""
    words = sentence.split()
    if len(words) < NGRAM_SIZE:
        return None
    # Start a third of the way in so we avoid common sentence openers
    start = max(0, len(words) // 3)
    end   = start + NGRAM_SIZE
    if end > len(words):
        start = len(words) - NGRAM_SIZE
        end   = len(words)
    return " ".join(words[start:end])


# ── Search ────────────────────────────────────────────────────────────────────

def phrase_in_snippet(phrase: str, body: str) -> bool:
    """Check whether a meaningful substring of the phrase appears in the body."""
    if not body:
        return False
    phrase_lower = phrase.lower()
    body_lower   = body.lower()
    # Require at least a 5-word contiguous run from the phrase to appear in the snippet
    words = phrase_lower.split()
    for start in range(len(words) - 4):
        subphrase = " ".join(words[start:start + 5])
        if subphrase in body_lower:
            return True
    return False


def search_exact(phrase: str, ddgs) -> list[dict]:
    """Return confirmed matches only: exact phrase must appear in the result snippet."""
    try:
        results = list(ddgs.text(f'"{phrase}"', max_results=5))
        confirmed = []
        for r in results:
            if OWN_REPO in r.get("href", ""):
                continue
            if phrase_in_snippet(phrase, r.get("body", "")):
                confirmed.append(r)
        return confirmed[:3]
    except Exception as exc:
        return [{"href": f"ERROR: {exc}", "title": ""}]


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        sys.exit("duckduckgo-search not installed. Run:  pip install duckduckgo-search")

    print("╔══════════════════════════════════════════════════════╗")
    print("║   What Rain Feels Like — Plagiarism Check            ║")
    print("╚══════════════════════════════════════════════════════╝\n")

    # ── Load chapters ──────────────────────────────────────────────
    chapter_files = sorted(CHAPTERS_DIR.glob("*.md"))
    if not chapter_files:
        sys.exit(f"No chapters found in {CHAPTERS_DIR}")

    all_sentences: list[tuple[str, str]] = []  # (chapter_name, sentence)
    total_words = 0

    print(f"Loading {len(chapter_files)} chapters:\n")
    for cf in chapter_files:
        prose = extract_prose(cf.read_text(encoding="utf-8"))
        sentences = split_sentences(prose)
        word_count = len(prose.split())
        total_words += word_count
        for s in sentences:
            all_sentences.append((cf.stem, s))
        print(f"  {cf.name:<35}  {word_count:>5} words   {len(sentences):>3} sentences")

    print(f"\n  Total: {total_words} words across {len(all_sentences)} sentences\n")

    # ── Sample phrases ─────────────────────────────────────────────
    sampled: list[tuple[str, str]] = []  # (chapter, phrase)
    for i, (chapter, sentence) in enumerate(all_sentences):
        if i % SAMPLE_EVERY != 0:
            continue
        phrase = phrase_from_sentence(sentence)
        if phrase:
            sampled.append((chapter, phrase))

    print(f"Checking {len(sampled)} phrases (one per ~{SAMPLE_EVERY} sentences, "
          f"{NGRAM_SIZE} words each)\n")
    print("─" * 60)

    # ── Search loop ────────────────────────────────────────────────
    matches:  list[dict] = []
    clean:    int = 0
    errors:   int = 0

    with DDGS() as ddgs:
        for idx, (chapter, phrase) in enumerate(sampled, 1):
            print(f"[{idx:>2}/{len(sampled)}]  \"{phrase}\"")
            results = search_exact(phrase, ddgs)

            if not results:
                print(f"         ✓  no match\n")
                clean += 1
            elif any(r["href"].startswith("ERROR") for r in results):
                print(f"         ⚠  search error — {results[0]['href']}\n")
                errors += 1
            else:
                print(f"         ⚠  MATCH  →  {results[0]['href']}")
                print(f"                       {results[0].get('title','')[:70]}\n")
                matches.append({"chapter": chapter, "phrase": phrase, "results": results})

            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

    # ── Report ─────────────────────────────────────────────────────
    print("═" * 60)
    print("FINAL REPORT\n")
    print(f"  Phrases checked :  {len(sampled)}")
    print(f"  Clean           :  {clean}")
    print(f"  Search errors   :  {errors}")
    print(f"  Matches found   :  {len(matches)}")
    print()

    if not matches:
        print("  ✅  No plagiarism detected.")
        print("      No 7-word phrase from the manuscript matched any online source.\n")
    else:
        print("  ⚠️   POTENTIAL MATCHES — review manually:\n")
        for m in matches:
            print(f"  Chapter : {m['chapter']}")
            print(f"  Phrase  : \"{m['phrase']}\"")
            for r in m["results"]:
                print(f"    → {r.get('href','')}")
                print(f"       {r.get('title','')[:80]}")
            print()

    print("  Note: this tool detects verbatim matches only.")
    print("  Style resemblance is not plagiarism and is not measured here.")
    print("═" * 60)


if __name__ == "__main__":
    main()
