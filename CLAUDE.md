# Saga workspace: rules for Claude and every agent

This repo is the working copy of Patrick's saga codex, set up so Claude and its agents can read the same canon and keep deep notes.

## Layout
- `codex_v5/` holds the canon: a verbatim snapshot of the Codex v5 artifact (https://claude.ai/artifact/DejDv6wZUCqZGEpZDonS4W), taken 2026-10-31. **Never edit these files.** If Patrick's project and this snapshot ever differ, the project wins, so re-snapshot it.
- `notes/` holds Claude's study notes on the codex: one file per group of codex files, plus `00_MASTER_BRIEF.md`. Notes are Claude's reading, not canon.
- `work/` holds agent output (option papers, idea batches). None of it is canon.

## What wins
1. Patrick's word in the current conversation.
2. `codex_v5/` (later markers beat earlier ones: `v5-wk2` > `v5-wk` > `v5` > `v5-jul` > untagged v4 text).
3. The Retired Archive artifact is NOT canon. Use it only to dig for ideas, and say so when you do.

## Stability markers (from `00_INDEX`)
🔒 law (only Patrick locks) · ✅ confirmed, not locked · ⚖️ flexible · 🌊 open · 🟡 story (clay) · 🚫 retired (a tripwire: never reintroduce) · ⏳ pending.
World layer is rigid; the story layer is clay. Story-vs-story conflicts are just unfinished story.

## Hard rules for any agent
- **Only Patrick makes canon.** Everything an agent produces is a 🌊 Claude proposal and is labelled that way.
- **Every line of prose is Patrick's** (`12_METHOD`, chat t257). Agents give ideas, options, beats and consequences, never finished prose passages.
- **Check every idea against** `02_CONSTITUTION`, the 🚫 RETIRED lists in each file, and `12_METHOD` before presenting it. Name which law or ruling it touches.
- **Don't invent names.** Names Claude invents are placeholders (t630).
- **No real-world racial or ethnic analogies** in codex-facing text.
- **Prefer closing loose ends** (`NEEDS_PATRICK`, `11_OPEN_THREADS`, `FLAGGED_ADDITIONS`) over opening new ones. An idea that adds a new open question has to say so.
- Cite sources the way the codex does: file plus marker or turn (`08`, `wk W44`, `t370`, `L6`).
- Design stance: science-flavored, scene-first. "The science serves the cool." There's no physics audit, no "users"/types, and magic is expression, not derivation.
