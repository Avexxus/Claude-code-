# Ch7 "Listen" polish log (step 5, pipeline v2)

🌊 Claude's working log, not canon. Source: `draft_v2.md`. Outputs: `draft_v3a.md` (dialogue), `draft_v3b.md` (word-watch), `draft_v4.md` (line pass), `draft_v4_guarded.md` (guard), `CH07_STORY_ONLY.md` (story text only).

**Tool limit, read first.** This session had no shell. `scripts/wordcheck.py` could not be run, and git commit and push could not be done. Counts below are Grep counts on the files (whole-word, case-insensitive, per line; close to the script's count but not the same method). The script must be run and the commit made by someone with a shell.

**Protected lines (checked in every file):** "Don't use more than you can control" (the crate, second use, verbatim; the pallet use is narrated only, as in v2) and "I don't leave the Cut" (verbatim, with "No." / "Not even—" / "Not for the door. Not for the—" unchanged). Both present word for word in `draft_v4_guarded.md` and `CH07_STORY_ONLY.md`.

---

## 1. Dialogue (dialogue-editor pass, `draft_v3a.md`)

Speaker check: master = flat declaratives, no question marks, "No." and "Listen."; Seffa = short, dry, "love", "Then stop on it"; Teo = few words, breaks off in the call; Oskel = fast, "Seff. Seff. Listen."; tall boy = few words, flat; Doc = dry on the job, goat only while he works; Eli = warm, narrates, arranges, doesn't hear; Jon = "Son", "Ya", "Mind yerself".

- Eli's introduction of Doc: "I should've told you about Doc" → "I should've said about Doc." The healer line and the stammer ("He sits with the—") stay.
- Eli's yard monologue: cut "It's going to be good." The account line stays (C1: the account is raised and never rung).
- Tall boy's count line: "to nobody" → "to no one"; "Row man reads the dials" kept (the count mechanism is the plant).
- Eli's "That's a yes? Isn't it?" → "That's a yes. Isn't it?" (matches the plan's wording; a statement, not a question to the master).
- Seffa "I'm listening. What's happened to you?" → "What's happened to you?" (cut the pointed echo of Eli's "I'm listening").
- Oskel's call report: cut "and it's been on the box since the bell" (the reader has the relay from the hut scene); "who'd asked" kept (R-017, the book).
- Eli's "At the berth" removed from "Did you hear him say that?" (a memory tag that explained itself).
- Eli to Jon, "The man there'd be" → "He's taken me on." (broken clause cut; the news is the same).
- Eli after the call: "That's the count, isn't it. The row man's count, on the ninth. He'll mean that." cut. It was the too-neat echo the ledger flagged (unsure point 3). Kept: "Well. He'll tell us, won't he."
- Eli's "Did you tell him" / "Did you say anything" kept as the absent-minded worry.
- Seffa's "Ferrel's got the lot" → "Ferrel's got the flour." (one clause, not a riposte).
- Seffa's "I'm going with them" reason kept ("He had the fit. Somebody's got to be on him when it comes back."). It is the LOCAL reason the ledger lists; it stays as the only reason she gives.
- Eli at the lamp: "You'd be the one who knows what to do when we get there" cut. It was Eli flattering the master into a yes. "You'd know, wouldn't you?" kept.
- Eli's "Nothing came. He laughed, and it didn't come out right" → Eli's "There was no rest of it" (narration; no event change).
- Master's terms and the refusal: no change to the words (protected lines verbatim; "Yes," "On what I say," "Then you're not taken on" unchanged).

Not changed, on purpose: Eli's "I felt it go" run; Doc's goat (he is working); the tall boy's "He always says that"; Jon's "Ya don't need me for the next bit"; Jon's "Mind yerself, son".

**Flagged, not fixed (dialogue):** Eli's "Then we'll see" echoes the master's yard line "Then we'll see" (5:L577). It is Eli's, not the master's, and it reads as Eli taking the last word. Left, because it is his habit and cutting it changes the last exchange's sting. Writer's call.

---

## 2. Word-watch (`draft_v3b.md`)

Caps: "didn't" ≤25; "nothing"+"nobody" ≤12; "something" ≤12; "then" ≤20; "the old man said" ≤2.

| Tic | v2 (est.) | v3a | v3b | v4 guarded (final) | Cap | Status |
|---|---|---|---|---|---|---|
| didn't | ~34 | 34 | 9 | 9 | 25 | met |
| nothing + nobody | ~22 | 22 | 8 | 8 | 12 | met |
| something | ~9 | 9 | 9 | 8 | 12 | met |
| then | ~30 | 30 | 17 | 18 | 20 | met |
| "the old man said" | 5 | 5 | 2 | 2 | 2 | met |

Method: `didn't` and `nothing`/`nobody` mostly swapped to "never", "no one", "wouldn't", "kept his eyes on", or cut. Cut the "Then" that was only a bridge. Sentence openers: "the old man said" kept only for "Breathing" and "Listen"; "Mornings," and "Shut your eyes," now end "he said".

**Known misses:**
1. **Sentence openings (cap 6 of any one).** Grep estimate in `draft_v3b.md`: sentences opening with "He" about 70, "The" about 45, "Eli" and "Teo" about 15 each, "It" about 20. The cap is not met and a full fix would rewrite most of the narration, which would flatten the voice. Flagged for the writer to decide whether the cap is meant for the two-word script metric (which will read as "he didn't", "he was", "he said" and so on) or for the first word.
2. **"never" is now a tic.** The word-watch swaps made "never" appear about 8 times ("He never hitched", "He never waited", "He never thought", "He never turned", "He never looked", "the cranes had never once cared", "I never saw him", "never said you were quick"). Not in the caps, but the same flattening. Writer may want two of them cut.
3. **4-word phrase repeats (cap 2).** Not checked by hand. "he said it to" and "the same words, without" may repeat. Script needed.

---

## 3. Line pass (`draft_v4.md`)

- Cut "He was quicker than Eli had ever been, the pallet, the cranes, all of it" to "He was quicker than Eli had ever been."
- Cut simile and explanation: the handset "the way you'd hold something that might still be hot" → "as if" removed; Oskel "like a boy showing off a thing he's been given" → "pleased with it"; Eli's "the way he used to come into rooms at the Terrace" → cut.
- Cut the motive sentence "He had meant it to be gentle." (kept "He didn't know how gentle he'd been until he opened it.")
- Cut the callback "It was the one word, and it was the same as it had been on the step at the Terrace and in the kitchen with the plums." (narration explaining the word; the reader has "Son," said Jon.)
- Cut "There was a line now, down at four." (Eli's lack of the account is already on the page: the walk back never mentions it.)
- "Not one of them was watching Eli" kept (R-016 mechanism).
- "He never thought about it" kept (the tall boy's speed is the setup for the arm).

## 4. Story-guard log (`draft_v4_guarded.md`)

Checked: events (every scene beat in `plan.md` §1–6 and `draft_v2.md`), what each person learns (Teo's handset, Eli's "He said yes", the master's refusal, Seffa's leaving, Oskel's pie), seeds (moth lesson; Jon "That's come right, then"; the door on the ninth; the master's "I don't leave the Cut"; Seffa's onions and "Somebody's got to feed you"; the master's look at Doc), protected lines (both verbatim), canon (R-014, R-016, R-017, R-021, R-034, R-040, R-043, R-047, R-051, R-028), LOCAL names and items (the row man's book, the handset, the pot, the onions on the sill, Ferrel, the tall boy's forearm, Doc's rag, the Ithe clock).

| # | Change | Found by | Result |
|---|---|---|---|
| G1 | v4 cut "the way it had been left the day they went for the barge" from the gate sentence | Guard: the barge date is a fact the page carries | **Reverted.** Restored in `draft_v4_guarded.md` and `CH07_STORY_ONLY.md`. |
| G2 | v4 cut "the look of a man who'd stood in one place long enough for the cold to stop bothering him" | Texture only, no fact | Kept cut. |
| G3 | v4 cut the plums callback (Jon's "Son" "in the kitchen with the plums") | A memory tie, not an event or seed in the plan | Kept cut. Writer may restore if the Terrace link is wanted. |
| G4 | v4 cut "There was a line now, down at four." | Eli's relay line is still on the page through the call itself | Kept cut. |
| G5 | v3a → v4: Eli's "That's the count, isn't it" cut | Ledger unsure point 3 asks for this cut if the echo reads too neat | Kept cut (dialogue only). |
| G6 | Motive sentence "He had meant it to be gentle." cut | Motive only, no fact | Kept cut. |
| G7 | Oskel's "and it's been on the box since the bell" cut | The relay is already logged in the hut | Kept cut. |

Result: one revert (G1). Protected lines verbatim. No event, canon, or seed changed.

---

## 5. Items for the writer

1. Sentence-opening cap (see §2, miss 1). Decide the metric and the bar.
2. "never" tic (see §2, miss 2).
3. Ledger (`draft_v2.md`) still lists "That's the count, isn't it" as present. It is cut in v3a onward. Update the ledger's unsure point 3.
4. Ledger unsure point 4 ("Then you're not taken on") is kept as written; not changed.
5. Overdue seeds from the ledger (S-008, S-019, S-032, S-047, S-106) are still not planted here. Same as v2.
6. Word count: about 6,200 words (hand estimate, no machine count; v2 was about 6,400 by the same method).
7. Not done by this session, for a shell-enabled pass: run `python3 scripts/wordcheck.py` on `draft_v3a.md` and `draft_v3b.md` and on the guarded final; commit and push with "Ch7 polish: dialogue, word-watch, line, guard" plus the trailers.
