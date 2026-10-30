---
name: interview-episode-prep
description: Prepare a Fragrant Hill Studio interview or documentary episode about a company, event or founder. Use when Lan asks for interview questions, a shooting plan, a script, or a brief to explain a Chinese company or technology to a Western audience. Produces three separate deliverables (brief, shooting plan, script and questions) in interviews/ and, when a doc tool is available, a Claude Doc with three tabs.
---

# Interview episode prep

Lan hosts and directs. The output must let a reader who did not watch the research understand the company, the hook for a Western audience, and exactly what to ask on camera.

## Method, in order

1. **Research fan-out first.** Launch three parallel research agents before writing anything: (a) the company itself, in English and Chinese, including legal names, founders, events held, numbers claimed, partners; (b) the global landscape and the underlying technology, with a verdict on "first" claims; (c) the format reference Lan names (for example a Circuit episode), with episode facts, structure and verbatim questions where available. Agents write raw notes with URLs to the scratchpad; copy the notes into `interviews/research/`.
2. **Separate the three deliverables.** Brief (what it is, tech, landscape, story, assessment of any supplied question list, checklist). Shooting plan (format, rundown, shoot days, shot list, crew and gear, graphics, deliverables). Script and questions (how to use, cold open and narration, one section per interviewee, rapid-fire, closers, must-get lines). Lan reads and practises the script; it must contain no production logistics.
3. **Question format.** Numbered. Bold label, then the English question in quotes, then the Chinese version on its own line, then one line "Why:". Questions under 20 words. Every camera question must produce a story, a number, a demonstration or an admission; otherwise it belongs in a workshop memo, not on camera.
4. **Borrowed methods to cite by name.** Emily Chang (place and origin first, one yardstick question, the critic's question asked kindly, rapid-fire close); Chris Voss (label, then ask); Terry Gross and Cal Fussman (the specific day, race, number); Pyramid Principle for the brief's lead sentences.
5. **Honest sparring.** Say plainly which supplied questions to keep, reframe or cut, and why. Flag claims that would fail a fact-check ("first in the world") and replace them with checkable ones.
6. **Numbers.** Label every figure as company claim, public literature or physics, and say which. Never put a number in narration that an interviewee has not said on camera; use brackets.
7. **Bilingual on-camera rule.** Ask in whichever language gets the better answer; a fluent long answer in Chinese beats a careful short one in English.
8. **Files.** `interviews/<slug>-brief.md`, `interviews/<slug>-shooting-plan.md`, `interviews/<slug>-script-and-questions.md`, `interviews/research/<slug>-*.md`. Commit on the designated branch.
9. **Chat reply.** Short. End with the "Your English" section correcting Lan's original message, per the master prompt.

## Example of the house format

Brief: `interviews/hura-gp-brief.md`. Shooting plan: `interviews/hura-gp-shooting-plan.md`. Script: `interviews/hura-gp-script-and-questions.md`.
