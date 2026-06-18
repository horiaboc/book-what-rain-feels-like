# Claude Project Initialisation — Memory & Session Log Architecture

This document describes how to set up a Claude Code project so that all
persistent memory and session logs live inside the git repository, are
tracked by git, and are portable across machines. Any Claude session can
execute these steps by adapting the paths to the current project.

---

## Architecture

```
<project-root>/
  .claude/
    memory/
      MEMORY.md              ← index of all memory files (auto-loaded by Claude Code)
      *.md                   ← individual memory files (user, feedback, project, reference)
      logs/
        .gitkeep             ← keeps the directory tracked on fresh clones
        YYYY-MM-DD_HHMMSS.md ← one session log per session, created at session start
    settings.json            ← Claude Code project settings (hooks, permissions, etc.)

~/.claude/
  projects/
    <encoded-project-path>/  ← path with every / replaced by -
      memory/                ← SYMLINK → <project-root>/.claude/memory/
```

The symlink is the only thing that does not live in the repo. Everything else
does. On a new machine, the symlink must be recreated — that is the only setup
step required.

---

## Setup steps (execute on a new machine or after moving the project)

### 1. Identify paths

- `PROJECT_ROOT` — absolute path to the project folder (e.g. `/Users/alice/workspace/my-novel`)
- `MEMORY_SOURCE` — `<PROJECT_ROOT>/.claude/memory`
- `ENCODED` — `PROJECT_ROOT` with every `/` replaced by `-` (e.g. `-Users-alice-workspace-my-novel`)
- `TARGET_DIR` — `~/.claude/projects/<ENCODED>`
- `TARGET_LINK` — `<TARGET_DIR>/memory`

### 2. Ensure the memory directory exists in the repo

If `.claude/memory/` does not exist, create it and add a `MEMORY.md` index file.
If `.claude/memory/logs/` does not exist, create it and add a `.gitkeep` file.

### 3. Create the Claude project directory

Create `TARGET_DIR` if it does not exist.

### 4. Create the symlink

Check whether `TARGET_LINK` already exists:

- If it is a symlink pointing to `MEMORY_SOURCE` → nothing to do, already correct.
- If it is a symlink pointing elsewhere → remove it, then create a new one pointing to `MEMORY_SOURCE`.
- If it is a real directory → stop and warn the user; do not overwrite (it may contain data).
- If it does not exist → create it: `ln -s <MEMORY_SOURCE> <TARGET_LINK>`

### 5. Verify

Confirm the symlink resolves correctly by listing the contents of `TARGET_LINK`
and checking that `MEMORY.md` is visible.

---

## Session log protocol

One log file is created per session in `<project-root>/.claude/memory/logs/`,
named by session start time: `YYYY-MM-DD_HHMMSS.md`. Files sort chronologically.

**What to log:** decisions made, files changed, structural choices, open questions
carried to the next session. Compress — not every exchange, only what matters
across sessions.

**When to write:**
- Session start: create the file immediately
- During session: update when something meaningful happens, or when the user says "update work" or "save work"
- Session end: write a final summary when the user says "I'm exiting", "save work", or equivalent

**On resume:** read `STATUS.md` (if present), all memory files, and the most
recent session log. Then create a new session log for the current session.

---

## Adapting to a new project

This architecture is project-agnostic. To apply it to a new project:

1. Create `.claude/memory/` and `.claude/memory/logs/` inside the project repo
2. Add a `MEMORY.md` index file (can start empty)
3. Add a `CLAUDE.md` at the project root documenting the resume and session log protocol (see this project's `CLAUDE.md` as a template)
4. Run the setup steps above to create the symlink
5. Start a session and create the first session log

The Python script `tools/init.py` in this project automates steps 1–4 for this
specific project, but is not required — Claude can execute the steps directly.
