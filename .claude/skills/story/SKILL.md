---
name: story
description: The story engine. Turns Patrick's world (the sandbox) into a finished, lived-in story through brief → planning room → scene cards → drafting → revision loop → readers → delivery, with two approval gates for Patrick. Use when Patrick asks for a story, a chapter, a book, or a test run, or says "run the engine".
---

# The story engine

Patrick builds the world; Claude writes the stories. The sandbox is `codex_v5/` plus `decisions/BANK.md`, and the BANK wins where they differ. Never change the world layer. Anything a story invents stays **local to that story** until Patrick promotes it.

Every story lives in `stories/<slug>/`. Commit and push after every stage.

## Speeds
- **Quick:** a short story under about 8k words. Stages 1–5 with one critic round and the cold reader.
- **Full:** a novella or book. Every stage and every pass, run per chapter, then the whole-book passes.

Usage is not a constraint (Patrick, 2026-11-09). Default to Full unless Patrick says otherwise.

## Stage 1: Brief (GATE 1, Patrick approves)
`00_brief.md` covers:
- premise
- where and when in the world (era, place, factions in play)
- POV and tense
- length and speed
- tone
- the shape of the ending (open, bleak, crushed glimmer…)
- what the story is *about* underneath
- which canon it leans on

If Patrick gives only a seed, pitch 3 short briefs, a few lines each, and let him pick. Show Patrick a phone-short version and wait for his yes or tweaks.

## Stage 2: The planning room (agents in this order; each writes its own file)
1. **`world-slicer`** → `01_world_slice.md`: all canon this story touches, quoted with cites, plus the local invention (towns, customs, minor people, ships), each tagged `LOCAL`.
2. **`cast-builder`** → `02_cast.md`: a dossier for every named character covering want, need, wound, lie, line they won't cross, price (what would make them leave), voice, secrets, and a relationship vector to every other main character. It also gives each character's "why they stay" at every point where they could leave.
3. **`conflict-mapper`** → `03_conflict.md`: overlapping interests, every faction's goal in this story, and **what every powerful character is doing offscreen** in each phase, so arrivals and absences have causes.
4. **`scene-carder`** → `04_scene_cards.md`: every scene as a card. The card is either goal / conflict / disaster or reaction / dilemma / decision, with POV, stress level (moment and baseline), value shift, promises set and paid, and who resists whom. Every scene must contain a failure or a hard choice.
5. **`plan-auditor`** → `05_plan_audit.md` covers:
   - canon check
   - the "why doesn't X just…" power audit
   - the cooperation audit (no character complies only because the plot needs them to)
   - the promise/payoff ledger
   - the coincidence audit
   - a cold logic read of the cards

   Fix by sending items back to the relevant planner; loop until clean.

## GATE 2 (Patrick approves the plan)
`DIGEST_plan.md` is one phone screen:
- the story in 5 lines
- the cast in one line each
- the 3–6 decisions Patrick should make, as lettered options with Claude's pick

Bank his answers in `decisions/BANK.md` only if they touch the world. Story-local answers go in `00_brief.md`.

## Stage 3: Drafting
**`story-writer`** writes `drafts/v1.md` chapter by chapter from the cards, the slice, the cast, `work/sample/STYLE_PROFILE.md` and `work/sample/NATURAL_PRINCIPLES.md`. Add a short ledger at the end: canon used, local inventions, unsure points.

## Stage 4: The revision loop (each pass writes a log in `reviews/`; the story-guard runs after every pass that edits)
1. **`dev-critic`** in three modes run in parallel: `lore` (canon), `logic` (motive, cause, power), `craft` (tone, voice, rhythm). Each writes its own report.
2. **`story-writer`** revises against all three, writing `drafts/v2.md` plus a rebuttals file.
3. **`judge`** rules on the disputes and applies the final fixes, writing `drafts/v3.md` and a fight log.
4. **`line-editor`** passes, each one on a new draft version, each followed by the **`story-guard`**:
   - `natural`: rough and human, cutting explanation and conveniences
   - `stress`: texture tracks the stress map, with uneven growth across the story
   - `pressure`: useless detail, wrong temperature, attention slips; then a SELECTIVE CUT keeping only what belongs to the POV's mind
   - `grimdark`: concrete horror, few glimmers, mostly crushed
   - `fog`: fog words, AI-isms, micro-contradictions
5. **`story-guard`** after each `line-editor` pass: the writing may change, the story may not. It reverts anything that changed events, canon or protected lines.
6. **Consistency:** the `story-guard` in `full-read` mode reads the whole draft as one piece.

## Stage 5: Readers
1. **`cold-reader`**: may open ONLY the draft file. It reports where it got lost, unexplained terms, "why doesn't X just…", contradictions, disbelief, boredom, and who it thinks the villain is.
2. A **reverse outline**: the `plan-auditor` compares what each scene actually does with its card.
3. Fix the top findings through the `story-writer` and the `judge`, then the `story-guard` once more.

## Stage 6: Delivery
- `FINAL.md`: the story.
- `DIGEST.md`: one phone screen covering what happens, what's strongest, what's weakest, and Claude's honest verdict.
- `99_inventions.md`: every LOCAL invention (people, places, customs, tech details, names) for Patrick to mark promote / keep local / cut.

Send Patrick `FINAL.md` and `DIGEST.md`. Offer an outside read (Grok or a fresh Claude) using the file.

## Standing craft rules (from the BANK)
- **Grimdark:** bleak, brutal and unforgiving, with few glimmers and those mostly crushed. Horrors are concrete and never titillating.
- **Orcs and victims are people** in the narration.
- **Language:** no AI-isms, no over-spelling, no clinical labels, no real-world ethnic analogies, no skin colour as identity, no "user", no force words in narration.
- **Characters:** they resist the plot. Powerful characters need visible reasons for what they don't do.
- **Jon** is never interpreted by the narrator.
- **Names:** story-local names are allowed, but must be flavored by race, never silly and never generic Earth names. The name engine is still to be built; until then, mark every invented name `LOCAL` in `99_inventions.md`.
