# 05 — Plan audit: Book 1, "The Emperor's Son"

> 🌊 **Claude proposal, not canon** (story layer, clay). Plan-auditor pass, 2026-11-09, over `00_brief`, `01_world_slice`, `02_cast`, `03_conflict` and `04_scene_cards` (50 cards), checked against `decisions/BANK.md` (which wins), `codex_v5/`, the v10 spine (`work/sample/SAMPLE_BOOK1_v10.md`) and the v10 reviews (`audit_v10.md`, `cold_reader_v10.md`).
> **Severity:** BLOCKER = breaks canon or the spine · MAJOR = a reader will stall or disbelieve · MINOR = wording, bookkeeping, small logic.
> **Owner** = the planner file that should change. `04` changes are scene-carder edits, `03` conflict-mapper edits, `02` cast-builder edits. (`01` items are housekeeping for the world-slicer.)

---

## 0. Verdict at a glance

**NOT CLEAN.** No blockers. **8 majors, 27 minors/notes.** The plan is strong: the override is applied cleanly, the C-ladder and N-defections are real, the 11 audit causes all land, and every protected line is in place. The majors are mostly holes **opened by this run's own fixes** (the dark elf's new backstory, the leaner master card, Teo's unplanted reason) plus two old timeline/logic seams (Jon around the crater; the cutter). All are fixable in one loop. Nothing needs a world ruling except the items in §12.

| # | Sev | Owner | One line |
|---|---|---|---|
| F01 | MAJOR | 04 (+02, 03) | The dark elf's "thirty": dead or waiting behind the seam? If waiting, why doesn't Eli reopen it? |
| F02 | MAJOR | 04 (+01, 02) | The pit-in-hell fix creates "why didn't she stow away on a human hull?" |
| F03 | MAJOR | 04 | The master's sacrifice card drops the operative oath ("no energy leaves") and the source of his blast. |
| F04 | MAJOR | 02 (+Gate 2) | BANK calls the master "one of their strongest fighters"; the cards make him "couldn't lift much". |
| F05 | MAJOR | 04 | Teo's "nobody notices the help" is the stated cause of his death and is never planted. |
| F06 | MAJOR | 03 (+04) | Jon's absence around the crater and the "five weeks" don't add up. |
| F07 | MAJOR | 04 (+03) | The cutter: why leave the ship if he won't board? Why doesn't he know the Queen? Why the gate man? |
| F08 | MAJOR | 03 (+04) | A "household reflex" warrant vs "his face on every wall" across a war. |

---

## 1. The scene-carder's flagged departures from v10

### 1a. The giant's hostage line (5.5): KEEP, trim. → F15 (minor)
- **Canon:** clean. It is the audit's own fix (`audit_v10` §2 item 2; A11) and plants BANK 11-01 L3 "drywall". The giant's knowledge has a public source: the warrant reads "RECOVER IMPERIAL PROPERTY" (L-D1).
- **Problems:**
  1. **The ledger and the beat disagree.** P58 says "your father would pay nothing", but beat 8's text is "Let you go, and we lose nothing." Put the "pay nothing" arithmetic in the line, or the floor speech has nothing to pay.
  2. **The bare `"No."`** after the hostage line has no speaker. In v10 the giant's "No" answers "knock on its door". Give it to the giant, after the door clause, as v10 has it.
  3. **Over-spelling risk** (BANK 11-07 craft; 11-01 W50). If the giant states the drywall verdict outright, the window loses its sting. Keep it to the arithmetic: "A hostage is worth what the other side would pay. I have read your father's posters." No adjectives, no "he doesn't care".
- **Fix (04 5.5):** rewrite beat 8 as one exchange: the giant thinks aloud → the arithmetic → "Keep you, and we feed you. Let you go, and we lose nothing." → back to the door: "No." Make P58's wording match.

### 1b. Doc's "Saving myself for something special" (6.8): KEEP, re-stage. → F14 (minor)
- **Canon:** clean. It is the cold reader's own ask (`cold_reader_v10` §3.6). It keeps the no-witness rule (`07`; BANK 11-01 L24) and reads as a joke on first pass.
- **Problems:**
  1. **Staging.** In beat 3 Teo is "the other way, firing". Doc can't say it "to Teo, puffing" across a dragon fight.
  2. **Doc's wound is terror of death** (`02` §1.6). A dragon breathing at the crew is exactly when he would open up to save his own skin. The card needs his safety to be visible: he's in the freighter's shadow, out of the breath line, and he only throws rocks from there.
- **Fix (04 6.8):** Teo runs past the freighter's shadow: "Do something!" Doc: "Saving myself for something special." Then the line takes Teo's hand. That also gives Teo's distrust in 6.9 (he won't let Doc dress him alone) a fresh cause. Keep Doc in the shadow for the whole fight.

### 1c. The dark elf's pit moved inside hell (4.5; `01` L-A11): GOOD FIX, but it opens two holes → F01, F02 (major)
- **What it fixes:** `cold_reader_v10` §4.1 ("when was she on a human world?"). Hell is a normal world with towns (BANK 11-07 #2), and the human FTL route runs through it, "which is how breakouts happen" (BANK 11-01 NP#5). So human crews stopping over in hell are canon-compatible.
- **Hole 1, F01:** see §5.
- **Hole 2, F02:** see §5.
- **Side note (minor, F35):** card 4.1 keeps Jon's list ("the pits…"). v10 L317 says "the pits **on the inner worlds**". That's a different pit (for the ones caught *outside*). It's fine, but the drafter must not let the two pits read as one. One word in her line does it: "a pit *down there*".

### 1d. The left-palm beat cut (6.13): CORRECT.
- BANK 11-07 cut the held hand; `audit_v10` unpaid 7 flagged Jon's left palm as its leftover; `01` §2 and `02` §1.2 both say cut. The card cuts it (beat 2). **No other Jon hand-beat reads as a device:** the hand lifted toward Eli's cheek and pocketed (5.7) has a plain emotional read. Clean.

### 1e. The "fifth breath" count removed (6.8): CORRECT, one more instance to catch → F13 (minor)
- `07` L326: the ≈5 beams are "scaffolding, NEVER on the page". The card's beat 7 says "No breath count (tripwire)". Good.
- **But v10 counts twice:** L623 "The fifth breath came out ragged" **and** L629 "labouring **after five breaths**". The card's beat 8 doesn't mention the second. Add it to the tripwire so the drafter doesn't carry it over from the spine.
- Ordinals in the conflict line ("the first breath… the second") aren't a tally of the limit, so they're fine. Never let a number reach the total.

### 1f. The [GATE 2 PICK] items: all canon-safe. Notes:

| Pick | Card | Audit note |
|---|---|---|
| The squeeze and the too-easy code | 2.1 | Safe (W41). **§Q 5 and §Q 9 are the same item; merge them** (F29). Teo stopping mid-sentence matches his secret (`02` §1.4). |
| "They tell me you answered well." / "I always do." | 5.2 | Safe (W44: they never learn what he is). It tells Eli that Jon was questioned; make sure Eli files it, because it feeds C3. |
| N2: Eli sees only the pack | 5.4 | Safe. **But the ship must be grounded** for a walk down a ramp (F24). |
| Mika's reply text, writer-only; did Jon warn the giant | 5.7 | Safe. Low stakes; Claude can decide these without Patrick. |
| *Ledger Closed* resold, the sighting | 6.6 | Safe; it's a soft coincidence (they happen to pass that port). Acceptable as a crushed glimmer. NOTE only. |
| The open terrace door; the spar on cost | 7.1 | Safe. The open door is a silent cause the reader can't see; it's fine because the Queen's "Then he was right" gives it a surface reading. |
| "He went alone," aloud | 7.3 | Safe. Three words; not over-spelling. |
| Jon's tear | 8.3 | Safe. |
| Jon's face goes clear, from outside | 9.1 | Matches BANK 11-08 ("Claude recommends showing it from outside in Book 1"). Placement is still unruled, so it belongs at Gate 2. |
| The cheek line; Eli refuses the hand-over | 8.4, 6.4 | Safe, and both pay real setups. |

---

## 2. Patrick's protected scenes and lines

| Item | Where | Status |
|---|---|---|
| **The master's sacrifice** ("blows himself up to punish the rule beast in his own sick game", BANK 11-01 L34; "the rule beast would have one by one killed them all", BANK 11-07) | 7.4 | **At risk → F03 (major).** The card keeps the shape but drops the mechanism. Beat 6 says "Swear it, three times", but leaves out the operative clause from v10 L783: "Do you swear this room will not allow any **energy** to leave?" Without that clause there's no "own sick game" for the master to turn. The card also never shows where a small-push master gets a blast big enough to kill the beast. |
| **Eli's emotional final attack** (BANK 11-08) | 8.4 | **Survives.** The words are "the real attack" and they come last. See F31 (minor): keep the physical run short and reflexive so nobody reads the reach as the attack. BANK also notes "whether the appeal lands is left open"; the card's value line ("certain he is drywall") closes it. Let the hand's stop stay ambiguous *to Eli*. |
| **The P40 boots line is Eli's** (BANK 11-08) | 8.1 b11 | **Survives**, Eli only. **ID collision (F16, minor):** BANK's "P40" is the *v10 sample's* number; in this ledger P40 is "the ninth; the worn floor", and the boots sit under P62. Relabel the inline tag "BANK 11-08 boots line", and tell the drafter to keep v10 L911 near-verbatim ("thought she ought to have had them seen to"). |
| **"Just enjoy the show, old man."** | 9.1 b6 | **Survives verbatim.** Jon sighs, head back against the glass. Derrek reminds him "who our master is" and that he "knows what he has to do" (BANK 11-01 L3 follow-up). The son asks; nobody answers (W50). Clean. |
| t768 apprentice speech · t774 litany and "It's quiet… peaceful" · "nice warm sunny weather…" · "Like a mean man would put down an unruly dog" | 8.1, 8.3, 8.3, 7.5 | All marked verbatim. Clean. |

---

## 3. The entropy breath: does it belong in Book 1? **No.** The card reaches the right answer for half the wrong reason.
- **Authorship:** Patrick's scene (BANK 11-01 L34). The codex text is `13` §Showpiece / `SCENES_COMPILED` §Showpiece, 🌊.
- **The card's reason ("a far-future showpiece") doesn't exclude it on its own.** Book 1 *is* the far future (`09 t334`).
- **The real reasons it's out:**
  1. **No slot in the spine.** It isn't in v10 or the brief, and no Book 1 BANK ruling places it.
  2. **The POV can't reach it.** The scene is set on a dragon's starship, among a mixed crew, with an enemy "god" arriving. Eli is the only POV and is never there.
  3. **It leans on open or cut ground.** The "god" *teleports* aboard (space-folding is a cut domain, `05`); entropy as a wielded power is cut (`05`), with the tension still open (`QUESTIONS 5.6`; `NEEDS_PATRICK` #30 and (e)); "god" usage after t666 is open (NP#7).
  4. **It fights Book 1's ending.** It's a god-kill. Book 1's whole logic is that the god can't be killed, only drained (BANK 11-01 L4, "Ya I dont think he can die lol").
- **Where it points:** the only label in the repo is the older `SCENES_COMPILED` copy, "Book-3 set-piece". That's a Gate 2 confirmation, not a fix.
- **Owner:** 04 §Q 17, reword the reason.

---

## 4. Canon check (beyond §1–3)

| # | Sev | Owner | Card | Issue | Cite | Fix |
|---|---|---|---|---|---|---|
| F09 | MINOR | 04 | 8.3 b9 | **The ruined hand gets used twice:** "lifts once and falls back" (b4), then "brushed aside with the back of the ruined hand" (b9). This is `cold_reader_v10` §micro 5 reintroduced, and it breaks `03` §4.1's hand-tracking rule. | `03` §4.1 | b9: the **good** hand, or a shrug of the bad shoulder. The track is: right palm opened (8.1), right arm wrung (8.2), left is the good hand from then on. |
| F10 | MINOR | 04 | 8.2 b4 | "The shadows behind the chair move, and she's there" reads as shadow-teleport. | `05` space-folding cut; NS4 is stealth | She has already moved while every eye was on the sliver. Eli just finds her there. |
| F11 | MINOR | 04 | 5.3 b4 | "From the sword, nothing. There's nobody there." This must read as grief (she has no body left, so the bond can't hold her), not as surprise that the bond can't read a blade. Elves never believed it read souls. | BANK 11-09: "elves never sensed each other's souls they just read the bond which is a sensory organ" | Keep the line, and add the beat that she *knew* it would be silent, and that this is the horror. |
| F12 | MINOR | 01, 02, 03 | — | **Stale override leftovers:** `01` §1.8 "Soul-sensing is… master-level; **the elves' bond is the exception**" (the bond isn't soul-sensing at all); `02` §5 Q2 "the dark elf's fracture **rests on yes**"; `03` §8 "Knock-on… update 02 §1.7 and 01 L-D5" (already done). | BANK 11-09 | Delete or reword all three. |
| F25 | MINOR | 04 | 6.6 | A crowd hangs a gnome for soul theft, and Doc says "They **always** get the wrong one." Patrick rules that the changeling threat is one "noone protects against", with no folk tests and no distrust of healers. | BANK 11-01 changeling paranoia | Keep it as one-off war panic picking the nearest small stranger (gnomes are the dwarves' indentured class, `10 t568`). Doc's "always" then reads as gnome prejudice, not as a custom of hunting changelings. |
| F34 | MINOR | 04 | 2.5 b4 | "The Hand… a Legion **pen-born**": "pen" is the orc pens' word (1.1). | `02` §1.9 "carrier boy" | Use "carrier-born". |
| — | NOTE | 04 | 2.2 b7 | "Reflex. Nobody home." Jon voices the world's pretence about clones. Fine as dialogue; the narration must not agree. | `10 wk W66` | Drafter note. |
| — | NOTE | 04 | 4.5 b5 | "It never goes out." The bond doesn't cross pocket worlds (`10 t230, t600`), so in hell she **never** felt the homeworld. She has only had the light for the four months since the door. Correct under canon, and sharper. | `01` §1.8 | Drafter note: don't imply she felt it down there. |

**Checked clean:** the bond as an organ throughout (5.3, 6.7, 8.1, 8.2); Remnant never spent, and burnout as the body's death (2.5, 8.1); Doc's barrage felt, never seen (8.3); Derrek drained and restrained, alive (8.5–9.1); no rose, no Lirael line; three time hints only; Jon not the elves' god (3.2 "my only one"); "drow" off the page; the Queen as a chess piece and Eli's rival; early Jon modest (1.2, "winded by the fifth or sixth", which matches v10 L51); no aliens; "Derrek" never in narration; the young moon dragon (`07` lock); the only Rule in the Tower is the beast's.

---

## 5. The "why doesn't X just…" power audit

The 11 v10 items (A1–A11, A-bonus) all have causes on cards (`04` §C index). **Verified, all land.** New or residual holes:

| # | Sev | Owner | Who | Why doesn't X just… | Reason visible? | Fix |
|---|---|---|---|---|---|---|
| **F01** | **MAJOR** | 04 4.3; 02 §1.7; 03 P5/K5 | Eli and the dark elf | **…open the door again for the others?** 4.3 says "twenty-nine are still on the other side **or dead**", and b7 has her look "at the closed air where the others are". If they're alive behind it, Eli should try again, or she should beg him to. `03` P5 says the opposite ("the last of thirty"). Her timeline also tangles: "I was a child" when they started, then fifty years on the road, a pit, forty years of the Collapse, and "pushed for years" (K5). | Missing / contradictory | **Make her the last one living.** "When we started" means the road, not the push. The others died on the road and at the door over fifty years; she pushed alone at the end. 4.3 b7 becomes "the closed air **where the others ended**". The disaster line becomes "Thirty started. She's what's left." Put one timeline line in `02` §1.7 (a child at the road's start → fifty years, three of them in the pit → the last years alone at the door). Align K5. |
| **F02** | **MAJOR** | 04 4.5; 01 L-A11; 02 §1.7 | The dark elf | **…stow away on a human transit hull** at the stopover pit she fought in for three years? BANK says the human route "is how breakouts happen". | Missing (opened by the fix) | One clause in 4.5 b2: "The crews are the farmers' customers. They count what they carry, and sell what they find at the next port." The door is the only way out that nobody owns. **Bonus:** the human crossings are what wear the floor thin (4.2 b2, P40/P41), so breakouts still "happen through the human route", just not *aboard* it. |
| **F03** | **MAJOR** | 04 7.4 | The master | **…how does a man who "couldn't lift much" kill a rule-beast?** | Implied in v10 (the oath), dropped in the card | (1) Keep v10 L775–797 as written: the energy clause, sworn three times, then "Then nothing reaches them. And nothing gets out. Including you." (2) Make the source visible: the Tower "makes everyone bigger" (P77), and he draws on the walls the way the apprentice will. **The shudder and the light dimming (b10) are his draw**, mirrored in 8.1 b4. His body burns out inside a room sworn to hold every spark (BANK 10-31: burnout covers "the master's and the apprentice's deaths"). (3) Add P77 and P21 to 7.4's Paid. (4) Put BANK 11-07's "one by one" in the beast's terms: if nobody goes in, it takes them one at a time, forever. |
| F23 | MINOR | 04 4.4 | Eli | **…kill Krell?** He killed the guard for seeing his face. | Missing | Make it visible: after the guard, he won't kill a man for a face again, and the refused water is his compromise, which is worse. One beat. |
| F30 | MINOR | 02 §1.2 | Jon | **…why can he move a wreck in full view of Earth's sky?** His tactical line was "never where a feed can see". | Implied | One line in `02`: the line ends at Earth. The chaos covers it, and nothing is left to hide from. No page trace needed. |
| — | NOTE | 04 6.4 | Eli | …reach into the cutter? He bent guns at the crater. | Implied (the grapple slam, ribs, range) | Optional: one clause on range ("a ship's length away, through two hulls"). |
| — | NOTE | 04 1.1, 6.10 | Eli | …free the orcs? | Implied (a fugitive; grimdark) | None. That's the book. |

---

## 6. The cooperation audit (no one complies only because the plot needs it)

**Strong overall.** Exit points 1–39 (`02` §4) each have a dossier reason. N1 (Teo), N2 (the dark elf), N3 (the master) and N3b (the Queen) are real near-defections, and N1 is on the page.

| # | Sev | Owner | Who | The suspect compliance | Fix |
|---|---|---|---|---|---|
| **F07a** | **MAJOR** | 04 6.4 | The whole crew | **They abandon the ship to a cutter that "won't board."** If he won't board, why leave? | One line, from the master or the Queen: "Stay aboard and he tows us to his station." That makes the lifeboat a choice (freedom and thirst against capture), not obedience to the plot. |
| **F07b** | **MAJOR** | 04 6.4 | Ilvaen | **He doesn't recognise the Queen**, Mika's famous piece ("They call her the Queen"). The scene depends on her *not* naming herself, so he must not see her. | She steps out of the hail's eye before it opens. Eli sees her do it (it doubles as Q3's silence). |
| F20 | MINOR | 04 6.3 | The master | After "cheap trick" he comes anyway, "until his own reason fires", but the card never shows what fires. | Show it: the last rig students go to the war, or the temple is shelled again on day three. He crosses the field with his master's bag. |
| F22 | MINOR | 04 6.13 | The dark elf | She agrees to *Jon's* ask, though she distrusts him ("hears the price in it", 4.6) and her price is being used. | She doesn't answer Jon. She looks at Eli, then nods. She's agreeing for Eli. |
| F24 | MINOR | 04 5.4 | The dark elf | N2's walk "toward the ramp" needs ground under the ship. | Set 5.3–5.4 while they're still grounded at the Dry. Where she'd go (the open desert) is the point: nowhere. |
| — | NOTE | 04 8.1 | The Emperor | He accepts Jon's leash ("Yours. Go on."). | Covered: offerings, the window, "thousands of times" (`03` §4.2; `02` §1.3). The look at Jon after each death is v10 behaviour, not a new love tell (BANK 11-08). Clean. |
| — | NOTE | 04 1.2 | The guard | He hangs at forty yards talking into his collar instead of running. | Covered: bounty, and backup coming. Clean. |

---

## 7. The coincidence audit

K1–K18 (`03` §7) are all converted to cause, cost or choice. **Verified on cards.** Residuals:

| # | Sev | Owner | Coincidence | Fix |
|---|---|---|---|---|
| **F07c** | **MAJOR** (bundled with F07) | 03 P8 | **The gate inquisitor is also the cutter's master** ("the same grey coat with eleven questions"). `02` merges the roles by design, but nothing *causes* the same man to be there. | A cause in `03` P8: it's **his** ledger, and he took the token that vouched for the party that emptied a station. The case is his failure, so he asked for it. Trace: his first question on the hail is question one from the gate, word for word (already 6.4 b3). |
| F07d | MINOR | 04 6.4 | **Krell** is the cause of the cutter knowing their faces (P45, U10 "paid"), but the card only writes "(Krell)". The reader never sees it. | Put it on the screen: "a dwarf in a good coat sends his regards", or Krell's grease-pencil mark beside Eli's face. |
| F27a | MINOR | 04 6.4 | **The part ping** (P65) is paid only offscreen ("Eli doesn't know"). | Optional: Teo, "Twice. How do they keep finding us?", and the dark elf or the master: "You ordered a part." Or mark P65 writer-only. |
| — | NOTE | 04 6.6 | *Ledger Closed* at the one port they pass. | Acceptable as a crushed glimmer (and dwarven ports are where Returned hulls go: `03` P8). |
| — | NOTE | 04 7.1 | A cathedral ship breaks right overhead during the drop. | War density, and the drop was timed into the assault (K12). Clean. |

---

## 8. Promise / payoff ledger (P01–P91)

All 91 IDs are present; each open item is marked as open by design. The audit closure claims (U1–U5, U8, U10, U12 paid; NS1–NS4 planted) **check out on the cards**, except where noted below.

**Payoffs with no setup (new):**
- **F05 (MAJOR, 04):** **Teo's "nobody notices the help."** It's the stated cause of his walk to the dais (7.5) and the cold reader's fix for "why nobody stops Teo" (`cold_reader_v10` §5). A grep of 04 finds it only in 7.5. **Plant it twice:** (1) in 2.1 b6, folded into the code line: he forged it because "nobody watches a servant's boy at a terminal"; (2) in 6.6 or 7.1, Teo slips past a checkpoint or a crowd unnoticed, and Eli registers it.
- **F05b (MINOR, 04):** **Teo's petition** for his parents (7.5 cost: "unsaid"). It's set only in `02`. v10 L843 hints at it ("something he had carried across a whole war"). Plant one beat in 6.10 or 6.12: Teo rehearsing under his breath, or asking Eli how you address an emperor.

**Setups with weak or invisible payoffs:**
- **F26 (MINOR, 04):** P36 "Disagreed. Out loud." is paid in 5.7, "writer-only". A payoff the reader can't see isn't a payoff. Either echo it on the page (the Queen's "Continue" said like a mouth sewn shut) or retag P36 as texture.
- **F27b (MINOR, 04):** the link from P62 ("she waits until he's up") to 8.1's boots is thin. A better pay is 8.1 b7: "she let him drive her there", where she chose her knees. Keep the boots as their own beat.
- **F27c (MINOR, 04):** 2.6 b6, **the secret happy hour**, isn't in the ledger, and `02` makes it load-bearing (the Tower is optional). Give it an ID and a pay: 7.2 (the master near to happy, which Eli recognises) or 9.1 ("a small feeling").
- **F27a:** P65 (see §7).
- **F07d:** P45 Krell (see §7).

**Bookkeeping:** F16 (the P40 ID collision, §2). The §L table and the per-card Set/Paid fields agree everywhere else.

---

## 9. Cold logic read, cards in order (a stranger with only the cards)

1. **Ch 1:** clear. The run → the fence → forty minutes. The self-theft custom (P04/P07) parses. **NOTE (F32):** 1.1 carries two orientation beats (O1's towers, O3's bath "in the Tower's shadow") inside a chase. BANK 11-07: "the opening should focus on the run." Keep each to a clause, or move the bath to 1.3's wait.
2. **1.3 → 2.1 (F18, MINOR):** "Lift-off… Where to?", then "a river gorge on **the next world**". A flyer crossing worlds needs one clause: it rides a transit hull, or it's a small hell-capable hull. The same question comes back at 4.1→4.2, where they fly the flyer to a dead moon.
3. **Ch 2:** strong. The poster decision (2.3) is the best-motivated scene in the plan.
4. **3.2 (F17, MINOR):** the stranger asks why they go to Seluvane at all. v10 L257 had the motive ("Eli wanted to see the elves… they would be his war, if he got the chair"); the card's goal is only "get in". Restore the motive as the first beat.
5. **3.2 Jon (F19-a, MINOR):** "Jon (rejoined)" — where? Say: at Holding Thirty-One, after the five months.
6. **Ch 4:** **F01** (the thirty) is the one real stall. Otherwise clean.
7. **4.4 → 4.6 (F06, MAJOR):** see §10, fix 9.
8. **Ch 5:** clean after F24. 5.5's hostage line reads well if trimmed (F15).
9. **6.2–6.4 (F19, MINOR):** Jon isn't listed on Tessid, yet 6.4 has his bunk "empty since the last port". Add where he got off and why (the tactical line, `02` §1.2), so the C3 pattern starts here on the page.
10. **6.4 (F07):** the one scene in Ch 6 a stranger can't parse without the fixes.
11. **6.6 (F08, MAJOR):** "his face is on every wall" collides with `03` P0's "nobody above a steward cares". Either the posters spread for a cause (bounty brokers reprint any notice with the seal on it, and in the war zone the seal is hated, so the faces get scratched, not reported), or cut "every wall" down to "a wall". Also say once why nobody collects: the poster is a year and a scar out of date, and there's a war.
12. **6.9 (F21, MINOR):** C5's "I don't know" is "honest" in `02` (§1.1 C5, the style line), but `03` K11 says Jon booked the freighter and hired the answer. Reconcile in `02`: he knew *where* they'd be and *that* Eli would do it, but not *how* he knew. Memory comes back as a feeling (BANK 11-07 NP#3). Then it's true.
13. **Ch 7–8:** clean and legible after F03 and F09. The leash reads through Eli ("You held me").
14. **Ch 9:** ambiguous by design (W50; BANK 11-01 Book 1 tone). A stranger is lost about *what's coming*, not about *what happened*. That's the target.

**Length (F28, NOTE):** the card words sum to **5,400 for Ch 6 (header says 5,350)** and **25,000 total (header says 24,950)**. That's the brief's ceiling (18–25k); the "aim 10% under" instruction matters.

**Jon is never interpreted (NOTE, F33):** card-level reads ("the shoulder comes when he wants something", "warmth that has a value") must not reach narration. Eli may notice the pattern (2.4, 6.5) as behaviour only.

---

## 10. The brief's 10 fixes: solved?

| # | Fix | Verdict | Notes |
|---|---|---|---|
| 1 | Climax is a queue | **Solved as "staged with a felt reason"** (Option B) | The stated reason is on the lander (6.12, P76), the enforcement is bodies (6.13, 7.5), each person goes on their own trigger, and Eli realises it ("You held me", 8.4). The hidden reason (a dead Derrek resets, BANK 11-01 L4) stays author-level. It's still a sequence on the page, so it's Patrick's A/B pick at Gate 2. |
| 2 | Characters cooperate with the plot | **Solved** | 39 exit points; N1 on the page. F07, F20 and F22 are small leftovers. |
| 3 | Eli never confronts Jon | **Solved** | C1–C7 plus C6b, each with a different deflection. C4 is the best scene in Ch 6. |
| 4 | 11 unreasoned power moments | **Solved, with new holes** | All A-items land. New: F01, F02, F03 (majors), F23, F30. |
| 5 | Orientation | **Solved** | O1–O12 placed, one fact per beat. Watch the opening load (F32). |
| 6 | The dark elf and the blade | **Solved, cleanly, under the 11-09 override** | Words (5.3), street knowledge (4.1/4.5), sight (5.2, 8.1); no sensing. F11 is wording only. |
| 7 | The dark elf's backstory contradictions | **Partly solved** | The pit-in-hell fixes the human-world contradiction, but opens F01 (the thirty, the timeline) and F02 (the stowaway). |
| 8 | The ledger (14 unpaid, 4 unprepared) | **Solved, with two new unprepared payoffs** | F05 (Teo's invisibility, major), F05b (the petition), plus thin pays F26 and F27. |
| 9 | Jon's offscreen life | **Mostly solved; one seam** | **F06 (MAJOR):** in 4.1 Jon leaves "to see elves" *before* the raid, is absent through 4.4–4.5, and returns in 4.6 "after five weeks", questioned *about the crater*. The Inquisition can't know about the crater until Krell talks on the next ninth (`03` P5). **Fix in `03` P5, simplest version:** Jon is already in Seluvane asking for the Queen when Krell's report arrives (the ninth after the raid), and they hold him. His absence runs from 4.1 to 4.6 (about two months), and "five weeks" is the questioning part of it. Put one trace in 4.5 (b1: "Jon still not back"), and make 4.6 b5 say "back after two months, five weeks of it nobody's business". Also F19 (Tessid). |
| 10 | Why Eli goes to the Tower | **Solved** | Four pressures at 2.3, and the happy hour he overrides (2.6). |

---

## 11. Fix list by owner

**`04` (scene-carder):** F01 (4.3), F02 (4.5), F03 (7.4), F05 and F05b (2.1, 6.6/7.1, 6.10/6.12), F07a/b/d (6.4), F09 (8.3), F10 (8.2), F11 (5.3), F13 (6.8), F14 (6.8), F15 (5.5), F16 (8.1), F17 (3.2), F18 (1.3, 4.1), F19 (3.2, 6.2–6.4), F20 (6.3), F22 (6.13), F23 (4.4), F24 (5.4), F25 (6.6), F26 and F27 (ledger), F29 (§Q merge), F31 (8.4), F34 (2.5), F35 (4.5), §Q 17 reason (§3).
**`03` (conflict-mapper):** F01 (K5, P5), F06 (P5 timeline), F07c (P8 cause), F08 (P0/P8 posters), F12 (§8 stale note).
**`02` (cast-builder):** F01 (§1.7 timeline), F02 (§1.7 clause), F04 (§1.5 "strongest fighter"), F12 (§5 Q2), F21 (C5 reconcile), F30 (tactical line ends at Earth).
**`01` (housekeeping):** F02 (L-A11 clause), F12 (§1.8 line).

**F04 detail (MAJOR, 02):** BANK 11-07: "The cost was one of their strongest fighters for derrek." `02` §1.5 and 2.6 b3 make him "couldn't lift much". **Reconcile:** his strength is the strength that matters, *fighting*. He reads any fight and calls it (the dragon kill is his plan), the Queen obeys him (`02` §3), and inside the Tower his small push becomes enormous (P77). "Strongest" means best, not heaviest. Put one line in `02` §1.5. Confirm the reading at Gate 2.

Loop: after `02`/`03`/`04` revise, re-audit only the changed cards and the ledger.

---

## 12. Verdict and Gate 2 items (Patrick's decisions, not fixes)

**Verdict: NOT CLEAN.** 0 blockers, 8 majors, 27 minors/notes. One revision loop should clear it.

**For `DIGEST_plan.md`** (Claude's pick first):
1. **The throne room:** B, Jon's leash that frays (pick), or A, the whole room at once.
2. **The master:** core A, the one who stayed (pick). And confirm "one of their strongest fighters" can mean the best fighter by craft, not by raw push (F04).
3. **The dark elf's thirty:** she's the last one living, and the others died on the road and at the door (pick, F01), or the others still wait behind the seam (that needs a reason Eli never reopens it).
4. **Eli's final attack:** a short failed reach, then the words as the real attack (pick), or words only, no reach at all.
5. **Jon's face goes clear:** shown from outside in Book 1 (pick), with the inner line kept for the later window book.
6. **The entropy breath:** confirm it stays out of Book 1 (pick: out; the repo's only label is "Book-3"). Which book is Patrick's call.

**Claude can decide these without Patrick (low stakes, story-local):** Mika's reply kept writer-only; Jon's tear left to the reader; the open terrace door; the squeeze and the code (merged); the *Ledger Closed* sighting; "He went alone" spoken aloud; "answered well"; N2 shown as the pack only; "Remnant" kept off the page.

**Names still for the name engine:** Teo (reads as a generic Earth name), Krell, Ilvaen (never printed).
