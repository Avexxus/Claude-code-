# Recurring issues: what the pipeline kept catching (Book 1 v1, the sample, v3 ch1–7)

🌊 Claude analysis for the Engine v3 ("foundry") overhaul, 2026-11-21. Not canon. Nothing else was edited.

**Read for this:** every `review_*`, `author_calls*`, `rebuttals*` and outside-read file under `stories/book1-emperors-son/v3/` (ch01–ch07, `outside/`, `outside_reads.md`, `revisit_later.md`); `stories/book1-emperors-son/reviews/` (v1 craft, logic, lore, plus `outside/grok_gemini_on_v1`); `work/sample/reviews/` (all); Patrick's craft and process notes in `decisions/BANK.md` and `decisions/BANK_passed_2026-10-31_to_11-17.md`. Commit messages were checked for interruptions.

**Path shorthand:** `v3/` = `stories/book1-emperors-son/v3/` · `rev/` = `stories/book1-emperors-son/reviews/` · `sample/` = `work/sample/reviews/` · `BANK` = `decisions/BANK.md` · `BANKp` = `decisions/BANK_passed_2026-10-31_to_11-17.md`.

**Agents named:** sense = sense-checker · cont = continuity-keeper · pay = payoff-keeper · dlg = dialogue-editor · words = word-watch · fcst = forecaster · panel = reader-panel · orig = originality-check · outside = Grok, Gemini or a fresh Claude, pasted by Patrick.

**How to read the counts:** "chapters" means v3 ch01–ch06 (ch07 has only a plan check). "Passes" means review rounds: v1 book, sample v1–v10, and each v3 draft round. "Late" means the item was caught after a draft had been through at least one full review round, or after a lock, or by an outside reader.

---

## Ranked catalogue

Ranked by how often the problem came back multiplied by how much fixing it cost. Each kind gets a script verdict: **YES** (a script can catch it outright), **PARTLY** (a script can flag candidates for an agent to judge), **NO** (it needs judgment).

---

### 1. Word tics, verbal habits and repeated motifs
- **Recurred:** every chapter and every pass, roughly 25 or more separate flags. Each fix pass threw up a new tic in place of the old one.
- **Examples:**
  - "didn't" 94, "Nobody" 54, "a long time/while" about 17 across the old 19k book (`v3/outside_reads.md`). After that, ch01 v5 still had "didn't" 48, "looked" 52, "something" 34, "then" 53 (`v3/ch01/review_words.md`).
  - "The 'never/ever' superlative tic… That's at least eight" and "The 'since they were' habit tag… four times to fake history" (`v3/ch01/review_panel_v9.md`). This is the same "ever" fog the fresh Claude found in the sample (`sample/fresh_claude_review_2026-11-09.md`).
  - "the gate is open 'a hand's width' five times… 'He laughed a bit longer than there was anything to laugh at'… word for word for the pad man and for Hollin" (`v3/ch05/review_panel.md`). Then ch06: "'cup' ×12… Doc's ears ×9… 'at no (particular) speed' ×3" (`v3/ch06/review_payoffs.md`).
  - Also: "Teo. Look." about 6–8 times in ch04 (`v3/ch04/review_panel.md`, `review_dialogue.md`); "studied" 6, Jon "smiled" 6, "ya" 6 (`v3/ch03/review_payoffs.md`); "Eli laughed" 4–7 times (ch01 panels); "face did nothing" twice (`v3/ch06/review_panel.md`); "didn't look" on 23 lines in v1 (`rev/v1_craft.md` A1).
- **Caught by:** words, but also pay (every payoff review has its own "Repetition caps" block), panel (the hater and the literary reader) and outside readers. **Late:** often. The words pass runs after drafting and dialogue, so the panel keeps finding tics that words didn't count ("never/ever" and "since they were" in ch01 v9, "hand's width" in ch05). Several words reports counted by Grep and said "rerun `scripts/wordcheck.py` to confirm" (`v3/ch01/review_words.md`, `v3/ch03/review_words.md`).
- **PREVENTION:** Give the writer the live tic list (book-wide counts plus this chapter's caps) before drafting. No gesture, phrase or simile shape may appear more than twice per chapter, and none can be copied word for word from an earlier chapter unless it's a logged motif.
- **Script?** **YES.** `wordcheck.py` plus a cross-chapter verbatim-sentence check and a per-chapter cap file. Run it automatically after every draft, not by hand.

### 2. Neat, explaining or riposte dialogue
- **Recurred:** every chapter (ch01 ×2 passes, ch03, ch04, ch05, ch06), plus v1 and the sample. Patrick flagged it himself: "it always feels so clunky… just exposition" (BANKp 2026-11-16).
- **Examples:**
  - "Eli explained the plot to Teo, who already knew it. Velk explained the world twice. A few lines landed as neat ripostes" (`v3/ch01/review_dialogue.md`). Again in v8: "It was a plot summary for the reader" (D10, the crewman's King line, `v3/ch01/review_dialogue_v8.md`).
  - "It was a rule recited for the reader… It was a tidy recap for the reader… Eli was stating his own theme twice" (`v3/ch03/review_dialogue.md` D1, D4, D12).
  - "He was telling Teo Teo's own life in clean sentences… a neat riposte… a two-beat epigram" (`v3/ch04/review_dialogue.md` D1, D8, D12); "The old line stated his watched-reach rule outright… an epigram button… a two-beat riposte" (`v3/ch05/review_dialogue.md` D3, D6, D9).
  - The deathbed and confession backstory dump came up again and again: "The dying flashback… is still backstory told to the reader by a dying man" (`v3/ch01/review_dialogue_v8.md` flag 1); "Ilder's path speech… is still backstory told to Eli" (`v3/ch03/review_dialogue.md` flag 2); "The dying speech that ties a bow" (`v3/ch03/review_originality_ch01-03.md` B1).
- **Caught by:** dlg every time, then panel and orig on what dlg left. **Late:** yes. dlg runs on v2 or v3, after sense and continuity have already approved the scene's content. It can't change events, so it keeps writing "Flags for the writer (can't fix without changing events)".
- **PREVENTION:** No character tells another something both of them already know. No line may be quotable out of context unless it's Patrick's. A speech is allowed only if the body or the listener breaks it. Backstory arrives through action or a dodge, never as a set piece.
- **Script?** **PARTLY.** A script can flag lines over a voice's word cap (from `voice_notes.md`), adverb and bookism tags, and two-sentence lines with a period in the middle that end on a short clause (the riposte shape). Exposition needs judgment.

### 3. Planning files, NOTES and fix logs contradicting the text
- **Recurred:** every chapter, and every plan check (ch04, ch05, ch06, ch07: 11–14 flags each, one HIGH). Also v1 and the sample.
- **Examples:**
  - "The NOTES fix log in `draft_v6.md` is stale… it quotes lines that aren't in the text" (`v3/ch01/review_continuity.md`). In v7 the fix log said the seed cap "6 + 3 holds", but the real count was "10 open Book 1 seeds and 6 FB" (`v3/ch01/review_payoffs_v7.md`).
  - "'The name Jon gave': Jon gave no name (P§2)", rated HIGH (`v3/ch05/review_plan_continuity.md`). Others: "the Tower's pressure, which only Eli feels" (ch04 plan, `v3/ch04/review_plan_continuity.md` #1); "Teo's line is past the shoulder now, not the elbow" (`v3/ch06/review_plan_continuity.md` P1); "The sock can't 'come back up'" and "Orcs can't come up the Long Stair" (`v3/ch02/review_continuity_split.md` P1, P2).
  - The ch07 plan reuses "Don't use more than you can control" as if it were new ("used once and earned"), but it was already spent at 5:L245. It also plans a handset "in the coat" when every pocket of that coat has been searched on the page (`v3/ch07/review_plan_continuity.md` P1, P2).
  - Also: "`ch02/review_king_redo.md` logs the chip as 'sunk in a plate the size of a palm', but the text has it 'At the back of his neck'" (`v3/ch04/review_continuity_v5.md` #6); "STRESS_LOG S3 says… v10 line 45 still has…" (`sample/audit_v10.md`).
- **Caught by:** cont, which is the only agent that reads plans against `story_state.md`. **Late:** the plan checks run before drafting, which is good. But planners keep writing from memory instead of from the state file, so every plan arrives with 11–14 breaks.
- **PREVENTION:** The planner writes only from `story_state.md` and the knowledge table, and cites a page line for every fact it reuses (objects, injuries, who knows what, lines already spent). A fix log may quote only text that exists in the draft it sits in.
- **Script?** **YES** for the mechanical half. Check that every quoted string in NOTES, fix logs and change logs occurs in the current draft. Check that every `L###` cite's quoted text appears at or near that line. Flag plan facts that have no state cite.

### 4. Breaking rules the page has already stated
- **Recurred:** every chapter, with 2–4 per chapter. The main repeat offenders were R-016 (reach fails when watched), the fob rule, the slot and reader rules, and the lean.
- **Examples:**
  - The fob rule broke four times: a v6 watch item, then flagged in v7 by cont and by sense #9, then "ONE now shows that a fob only works on its own house's orcs. But Vosk's dying story… has the Ilder father's fob working on a boy from Eli's house" (`v3/ch02/review_sense_split.md` #1).
  - "the reader has just learned that Eli's reach fails when he's watched, then learns a man sat ten yards off watching the whole lift" and "Seffa's catch of the cup reads as Eli's reach working while he's watched" (`v3/ch05/review_sense.md` #1–2; the same two items appear as `review_continuity.md` C2–C3 and `review_payoffs.md` #1).
  - "The gutter carries the core 'toward the Tower, uphill'… But 4:L23 says walking out, away from the Tower, is uphill" (`v3/ch04/review_payoffs.md` #1; also cont 1a and sense #4).
  - Also: "The gate greets Teo without a name" (`v3/ch02/review_continuity_split.md` W1); "the slot shocked him for fourteen minutes' lateness this morning, yet it lets him out at night with nothing" (`v3/ch01/review_sense_v7.md` #6, then again `v3/ch02/review_sense_split.md` #9); "The orc gate bites a man ten places back" (`v3/ch04/review_sense.md` #5); "the checkpoint 'reads Teo's fever'" (ch04 plan); "R-027… is eroding" (`v3/ch05/review_payoffs.md` #6); "The landing numbers can't be true" (`v3/ch01/review_sense.md` #4).
- **Caught by:** sense, cont and pay, very often all three on the same item. **Late:** rarely late inside a chapter, but the same rule broke again in the next chapter because the writer never saw `ledger_rules.md` as a checklist.
- **PREVENTION:** Before drafting, the writer gets the five or six rules this chapter's scenes touch, each with its exact page wording ("reach fails when he *believes* he's watched", "a house fob drives its own orcs; the father's drives any", "readers light humans, bite loitering orcs at the disc"). Any scene that bends one must say why on the page.
- **Script?** **PARTLY.** A script can list which rule keywords (fob, slot, reader, disc, reach, gate, lean) appear in the draft and attach those rules to the review. Judging a break needs an agent.

### 5. Object, injury and hand-state drift
- **Recurred:** every chapter (ch01 ×2 passes, ch02, ch03, ch04, ch05, ch06), plus sample v10. Grok flagged Eli's hand in both ch5 and ch6.
- **Examples:**
  - "The chip scar is flat, then raised… The apple core goes out the door, then lies inside it… Teo's cut hand: 'the hand that worked', then he uses it" (`v3/ch01/review_continuity.md` #4–6).
  - "Eli's hand, a vanished injury… he picks the knot 'with his nails'… The partial fist isn't mentioned anywhere in FOUR" and "Teo's coat… No coat [in THREE]" (`v3/ch04/review_continuity.md` 4a, 4b).
  - "The sock is knotted, but the coins scatter… The knot is never undone on the page" (`v3/ch06/review_continuity.md` F1). The same chapter's blanket vanishes (F2).
  - Also: "the 'two' counted on top of the watch" (`v3/ch03/review_continuity.md` #1); "The pills: white ones were never in a twist", "Where the board is" (`v3/ch05/review_continuity.md` A2–A3); "The hand still improves or fails without being marked" (`v3/ch05/outside/grok_ch05.md`); "The hand is inconsistent" (`v3/ch06/outside/grok_ch06.md`); "The peach and two hands… The ruined arm" (`sample/audit_v10.md`).
- **Caught by:** cont. **Late:** the hand was late both times, because Grok caught it after the chapter had passed cont.
- **PREVENTION:** Open every scene card with a one-line inventory for each person: what's in their hands and pockets, what they're wearing, and every injury with its current state (the hand: "partway; cold stiffens; a big reach locks it"). Any change must happen on the page. Mark the hand once per chapter.
- **Script?** **PARTLY.** A tracked-objects list (sock, letter, watch, coat, pills, hand, Teo's palm) can be grepped per chapter. The script would report each mention in order and flag a chapter where a tracked injury never appears.

### 6. Geography and timeline slips
- **Recurred:** every chapter, plus the sample.
- **Examples:**
  - "The return lands at the morning-count hour, but the bell is the night count" and "The shaft 'off the sumps' is reached too fast" (`v3/ch01/review_continuity.md` #1, #3); "A soft Terrace boy climbs down the full height of the Long Stair on a ladder" (`v3/ch01/review_sense_v7.md` #3).
  - "The time jump between the two POV blocks reads as night… 'at a quarter past eleven'" and "The clock doesn't add up" (`v3/ch02/review_sense_split.md` #3–4).
  - "'Three mornings' is four" (`v3/ch03/review_sense.md` #9); "Two hours go missing between the culvert and the checkpoint" and "The cloud is both above and below the city" (`v3/ch04/review_sense.md` #6, `review_continuity.md` 3a); "The headache 'for four days'" (`v3/ch05/review_continuity.md` A1); "'all the first night' while it is still the first night" (`v3/ch06/review_continuity.md` T1).
  - The sample's cold reader: "Ch 1, where are we?… I never knew which world Eli grew up on or ran from" (`sample/cold_reader_v10.md`).
- **Caught by:** cont and sense, often both on the same item. **Late:** a book-wide calendar wasn't built until ch06 (`v3/ch06/review_continuity.md` Part B), five chapters in.
- **PREVENTION:** Keep a running day-by-day calendar and a vertical map (Terrace, mid-levels, sumps, Scald, Spur) in `story_state.md` from chapter one. Every scene card states its day, its hour cue (bell, horn, light) and its height or place on that map, and every "N days ago" must be checked against the calendar.
- **Script?** **PARTLY.** A script can pull time phrases ("three days", "four nights ago", "this morning", clock times, weekdays) into a table for cont to check against the calendar.

### 7. Quest markers and convenient arrivals
- **Recurred:** Patrick's own flag on v1, then the sample (Grok ×3), then ch01, ch02, ch03, ch04, ch05 and ch06. That's about 10 passes.
- **Examples:**
  - Patrick: "We need a healer. Feels to video game… What other scenes could I rework this same way where its to quest marker or do x" (BANKp 2026-11-10; Grok's list is in `rev/outside/grok_gemini_on_v1_2026-11-10.md`). Grok on the sample: "Everything arrives exactly when the plot needs it" (`sample/grok_review_2026-11-08.md`).
  - "The arch falls exactly when Vosk reaches it… Teo has the sump rota up 'since the purse came out'" (`v3/ch01/review_panel.md`, the hater); "Teo's ladle comes to hand on cue" and "Velk says 'Don't' with her back turned" (`v3/ch01/review_sense_v7.md` #8, #10).
  - "'Nobody came in' rests on a log invented on cue" (`v3/ch03/review_sense.md` #3); "the crate falls in the one moment nobody is looking up the ramp" (`v3/ch04/review_panel.md`); "The other teacher is across the lane from the dead one… Eli walks into it by chance" and "Hollin shows up on cue with a chip and a nosebleed exactly when the reader needs the chip explained" (`v3/ch05/review_sense.md` #4, `review_panel.md`).
  - "Doc walks out on a full ward within a minute of one shove… with a risk of reading as a quest marker" (`v3/ch06/review_sense.md` #1).
- **Caught by:** sense, panel (the hater) and outside readers. **Late:** usually, because these are structural and are baked in at plan level.
- **PREVENTION:** Every arrival, find, tool or rescue needs a cause planted at least one scene earlier, one that a character would mention anyway. If a person, object or exit shows up exactly when needed, add friction: a delay, a cost, or a failed first try.
- **Script?** **NO.** It needs judgment, though a planner checklist ("where was this planted?") can force the question.

### 8. Characters acting for the plot ("why doesn't X just…")
- **Recurred:** ch01 ×2, ch02, ch03, ch04, ch05, ch06, plus v1 logic and the sample audit (10 missing reasons). That's about 9 passes.
- **Examples:**
  - "The cutter attack has no motive… The King's own man slashing at the prize's face makes no sense" and "Nobody follows the prize" (`v3/ch01/review_sense.md` #1, #10). Also "Why tonight? Vosk acts for the plot" (`v3/ch02/review_sense_split.md` #2).
  - "Eli isn't afraid of a big stranger in his kitchen the morning after 'He's asking'" (`v3/ch03/review_sense.md` #1); "Jon queues Eli for a reader arch" (`v3/ch04/review_sense.md` #1).
  - "The Queen hears 'we don't kill him' and says nothing" and "The dragon lord lets his hunter's killers… walk off" (`rev/v1_logic.md` #4, #6); "Throne room: why do they fight one at a time?" (`sample/audit_v10.md`); "Characters cooperate with the plot instead of resisting, delaying or choosing badly" (`sample/grok_review8_next_steps_2026-11-08.md`).
- **Caught by:** sense and the v1 logic attack. The audit and cold reader created the check on the sample after the fresh Claude found it missing. **Late:** in v1 and the sample, yes; in v3 sense catches it on draft v1.
- **PREVENTION:** For every scene, character-sim answers in one line each: "What does each person present want right now, and what would they do if the plot didn't need them?" The writer drafts from those answers. Any powerful person who doesn't act gets a visible reason.
- **Script?** **NO.**

### 9. Telling: narrated feelings, glosses and meaning stated
- **Recurred:** ch01 ×3, ch03, ch04, ch05, ch06, v1 craft (F10, A2) and the sample. Patrick: "you have stuff that just feels way to spelled out" (BANKp 2026-11-07) and "still way to forward with telling not showing" (BANKp 2026-11-16).
- **Examples:**
  - "'He wanted to tell someone.'… 'Eli laughed out loud, mostly from relief.' Cut 'mostly from relief'" (`v3/ch01/review_sense.md` #12); "'He thought that was courtesy. He said so to Teo, who didn't answer.' is the author nudging me" (`v3/ch01/review_panel.md`); "'on the breath he'd been keeping for it'… telling inside close third" (`v3/ch01/review_sense_v7.md` #12).
  - "'the house was quiet in a different way from before'. It tells me there's a mood without saying what it is" (`v3/ch03/review_panel.md`); "'His good hand had stopped shaking. He noticed that, a long way off.'… 'It looked like a hand.'" (`v3/ch04/review_panel.md`).
  - "'the way a boy looks at a man who's done something he wants to do'… explains a look" (`v3/ch05/review_sense.md` #13); "'She had a look on her he couldn't read. It went on a while.'" (`v3/ch05/review_panel.md`); "Seffa spells the laugh" (`v3/ch05/review_payoffs.md` #5).
  - The narrator explaining its own callbacks: "Twelve is a study guide" (`rev/v1_craft.md` A2).
- **Caught by:** sense, panel and pay. **Late:** the panel catches what sense misses, at v3–v4.
- **PREVENTION:** Never name a feeling, explain a look or say why a callback matters. End the beat on the action or the object. Purpose clauses ("to find the next bite"), "mostly from", "couldn't read", "in a different way" and "a long way off" are banned.
- **Script?** **PARTLY.** Filter-word and phrase list (felt, realised, seemed, couldn't read, "in a different way", "mostly from", "the way a … looks at", "as he had…") plus a count of "as he had / the way he'd" callbacks.

### 10. Narrating or interpreting Jon
- **Recurred:** v1 (14 instances), the sample, ch03, ch04 and ch05. Then ch06 ran the same leak through Doc (steering the reader at his nature).
- **Examples:**
  - "He was sorry. He said so, and looked it" and "The man against the fence had died for nothing, and Jon had known" (`rev/v1_craft.md` C1–C2).
  - "'He said it round the plum, plainly'… 'turned the plum to find the next bite'… 'not at the watch'… 'He was very clear.'" (`v3/ch03/review_sense.md` #7). The dlg pass on the same chapter also found Jon "explaining someone Eli already knows" (`v3/ch03/review_dialogue.md` D5, D7).
  - "the staging does. It's the vanish trick… a 'Jon knows / Jon is more' beat" (the cart exit, `v3/ch04/review_sense.md` #9); "'Nobody had given him one' (narration…) still sits close to explaining Jon" (`v3/ch05/review_dialogue.md` flag 2).
  - The Doc version: "the only line in the chapter that steers the reader toward 'something is in him'" (Teo's look compared to the chip scar, `v3/ch06/review_sense.md` #2).
- **Caught by:** sense (strict-Jon section) and dlg. **Late:** in v1 it was found only by the hostile craft read. In v3 sense catches it on draft v1, but the next chapter's writer reintroduces it.
- **PREVENTION:** Jon gets action, sight and speech only. No adverbs of manner (gently, pleasantly, plainly), no purpose clauses, no "not X" noticing, no verdicts by Eli, and no staging that makes him uncanny (vanishings, impossible timing). The same applies to any character whose nature is withheld (Doc).
- **Script?** **PARTLY.** Within N words of "Jon" or "the man", flag: -ly adverbs, "as if/as though", "to + verb" purpose clauses, "knew", "not at", "very".

### 11. Seed overload
- **Recurred:** ch01 (v1 and v7), ch03, ch04, ch05 and ch06: over the cap or at it every time. Patrick: "You cant have 24 seeds in chapter 1 dude" (BANK 2026-11-17).
- **Examples:**
  - "Seven accidental seeds need a yes or no from the plan" (`v3/ch01/review_payoffs.md`); "The seed cap is over… my count is 10 open Book 1 seeds and 6 FB" (`v3/ch01/review_payoffs_v7.md`).
  - "Seed cap: 8 new Book 1 seeds against a cap of 6" (`v3/ch05/review_payoffs.md` #4); "Seed cap: 7 against 6… Demote the baby to texture" (`v3/ch06/review_payoffs.md` #2).
  - "The camera adds 3" accidental seeds in ch04: the headache link, the man in house colours and the stern knock (`v3/ch04/review_payoffs.md`). Also "The descent is a seed parade" (`v3/ch01/review_sense.md` #11).
- **Caught by:** pay. **Late:** always after drafting. The writer's own seed count was wrong in v7.
- **PREVENTION:** The plan names the six Book 1 seeds and up to three future-book seeds by ID. Anything else lingered on is texture: mention it once, no second look, no character noticing it twice.
- **Script?** **PARTLY.** Count new seed IDs per chapter in `ledger_seeds.md` against the cap. Flag any noun phrase that appears 3+ times in a chapter and isn't a logged seed or motif.

### 12. Clue stacking (telegraphing)
- **Recurred:** the sample (Doc), ch01, ch03, ch04, ch05, ch06. Six passes.
- **Examples:**
  - "Three ovals in one chapter: TELEGRAPHED" (`v3/ch04/review_payoffs.md` #2).
  - "The Doc cluster is TELEGRAPHED… about 9 pointers in one chapter" (`v3/ch06/review_payoffs.md` #1). The panel agreed ("Over-seeded Doc tells", `v3/ch06/review_panel.md`), and so did orig: "two clues land on Doc in a row, before he has even appeared" (`v3/ch06/review_originality.md` #1).
  - "S13 is over-signposted (S9 and S12 both point at it)" (`v3/ch05/review_forecast.md`); "The master's power is HEAVY-risk… four cost signs" (`v3/ch05/review_payoffs.md` #3).
  - Also: "S-029, Jon knows: HEAVY by count" (`v3/ch03/review_payoffs.md` #6); the coat as bait "EARNED, at the limit… make five beats. Add no more" (`v3/ch01/review_payoffs_v7.md`); "Doc's healer plant is a touch loud" (`sample/grok_review2_2026-11-08.md`).
- **Caught by:** pay, panel, orig and fcst, often all four on the same cluster. **Late:** yes, after v1 every time.
- **PREVENTION:** Each secret gets a pointer budget in the plan: at most 2–3 per chapter, each with a plain surface reading. Never put two pointers in adjacent paragraphs, and never echo a word ("Might be three" / "Three").
- **Script?** **PARTLY.** If the plan tags pointer phrases, a script can count them and measure the distance between them.

### 13. Repeated beats and scene shapes
- **Recurred:** ch01, ch03, ch04, ch05 and ch06, plus the sample (the montage).
- **Examples:**
  - "this is the second place in a row that re-walks ch01 (lift core, eyes sorted by colour, hands in pairs)" (`v3/ch04/review_forecast.md` S2); "Ch01 world beats re-delivered" (`v3/ch04/review_panel.md` #3).
  - "Coming straight after S3 it gives a second beat of 'nobody's here'" and "That's the second quiet night against the wall in a row" (`v3/ch05/review_forecast.md` S4; `review_panel.md`); "the double vigil… two quiet sections of the same shape" (`v3/ch06/review_forecast.md`).
  - "Three times a plum is turned over and put back" and "the gate log… is laid out twice in full" (`v3/ch03/review_panel.md`); "One more unchanged re-run [of dog-kindness] becomes a tic" (S-004, `v3/ch04/review_plan_continuity.md` #4).
  - Teo's exam simile twice, "interested" echoed onto the King (`v3/ch01/review_panel*.md`); "It took them most of a year to cross the war… a checklist and I went numb" (`sample/cold_reader_v10.md`).
- **Caught by:** fcst, panel and pay. **Late:** yes.
- **PREVENTION:** A scene may not repeat the previous scene's function: two dead ends, two vigils or two tours in a row become one. A world detail from an earlier chapter returns only if it does new work, never as a re-listing.
- **Script?** **PARTLY.** Cross-chapter n-gram and noun-list overlap catches re-listed world beats. Scene function needs the plan.

### 14. Rhythm on autopilot: polysyndeton, wry closers, buttons, the perfect last image
- **Recurred:** every panel (ch01 ×2, ch03, ch04, ch05, ch06), v1 craft and the sample.
- **Examples:**
  - "The chapter keeps ending paragraphs on a short punchline: 'Dogs didn't last.' 'Orcs didn't ride the lift.'" (`v3/ch01/review_panel.md`); "Of about 55 scenes, roughly 14 close on a negated verb and 12 on a clipped line of dialogue" (`rev/v1_craft.md` A3).
  - "'and... and... and' chains on nearly every paragraph. It's McCarthy cosplay" (`v3/ch04/review_panel.md`); "the chapter never stops doing it" (`v3/ch05/review_panel.md`); "The polysyndeton engine" (`v3/ch06/review_panel.md`).
  - "A mild addiction to the perfect final image" (`sample/grok_review4_prose_2026-11-08.md`); "The letter is now the chapter-closer tic… the third chapter running" (`v3/ch06/review_payoffs.md` #4); "Teo's 'Right.' now ends both FIVE and SIX" (#5).
- **Caught by:** panel, then pay. **Late:** yes. No agent owns rhythm before the panel.
- **PREVENTION:** No more than one "and…and…and" chain per scene outside action. At least half of all scenes end flat or mid-business. No chapter may close on the same object or line as either of the previous two chapters.
- **Script?** **YES.** Count "and" per sentence, measure paragraph-final sentence length, and compare the last 10 lines of each chapter for shared objects.

### 15. Stock phrases ("the end of the", "the edge of the")
- **Recurred:** ch01, ch03, ch04, ch05 and ch06. Every author-calls file from ch04 on carries caps for them.
- **Examples:**
  - "the end of the 8 → 2, at the end of 7 → 2, the top of the 7 → 2, the edge of the 6 → 2, came out of the 6 → 1" (`v3/ch03/review_words.md`).
  - "'in front of him', 'the top of', 'the edge of', 'the end of' and 'at the top of' ≤2 each" (`v3/ch04/author_calls_v2.md` #8); "'the edge of the' ≤2; 'he looked at the' ≤2" (`v3/ch05/author_calls_v2.md` #13); "'at the end of the' / 'the end of the' ≤2" (`v3/ch06/author_calls_v2.md` #9).
  - "'in front of' 12" and "'the foot of the', 'on the far side', 'walked out of the'… 3 each" (`v3/ch01/review_words.md`).
- **Caught by:** words. **Late:** always after the draft. The caps are known, yet each new draft breaks them again.
- **PREVENTION:** The writer gets the banned 4-gram list up front, with a cap of 2 per chapter on any place phrase. Name the place instead ("where the hedge ended", "by the slot").
- **Script?** **YES.** `wordcheck.py` already does this.

### 16. Repeated sentence openings
- **Recurred:** ch01, ch03, ch04, ch05 and ch06.
- **Examples:**
  - "Opening 'Then he' 14 → 4… 'It was' 11 → 6… 'He was' 10 → 5" (`v3/ch01/review_words.md`).
  - "The man 9 → 5, He was 9 → 6, The steward 8 → 4, He stood 7 → 4" (`v3/ch03/review_words.md`).
  - "sentences opening 'He looked' ≤6, 'He was' ≤6, 'It was' ≤6, 'He didn't' ≤4" (`v3/ch05/author_calls_v2.md` #13); "openings 'Then he' ≤4, 'He went' ≤5, 'He looked' ≤5" (`v3/ch06/author_calls_v2.md` #9).
- **Caught by:** words. **Late:** after the draft.
- **PREVENTION:** No two consecutive sentences may open with the same two words. Each two-word opening has a cap of 4 per chapter.
- **Script?** **YES.**

### 17. Trope echoes and borrowed images
- **Recurred:** the sample, v1, ch01, ch03, ch04, ch05 and ch06. Every orig run found at least one.
- **Examples:**
  - Yoda, twice. First the flyer: "Eli once lifted 'the whole flyer up out of the lake with the water pouring off it'… This resembles Yoda" (`v3/ch03/review_originality_ch01-03.md` A1). Then, two chapters after the fix: "'You lifted it blind. You opened your eyes and it fell.'… the beat that makes a reader think 'that's Yoda'" (`v3/ch05/review_originality.md` #1).
  - The nosebleed (Eleven): "Since 2016 this is the signature image of Eleven" (`v3/ch04/review_originality.md` #1), then "Three nosebleeds here" (`v3/ch05/review_originality.md` #4).
  - The stock mentor and the stock smuggler: "'Everything's got a price, son.' That's a recruiter's line from a hundred other books" (`v3/ch03/review_panel.md`); "The master's kit is a stock set: cross-legged on the floor, eyes shut" (`v3/ch05/review_panel.md`); "'No names.' / 'After this I don't know you.'… every gruff smuggler" (`v3/ch04/review_panel.md`).
  - Also: the Mos Eisley sequence (ch04), the Gandalf kitchen (ch03), the Shaolin gate vigil and Karate Kid "wax-on" (ch05), "You never know who your neighbour is" body-snatcher line and Mirri Maz Duur (ch06), "proud of the man you've become" (ch01–03), "Hot's alive" as a fridge-magnet line (`v3/ch06/review_panel.md`). Patrick: "You tend to just use generic tropes" (BANK 2026-11-18).
- **Caught by:** orig and panel. **Late:** orig runs after the dlg pass and the panel, so fixes land as v4 polish.
- **PREVENTION:** For each power moment, mentor beat or recruitment, the writer names the stock version first and then picks this world's own image (chips, readers, the hand locking, flesh tech). Nosebleeds, "lifted it blind", gate vigils and mentor maxims are banned unless Patrick wrote them.
- **Script?** **PARTLY.** A watch-list of known trope phrases in `scripts/slop_list.txt` (nosebleed, "eyes shut… it fell", "price, son", "no names", "never know who your neighbour"). Recognition needs orig.

### 18. Name collisions (outside works, and internal double meanings)
- **Recurred:** ch01–03, ch04, ch05, ch06 and ch07 plan. Every chapter with new names produced one.
- **Examples:**
  - Outside works: "'Vosk.' He shares the name of the Na'kuhl leader in Star Trek: Enterprise" (`v3/ch03/review_originality_ch01-03.md` A2); "Hollin is Tolkien's common name for Eregion" (`v3/ch05/review_originality.md` #2), renamed Oskel; then "Nathaniel Garro is a lead character in the Horus Heresy books" (`v3/ch06/review_originality.md` #2), the next chapter.
  - Earth names: "'Dace' reads as an Earth surname" (`v3/revisit_later.md`); "The name 'Jon.' It's a plain Earth name" (`v3/ch03/review_panel.md`; declined, it's Patrick's).
  - Internal: "'Loader' now has two meanings" (machine vs orc labourers, `v3/ch05/review_plan_continuity.md` #6); "'He's grey' reads as 'he's an orc'" (`v3/ch05/review_sense.md` #9); "'depot' now has two senses" (`v3/ch03/review_continuity.md` #8); "'the ninth': no date has been on the page, and 'nine' is taken" (`v3/ch07/review_plan_continuity.md` C3).
  - Also: the invented King name "Rauk" was cut because the King is Patrick's character (`v3/ch03/author_calls_v2.md` #1).
- **Caught by:** orig (web search) and cont. **Late:** after drafting. Hollin and Garro were caught only at v3–v4, so the rename churned the notes and ledgers.
- **PREVENTION:** Run every invented name through a name check before it enters a draft: a known-IP search, an Earth-name test, and a check against the book's own word list. Never reuse an existing word (loader, grey, depot, nine) for a new thing, and never name a Patrick character.
- **Script?** **YES** for internal collisions (a name and term registry, with a check of each new term against existing terms and against common words used in another sense). **PARTLY** for outside IP (a cached list of famous fantasy and sci-fi names, plus a web-search hook).

### 19. Reader lost: unanchored terms, pronouns and references
- **Recurred:** ch01 (both panels), ch03, ch04, ch05, ch06 and the sample cold read.
- **Examples:**
  - "'I asked at breakfast and it came back before he'd put the slate down.' Who's 'he'?… The apple core floating across the kitchen. Did Teo do that, or Eli?" (`v3/ch01/review_panel.md`; both readers asked the same thing).
  - "The house-bell calls. I didn't know who 'madam' is… 'He's asking.' I wasn't sure who 'he' was" (`v3/ch03/review_panel.md`); "'The watch said nine.' Why does nine matter?… The italic line… I didn't know who was speaking… 'Earth'" (`v3/ch04/review_panel.md`).
  - "'not one of them grey' and then 'He's gone grey.' Is grey a kind of person?" (`v3/ch05/review_panel.md`); "'Three.' I didn't know what it meant" (`v3/ch06/review_panel.md`).
  - Also: "Pronoun fog at the biggest death" (`rev/v1_craft.md` F2); "Remnant… appears once and never again" (`sample/cold_reader_v10.md`).
- **Caught by:** panel (the casual reader) and the cold reader. **Late:** always last.
- **PREVENTION:** Every new term, title or callback gets a half-clause anchor the first time it appears in a chapter, as context and never as explanation. Name a person outright whenever two people of the same pronoun share a beat.
- **Script?** **PARTLY.** Flag capitalised terms on their first use per chapter, and flag paragraphs where two same-gender named characters are followed by 3+ bare pronouns.

### 20. POV leaks and knowledge slips
- **Recurred:** ch01, ch02, ch03, ch05 and ch06, plus v1.
- **Examples:**
  - "Eli's POV names 'the King' before anyone says it" (`v3/ch01/review_continuity.md` #8; it had already been flagged in v1 by `review_sense.md` #3, so it was reintroduced); "Vosk sees the stitches on a standing man's nape while his own face is to the wall" (`v3/ch01/review_sense_v7.md` #5).
  - "Eli knows of 'Both' lates" (`v3/ch02/review_continuity_split.md` F1); "Eli reports something he couldn't hear" (`v3/ch02/review_sense_split.md` #6).
  - "the opening is in the cook's POV" (`v3/ch03/review_continuity.md` #3); "Garro's son knows 'Off the boat this morning'" (`v3/ch06/review_continuity.md` K1).
  - Also: "'The god' arrives unintroduced… Eli cannot know" (`rev/v1_craft.md` F5).
- **Caught by:** cont and sense. **Late:** no, but the same kind of slip recurs.
- **PREVENTION:** The writer checks every name, title and fact against the knowledge table: who could have heard it, and when. A character says only what they witnessed or were told on the page.
- **Script?** **PARTLY.** Check the first narrated use of each title or name against its first spoken use.

### 21. Pacing sags and travelogue stretches
- **Recurred:** ch01 (both panels), ch03, ch04, ch05 and ch06, plus the sample.
- **Examples:**
  - "S2 is a travel section… Nothing turns" and "The Long Stair to culvert stretch… is all scenery" (`v3/ch01/review_forecast.md`, `review_panel.md`); "The kitchen. … I skimmed until the knock" (`v3/ch01/review_panel_v9.md`).
  - "the first 40% has no forward motion" (`v3/ch03/review_panel.md`); "S1–S2: two flat sections back to back" (`v3/ch04/review_forecast.md`); "two peaks… with a long trough at S6–S9" (`v3/ch05/review_forecast.md`); "the opening hold section… is slow going" (`v3/ch06/review_panel.md`).
- **Caught by:** fcst and panel. **Late:** yes.
- **PREVENTION:** Every scene card names its turn (what is different at the end). Travel and waiting carry a clock or a threat (Teo's line, a pursuer, a deadline). No two low-tension scenes in a row.
- **Script?** **NO.** A tension curve from the scene cards can be checked, though.

### 22. Promises left hanging, and overdue seeds
- **Recurred:** every payoff review from ch03 to ch06 lists the same overdue items, plus the sample audit (14 unpaid).
- **Examples:**
  - "Overdue: S-008 Queen (no touch since ONE) · S-019 King (no touch since THREE, no payoff) · S-046 the hand… · S-106 tune (no plant)" (`v3/ch05/review_payoffs.md`). The same list recurs in `v3/ch04/review_payoffs.md` #9 and `v3/ch06/review_payoffs.md`.
  - "'Who sent you' is never followed up" (`v3/ch05/review_forecast.md`); "the man in house colours… goes nowhere in this chapter" (`v3/ch04/review_panel.md`).
  - "Setups with no payoff… The drone… The inquisitor takes Jon's only token… Eli's cheek scar" (`sample/audit_v10.md`).
- **Caught by:** pay. **Late:** the warnings are timely, but nobody acts on them, because the planner doesn't read the overdue list.
- **PREVENTION:** The chapter plan must take each overdue seed and either touch it, schedule it with a chapter number, or cut it.
- **Script?** **YES.** Track the last-touched chapter per seed ID in the ledger and fail any plan that doesn't address seeds overdue by 2+ chapters.

### 23. Misreading the soft protagonist
- **Recurred:** 6 outside or panel reads across ch01, ch03, ch04, ch05 and ch06. It took two Patrick rulings to settle (BANK 2026-11-18, then 2026-11-21).
- **Examples:**
  - Gemini: "Eli's insulated, bored detachment… make sure Eli's internal calculation is explicitly framed around *boredom*" (`v3/outside/gemini_ch01-03_audit.md`). Patrick then ruled on it (BANK 2026-11-18). Claude's call: "That misreads Eli… 'Explicitly framed' would also mean telling" (`v3/revisit_later.md`).
  - Grok: "Kill or weaponise the soft Eli beats: the kittens line, 'Thank you' to the bin… the easy 'I'm coming'" (`v3/ch01/outside/grok_ch01_v3.md`); "Eli's optimism speeches. Patrick recalibrated these: intended" (`v3/ch05/outside/grok_ch05.md`).
  - The ch04 hater: "He reads as performing warmth more than feeling it" (`v3/ch04/review_panel.md`). Grok on ch06: "'Everyone likes you' can stay, but the narrative mustn't endorse it" (`v3/ch06/outside/grok_ch06.md`).
  - Patrick, decisively: "Eli isnt meant to read as cold and detatched… The softness is the point" (BANK 2026-11-21).
- **Caught by:** Claude's author calls declined it, then Patrick's calibration settled it. **Late:** yes. Two chapters were drafted under the "make it more evident" instruction before the calibration landed.
- **PREVENTION:** Every reviewer and the writer get Patrick's Eli calibration verbatim. His warm, future-tense, arranging care is designed. Flag it only if it removes the pressure or makes the others vanish, and always show the warmth and the blindness in the same beat.
- **Script?** **NO.**

### 24. AI readings and "[P]" protections treated as Patrick's rulings
- **Recurred:** ch01, ch03, ch05 and ch06, plus the sample and the v1 outside reads.
- **Examples:**
  - "Vosk's speech is a [P] beat (brief §2), but its words are Claude's. No Patrick-verbatim line exists in ch01" (`v3/ch01/review_dialogue.md`). The protection travelled through four passes as if the words were his.
  - "Protected, word for word (the brief and the charsim [P]): 'Sorry about Vosk', 'I'd love ya to come.', 'Everything's got a price, son.'… 'There's a teacher'" (`v3/ch03/review_dialogue.md`). These were character-sim protections, and the panel then flagged them as stock mentor lines (`v3/ch03/review_panel.md` #1). They had to be reworked in `author_calls_v5.md` #2.
  - "Teo's 'Right' restored… It's a protected line, and v2 had cut it" (`v3/ch06/review_dialogue.md` #6), even though pay had retired it as a closer (`v3/ch06/review_payoffs.md` #5).
  - A Gemini misread became a Patrick ruling: "Patrick, 2026-11-18: Eli reads as bored and detached (from Gemini's misread)" (`v3/revisit_later.md`). Grok's model-swap test "follows what it was told", including Patrick's mistaken framing (`rev/outside/grok_gemini_on_v1_2026-11-10.md`). Patrick: "Mostly do ignore anything gemini you or grok added and I didnt approve" (BANKp 2026-11-16).
- **Caught by:** dlg (once) and Claude's author calls. **Late:** yes. Nothing checks provenance mechanically.
- **PREVENTION:** "Protected" means only lines with a BANK, RULINGS or CATCHUP cite to Patrick's own words. Anything an agent or outside model proposed is a 🌊 proposal, labelled with its source. A ruling that responds to an AI read records which read prompted it.
- **Script?** **YES.** Every [P] or "protected" item must carry a cite, and the script checks that the cited file contains that string in a Patrick-attributed line.

### 25. Stale ledgers and state files
- **Recurred:** ch01 ×2, ch02, ch03, ch04, ch05 and ch06. Every continuity review ends with "state files not updated yet".
- **Examples:**
  - "`ledger_seeds.md` and `ledger_rules.md` still cite `draft_v1` lines… The payoff-keeper should rebase both ledgers on v6" (`v3/ch01/review_continuity.md`), and again for v7 (`review_continuity_v7.md`). Also "R-007 in the ledger no longer matches the page".
  - "`ledger_rules.md` still cites `draft_v7` lines. These cites are now wrong" (`v3/ch02/review_continuity_split.md`); "the ledgers' older `3:L` cites are draft_v1 and stale" (`v3/ch04/review_payoffs.md`).
  - "R-026 in the ledger is now stale" after the King redo (`v3/ch04/review_continuity_v5.md` #6); "R-016… Fixed in the ledger (stale since ch05 v4)" (`v3/ch06/review_payoffs.md`).
  - "voice_notes.md is stale. Its samples cite the v7 wording" (`v3/ch01/review_dialogue_v8.md` flag 3); "S-012 'Walk well' is no longer paid", though the earlier review had ruled it EARNED (`v3/ch01/review_continuity.md` against `review_payoffs.md`).
- **Caught by:** cont. **Late:** structurally late. Ledgers are rebased one or two drafts behind the text, so every agent that reads them works from stale cites.
- **PREVENTION:** Ledgers and state are updated by script at every draft bump, not "after approval". A ledger entry carries a quoted string, not just a line number.
- **Script?** **YES.** Re-resolve every ledger cite by its quoted string in the current draft, report misses, and rewrite the line numbers automatically.

---

## (a) Caught, then reintroduced by the next stage

| Problem | Caught | Reintroduced by |
|---|---|---|
| **Vosk's "proud" line oscillated through 5 passes** | v3 panel: "deathbed runs long… 'Proud.' 'Of him.' 'What he. Grew.'" (`v3/ch01/review_panel.md`). dlg broke it into fragments (`review_dialogue.md` #16). | `author_calls_v7.md` #3 restored the whole sentence (Patrick's beat). Then 4 of 5 in `review_panel_v9.md` wanted it cut, orig B1 wanted it cut, and Grok v9 called it "too complete". Patrick settled it: "eloquent but also broken" (BANK 2026-11-17). |
| **The Yoda lift** | orig ch1–3: the flyer out of the lake → changed to the loader. | The ch05 writer wrote "You lifted it blind. You opened your eyes and it fell" plus "the size of that" (`v3/ch05/review_originality.md` #1). |
| **Nosebleed as the reach cost** | orig ch04 #1, declined by `author_calls_v4.md` #9. | The ch05 draft gave three nosebleeds, orig #4 flagged it again, and `author_calls_v4` (ch05) took Eli's out. Then the ch06 fcst recommended a nosebleed for Doc (rebutted, `v3/ch06/rebuttals_v2.md` #1). |
| **The fob rule** | v6 cont watch item; v7 cont and sense #9. | The split rewrite broke it inside the new text (`v3/ch02/review_sense_split.md` #1). |
| **The slot's cost** | `v3/ch01/review_sense_v7.md` #6. | The split's TWO again (`v3/ch02/review_sense_split.md` #9). |
| **"The King" named in Eli's POV before anyone says it** | v1 sense #3, fixed. | Back in v6 (`v3/ch01/review_continuity.md` #8). |
| **The arch telegraph "no one was watching it"** | v3 panel #2. | words reworded it instead of cutting it ("Nobody was looking at it" → "no one was watching it", `review_words.md`), so v6 still had it. Cut only at `author_calls_v7` #4. |
| **The lean rule (water runs toward the Tower)** | Set in ch01 (1:L51). | Broken by the ch04 draft ("uphill" ×2), caught three times. |
| **Interpreting Jon** | ch03 sense #7 cuts. | The ch03 v2 dialogue still had Jon explaining the King (dlg D5, D7). ch04 added the cart vanish, ch05 had "Nobody had given him one", and ch06 moved the same leak onto Doc (Teo's look). |
| **Hand-state marking** | ch04 cont 4a, fixed in v5. | Unmarked again in ch05 and ch06 (Grok both times). |
| **Name collisions** | Hollin → Oskel (ch05). | The next chapter coined Garro (Horus Heresy), `v3/ch06/review_originality.md` #2. |
| **Teo's warning count (capped at 3)** | ch01 pay: "There are five warnings, not three". | ch03 again had "5 Teo warnings, not 3" (`v3/ch03/review_payoffs.md` #2); ch05 had a possible 4th ("Nobody's coming, Eli", cont). |
| **The sock telegraphed by refusals** | ch05 pay #2 ("You'll want it for something"). | ch06 offered it three more times. pay: "offered five times since FOUR… That works once, and only once". |
| **The letter as chapter closer** | ch06 pay #4: the third chapter in a row. | It is still the pattern. ch07 has to break it by rule. |
| **Dialogue-editor vs payoff-keeper on "Right"** | pay retired "Right" as a closer (ch06 v2). | dlg restored it as "protected" (ch06 v3). |
| **Dialogue-editor cutting a charsim line** | dlg cut "Then I buried them." (ch05 D6). | dlg itself flagged it might be meant to stay: the editor removes content another stage specified. |
| **Doc clue thinning** | `author_calls_v2` (ch06) #1 thinned the clues. | The v3 panel still found the tells "over-seeded" (cold hands plus crones), and the v4 rebuttals had to thin them again. |

---

## (b) Reviewer notes that were wrong or misread, and why

| Note | Why it was wrong | Cause |
|---|---|---|
| Gemini: Eli is "bored and detached"; frame his choice "explicitly… around boredom" (`v3/outside/gemini_ch01-03_audit.md`) | It misreads the design. "Explicitly framed" asks for telling. | **Conflicts with Patrick** (BANK 2026-11-21). It still triggered an interim ruling (11-18). |
| Gemini ch1–5: the day counts "three days / four nights ago / in four days" disagree (`v3/revisit_later.md` TAKE #1) | They all agree once Night 1 is the Scald (`v3/ch06/review_continuity.md` Part B). | **Partial reading.** The revisit list still carries it as a TAKE. |
| Grok ch04: "Jon is completely absent" (`v3/ch04/author_calls_v5.md` #6) | He's in the walk and the handover. | **Partial copy** pasted to Grok. |
| Grok ch01 v3: "radiation" as the city's wrongness (`v3/ch01/outside/grok_ch01_v3.md`) | Patrick ruled the radiation cleared long before Book 3. | **Stale or no context** (no BANK). |
| Grok ch01 v3/v4 and panel v9: break or cut Vosk's speech | Patrick asked for an "eloquent speech" (CATCHUP §4; BANK 11-17). | **Conflicts with Patrick.** Reviewers didn't know it was his beat. |
| Panel ch05: "Don't use more than you can control" is a "fortune-cookie line" (`v3/ch05/review_panel.md`) | It's Patrick's line (BANK 11-16, cc R075). | **No protected-lines list given** to the panel. It hedged "If this is a Patrick line". |
| Panel ch05 lost on "the sock", "grey", the watch, "the cutter" | These are set up in ch01–04. The panel "did not open the ch01-04 context file". | **Partial context by the agent's own choice.** |
| Panel ch03: rename "Jon" (generic Earth name) | Patrick's name. | **Conflicts with Patrick.** Declined in `author_calls_v5.md`. |
| Cold reader v10: "Like a mean man would put down an unruly dog" is a cliché; "What he felt first was left out" reads like an editor's note (`sample/cold_reader_v10.md`) | Both are Patrick's protected lines (P-items, t202). | **Blind by design.** The cold reader can't know provenance, so its notes need a provenance filter before they reach the writer. |
| orig ch04: cut the nosebleed | The panel loved it, and it's a generic device. Declined (`author_calls_v4.md` #9). Then ch05 orig raised it again. | **Agents disagree,** with no shared record of the decline. |
| fcst ch06: give Doc "a thumb to the nose"; "anchor Doc as Jon's man" (`v3/ch06/review_forecast.md`) | They break R-047 (never a nosebleed for Doc) and R-034 (never read Jon), plus author call 1. | **fcst reads blind of the rules,** by design, so its fix proposals violate canon. |
| pay ch01 v1: "S-012 'walk well' → 'Walk. Walk well.': EARNED" | v6 had dropped the payoff (cont v6). | **Stale draft.** pay ruled on an older version. |
| Writer's fix log v7: "seed cap 6 + 3 holds" | It was 10 + 6 (`review_payoffs_v7.md`). | **Self-report not checked.** |
| King-redo change log: the chip "sunk in a plate the size of a palm" | The text says "At the back of his neck" (`v3/ch04/review_continuity_v5.md` #6). | **Log written from intent, not from the text.** |
| Grok on the sample (reviews 1, 2), the fresh Claude: notes on Tam, Vael, Pip, Grun | They reviewed the OLD four-chapter sample, not this repo's (`sample/grok_review_2026-11-08.md`, `fresh_claude_review_2026-11-09.md`). | **Stale copy.** |
| Grok's third review: Jon as the elves' hidden god; "Eli's knowledge of his father" is a live tension | The first is retired; the second is "NOT REAL" (`sample/grok_review3_2026-11-08.md`). | **Read the codex without BANK.** |
| Grok v1 model-swap: "tighter 1–6, smoother 7–9" | It followed what it was told ("ran the full pass", which was false) (`rev/outside/grok_gemini_on_v1_2026-11-10.md`). | **Misinformed prompt.** |
| Grok ch05: a "slight chosen-one tilt" | "Not me. Him." is already the anti-chosen-one turn (`v3/ch05/outside/grok_ch05.md`). | **Misread.** |

---

## (c) Where the process wasted effort

**1. The same flag caught by 2–4 agents, then reconciled by hand.** Each author-calls file opens "Take every flag in all four", and the writer de-duplicates them by hand. Clear cases:
- **ch04 "uphill" water:** cont 1a, sense #4 and pay #1.
- **ch05 R-016 cup:** cont C3, sense #2 and pay #1. **The master watching:** cont C2 and sense #1. **The headache "four days":** cont A1 and sense #7. **The board's position:** cont A2 and sense #8. **"He's grey":** cont, sense #9, fcst and panel. **Pills "None":** cont C1 and sense #6.
- **ch03 Velk's soap:** cont #7, sense #8 and pay #5. **The slot and the gate log:** cont #2, sense #3–4 and pay #1.
- **ch06 sock coins:** cont F1 and sense #3. **"First night":** cont T1 and sense #5. **Teo's chip-scar look:** pay #1 and sense #2. **Doc's clues:** pay, panel, orig and sense.
- **The fob rule:** four reviews across three drafts.

**2. Repetition counted by four agents.** words counts tics. pay has its own "Repetition caps" block in every review (ch01, ch03, ch04, ch05, ch06). panel counts them again (the hater's lists), and cont adds "Style counts". Meanwhile words often counted by Grep and left "rerun `scripts/wordcheck.py` to confirm" (`v3/ch01/review_words.md`, `v3/ch03/review_words.md`): the script existed and wasn't run.

**3. Long "checked and clean" tables.** About 30–50% of every cont and pay review restates what holds. The payoff tables list every EARNED item (12 rows in ch01 v7, 20 in ch03, 24 in ch04). They are useful once for the ledger, but they are re-read every round.

**4. Agents that found little or nothing to act on.**
- Post-lock reviews: `v3/ch04/review_continuity_v5.md` ran on an approved chapter ("notes only", 8 LOW). `review_originality_ch01-03.md` ran on locked text.
- The ch06 dlg pass was "a light pass: 6 changes".
- fcst sections mostly graded HIT and said "No change needed".
- ch04 orig #3 (Mos Eisley) needed no fix.

**5. Contaminated tests.** fcst's read chunks overran the breaks: ch04 had three forecasts written "after the fact", ch05's first read "ran about 10 lines into S2", and ch06 had two "discounted" grades. The ch05 panel skipped the context file and reported confusions that weren't real.

**6. Plan checks catching the planner, every chapter.** ch04: 11 flags. ch05: 12 (1 HIGH). ch06: 11. ch07: 14. That's useful work, but it exists only because the planner doesn't draft from `story_state.md` (see kind 3).

**7. Draft churn.** ch01 went through `draft_v1`–`draft_v9`, then `new_ch01_v1`/`v2` (11 versions), with the proud line and the arch telegraph swinging back and forth. Every chapter had 4–5 drafts plus a story-only copy regenerated at each step.

**8. Interrupted runs.** Commits record work cut short: "WIP: ch4 v2 fix pass in progress" (twice); "Ch6 character sim (in progress)"; "Ch6 originality check (in progress)". On the codex side: "WIP: canon-check fixes (cut off by usage limit)" and "WIP: partial clean adds in codex (rate limit cut the editor)". The review files themselves record no rate-limit loss, but these runs had to be restarted or finished across sessions.

**9. Outside notes re-litigating settled calls.** The Eli softness was argued over 6 times before Patrick's calibration. "Break the speech" was raised 3 times after Patrick's "eloquent". The nosebleed went through three agents in three chapters. Without a shared "declined, and why" register, each reader raises the same point again.

---

## Top changes the overhaul should make (from the above)

1. **Pre-draft packet** for the writer: the rules touched, the inventory and injuries, the calendar slot, the seed and pointer budget, the overdue seeds, live tic caps, the banned n-grams, Patrick's protected lines with cites, and the Eli calibration. This prevents kinds 1, 3–6, 11–12, 15–16 and 22–24.
2. **Script gate after every draft:** `wordcheck.py`, verbatim-repeat, cite and quote resolution for NOTES and ledgers, provenance for [P] items, the term registry, tracked-object mentions, chapter-closer comparison and overdue seeds. This removes most of the duplicate counting.
3. **One merged review** from sense, cont and pay, de-duplicated by line before it reaches the writer, with "checked and clean" moved to a ledger update instead of the report.
4. **A provenance filter on blind readers** (panel, fcst, cold reader, outside models): drop notes that hit protected lines, settled calls, or rules the reader can't see.
5. **A shared "declined, and why" register** that every reviewer and outside paste is checked against.
