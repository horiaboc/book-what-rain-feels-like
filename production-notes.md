# Production Notes — Formats, Ebooks & Audiobook

Reference for turning the finished manuscript into distributable formats. Numbers are for the current draft: **78,577 words ≈ ~450,000 characters ≈ ~8.5 finished audio-hours**.

Build scripts live in the session scratchpad during a run; the outputs (`*.pdf`, `*.epub`, `*.azw3`) are git-ignored build artifacts, regenerated on demand.

---

## Ebook formats

| Format | File | Reads on | How it's built |
|---|---|---|---|
| **EPUB** | `What-Rain-Feels-Like.epub` | Apple Books (native); the source for Kindle via Send-to-Kindle | Hand-rolled EPUB3 (Python, no deps): 55 chapters + cover + TOC, real א glyph |
| **AZW3** | `What-Rain-Feels-Like.azw3` | e-ink Kindle over USB; Kindle for PC/Mac | `ebook-convert in.epub out.azw3 --output-profile kindle_pw3` (calibre 9.2.1, installed on monkey) |
| **PDF (A4 draft)** | `What-Rain-Feels-Like_DRAFT-A4.pdf` | print, 2-up | Hand-rolled PDF (Times core fonts, cover embedded) |

### Kindle: how a personal book actually gets there
Amazon's own path for personal manuscripts is **Send to Kindle** (send-to-kindle.amazon.com, or email to your @kindle.com address). **Upload the EPUB, not the AZW3** — Amazon converts the EPUB to its proprietary format server-side, and it then appears in the Kindle app and on devices as a native Kindle book (fonts, layout, reading-position sync). The AZW3 file is only for sideloading an e-ink Kindle by cable, or Kindle for PC/Mac. The mobile Kindle **app cannot import AZW3 directly** — that's why EPUB→Send-to-Kindle is the route for phones/tablets.

Apple Books: open/AirDrop the **EPUB** — native, and the א renders as a real glyph.

---

## Audiobook

### Whispersync (ebook↔audio position sync)
Only exists for **Kindle-store + Audible purchases**. No personal-document format (EPUB/AZW3 included) can get it. Workaround for a personal audiobook: **one MP3 per chapter** so finding your place is trivial.

### Single vs multi-voice — the industry norm
- **~85–90% of audiobooks are single-narrator**: one reader performs everyone via subtle pitch/accent/pace shifts. Most cohesive; what listeners expect.
- **Dual / "duet" narration** (a male + female voice splitting alternating first-person POVs) is standard in romance/YA — and *fits this book's Jonas/Iris/ALEPH structure*, so it's a legitimate, non-weird choice here.
- **Full cast** (every speaking character voiced) is rare, drifts toward audio-drama, and is a lot more production work.

Voices this book would need (by narrator): **Jonas** 23ch (male, British, warm, 30s), **Iris** 19ch (female, British, mid-20s), **ALEPH** 5ch (*neither male nor female* per bible — hardest to cast), **Conrad** 3ch (male, older, 60s), **Mara** 2ch (female, cooler than Iris), **neutral+article** 3ch (plain narrator). → ~5–6 distinct voices.

### Can AI do the professional intonation-based character differentiation?
Not automatically — standard TTS reads everything in one register. But the top engines are **steerable/directable**:
- **ElevenLabs v3** — inline **audio tags** (`[whispers]`, `[sighs]`, emphasis) change delivery per line; best expressive long-form.
- **OpenAI `gpt-4o-mini-tts`** — **plain-English style instructions** per passage ("warm, dry, older man"); one base voice bends into characters.
- **Azure** — preset speaking styles (calm/sad/cheerful/whispering) via markup.

The real workflow = a **"direction" pass**: mark up dialogue/emotion per passage, then render. Model supplies the voice; you supply the acting notes. Gets impressively close line-by-line; still short of a top human narrator sustaining a cast over hours.

### AI TTS quality & cost — for THIS book (~450k chars)
| Engine | Quality | Whole-book cost |
|---|---|---|
| **ElevenLabs** (v3) | **Best** intonation; British voices; androgynous option for ALEPH; multilingual keeps one voice identity across ~30 languages (good for future translations) | ~**$99** (one month Pro ≈ 500k credits, then cancel) |
| **OpenAI** `gpt-4o-mini-tts` | Very good; instructable per-passage | ~**$7–15** |
| **Azure** neural | Good; many en-GB voices; less "acting" | ~**$7, often effectively free** (Azure grants ~500k chars/month free) |

**Recommendation:** best single-narrator = **ElevenLabs** (~$99 one-off). Value pick = **OpenAI ~$10**. Near-free = **Azure**. Test voices in-browser before buying: ElevenLabs Voice Library, Azure Speech Studio, OpenAI playground.

### Real human narrator — for THIS book (~8.5 finished hrs)
Priced per finished hour (PFH):
- Budget/newer pro (~$150/hr): **~$1,300**
- Solid professional (~$300–400/hr): **~$2,500–3,400**
- Top-tier/name ($600–1,000+/hr): **~$5,000–8,500**
- **$0 upfront option:** ACX **royalty-share** — narrator takes a cut of sales instead of a fee.

**Bottom line:** whole book AI-narrated = **free to ~$100** one-time; a good human narrator = **~$1,300–3,500**. Common path for a debut: start with AI, commission a human only if the book finds an audience.

### Free pipeline (proven on monkey)
- **Piper** (local, free forever): `en_US-lessac-medium` (flat/robotic), `en_GB-cori-high` (warmer British). Slow (~book = ~19h compute).
- **edge-tts** (free MS neural, needs network; installed in a scratchpad venv): `en-GB-SoniaNeural` etc. — much more natural; whole book ≈ ~2h compute, $0. Best free option for a draft audiobook.
- Encode WAV→MP3 with `ffmpeg` (present). Delivered ch01 samples in lessac, Sonia, Cori.

---

## Editor deliverable
- **DOCX** (`What-Rain-Feels-Like_EDITOR.docx`) — standard manuscript format (cover on page 1, 12pt Times New Roman, double-spaced, chapters on new pages), for Word Track Changes/comments or Google Docs (upload → open as Google Doc → Suggesting mode). Built hand-rolled from the chapters.
- A4 draft PDF also exists for print markup (2-up).

*Last updated: 2026-07-19*

## Author name (decided)
Publish as the mononym **`_horia`** — stylized with a leading underscore, echoing the book's cursor motif (ch23 `_`). Underscore is a **cover/art treatment**; retail metadata registers as **Horia** (searchable); legal name only on the copyright page. Stays `_horia` across all languages/marketplaces. See `back-cover.md`, `book-matter/`.
