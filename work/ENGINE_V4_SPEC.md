# Engine v4: the build spec (2026-11-22)
🌊 Claude proposal, built on `work/RESEARCH_AI_FICTION_SYSTEMS.md` (10 patterns, evidence labelled) and `work/ENGINE_V3.md` (the frame). This is the concrete version: file contracts, gates, budgets and the agent map. Numbers marked **default** are my starting values and are unmeasured. Everything is tested on a gold set before we trust it.

## 1. The seven rules the engine must obey
1. **Typed state is the authority.** Facts live in typed rows with IDs, a chapter stamp and a visibility set. Summaries are derived, never the source.
2. **Commit only after checks.** A scene writes to state only when it has zero blocking violations. A failed scene leaves state untouched (pattern 2).
3. **Scripts count, models judge.** Word counts, cites, names, timelines, IDs and banned terms are scripts that block a stage on failure (pattern 8).
4. **Every scene has a contract.** Pre, Post and Forbid fields, checked before drafting (pattern 3).
5. **Prose is sequential.** Checks run in parallel; drafting never does (pattern 9).
6. **Every stage checkpoints.** A run log says what finished, so a rate limit or crash resumes, not restarts.
7. **Humans gate canon, not sentences.** Patrick sees a checked digest, never raw output.

## 2. The stage line, per story
| # | Stage | Who | Output file | Gate |
|---|---|---|---|---|
| 0 | Commission | commissioner, from `foundry/IDEA_POOL.md` | `brief.md` | Patrick (optional, by autonomy level) |
| 1 | Gap detect | gap-detector + script | `gaps.md` → `world/GAP_QUEUE.md` | none; world gaps wait, story gaps are invented and tagged LOCAL |
| 2 | Plan | slicer, cast, conflicts, scene-carder | `cards.jsonl` (Pre/Post/Forbid, failures per beat, clue plan) | — |
| 3 | Plan check | scripts (IDs, names, timeline) + plan-auditor (motive, power) | `plan_audit.md` | **Gate B**: Patrick approves the one-screen digest |
| 4 | Scene loop (per scene, sequential) | see §3 | `scenes/<id>/` | none, only the commit rule |
| 5 | Chapter polish | word-watch (script + model), dialogue-editor, line-editor, story-guard (diff) | `chapters/<n>/final.md` | none |
| 6 | Read | reader-panel, cold-reader (relative ranking only) | `reads/<n>.md` | a human check before any decision |
| 7 | Digest | orchestrator | `DIGEST.md` (one phone screen) | **Gate C**: Patrick approves; approval triggers the final state commit |

## 3. The scene loop (stage 4), in order
1. **Pre-check (script):** the scene's Pre conditions hold in current state. Fail → back to planning.
2. **Character critic gate (pattern 6):** character-sim proposes each main character's action; a critic accepts or revises. **Cap: 2 revisions (default).** Only accepted actions become state updates.
3. **Draft:** story-writer, from the card, the visibility-filtered context and the pre-flight sheet.
4. **Script gate:** word count, cites, name collisions, banned terms, schema. Fail → repair.
5. **Model checks, in parallel:** sense-checker (does it follow motive), continuity-keeper (against state, five categories, quoting both lines), payoff-keeper (seeds), forecaster (predictability as diagnostic only).
6. **Repair (pattern 7):** the repair spec is fixed: violated constraint, evidence, what to keep, what's forbidden. **Budget: 2 repairs (default).** Still failing → scene rejected, state untouched, flagged in the digest.
7. **Commit (pattern 2):** append the scene's typed facts to state, with IDs, chapter stamp and visibility. Log the commit in the run log.

## 4. The state store (what gets written)
Files under `stories/<slug>/state/`, one JSONL file per type, each row with `id`, `chapter`, `scene`, `visible_to` (a list), `source` (the scene ID that wrote it):
- `entities.jsonl`: people, places, objects, with current status (location, injuries, possessions, money).
- `facts.jsonl`: subject, action, object, chapter (the DOME-style quadruple, pattern 4).
- `knowledge.jsonl`: who knows what, and when they learned it (pattern 5). The "already knows" marker for each character comes from this file.
- `seeds.jsonl`: planted clues and promises, with status (planted, paid, overdue).
- `clocks.jsonl`: travel times, wound timers, the calendar.
- `summary.md`: derived from the rows, never edited by hand.

The world layer (Kernel, Era Bibles) is read-only in every story. Story-only facts go in state, and promotion to the Registry is a separate step, as before.

## 5. The context packet (caching, pattern 1 and cost)
Each agent call is built in a fixed order so the cache hits:
1. **Stable prefix (cached, one breakpoint):** tool definitions, the World Kernel, the era bible, the Taste rubric, the Voice sheet, the Declined list.
2. **Story prefix (cached per story):** the brief, the plan's Pre/Post/Forbid for the current chapter, the entity summary.
3. **Scene payload (not cached):** this scene's card, the visibility-filtered facts for each POV, the last paragraph of verbatim prose.

Rule: never reorder the prefix; never put a timestamp or run ID above the breakpoint. Overnight reader and scan jobs go through the batch interface (half price, results within a day).

## 6. The run runbook
- `stories/<slug>/RUN.md`: one line per stage and scene, with status (done / running / failed), output path and the commit hash.
- On a 429 with `retry-after`: wait that long, then retry. On `ramp_limit_exceeded`: raise usage by at most one step a minute. On `enforced_spend_limit_reached`: halt, checkpoint, and tell Patrick. Do not retry.
- Each stage writes its output before the next starts. A resume reads RUN.md and continues at the first unfinished line.
- Claude commits after every stage, since subagents can't.

## 7. The agent map (existing roles, changed)
| Role | Change in v4 |
|---|---|
| world-slicer | pulls the Kernel and Registry; tags visibility on every fact |
| cast-builder, conflict-mapper | write knowledge rows (who knows what) |
| scene-carder | outputs Pre/Post/Forbid and planned failures per beat |
| plan-auditor | model checks only: motive and power. IDs, names and timeline move to scripts |
| character-sim | becomes the critic gate's proposer (pattern 6) |
| story-writer | sequential; reads the repair spec format |
| sense-checker, continuity-keeper, payoff-keeper, forecaster | run in parallel after the draft; continuity-keeper now writes only through the commit rule |
| dialogue-editor, line-editor | kept as polish passes, but measured against the gold set before trusted |
| story-guard | a script diff plus a model check |
| word-watch | counting in script, tic detection in model |
| reader-panel, cold-reader | relative ranking only; human check before any decision |
| originality-check | kept; no evidence yet for its value, so measure it |
| judge | single rubric call, 0.0–1.0 plus pass/fail (Anthropic's most consistent design) |

## 8. The gold set (how we know anything works)
Before any role is trusted, we measure it:
- **Gold set v1:** Book 1 chapters 1–6, with human labels from you: every real continuity break and every line you'd call a problem. Our past review notes (`work/RECURRING_ISSUES.md`) give the seed list.
- Each checker is run on the gold set. Report its recall and precision, the way ConStory-Bench does. A checker that misses half the planted errors is shown as such, not trusted.
- Repeat after every change to a role.

## 9. Decisions for you (short)
- **D1. Gates:** keep three (Gate B plan, Gate C digest) as above, or add a gate before each commit?
- **D2. Gold set:** will you label Book 1 chapters 1–6 for real breaks, or should I label them and you spot-check?
- **D3. Unit:** first build a short story in one era, to measure the engine end to end?
- **D4. Visibility:** do you want to name the secrets (who must not know what) for the first story, or should the planner propose them for your yes?
- **D5. Budgets:** keep the defaults (2 critic revisions, 2 repairs), or do you prefer one?

## 10. What's still unknown (from the research)
No controlled test of typed state against a plain summary for long-form fiction. No grimdark or tone target. Nothing at novel length (80k+). No reader simulation validated against real readers. The gold set is the only way we'll learn these, so it's the first build step.
