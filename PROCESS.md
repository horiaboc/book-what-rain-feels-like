# Process Log — What Rain Feels Like

Each entry: user prompt → conclusion from that session.

---

**2026-06-08**

*Prompt:* Set up a Telegram daemon to send chapters and collect reader notes via @whatrainbot.

*Conclusion:* Created `tools/telegram_daemon.py` with three subcommands: `get-chat-id`, `daemon` (polls and appends messages to `reader_notes.md`), and `send` (sends text or chapter files). Bot @whatrainbot configured, chat ID set, daemon tested and working end-to-end.

---

**2026-06-09**

*Prompt:* Fix chapter splitting to not break mid-word; auto-start daemon on session open; create process.md for prompt/conclusion log.

*Conclusion:* Splitting now breaks at paragraph boundaries (falls back to word boundaries only for very long paragraphs). Daemon auto-start hook added to project settings. PROCESS.md created and will be maintained going forward.

---

**2026-06-10**

*Prompt:* Resume. Write chapters 14–17 with approved plan. Add Jonas's Heidelberg backstory and Iris's Heerlen backstory (Opa Kees, Oma Ingrid) to the bible. Confirm finger cut and Amsterdam timing.

*Conclusion:* Bible updated — Jonas from Heidelberg (parents Martin and Anke, never appear in the novel), Iris's hometown now Heerlen, Limburg (~30km from Aachen; Opa Kees spoke Dutch, Oma Ingrid German, explains her bilingualism). Finger cut planned for chapter 22; Amsterdam arc chapters 27–30. Chapters 14–17 written: Heerlen (Iris's journalism beat irony + constructed grief for grandparents), June (the off-tempo coin moment; Jonas notices without examining), The Margin (Iris's private list of calibration gaps; first seed of self-doubt), The Cursor (routing anomaly at Merkon seeds moral choice; Jonas tells Iris about the chat; cursor blinks). All four sent to Telegram.

---

**2026-06-12**

*Prompt:* Move memory into git repo for cross-machine portability. Build an init tool so setup on a new machine is automatic.

*Conclusion:* Memory files moved from `~/.claude/projects/.../memory/` into `.claude/memory/` inside the repo (now git-tracked). Original location replaced with a symlink. `tools/init.py` written — detects project root and clone path automatically, creates the correct symlink, handles edge cases safely. CLAUDE.md updated: "init" now triggers the script, "resume" remains the session-resumption command.

---
