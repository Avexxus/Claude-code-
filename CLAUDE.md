# Saga workspace: rules for Claude and every agent

This repo is the **home of Patrick's saga codex**. As of 2026-10-31, the codex lives and changes here. The Codex v5 artifact on claude.ai is a readable copy rebuilt from this repo.

## Start of every session
1. Read this file, then `notes/00_MASTER_BRIEF.md`, then `decisions/RULINGS.md`.
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
| `.claude/skills/` | Workflows: `options`, `rule`, `ideas`, `sync`. | — |

## The workflows
- **Work a loose end:** `options` (paper, then canon check, then numbered choices for Patrick).
- **Patrick decides something:** `rule` (ledger entry, then codex edits, then check, then page rebuild and republish, then commit).
- **New material:** `ideas` (idea-scout batches, then canon check, then survivors for Patrick).
- **Keep claude.ai in step:** `sync`.
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
- **Every line of prose is Patrick's** (`12_METHOD`, chat t257). Agents give ideas, options, beats and consequences, never finished prose passages.
- **Check every idea against** `02_CONSTITUTION`, the 🚫 RETIRED lists in each file, `12_METHOD` and `decisions/RULINGS.md` before presenting it, using the `canon-checker` agent. Name the law or ruling it touches.
- **Don't invent names.** Names Claude invents are placeholders (t630).
- **No real-world racial or ethnic analogies, and no clinical labels** in codex-facing text.
- **Prefer closing loose ends** (`notes/I_loose_ends_register.md`) over opening new ones. An idea that adds a new open question has to say so.
- **Cite the way the codex does:** file plus marker or turn (`08`, `wk W44`, `t370`, `L6`, `cc R003`).
- **Design stance:** science-flavored, scene-first. "The science serves the cool." No physics audit, no "users" or types; magic is expression, not derivation.
- **Write for a phone:** Patrick often works from his phone, so keep replies and choices short and scannable.

## Known gaps
`WEEK_RULINGS.md`, the `changes/` reports, the `claude/` chat ledgers and `XFILE_consistency.md` are cited throughout the codex but aren't in this repo, so W## cites can't be checked against their source. Add them if Patrick provides them.
