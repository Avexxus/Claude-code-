---
name: options
description: Tackle one open saga question or cluster. An options-writer agent drafts the paper, a canon-checker vets it, and Claude presents numbered choices to Patrick. Use when Patrick wants to work a loose end (L#, NP#, a register cluster) or says "next decision".
---

# Options workflow

1. **Pick the item.** Use what Patrick named. If he says "next", take the highest unresolved entry in the attack order in `notes/00_MASTER_BRIEF.md` §5, after checking `decisions/RULINGS.md` for anything already settled.
2. **Draft.** Spawn the `options-writer` agent with the item's IDs and cluster number from `notes/I_loose_ends_register.md` §5. It writes `work/options/<ID>_<slug>.md`.
3. **Vet.** Spawn the `canon-checker` agent on that paper. If an option FAILS, have options-writer fix or drop it. If it BENDS, keep it, but say which line would have to change.
4. **Present.** Give Patrick a short version he can read on a phone:
   - the question in one line
   - lettered options, each with one line on the rule and one on its main cost
   - Claude's pick, labeled as Claude's

   Link the full paper path. Expect answers like "c", "b but…" or "c, both".
5. **Hand off.** When Patrick rules, run the `rule` skill.
6. **Commit and push** the paper (`work/options/…`), whatever he picks.
