# ch08 fix_log_v5 (outside-read fixes, 2026-11-27)

🌊 Story-local. Source: Patrick's fix list (12 items), with the audit decisions, brief and cards as the binding frame. The `reads/` folder is not in this chapter folder; the findings are taken from the brief and the fix list as given. No critic or judge file beyond these was available.

## Fix list

| # | Fix | Status | What changed / why |
|---|---|---|---|
| 1 | Orientation in first 80 lines (Teo, Seffa, Doc, tall boy, woman, Cut, Jon went down ahead; tall boy named once) | TAKEN | Scene 1 paragraph 1 and the "It was the ninth" paragraph give one clause each. The Cut is "the iron yards and cranes along the cut on Ithe." Jon: "had gone down ahead of them, years back, off this same rim." Tall boy named Kell once, then "the tall boy" everywhere else. The woman is given as the thing the Cut's old men say kept the count "since before the cranes," which is hearsay for Eli, so it reads as rumour and not as introduction. |
| 2 | Define count / read / blank at the first lintel, in one concrete instance | TAKEN | Count-house lintel now has a small band of names cut under the rule. "The count was the names on the band." Read = a name that comes off the band into the count. Blank = a notch with nothing cut in it; the count never reads through one. Teo says it; Eli: "I didn't ask." |
| 3 | Grille: one rule (a gift is taken only if given; grille takes names, not gifts; reach was given to the gate, not to the grille; said once; Eli does not argue again) | TAKEN | Her line now: "It takes names. It takes no gifts. Your reach was given to the gate. The gate isn't this." Said once. Eli "opened his mouth to argue it, and did not" and tries. Removed the older "takes a gift as given" wording, which contradicted "doesn't open for gifts." |
| 4 | Doc's coat stays folded under the table leg | TAKEN | Coat folded under the table leg, stays there. Later "put it in his coat" changed to "put it in his pocket." No later coat on Doc. |
| 5 | Doc's "I'll go with the one who's bleeding" | TAKEN (reason given) | Doc goes down with Eli and Teo and says why in one line: "Seffa's got the boy, and she's got the ladder. Somebody's to keep you off that count." |
| 6 | Jon on the surface, relay only; one line makes it clear | TAKEN | "Jon had gone down ahead of them, years back, off this same rim. The horn was the rows' relay. His voice came up it from the rows and went no further." Jon's voice is "thin, from a long way off." |
| 7 | Count arithmetic honest | TAKEN (cut to what the count shows) | Line kept: "Seven were in. Six come out. One stays." Five came through the seam from the yard side; the woman and the old man were already inside, so seven were in the place. Six come out (Teo, Seffa, Kell, Doc, Eli, the woman). The old man stays. "Seven went in" was the inaccurate form. |
| 8 | Pillar loop halved: "Walk again" / "Eleven" / "back at ten" at most twice | TAKEN | "Walk again" cut. "We walked eleven" cut. Now "Eleven" once and "back at ten" once. Seffa runs without an order; the floor "had taken three back." |
| 9 | "Sitter": explain in one line or cut | TAKEN (one line) | Ysvet: "Sitter. You sit with them and take something off the top, and call it a kindness." Eli "heard the word and did not ask what it cost." |
| 10 | Woman: one visible reason to stay in the cell (the old man's breath in her hand); she leaves it when she decides; keep "I go where I like. Nobody hands me back." | TAKEN | After the cough: "Her palm stayed where it was on his chest. What she had taken from him was still in her hand, and she kept it there." Leaving: "Her palm came off him, and she stood up." Line kept. |
| 11 | Teo's finger: one visible reason (he reached through to hold the old man's hand; the groove was there) | TAKEN | "The old man's hand had come off his chest... Teo reached through the bars with his right hand, over the groove, and took hold of it. The groove was under his foot, where it had been all along." |
| 12 | Tics: "No one answered/Nobody/No answer came" at most 5; "a little late" at most once; "flat" at most 4; "the way" at most 8; "nothing" and "nobody" under 12 | TAKEN | Counted by Grep on draft_v5. "No one/nobody/no answer" = 5 (lines 63, 199, 355, 463 x2). "a little late" = 1 (count voice). "flat" = 3. "the way" = 6. "nothing" = 9. "nobody" as a word = 5 (in the same 5 above). |

## Protected lines

All kept verbatim:
- "Only a joint, he thought… was not ashamed for long." (Only a joint, he thought. You would hardly miss a joint. He was ashamed of thinking it, and was not ashamed for long.)
- "He had not known how much of his walking was looking."
- "The cold stayed on the left. The warm stayed on the right. Neither of them moved over."
- "Seven were in. Six come out. One stays." (one word changed from "went in"; see fix 7)
- The ending "and it did not."

## Extra changes made under the brief (not on the list)

- Seffa's "Nobody looked up" changed to "The landing did not look up" (tic budget).
- "Nobody agreed with him" changed to "The room did not agree with him" (tic budget).
- "No one told him no" changed to "He was not told no" (tic budget).
- "Nobody answered him" at the rail changed to "He had not expected them to say anything, and they didn't" (tic budget).
- "No answer came for that" changed to "That one he could not answer" (tic budget).
- "No answer from Teo" changed to "Teo did not answer" (tic budget).
- "No one laughed with him" changed to "The room did not laugh with him" (tic budget).
- "to nobody" (count-house) changed to "to the wall" (tic budget).
- "a flat iron note" changed to "a hard iron note"; "pressed flat" to "pressed smooth"; "healed flat" to "healed smooth"; "came out of the brass flat" to "thin"; "Flat, through the gap" and "said it flat" cut; "and flat" to "and open."
- "the flat of its many voices" changed to "the one tone of its many voices."
- Ysvet's cell line "Don't put a hand on the grille": "said it flat" changed to "without any lift in it."
- "Teo's hand" clarified (was "the boy's hand," which read as Kell).
- "Up he got" changed to "Eli got up" (it read as Ondry).
- Scene 3 gate: "Nobody's given it anything" kept (the one Nobody in that scene).
- The seam logic (blank cannot cross) kept as drafted. It differs from the card's "reads bodies already read" wording; see LEDGER point 2.

## Rejected

None of the twelve items was rejected.

## Open points for the next pass

- Word count: not run. This session has no shell, so `scripts/wordcheck.py` could not be executed. Estimate only (the draft is near the brief's 6,000–6,500 range, but this is not measured).
- The count-house band of names is a new object. Decide whether it stays.
- Seam logic (blank vs read-through) to be checked by the continuity-keeper against the cards' S-127 wording.
- Her name is not printed; Kell is the only named tall boy (LOCAL).
