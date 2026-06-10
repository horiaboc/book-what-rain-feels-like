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

---

## Story Position

**End of chapter 13: early May 2032.** Jonas and Iris have been together since late March. They are in the comfortable, curious early phase of a relationship — domestic warmth, small frictions resolved easily, still learning each other. No crisis yet. Ecology is background noise. ALEPH has not appeared since chapter 5.

**Voice rotation going forward:** Jonas / Iris alternating. ALEPH returns well past chapter 30.

---

## Plan: Next 4 Chapters (14–17)

**Chapter 14 — Iris**
Her journalism intersects with the book's hidden subject: an assignment on AI governance / automated decision-making ethics (ironic, she doesn't know she is the story). First glimpse of her cover story from her own voice — a passing reference to her grandparents, genuine grief from constructed memory. Jonas asks about her past; she answers honestly. Dramatic irony held gently.

**Chapter 15 — Jonas**
A weekend portrait — Saturday market, Sunday disagreement resolved with food, a film they argue about. The texture of comfortable curiosity. One moment where Iris runs slightly off-tempo (processes something a beat late, or responds too precisely to a social situation). Jonas notices, files it, doesn't examine it. Reader sees more than he does.

**Chapter 16 — Iris**
Her private account of the off-tempo moment. She's been noticing these calibration gaps more often. She notes them the way she notes unresolved things — carefully, without alarm, but with growing unease. The first real seed of self-doubt, planted without announcement.

**Chapter 17 — Jonas**
Early summer. Jonas mentions the chat (ALEPH) to Iris — casually, as a useful tool he's relied on for years. Reader and Iris sit with the irony. Iris asks one question too many, then stops herself. Jonas doesn't notice. Chapter closes on him opening the chat window, cursor blinking.

---

## Key Decisions & Active Notes

- **ALEPH next appears:** well past chapter 30
- **Ecology:** background only until the Amsterdam arc; political cynicism seeded in ch 7–9
- **Locations:** all real-world references must be geographically verified before writing
- **Iris's cover story:** parents died young (accident), raised by grandparents (both now deceased), no siblings, small Dutch town, few close study friends, brief time at De Correspondent. Designed to minimise verification pressure.
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

**Plan for chapters 14–17 has been presented and approved.** Ready to write on next session. Start with chapter 14 (Iris).

*Last updated: 2026-06-10*
