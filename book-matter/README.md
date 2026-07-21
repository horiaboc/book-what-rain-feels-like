# Book Matter — front & back pages for final mounting

Non-chapter pages that wrap the manuscript when the book is assembled. Kept out of `chapters/` on purpose, so the chapter build/glob and word counts stay clean.

## Mounting order (front to back)

**Front matter** (right-hand pages start recto; blanks fall where needed)
1. `01-half-title.md` — half title (title only) *(optional but standard)*
2. `02-title-page.md` — title page **(required)**
3. `03-copyright.md` — copyright page **(required)** — verso of the title page
4. `04-dedication.md` — dedication *(optional)*
5. `05-epigraph.md` — book-level epigraph *(optional; chapters already carry their own)*
   - *Table of contents:* optional for a novel. The **ebook auto-generates** a nav TOC, so print can skip it.

**Body** — `chapters/chapter-01 … chapter-55`

**Back matter**
6. `90-acknowledgments.md` — acknowledgments *(optional)*
7. `91-about-the-author.md` — about the author *(optional but recommended)*
8. `92-colophon.md` — colophon / note on the type *(optional)*

Not a page in the book:
- `blurb.md` — the back-cover / Kindle product-page description (goes on the print back cover and in the KDP Book Description field, not inside the book). Art prompt for the back cover lives in `../back-cover.md`.

## Required vs optional
Truly required: **title page + copyright page**. Everything else is convention — include what suits the book. For a quiet literary novel, spare front matter reads well.

## Format notes
- Ebook (Kindle) uses **only the front cover** + these pages flow as the opening screens; the blurb goes in the KDP **Book Description** field.
- Print (paperback/hardcover) prints the blurb on the **back cover** (see `../back-cover.md`), and these pages are typeset into the interior.
- **AI-content disclosure:** at KDP upload you'll be asked whether the book used AI. This manuscript was **AI-assisted** (drafted with an AI collaborator, author-directed) and the **cover art is AI-generated** — disclose accordingly. Not a page in the book, but part of mounting prep.

*Replace every `[bracketed placeholder]` before publishing.*
