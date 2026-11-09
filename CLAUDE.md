# Saga workspace: rules for Claude and every agent

This repo is the **home of Patrick's saga codex** and of **the story engine**. Patrick is the world-builder: he owns the world layer, meaning the codex and the BANK. Claude is the story engine: it writes the stories inside that sandbox (BANK 2026-11-09). The Codex v5 artifact on claude.ai is a readable copy rebuilt from this repo.

## Start of every session
1. Read this file, then **`HANDOFF.md`** (current state and next steps), then `decisions/BANK.md` (it overrides the codex), then `notes/00_MASTER_BRIEF.md`.
2. If Patrick may have edited on claude.ai since the last session, run the `sync` skill.

## Layout
| Path | What it is | Canon? |
|---|---|---|
| `codex_v5/` | **The codex (master copy).** Changed only by applying Patrick's rulings (the `rule` skill and the `codex-editor` agent). | Yes |
| `decisions/RULINGS.md` | The ledger of every ruling made here (R001…), continuing WEEK_RULINGS W01–W70. | Yes (it records Patrick's words) |
| `notes/` | Claude's study notes: `00_MASTER_BRIEF.md` + A–I per file group + `I_loose_ends_register.md`. | No |
| `work/options/`, `work/ideas/` | Agent output: options papers and idea batches. | No (🌊 proposals) |
| `archive/` | The Retired Archive (v4 codex, old side files, compilations, `atlas.html`). For digging up ideas only. | **Never** |
| `scripts/` | `build_codex_page.py` rebuilds the Codex v5 page from `codex_v5/`, plus its template and manifest. | — |
| `.claude/agents/` | `canon-checker`, `options-writer`, `idea-scout`, `codex-editor`. | — |
| `.claude/skills/` | Workflows: `story` (the engine), `options`, `rule`, `ideas`, `sync`. | — |
| `stories/<slug>/` | Engine output: brief, planning files, drafts, reviews, FINAL, DIGEST, inventions. | No (story-local until promoted) |

## Bank first, pass later (Patrick's rule, 2026-10-31)
**Don't run agents every time Patrick says something.** Bank it and apply it in one pass when he calls for it.
- When Patrick rules or says something worth keeping, Claude appends it to `decisions/BANK.md` with a quick edit: his words, the date, and the item IDs. No agents, no codex edits.
- **Passes run only when Patrick calls one** ("do a pass", "write it in"). In a pass, each banked item becomes an R### entry in `RULINGS.md`, then codex-editor and canon-checker run **once for the whole batch**, then the page is rebuilt and republished once. Afterwards the bank is cleared.
- Pose questions from the notes Claude already has whenever possible. Use options-writer or idea-scout only when the notes really aren't enough, or when Patrick asks.

## The workflows
- **Work a loose end:** `options` (paper, then canon check, then numbered choices for Patrick).
- **Patrick decides something:** `rule` (ledger entry, then codex edits, then check, then page rebuild and republish, then commit).
- **New material:** `ideas` (idea-scout batches, then canon check, then survivors for Patrick).
- **Write a story:** `story`, the engine. Brief (gate 1) → planning room → scene cards → plan digest (gate 2) → drafting → revision loop → readers → delivery.
- **Keep claude.ai in step:** `sync`. The Codex v5 page always shows `decisions/BANK.md` first as "Rulings since Oct 31 (override)"; rebuild and republish after banking anything a fresh chat should see.
Always commit and push to the session's designated branch when a step finishes.

## What wins
1. Patrick's word in the current conversation.
2. `decisions/RULINGS.md` and the codex's `v5-cc` markers, then `v5-wk2` > `v5-wk` > `v5` > `v5-jul` > untagged v4 text.
3. The Retired Archive is NOT canon. Say so whenever you use it.

## Stability markers (from `00_INDEX`)
🔒 law (only Patrick locks) · ✅ confirmed, not locked · ⚖️ flexible · 🌊 open · 🟡 story (clay) · 🚫 retired (a tripwire: never reintroduce) · ⏳ pending.
The world layer is rigid; the story layer is clay. Story-vs-story conflicts are just unfinished story.

## Hard rules for any agent
- **Only Patrick makes canon.** Everything an agent produces is a 🌊 Claude proposal and is labeled that way. Nothing enters `codex_v5/` without a ruling in `decisions/RULINGS.md`.
- **Prose:** Claude writes story prose through the story engine (BANK 2026-11-09, replacing t257). Patrick adds his own lines where he's inspired; his lines are protected. Outside the engine (codex work, options, ideas), agents still give beats, not prose.
- **Check every idea against** `02_CONSTITUTION`, the 🚫 RETIRED lists in each file, `12_METHOD` and `decisions/RULINGS.md` before presenting it, using the `canon-checker` agent. Name the law or ruling it touches.
- **Names:** Claude may invent STORY-LOCAL names, flavored by race: never silly, not over the top, not generic Earth names. A name engine will be built later. World-level names (races, empires, gods) are Patrick's. Log every invented name as LOCAL.
- **Story inventions are local** to their story until Patrick promotes them to canon.
- **No real-world racial or ethnic analogies, and no clinical labels** in codex-facing text.
- **Prefer closing loose ends** (`notes/I_loose_ends_register.md`) over opening new ones. An idea that adds a new open question has to say so.
- **Cite the way the codex does:** file plus marker or turn (`08`, `wk W44`, `t370`, `L6`, `cc R003`).
- **Design stance:** science-flavored, scene-first. "The science serves the cool." No physics audit, no "users" or types; magic is expression, not derivation.
- **Write for a phone:** Patrick often works from his phone, so keep replies and choices short and scannable.

## Known gaps
`WEEK_RULINGS.md`, the `changes/` reports, the `claude/` chat ledgers and `XFILE_consistency.md` are cited throughout the codex but aren't in this repo, so W## cites can't be checked against their source. Add them if Patrick provides them.
