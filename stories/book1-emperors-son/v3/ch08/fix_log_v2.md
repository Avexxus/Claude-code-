# Ch8 fix log v2 (draft_v2, 2026-11-27)

🌊 Story-local. Every flag in `review_sense_v1.md`, `review_continuity_v1.md`, `review_payoff_v1.md`, `review_forecast_v1.md` (setup list only), `fix_log_v1.md` departures, and Patrick's binding decisions 1–10. Each line: TAKEN (what changed), PARTLY (what changed and what did not), or REJECTED (reason). Rejections are defended again in `reviews/rebuttals.md`.

Tool note: this session had no shell. `scripts/wordcheck.py` was not run, and nothing was committed or pushed (see the report). Tic and opener counts were taken with Grep on the file.

## 0. Patrick's binding decisions

1. **POV, whole chapter Eli close.** TAKEN. Teo's and Seffa's scenes are told from Eli's position. Ysvet's grief is seen from outside and misread by Eli ("She's just getting it up for him… She's got him sorted"; "She's worn out. Anyone would be."). No narrated interior for her anywhere. Two small Eli-view repairs: "She did not think about the place it belonged to" became Eli's guess; "She did not believe him" became "Eli could not tell whether she believed him."
2. **Cut "The old man was the blank" and any price line before the seam.** TAKEN. The blank line is gone. "One less than it wants. It wants his." is gone. The grille no longer says "Five came in. Six go out. One stays." The arithmetic is said only once, at the seam, after Ondry sits down (L531).
3. **Right arm everywhere; four teeth; the tall boy's exit set up.** TAKEN. The finger is the right little finger (L109). The gum now reads "with four teeth loose in it" (L293). The tall boy's exit has its line at the bridge, tied to ch07's yard gate: "He had been left at the yard gate once already, with his hand up, and he had come after them anyway" (L547). The pit opening also has a clause that he came down the lane after them (L7).
4. **Gate and grille plate read as one rule.** TAKEN. The gate reads a gift as given: two grabs are refused, the third is a whole gift and opens it (L209–215). The grille takes Eli's gift as given and still opens only for names (L359, L365). The old line "You haven't got one" is gone (R-054).
5. **Seam rule ties to the blank.** TAKEN. First crossing: "First through was Teo… The seam took what the count had finished with. The count had finished with Teo." (L491). Then, at the threshold: "It takes a name only when it's read through. His never was. He's the blank." (L501–505).
6. **Doc's cold into the stump.** TAKEN (cut, R-047 and R-060). The cold clause is gone. Doc binds Teo's wrist with a strip of his own shirt and says he does not touch the stump (L439). The cards' "His fingers are cold" is gone too.
7. **Teo's crossing needs one reason on the page.** TAKEN. Ysvet gives the cost first ("The nearest joint. Whoever broke it."), then Teo gives his reason ("It's taking him in pieces"). Eli tries to stop him ("Teo, we can—" / "You can't"). Then Teo crosses.
8. **Fix log v1 departures that are wrong.** TAKEN, see §4 below. The "Who carries him" departure is withdrawn: the line stays flat, and it is not a departure at all (cast §1 says she never asks).
9. **Tics.** TAKEN. Counted with Grep on the file: "nothing" 8 (cap under 12), "nobody" 7 (cap under 12), "then" 8 (cap 20), "she did not look" 2 (cap 2), paragraph openers at most 6 of any word (The 6, A 6, On 6, It 6, He 6, She 6, At 6; no other word above 5).
10. **Length 6,000–6,500.** PARTLY. Hand estimate from byte count of the file: about 5,900 to 6,000 words of story. Not machine-counted (no shell). Run `python3 scripts/wordcheck.py` on `CH08_STORY_ONLY.md` before delivery. The chapter sits at the floor, not the middle of the range.

## 1. review_sense_v1.md (6 HIGH, 8 MED, 11 LOW)

- **S1 HIGH · seam rule contradicts the crossing.** TAKEN. The seam's rule now ties to the read-through (decision 5). Teo is read through and goes first; Ondry is not, and is the blank.
- **S2 HIGH · dark elf's confinement and reason.** TAKEN in part. The cell opens for the one it took from, and she says so: "It has never taken anything from me in here" (L435). Her finger was taken in the corridor. Her want is not written as interior (POV). Her terms are said aloud and carry the want: "I go where I like. Nobody hands me back. Nobody puts a door on me." (L459).
- **S3 HIGH · gate opens on an aimed catch.** TAKEN. The first two pushes are grabs and fail. On the third Eli stops holding and gives the lock the whole of it (L215). No aim, no listening.
- **S4 HIGH · blank has three owners.** TAKEN. Doc's "Nobody's" and the count-house blank are gone. The one blank is the cell's, and it is Ondry's (decision 5). Ysvet's own name is the struck first cut that she passes over (L345).
- **S5 HIGH · Teo crosses with no reason.** TAKEN (decision 7).
- **S6 HIGH · pit horn unplanted.** TAKEN. Pask's line from the row man's hut to the post, years back (L7). The ledger calls the horn LOCAL pending R-050. The ledger no longer cites ch07 for it. Patrick must rule R-050 before the horn is used again.
- **S7 MED · dark elf named in print.** TAKEN. The name is not printed anywhere in the story.
- **S8 MED · knife with no source.** TAKEN. "Where'd you get that?" / "Paid for it," she said. That was all. (L329–331.)
- **S9 MED · hand through the bars at the ninth cell.** TAKEN (cut). The upper rail is seen only from below by Eli, so the hand is not visible to him, and the scene is not in Seffa's view.
- **S10 MED · cold into Teo's stump.** TAKEN (decision 6).
- **S11 MED · count logic muddled.** PARTLY. "It wants his" is cut. "Living first, it read" stays. REJECTED: adding "the count reads the living to find the names it still needs." That is an explanation of the count's logic, and the audit left the workings unexplained by design.
- **S12 MED · POV breaks.** TAKEN (decision 1).
- **S13 MED · a night is missing.** TAKEN. The slot lamps dim while they come down the gallery, and Doc says it is night (L291). The exit is at first light.
- **S14 MED · too much at once.** PARTLY. The gate and grille rules now share the one phrase "gift as given" and are each a single line. REJECTED: cutting the corridor to one step-back. Brief shape 3 names the corridor trap as a set piece, and the chapter has no other mechanism of that kind.
- **S15 LOW · tall boy's lie and motive.** TAKEN. Seffa gives the reason: "He can't do a ladder on his own with that arm… I'll keep him where I can see him" (L273). Eli does not say anything about being read.
- **S16 LOW · which arm and hand.** TAKEN. Right little finger, right forearm rag, Seffa holds the "good" (left) arm.
- **S17 LOW · pot left and never mentioned again.** TAKEN. Eli watches Seffa leave it under the lamp (L283). At the bridge: "She had no pot" (L553).
- **S18 LOW · "went to stone."** TAKEN. "The old man's weight went heavy, and stayed heavy" (L507).
- **S19 LOW · cart men "told to wait."** TAKEN. Oskel brought the cart down from four and the men came with him (L545).
- **S20 LOW · "from the crate."** TAKEN (cut). The clause is gone.
- **S21 LOW · Doc obeys "Sitter" without a reason.** REJECTED. Flag asked for one line of Doc seeing her hand on the old man's chest the way his was. That would be Doc's nature stated on the page, which the audit forbids. Doc's hand going back into his coat and his face "shut like a door" carries it, and Eli "did not know what the word meant."
- **S22 LOW · SIRRIN.** REJECTED. Flag asked for a line on who SIRRIN was to her. That is a stated motive. The flake is the chapter's token for S-129 and stays unexplained.
- **S23 LOW · Eli's wish to write the account.** TAKEN. Now a want with no cost: "I'd like my name in it, Teo, with the rest of you."
- **S24 LOW · telling lines.** TAKEN. "He did not like what it cost to stop" cut. "Teo had not meant it" becomes "Teo looked at it as if somebody else had done it." "The old man was the blank" cut.
- **S25 LOW · the bridge line's speaker.** TAKEN. "Where you can see me," said the boy.

**Dark elf reasons (sense review, four points):**
- Cell shown shut to her: TAKEN (see S2).
- She is never shown wanting out: PARTLY. Her terms and her "thirty" carry it. No interior want line (POV).
- Accepts the seam once: TAKEN in part. "Yes" from Eli, then from Teo, then "Two." She goes through on her own step after Ondry's "Go" and her palm on his chest (L521–525).
- Cost real, and the turn pushed by Ondry's line: REJECTED. The flag said let her decide first. Patrick's binding and audit N12 make Ondry's price the thing that falls on him. Her acceptance comes before his "Go" (the terms, the flake) and his line makes the cost fall, which is the design.

## 2. review_continuity_v1.md (15 contradictions and notes)

- **T1 walk back to the pit.** TAKEN (pit opening names the lane past Pask's gate).
- **T2 the ninth tied to the count.** TAKEN. Teo read the date off the row man's book that morning (L13).
- **T3 tall boy's exit vs ch07.** TAKEN (pit clause L7; bridge line L547).
- **W1 Doc's cost onto another body.** TAKEN (decision 6).
- **W2 two comm devices.** PARTLY. The pit horn is now a line run from the row man's hut (Pask's). It is one relay branch, not a second device. Ledger corrected. R-050 is still open (Patrick).
- **W3 R-050 "city" quote.** TAKEN. The ledger no longer quotes ch07 for it.
- **W4 reach-when-watched (state L402 vs R-016).** TAKEN in ch08: the draft is consistent with R-016 as reframed (strangers look up: Ysvet watches the bars and the reach fails; friends watch and the gate opens). The state file's line 402 is NOT edited (out of this chapter's files). Flag for the state update.
- **W5 count rules not in ledger.** TAKEN. Listed as LOCAL in the ledger.
- **F1 tall boy's stump left vs right.** TAKEN (right little finger).
- **F2 teeth "nothing in it" vs four out.** TAKEN ("four teeth loose in it").
- **F3 Seffa's sleeve used twice.** PARTLY. The good wool sleeve goes round the finger at the landing; the coughs go "into her sleeve," which is not disambiguated. Unsure, listed in the ledger. A one-word change ("her other sleeve") is available if Patrick wants it.
- **F4 Teo's binding used but never done.** TAKEN (Doc binds with a strip of his own shirt, L439).
- **F5 Pask's chain moves from gate to pit.** TAKEN. The pit's chain lies off its post (L25).
- **F6 ledger names Ysvet as withheld.** TAKEN. The ledger now reads "not printed and not given."
- **F7 pallet status (ch07 vs state).** REJECTED for ch08. It is a state update, outside this chapter's files. The pallet line in ch08 ("the look he'd had at the pallet") does not contradict either version.
- **N1 POV breaks.** TAKEN (decision 1).
- **N2 LEDGER inside the draft.** TAKEN. The draft keeps its engine ledger at the end (per the engine rule); `CH08_STORY_ONLY.md` has none.
- **N-C1 Doc refuses Eli's hand.** REJECTED. The review said "not a clash." The reason is on the page ("You've bled on the lock"), and the audit (F7) keeps it.
- **N-C2 Jon knows where they are ("I jumped from here").** REJECTED: kept. Brief shape 1 and R-034 need the line. It is a fact ch09 must respect (note for ch09).
- **N-T1 the night is unmarked.** TAKEN (see S13).
- **N-F1 Eli's hand, new cost.** TAKEN as a ledger entry (costs in §5 below).
- **N-F2 Teo's index.** TAKEN (logged).
- **N-F3 Seffa's palm grey line.** TAKEN (logged; present at L299).
- **N-F4 "strapmaker."** REJECTED for ch08. The label is not in this chapter's text any more (the strapmaker's gate is ch07 only).
- **N-S1 "It's dirt. Not a thread."** TAKEN. Eli does not know what a thread is and nods (L253–255).
- **N-S2 "You had a pot."** PARTLY. The pot is on the landing and Ysvet's line stays as a count-joke. REJECTED: answering the ch07 "Where's my pot?" in ch08. That is outside this chapter.
- **N-S3 "old man" label shared with ch07.** REJECTED. Eli calls the master "the old man" in ch07 too, and the cell prisoner is "the old man" throughout ch08. Splitting the label is Patrick's call, not a craft fix.

## 3. review_payoff_v1.md

- **§1 seed cap.** Five Book 1 seeds (S-123 to S-127) and three future seeds (S-128 to S-130) stay as the cards set them. Not re-counted.
- **§2 S-127 telegraphed.** TAKEN. Cut the "blank" identity sentence; the price is said only after the seam takes nothing from Ondry.
- **§2 S-115 door on the ninth.** No change needed.
- **§2 S-123 lintel joint.** No change. Paid on Teo's right index (L431).
- **§2 S-119 the tall boy's rag.** TAKEN. Closed: the rag goes back on his forearm, "Dirt. Not a thread."
- **§2 S-007 Teo's cool head.** No change.
- **Internal "Rule's for slow ones" → "I was quick."** No change. Kept.
- **Internal "We'll carry him out" → "Who carries him" → can't.** TAKEN. The line is flat with no question mark, and the narration says "It was not a question. He answered it anyway."
- **§2 S-002 Teo's warnings.** Kept, no change. No new warning added. The payoff-keeper's "do not add another" is respected.
- **§2 S-038 Jon's absence.** No change.
- **§2 S-032 Jon's price.** No change. "I jumped from here" stays, and it is a fact for ch09.
- **§2 S-005 the reach.** PARTLY. Eli's misread: "It was a good reach… no one had ever told him a gift could be refused like that" (L499).
- **§2 S-006 freeze.** PARTLY. Two grabs fail and the third works as a whole gift (not aimed). R-016 as reframed.
- **§2 S-050 Seffa.** Kept.
- **§2 S-061 Doc.** REJECTED for ch08: naming a payer is Patrick's call. Doc's refusal and bandage are kept as set.
- **§5 bad hand over cap.** PARTLY. Eli's bad hand or arm is named 11 times in the first count; three mentions cut (the lintel's second "bad hand," the seam's "bad hand," and "bad arm" in one place). Still about eight: over the cap of five. Flagged. The hand is the cost thread, so it is kept.
- **§5 "coat" eleven uses.** PARTLY. Cut to six: the sling, Doc's pocket, the shoulder, the pocket on the walk out, and the pocket at the pit. Remaining uses are Teo's coat, which is his object. Flagged as over the cap of five.
- **§5 "You said" three.** TAKEN. Two uses, plus "I'm saying again."
- **§5 "a hand's width" three.** TAKEN. Two uses (gate L217, grille L433).
- **§5 counted numerals.** REJECTED. Patrick did not ask for a count cap, and the count is the chapter's subject.
- **§5 similes cap of five.** REJECTED. Patrick's list (decision 9) covers tics, not similes. The count-house, corridor and counter need comparisons in the Eli register. About ten remain.
- **§5 Teo's "Right."** Kept (once in the lower gallery, mid-scene).
- **R-054 gate vs grille gift.** TAKEN (decision 4).
- **R-057 seam wording.** TAKEN as "takes what has been read through." MAGIC_DESIGN's "reads only what it can grip" is still on the books; Patrick chooses.
- **Overdue S-008, S-019, S-047, S-030, S-106, S-061, S-056.** REJECTED for ch08. The cards deferred S-008 and S-019 to ch09 and S-032/S-106 later. S-047 is unpaid and misapplied (audit F20). S-056 "the room" stays open. S-030 ("ch08 squad") was dropped silently in v1 and is now a flag for Patrick (ledger).
- **R-047 / R-060 watch.** TAKEN (decision 6).
- **R-050 relay.** Unruled. Flagged for Patrick.
- **R-027 untrained reach.** Kept: the reach "went wide" at the seam (L499).
- **R-043 listening.** TAKEN. The aim is gone. The listening theory remains live through the moths in ch07 and Eli's "I'm listening all the time," which the chapter does not repeat.

## 4. review_forecast_v1.md (invalid run; setup list only)

The forecast's own method note says the run was not blind. Its scores are ignored. Its setup list is used:
- The pencil on the short string: TAKEN in part. Eli wants his name in the account (L83), and it is never written. Texture under S-002.
- Doc's "Not you" (the lock): kept, with its reason on the page.
- Seffa's sleeve and "It's dirt. Not a thread.": TAKEN. Eli's misreading turns it into a small beat.
- Ysvet's right hand: kept. Eli sees it held close (L327) before the reveal (L441).
- "You said that before" overuse: TAKEN (two uses).
- The old man stays, telegraphed: PARTLY. "Go. Or you're counted with me" and "I'm counted already" stay. The arithmetic moves to the seam.
- Closing "It went on. It went on.": TAKEN. The ending is the horn's hiss, and Eli waits for it to stop, and it does not.
- Lowest-tension scene (the rail): PARTLY. The rail is now seen from below by Eli, with the pot set down under the lamp. REJECTED: adding a threat. The landing now carries the split and the pot.
- Jon as a thin thread: REJECTED. Brief shape 1 and 7 keep him on the relay.
- Doc "no visible turn": REJECTED for ch08. The refusal and the bandage are his beats.

## 5. Departures in fix_log_v1.md, reviewed

1. **Doc and the stump (scene 2).** Audit wins, kept. Doc binds with a shirt strip (L439); the first stump is "I've no bottle left" with no touch.
2. **The counter's rule, as Teo's line.** Kept. "It takes back what it sees" stays. Same mechanism as the cards.
3. **"Who carries him" with no question mark.** Withdrawn as a departure. The cards have the question mark, but cast §1 says she never asks. The line stays flat, and the narration says so.
4. **Teo's cross: "reads him through" not "finishes him."** Kept.
5. **Groove for Teo at the lower grille.** Kept. The rail-corridor groove outside her own cell is only in her speech.
6. **Ending: cough goes on.** Kept in form. The last beat is the horn's hiss; Eli hears "a cough" once, not as a button.
7. **The carry: arch "slackened" not "flat."** Kept.
8. **Gate farewell callback to ch07.** Changed. The bridge line now ties to ch07's yard gate (decision 3), which Eli saw, not Ysvet.
9. **Two stock similes cut.** Kept.
10. **Name use.** Ysvet is not printed in the story. Ondry is not printed. SIRRIN is printed as a cut name.

## 6. New costs to log (for the state file)

- Eli's bad hand locked shut after the gate (L221), and nosebleed (gate L223; grille L365).
- Teo's right index, top joint, taken by the counter (L431).
- Ondry's four teeth, taken (L409).
- Seffa's palm, a grey line from the grille (L299).
- Ysvet's cough-take, blood in the sleeve (L321, L521).
- The boy's right little finger, top joint, taken at the count-house groove (L109). The right forearm is still skinned (ch07).

## 7. Riskiest change

The seam's rule (decision 5): "The seam took what the count had finished with" and "It takes a name only when it's read through. His never was. He's the blank." Both lines are new on the page, and they are the chapter's only statement of how the seam chooses. If Patrick wants the rule left unstated, cut L501 and keep L491. Ondry is still refused by the seam, and the reader still has to work out why.
