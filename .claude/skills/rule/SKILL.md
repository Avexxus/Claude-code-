---
name: rule
description: Record one of Patrick's saga decisions and apply it everywhere — ledger entry, codex edits with v5-cc markers, open items closed, notes updated, the Codex v5 page rebuilt. Use whenever Patrick makes a ruling ("go with b", "lock that", "c, both") or states new canon.
---

# Rule workflow

**Bank first, pass later.** Outside a pass, a ruling only gets appended to `decisions/BANK.md` (his words, date, IDs), and that's it. Run the steps below only when Patrick calls a pass, and run them once for everything banked: one R### per item, one codex-editor run, one canon-checker run, one rebuild, one commit. Then clear the bank.

1. **Confirm the ruling.** Restate it back to Patrick in one or two lines. If his words leave a real ambiguity, ask one short question first. Don't record your interpretation as his words.
2. **Record it.** Add the next `R###` entry to `decisions/RULINGS.md`, quoting Patrick verbatim with the date. Include the question and its IDs, the decision, its stability (🔒 only if he said lock, otherwise ✅), and what it closes or opens.
3. **Apply it.** Spawn the `codex-editor` agent with the R### ID. Then spawn `canon-checker` on the diff (`git diff codex_v5/`) to catch anything the edit broke or missed.
4. **Rebuild the page.** Run `python3 scripts/build_codex_page.py`, then republish `build/codex_v5.html` to https://claude.ai/artifact/DejDv6wZUCqZGEpZDonS4W (the Artifact tool, with `url`), so claude.ai matches the repo. Before the first republish of a session, read that artifact. If someone edited it on claude.ai, merge those edits into `codex_v5/` first.
5. **Commit and push**, with a message naming the R### and what changed.
6. **Report to Patrick:**
   - what changed, in 3–5 lines
   - what it closed
   - anything left open or newly raised
   - the next item in the attack order
