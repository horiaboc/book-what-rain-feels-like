---
name: feedback-process-log
description: "User wants process.md maintained — each prompt and conclusion logged there, timestamped"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 20d435f4-fb11-40d6-a0bc-2192e165a43a
---

Maintain `PROCESS.md` in the project root. After each significant exchange, append an entry with:
- The date
- The user's prompt (summarised if long)
- A one-sentence conclusion of what was done or decided

**Why:** User wants a durable log of the writing process and decisions, readable independently of Claude Code transcripts.

**How to apply:** At the end of any session where something meaningful happened (chapter written, tool built, structural decision made), append to process.md before closing.
