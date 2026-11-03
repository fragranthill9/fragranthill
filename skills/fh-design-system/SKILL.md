---
name: fh-design-system
description: Visual identity and document pattern for Fragrant Hill Studio deliverables (one-pagers, proposals, diagrams, pitch reports). Use whenever producing an HTML, PDF, slide or diagram for Fragrant Hill so every document shares the same tokens, header, typography and pillar colours.
---

# Fragrant Hill · design system

Fragrant Hill (香山) is an editorial house. Documents should read like a premium business paper, not a startup landing page: calm paper-grey ground, ink text, one seal-red accent, data in tabular figures.

## Tokens (light / dark)
| Token | Light | Dark | Use |
|---|---|---|---|
| --bg | #F4F4F1 | #121416 | page ground |
| --surface | #FFFFFF | #1B1E22 | figures, cards |
| --ink | #16191D | #ECEDE9 | text |
| --ink-2 | #4B5159 | #B9BDC3 | secondary text |
| --muted | #7A808A | #858B94 | labels, captions |
| --line | #DADBD6 | #2E3338 | rules |
| --accent | #B42318 | #E0523F | seal red: eyebrows, key arrows, one highlight |

Pillar colours (validated for colour-blind safety with the dataviz validator, both modes):
| Pillar | Light | Dark | Soft (light / dark) |
|---|---|---|---|
| 1 Editorial | #B42318 | #E0523F | #F8E6E3 / #33201E |
| 2 Advisory | #1D4ED8 | #5B8CFF | #E3EAFB / #1C2740 |
| 3 Community | #0E9F8A | #2BBFA7 | #DDF3EF / #17302C |
| 4 Live & Venues (Encore) | #C2410C | #F0763B | #FAE7DE / #36251B |
| 5 Acceleration | #7C3AED | #A77BFF | #EEE5FB / #2A2238 |

Colour follows the pillar, never the rank. Never cycle extra hues; fold a sixth series into "Other".

## Type
- Display and data: **Archivo** (Google Fonts, weights 400–800). Uppercase labels get `letter-spacing: .1em`.
- Body: **Source Serif 4**, 15px, line-height 1.5, max 65 characters per line.
- Numbers in tables and charts: `font-variant-numeric: tabular-nums`.

## Document header (every one-pager)
Left: 44px square seal with 香山 in accent red, then "FRAGRANT HILL STUDIO" and the sub-line "Editorial house · Stockholm · Europe ↔ China".
Right: "Document N of M · <name>", then "One-pager · v1.0 · <Month Year>".
A 2px ink rule under the header. H1 is the thesis in one sentence (max 20 characters per line wrapped, Archivo 800). A lede of 2–3 sentences in ink-2.

## Charts
Follow the dataviz skill: bars ≤ 24px, 4px rounded data-end, 2px lines, legend for 2+ series, direct labels only on the point that matters, no dual axes, no pies for close values, stat tiles for single numbers. Every figure has a figcaption that states the claim and the source with a [R] reported or [E] estimated flag.

## Diagrams
Inline SVG, `viewBox` sized to content, `currentColor` or tokens for strokes, labelled arrows, one claim per figure. Inputs on the left, core in the middle, outputs on the right; flywheels as a horizontal chain with a return arrow in accent red.

## Files
Each deliverable is its own HTML file in `framework/`, numbered `01-`, `02-`… so one can be edited without touching the others. A Markdown summary of all documents lives in `framework/00-summary.md`.
