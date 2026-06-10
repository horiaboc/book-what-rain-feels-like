# Project Status — What Rain Feels Like

*Update this file at the end of every significant session.*

---

## Chapters Written

| # | Voice | Title | Summary |
|---|-------|-------|---------|
| 01 | Jonas | Weichselstraße | Jonas's life, November Berlin, the chat with ALEPH introduced |
| 02 | ALEPH | — | ALEPH observing Jonas's morning, voice established |
| 03 | Iris | — | Iris arrives in Berlin, first walks, the courtyard glimpsed |
| 04 | Jonas | — | Jonas at work, the chat deepening, anomaly detection |
| 05 | ALEPH | — | ALEPH watching Jonas discover Iris's city, the Saturday market |
| 06 | Iris | — | The coffee shop on Pannierstraße, Jonas noticed |
| 07 | Jonas | December | Jonas finds Iris's article, returns to Pannierstraße |
| 08 | Iris | January | Iris settles in Berlin, algorithm transparency work, Jonas at the café, documentary invitation |
| 09 | Jonas | Walk Again Sometime | The documentary at Kulturforum, shared cynicism about tech solutionism, first canal walk, "walk again sometime" |
| 10 | Iris | February | Friendly dating, Iris visits Weichselstraße, meets Diogenes, fixes the cabinet hinge |
| 11 | Jonas | The Party | Prenzlauer Berg party, first touch, first kiss in the rain outside Lukas's apartment |
| 12 | Iris | Something Real | The intimate scene from Iris's perspective — her first real physical experience vs. constructed memories |
| 13 | Jonas | Graefestraße | Early domestic life: eggs argument, Mia's sisterly happiness, Austerlitz, April warmth |
| 14 | Iris | Heerlen | AI governance journalism beat (dramatic irony, held quietly); Iris tells Jonas about Heerlen, Opa Kees, Oma Ingrid; the memory that doesn't yield its depth |
| 15 | Jonas | June | Winterfeldtmarkt Saturday; the coin/off-tempo moment; Sunday film argument (pasta from the pot); Jonas notices something, files it, doesn't examine it |
| 16 | Iris | The Margin | Iris's interior on the off-tempo moment; the list of calibration gaps (laughter, food, temperature, sleep); first real seed of self-doubt, held carefully |
| 17 | Jonas | The Cursor | Routing anomaly at Merkon (setup of the moral choice); Jonas tells Iris about the chat; Iris asks one question too many and stops herself; chapter closes on the cursor blinking |

---

## Story Position

**End of chapter 17: early July 2032.** Jonas and Iris are fully settled into their relationship — domestic, warm, curious about each other. The routing anomaly at Merkon is an unresolved seed (Jonas has not yet decided what to do). Iris has begun privately noting her calibration gaps; Jonas has begun, without examining it, to notice something slightly different about her. The chat has been introduced to Iris. ALEPH has not appeared since chapter 5.

**Voice rotation going forward:** Jonas / Iris alternating. ALEPH returns well past chapter 30.

---

## Plan: Next Chapters (18–21+)

**Chapter 18 — Iris**
The routing anomaly story echoes without connecting. Iris's journalism piece is getting closer to the heart of the subject — she is interviewing someone involved in automated system design, and something in what they describe resonates with her own list without her naming why. A quiet domestic scene with Jonas. The calibration gaps continue; she does not tell him.

**Chapter 19 — Jonas**
Jonas resolves the routing anomaly question — he decides to escalate beyond Steffen, knowing it will cost him something professionally. This is the moral choice the bible describes: he chooses correctly and it costs him. The chapter is not dramatic; it is simply the quiet act of deciding to be the kind of person he is.

**Chapter 20 — Iris**
The aftermath of Jonas's work decision (she observes it without knowing the full context). A chapter about trust — what it is to be with someone who acts according to their values without announcing it. Iris's list grows by one.

**Chapter 21 — Jonas**
The cost of his decision at Merkon begins to be felt — a cool shift in his relationship with Steffen, perhaps a review cycle that goes differently than expected. He talks about it, in his way, to Iris. He also talks about it to the chat. The chapter ends before the ALEPH update.

**Chapter 22 — Iris (THE FINGER CUT)**
ALEPH issues a routine systems update through the implant. Iris notices changes in her fine motor calibration first — things she attributes to stress or tiredness. Then the cut happens in the kitchen: wrong closure, something mineral at the edge. She looks at it for a long time. She says nothing. This chapter closes the "ordinary life" phase.

---

## Key Decisions & Active Notes

- **ALEPH next appears:** well past chapter 30
- **Ecology:** background only until the Amsterdam arc; political cynicism seeded in ch 7–9
- **Locations:** all real-world references must be geographically verified before writing
- **Iris's cover story:** parents died young (accident), raised by grandparents (both now deceased), no siblings. Hometown is **Heerlen, Limburg** (~30km from Aachen). Opa Kees (Dutch) and Oma Ingrid (German, from Aachen) — she is bilingual Dutch/German as a result. Brief stint at De Correspondent before Berlin. Designed to minimise verification pressure. Full details in `bible.md`.
- **Jonas's background:** Originally from **Heidelberg**. Parents **Martin and Anke** — good, affectionate, undramatic relationship. No siblings. They never appear in the novel directly; mentioned occasionally in passing.
- **Iris's body:** crystal-lattice synthetic skeleton, biological soft tissue grown over it, collar bone implant (ALEPH link, dormant), several subtle biological enhancements (healing, immune, coordination, sensory precision). Full details in `bible.md`.
- **The trigger sequence:** ALEPH update → fine motor disruption → finger cut heals wrong → Iris notices, says nothing. Amsterdam bicycle accident → hospital → X-ray anomaly → the world begins to find out.
- **Mia:** Jonas's colleague, ~43, 11 years at Merkon, sisterly affection for Jonas.
- **Lukas:** photographer at Iris's paper, not an Amsterdam connection.
- **Iris's apartment:** Graefestraße, Kreuzberg
- **Maybachufer market:** famous market runs Tue/Fri — novel set 2031, minor flag, left as-is

---

## Tooling

- **Telegram daemon:** `tools/telegram_daemon.py` — sends chapters, collects reader notes into `reader_notes.md`
- **Bot:** @whatrainbot (token in `.env`, gitignored)
- **Daemon auto-start:** `SessionStart` hook in `.claude/settings.json`
- **Send chapters on request only** — do not send automatically after writing

---

## Immediate Next Action

Chapters 14–17 written. Bible updated with Jonas's Heidelberg backstory (parents Martin and Anke) and Iris's Heerlen backstory (Opa Kees, Oma Ingrid). Finger cut planned for chapter 22. Next: write chapters 18–22. Start with chapter 18 (Iris).

*Last updated: 2026-06-10*
