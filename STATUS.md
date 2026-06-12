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
| 18 | Iris | Accountability | Reinhardt interview (legibility never a design criterion — irony held quietly); Jonas tells Iris he is escalating the anomaly; she watches him decide to be who he is |
| 19 | Jonas | Tuesday | Jonas sends the email; meeting with Thomas Würfel; fired quietly with two months' pay; tells Iris over dinner; steadied rather than consoled; opens the chat to tell it what happened |
| 20 | Jonas | August | First week of freedom; Mia and parents (Heidelberg); Iris proposes Amsterdam assignment; Airbnb on the Bloemgracht; she describes her student Amsterdam — precise, slightly too organized |
| 21 | Iris | What You Remember | One week before departure; reaches for Amsterdam memory, finds it flat; packing scene; "you arrive, and then you remember" |
| 22 | Iris | Bloemgracht | Amsterdam — arrival, Algorithm Register interview (De Vries), Waag interview (Leonie); walking discrepancies (wrong canal turning); cooking stamppot, the cut; she looks at it alone, says nothing |
| 23 | — | — | Bloemgracht at 2:14am; neutral voice; two people sleeping; the light signal sequence; undisturbed; gone |

---

## Story Position

**End of chapter 23: late August 2032, night two of Amsterdam stay.** The signal has been sent. Iris carries the knowledge of the cut privately. The ordinary-life phase is over. What follows is the unravelling.

**Voice rotation going forward:** Jonas / Iris alternating. Chapter 23 was neutral/ALEPH. ALEPH's named voice returns well past chapter 30.

---

## Plan: Amsterdam Continuation (chapters 24+)

The bicycle accident and hospital revelation follow. Three possible directions for what triggers the public unravelling — to be decided with the user:

**Option A — The journalist thread:** Iris's piece on Amsterdam's Algorithm Register accidentally surfaces data touching her own documentation trail — a record in the municipal system that shouldn't exist, or an anomaly in how certain identity records were created. Her story becomes her story about herself.

**Option B — The recognition:** One of Iris's interview subjects recognizes her — not from journalism, from somewhere they can't place. The encounter is brief and unresolved, but it lodges in both of them.

**Option C — Jonas the engineer:** After the bicycle accident and the hospital revelation, Jonas — unemployed, skilled, with time — begins pulling the infrastructure thread himself. The same forensic instinct that found the routing anomaly turns toward the question of how Iris was built. The moral-choice engineer becomes the investigator.

---

## End of Story (confirmed)

In the final act, ALEPH and Jonas have their dialogue — Jonas now knows what the chat is, and what Iris is, and what ALEPH did. In that dialogue, ALEPH advises Jonas to apply at a specific institute or company in Berlin — a place where his abilities and the ideas that got him fired at Merkon can actually be put to work. What cost him his job becomes the thing that launches him somewhere better. The ending is open but optimistic.

---

## Key Decisions & Active Notes

- **Jonas fired from Merkon:** escalated the routing anomaly past Steffen → meeting with Thomas Würfel → let go with two months' severance. Framed as "restructuring." He is fine with it. This is the moral choice the bible described.
- **Thomas Würfel:** Director of Operations at Merkon. The person who delivers the firing. Civil, careful, not unkind.
- **End-of-story job:** ALEPH advises Jonas (in their final dialogue) to apply at a specific Berlin institute/company where his ideas and ethics can be put to real use. TBD which institution — decide closer to that arc.
- **Amsterdam trip:** Triggered by Iris's journalism assignment (Dutch civic AI governance piece). Jonas joins because he is now free. Travel planning in chapter 20.
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

Chapters 20–23 written. Amsterdam arc underway. Finger cut in ch22; ALEPH signal in ch23 (neutral voice, no chapter title). Next: decide direction for ch24+ (three options in plan section above).

*Last updated: 2026-06-12*
