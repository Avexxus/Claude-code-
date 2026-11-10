# Handoff: read this at the start of a new session

*Last updated 2026-11-09. This file is the bridge between sessions: everything important is in the repo, and this says where.*

## Who does what
- **Patrick is the world-builder.** He owns the world layer: `codex_v5/` plus `decisions/BANK.md`.
- **Claude is the story engine.** It writes the stories inside that sandbox, with heavy creative freedom (BANK 2026-11-09).
- Patrick works from his phone. Keep replies short and scannable, with lettered choices and Claude's pick. Give short digests and never expect him to reread full drafts.

## Read in this order
1. `CLAUDE.md`: the house rules and workflows.
2. `decisions/BANK.md`: **about 75 rulings since Oct 31 that override the codex.** Not yet written into `codex_v5/`, because passes are rare and happen at milestones. Includes the character layer: Derrek's love for Jon and the altar of his name, the Queen as Lilith, the private parable lens, and the bond as a sensory organ.
3. `notes/00_MASTER_BRIEF.md`: a summary of the codex (it predates the BANK, so the BANK wins).
4. `.claude/skills/story/SKILL.md`: the engine pipeline.

## Where things stand
- **The story engine is built:** the `story` skill plus 11 agents in `.claude/agents/`.
- **The first engine run is in progress:** `stories/book1-emperors-son/`. It re-plans Book 1, with `work/sample/SAMPLE_BOOK1_v10.md` as the spine.
  - ✅ `00_brief.md`: it lists the 10 problems this run must fix.
  - ✅ `01_world_slice.md`: includes ORIENTATION, LOCAL inventions and TRIPWIRES.
  - ✅ `02_cast.md`: 13 dossiers. **Note the override at the top:** the dark elf can't feel the drow blade.
  - ✅ `03_conflict.md`: done (Tower staging pick B, bond override applied; 6 questions in §9). Slice and cast updated to the override.
  - ✅ `04_scene_cards.md`: 50 scenes, 9 chapters, ~25k target; 91-promise ledger; 18 Gate 2 questions.
  - ✅ `05_plan_audit.md`: round 2 CLEAN; the R2 one-line fixes are applied
  - ✅ GATE 2 answered "1b 2b 3a 4b 5c 6b" (in 00_brief). Re-plan done; plan audit round 3 fixes applied. God identity pending with Patrick (drafting with pick A, a giant who became a god).
  - ✅ Stage 3: `drafts/v1.md` (22.6k words, with ledgers) and `drafts/v1_STORY_ONLY.md` (story only: give THIS to outside readers, never the notes; Patrick 2026-11-10). Ch 1–6 were drafted on the old model, 7–9 on the new: Patrick may ask an outside reader, blind, whether the style changes anywhere.
  - ✅ v1 critics done (`reviews/v1_*.md`); outside reads in `reviews/outside/`. Patrick then asked for the door as a rift, no quest markers, and GRIT. `06_v2_replan.md` holds the re-plan (overrides 02/03/04): Teo holds the rift; narration calls her "the hill woman"; fix list; grit brief.
  - ⏳ Second draft in 4 batches: drafts/v2_part1.md (ch 1–3), part2 (4–5), part3 (6), part4 (7–9); each ends with a "<!-- LEDGER -->" line then notes. Join into v2.md and v2_STORY_ONLY.md. Then judge, line passes, guard, cold reader.

## Open questions waiting on Patrick
- Where the "Jon's mind was clear for the first time in a very long time" line goes. Claude's pick: show it from outside in Book 1 and give the inner line to the later window book.
- `decisions/QUESTIONS.md`: the older master question list. Partly superseded by the BANK.
- The tech questions in `work/ideas/tech_*.md` (minds and industry A–H, bodies, space travel, war, daily life) were never answered.
- The name engine is to be built later: race-flavored names, nothing silly, no generic Earth names.
- The full PASS that writes the BANK into the codex: Patrick calls it at a milestone.

## Key reference files
- **Voice and craft:** `work/sample/STYLE_PROFILE.md`, `work/sample/NATURAL_PRINCIPLES.md` and `work/PRO_METHODS.md` (how others use AI for fiction).
- **The sample's history and reviews:** `work/sample/` (v1 → v10, every pass log) and `work/sample/reviews/` (Grok ×8, a fresh Claude, the cold reader, the v10 audit).
- **Sources:** `sources/world_rules/` (World Rules snapshot), `sources/transcripts/` (the Tony pod-world chat), `archive/` (the retired v4 codex, not canon).
- **The Codex v5 page** (https://claude.ai/artifact/DejDv6wZUCqZGEpZDonS4W) shows the BANK first as overrides. Rebuild with `python3 scripts/build_codex_page.py` and republish after banking.

## Habits that worked
- Bank Patrick's words verbatim, then republish the codex page.
- Run agents in the pipeline order. Run the story-guard after every editing pass.
- Outside readers (Grok, a fresh Claude) plus a cold reader with no codex catch what the codex-aware checkers miss.
- Commit and push after every step (the branch is in the session's git instructions).
