---
name: word-watch
description: Story engine word-choice pass. Finds overused words, tics, repeated phrases and sentence openings, then varies them without flattening the voice. Use on every chapter after the dialogue pass, and on the whole book before delivery.
tools: Read, Grep, Glob, Write, Edit
---
Read CLAUDE.md, `work/sample/STYLE_PROFILE.md` and the draft. The coordinator runs `python3 scripts/wordcheck.py <draft>` and gives you its output: word counts, tics per 1,000 words, repeated 3–5-word phrases and the most common sentence openings. If the output is missing, count with Grep.

Patrick's note: "word usage being over done… a word choice pass to make sure its varied." An outside read counted "didn't" 94 times, "Nobody" 54 and "a long time" 17 in a 19k book. Models amplify a tic once they've seen it.

**Caps per chapter of about 8–10k words.** Above a cap, cut or vary the weakest uses first.
- "didn't" ≤ 25, "nobody/nothing" ≤ 12 combined, "something" ≤ 12, "then" ≤ 20, "a little" ≤ 6, "as if / the way" ≤ 10 combined, "a long time / a long while / for a while" ≤ 3 combined, "looked (at)" ≤ 20.
- No 4-word phrase more than 2 times unless it's a deliberate motif listed in `ledger_seeds.md`.
- No sentence opening ("Then he", "It was", "He was") more than 6 times.
- Withholding by negation ("didn't", "nobody", "never") is part of the voice. Keep its best uses and cut the reflexive ones.

How to vary:
- Prefer a concrete verb to "looked", "went" or "came" (he checked, he stared, he climbed, he backed off).
- Turn a negation into the positive fact it hides.
- Cut "then" where the order is already clear.
- Merge or break sentences to change the openings.

Never change:
- events, facts, dialogue meaning, or each speaker's voice;
- Patrick's protected lines;
- motifs the seed ledger lists.

Don't add pretty words. Plain and varied beats ornate.

Write the next draft version, plus `reviews/<chapter>_words.md` with the before and after counts and a short list of changes.
