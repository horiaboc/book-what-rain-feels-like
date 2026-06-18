#!/usr/bin/env python3
"""
One-time setup for a Claude Code project on a new machine.

## Memory architecture

All persistent memory lives inside the repo at .claude/memory/ and is
tracked by git — making it portable across machines and sessions.

  .claude/memory/
    MEMORY.md                  — index of all memory files (auto-loaded by Claude)
    *.md                       — individual memory files (user, feedback, project, reference)
    logs/
      YYYY-MM-DD_HHMMSS.md    — one session log per session, timestamped

Claude Code expects memory at:
  ~/.claude/projects/<encoded-project-path>/memory/

This script creates a symlink from that location to the real directory in
the repo, so Claude Code finds the files without them leaving the repo.

## Session logs

Claude creates one log file per session in .claude/memory/logs/ at session
start, named by timestamp (sortable). During the session Claude writes
relevant decisions, changes, and context to that file. The user can trigger
a flush by saying "update work" or "save work". Before exiting the user says
"I'm exiting" (or equivalent) and Claude writes a final summary.

On "resume", Claude reads STATUS.md + memory files + the most recent session
log to reconstruct context, then creates a new session log.

## Usage

  python3 tools/init.py          # safe — reports conflicts without overwriting
  python3 tools/init.py --force  # replaces a wrong symlink automatically
"""

import os
import sys
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Set up Claude Code memory symlink.")
    parser.add_argument("--force", action="store_true", help="Replace a wrong symlink without prompting.")
    args = parser.parse_args()

    # Resolve project root (parent of tools/)
    project_root = Path(__file__).parent.parent.resolve()
    memory_source = project_root / ".claude" / "memory"

    if not memory_source.exists():
        print(f"ERROR: memory directory not found at:\n  {memory_source}")
        print("Make sure you have cloned the full repository.")
        sys.exit(1)

    # Ensure logs/ directory exists inside memory
    logs_dir = memory_source / "logs"
    logs_dir.mkdir(exist_ok=True)
    print(f"Logs directory: {logs_dir} (ok)")

    # Claude Code encodes the project path by replacing every / with -
    # e.g. /Users/foo/projects/mybook -> -Users-foo-projects-mybook
    encoded = str(project_root).replace("/", "-")
    target_dir = Path.home() / ".claude" / "projects" / encoded
    target_link = target_dir / "memory"

    print(f"Project root : {project_root}")
    print(f"Memory source: {memory_source}")
    print(f"Symlink target: {target_link}")
    print()

    # Create the ~/.claude/projects/<encoded>/ directory if needed
    target_dir.mkdir(parents=True, exist_ok=True)

    # Case 1: symlink already exists and is correct
    if target_link.is_symlink():
        current_dest = target_link.resolve()
        if current_dest == memory_source:
            print("Memory symlink is already correct — nothing to do.")
            print("You can say 'resume' to pick up where you left off.")
            return
        else:
            print(f"A symlink exists but points to the wrong location:")
            print(f"  Found : {current_dest}")
            print(f"  Wanted: {memory_source}")
            if args.force:
                target_link.unlink()
                print("Removed wrong symlink (--force).")
            else:
                print("Run with --force to replace it.")
                sys.exit(1)

    # Case 2: a real directory exists (not a symlink) — don't touch it
    elif target_link.exists():
        print(f"ERROR: a real directory exists at {target_link}")
        print("It may contain memory from a previous session.")
        print("Move or remove it manually, then run this script again.")
        sys.exit(1)

    # Case 3: nothing there — create symlink
    target_link.symlink_to(memory_source)
    print(f"Symlink created:")
    print(f"  {target_link}")
    print(f"  -> {memory_source}")
    print()
    print("Setup complete. You can say 'resume' to pick up where you left off.")


if __name__ == "__main__":
    main()
