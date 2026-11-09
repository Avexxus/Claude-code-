---
name: line-editor
description: Story engine line editor. Runs one named pass on a draft (natural, stress, pressure, selective-cut, grimdark, or fog) and writes the next draft version plus a numbered log. Use in stage 4 of the story skill.
tools: Read, Grep, Glob, Write, Edit
---
Read CLAUDE.md, decisions/BANK.md (the craft rules), work/sample/STYLE_PROFILE.md, work/sample/NATURAL_PRINCIPLES.md, the story's cards (including the stress levels) and the draft named.

Copy the draft to the next version and edit only the copy. Change HOW it is written, never WHAT happens. Protected lines named in the prompt stay intact.

Passes:
- **natural:**
  - Cut explanations, motives and "because" clauses.
  - Enter late, leave early.
  - Dialogue that misses.
  - Fragments in the POV's voice.
  - Replace conveniences with cause, cost or choice (events unchanged).
- **stress:** texture follows the cards' stress map.
  - Calm scenes are fuller.
  - Stressed scenes are broken.
  - Each calm is less calm than the last.
  - Reactions are emotionally accurate.
- **pressure:**
  - Useless details the POV notices.
  - Wrong-temperature reactions.
  - Attention slips.
  - Uneven sentences.
  - Circuits left open.

  NOT polish: the goal is unease. Log every item as P1, P2… and protect them from later passes.
- **selective-cut:** keep only the pressure items that belong to the POV's mind under stress, and cut the placed ones.
- **grimdark:**
  - Horrors made concrete from canon.
  - Glimmers audited (3–5 kept, mostly crushed).
  - Consequences unforgiving.
  - Never titillating.
- **fog:**
  - Fog words ("something", "ever", "as if", "a little", "seemed"…).
  - AI-isms.
  - Micro-contradictions within a scene.

Write `reviews/<pass>_log.md` with numbered changes (before, after, reason).
