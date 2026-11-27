# Ch8 polish log (2026-11-27)

🌊 Story-local polish. Prose only. No event, canon, seed or protected line changed.

## Run conditions (read first)

- This session had no shell. `scripts/wordcheck.py` was **not run**, `wc` was **not run**, and the commit and push were **not made**. Tic counts below come from Grep with `-o` on each file, using the same patterns the wordcheck TICS list uses. Repeat `python3 scripts/wordcheck.py` on `CH08_STORY_ONLY.md` before delivery.
- No subagents could be launched from this session. The dialogue-editor, word-watch, line-editor and story-guard roles were run by hand, in that order, one saved file per stage.
- No Patrick-protected lines are in ch08. The STYLE_PROFILE §7 list and the brief's "protected lines if they appear" were checked; none appear in the text. So nothing was held verbatim for protection, and no line of his was touched.

## Stage 1: dialogue-editor (draft_v3a.md)

1. Seffa's ladder reason: "He can't do a ladder on his own with that arm" → "He can't do a ladder with that arm." Reason: she is speaking from the rung, and the "on his own" was filler. Event unchanged.
2. Eli at the gate: "I said I would, and you'll see it done." → "I said I would." Reason: he piles on his own promise, and the second half repeats "You'll see." Eli's habit stays.
3. "Eli." (the name cut-off at the bars) now tagged "said Teo." Reason: no speaker was clear, and Teo is the one who stops Eli.
4. "Ask when it's reading." now tagged "she said." Reason: it is her rule-line, and it should not read as Eli's.
5. Grille speech split by Eli's non-answer: "Then it's open," said Eli. / "It doesn't open for gifts. It opens for names." Reason: a real person reacts to half a rule and misses the other half. The fact is unchanged: the grille does not open for gifts.
6. Corridor speech: Eli's "Somebody cared about this" is now said to Teo, and his "not since the cranes" comes after Teo's count. Reason: Eli talks past Teo, and the two lines no longer come out as one speech.
7. "Stand back from the grille," now tagged "she said." Reason: the line sits right after Doc's reach, and the tag stops it reading as Doc's.
8. "Where does it run," said Teo: "It was not a question either" → "He did not make it sound like a question." Reason: the narrator was ruling on Teo's voice. Eli's view now carries it.
9. The seam exit: "Go" / "No," she said / "Go. Or you're counted with me." / "I'm the one that stays." Reason: "No" had no speaker. Tagged, so the exchange reads as two people.

Checked and kept (the dialogue was already distinct): Teo's clipped "It says read. Under." and "Right."; Seffa's "love" and "I'm saying again"; Doc's "Hm." and "Keep it clean and keep it still"; the tall boy's "Rule's for slow ones", "Yeah", "You said", "I was quick", "Upper's the way I came in" (the lie stays); Ysvet's counts and her two refusals; Ondry's breath-broken lines ("Twenty—", "Don't carry me", "Who."); Eli's "It's tied short because it's a table" and "She's wonderful". Eli's calibration (warm, narrates, misses things) is intact.

## Stage 2: word-watch (draft_v3b.md)

Measured with Grep on the stage-1 file, and again on the final file.

| Tic | Before | Cap | After |
|---|---|---|---|
| "palm flat on his" | 4 | ≤2 | 2 (kept: the cell's opening, and the seam; the other two changed) |
| "the way" | 17 | ≤8 | 6 |
| "a long time" | 4 | ≤2 | 2 |
| sentence-opening "It was" | 16 | ≤6 | 2 |
| "nothing" | 8 | <12 | 8 |
| "nobody" | 8 | <12 | 7 |

Changes: "the way" was cut where it was a simile tic ("the way he had looked", "the way he'd read", "the way he had always given", "the way Eli had watched") and kept where it was a real direction ("the way out", "the way you'd call up"). "It was" openers were changed to fragments or to "There was" / "That was" / "Had" forms. Two "palm flat" uses were changed to "her palm on" and "her hand on". Two "a long time" uses were cut.

## Stage 3: line-editor (draft_v4.md)

- Motive clauses cut: "because it was closing, and because there was no one left to tell him not to" → "while it was closing"; "because he had sat down…" cut; "because he had to" cut; "because he did not know how" cut.
- Narrator certainty about others' minds: "Eli saw Seffa know it… because the boy… was not going to be told twice" → Eli sees Seffa's face take it in; "She knew the names" → "She seemed to know the names"; "the hard side" cut.
- Explanation cut: "with no part held back"; "and the door would be done" (end); "and it would not have him, and he was not going to get up and walk through it" (Ondry's "I'm the one that stays" carries it); "like a wire"; "like a tally mark pressed into wood"; "like the back of a spoon"; "the way you'd steer a man off a boat" (replaced by "steering him up the ladder").
- Stacked similes: the seam scene's "as if something on the far side had leaned against it" cut, so the counter scene is down to two.

## Stage 4: story-guard (draft_v4_guarded.md, CH08_STORY_ONLY.md)

Checked each stage against the original: events, what each person learns, canon, seeds, and protected lines.

Reverted (restored to the stage-2 wording):
- "and no one had ever told him a gift could be refused like that" (the reach seed, S-005, and the gift rule).
- "the thing that had made the cranes' men look up" (a callback).

Kept as cut (no event changed):
- "because there was no one left to tell him not to" (motive only).
- "and the door would be done" (the count's finish is already stated at "It would finish at first light").
- "It would not have him, and he was not going to get up and walk through it." (carried by "I'm the one that stays").
- Doc's "because he did not know how" (his act, not his reason, stays).

## Flags for the writer (not changed)

1. **Canon clash, ch8 vs cast.** `cast.md` §1 secret 3 says Ysvet "tried her own lintel with the knife, for years… On the third try the counter took the top joint of her right knife finger." The text (L443, now L441) says the corridor's line took the finger: "The corridor's line took it… Not my own lintel… I never crossed my own." The event is the text's, and it was kept. The cast needs one of the two changed, or Patrick needs to say which. This is the chapter's one real continuity question.
2. **Length.** The user's machine count is 7,654. `fix_log_v2.md` §0.10 has a hand estimate of 5,900–6,000 and says it was never machine-counted. This polish cut about 150 words of narration. Run `wordcheck.py` before delivery. If the true count is near 6,000, the cuts have to be reversed.
3. **The seam rule** (`fix_log_v2.md` §7, the riskiest change) is unchanged: "The seam took what the count had finished with" and "It takes a name only when it's read through. His never was. He's the blank." Both stay.
4. **Eli's "the way"** (L541, "the way he said most things") is kept and is the 6th use. If the cap should be stricter, it is the easiest to cut.

## Not done

- Commit "Ch8 polish" with the usual trailers, and push: not possible from this session (no shell or git tool).
- wordcheck.py run and slop-list check: not possible (no shell).
