---
name: ideas
description: Generate a vetted batch of new saga ideas for a category (a race, a thin spot, plot points, a character gap). Idea-scout agents draft, canon-checker vets, Claude presents the survivors. Use when Patrick wants new material.
---

# Ideas workflow

1. **Scope it.** Settle the category and any angle Patrick gave ("weak spots", "plot points for Book 1", "the trolls"). Check `notes/00_MASTER_BRIEF.md` §7 for thin spots, and the register for open items that new ideas could close.
2. **Generate.** Spawn one or more `idea-scout` agents, each on a distinct category or angle. Run several in parallel when the angles are independent.
3. **Vet.** Spawn `canon-checker` on each batch. Drop anything that FAILS. Keep BENDS ideas only if they're strong, and say what line they'd bend.
4. **Present.** Give Patrick the survivors, grouped, one or two lines each, with what each closes or opens. Lead with Claude's top 3. Link the batch files.
5. **Follow up.** For any idea Patrick adopts, run the `rule` skill. Ideas he likes but hasn't ruled on go into `codex_v5/FLAGGED_ADDITIONS.md` as new F### entries via `codex-editor`, marked 🌊 with the source path.
6. **Commit and push** the batch files.
