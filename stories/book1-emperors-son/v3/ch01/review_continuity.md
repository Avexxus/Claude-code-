# Continuity review: Chapter One (draft_v6), checked within the chapter
🌊 continuity-keeper, 2026-11-17. **This is ch01, so there is no prior state.** I checked earlier passages against later ones, using the five ConStory-Bench categories, and cross-checked against `v3/ledger_rules.md`. Lines are `draft_v6.md`. I changed no story text. **[P]** marks a passage the draft's NOTES call protected: Patrick's call.

**Verdict:** no hard breaks. 2 medium issues (both timeline), 6 low.

---

## Timeline and plot logic

**1. The return lands at the morning-count hour, but the bell is the night count (MEDIUM)**
- **Earlier:**
  - L51: "The flesh market at Ninth Spur was opening… They were hosing down the slabs."
  - L69: "Vosk was fourteen minutes past the count." The next lines are breakfast (L75).
- **Later:**
  - L589: "In the flesh market at Ninth Spur they were hosing down the slabs."
  - L601: "The soft voice said, 'Good evening.'"
  - L613: "the barracks bell was going for the night count."
- **Problem:** the echo puts Eli at the market at its opening hour, which yesterday was just before the morning count. The house then rings the *night* count.
- **Smallest fix:** L589 "they were hosing down the slabs" → "they were hosing the slabs down for the night". This keeps the echo and makes it closing time. The night count itself [P] is untouched.

**2. Vosk's missed night count last night goes unpunished (LOW-MEDIUM)**
- **Earlier:** L5: "He had come off the evening shift and gone straight down to her, and now he was heading back with the night gone".
- **Later:** L613: a night count exists and is taken late, after an 11 pm departure. Yet the only penalty shown is the morning one, at L71: "Late. Logged."
- **Problem:** if he went "straight down", he missed last night's night count.
- **Smallest fix:** L5, delete "straight", so the count can fall between the shift and the trip down. L5 is in the opening [P], so this is Patrick's call. Alternatively, accept it and leave it.

**3. The shaft "off the sumps" is reached too fast (LOW)**
- **Earlier:**
  - L45: "Halfway up, the stair left the old ground and passed through the sumps."
  - L183/L191: they left "just after eleven" and met Vosk "twenty minutes later".
- **Later:** L177/L197: "a shaft off the sumps with a crew change at half past eleven"; "Teo led them to a service shaft off the sumps".
- **Problem:** the sumps sit about 2,000 steps below the mid-levels, and the route skips the stair, yet they reach the shaft head within about ten minutes.
- **Smallest fix:** L197 "a service shaft off the sumps" → "a sump crews' shaft", so the shaft head is up top and the shaft runs down past the sumps.

## Characterization
No breaks. Eli doesn't listen (L111/L155/L235/L355). Teo stays cool and shows the cost afterwards (L591, L605). Vosk is terse throughout. The beats are consistent.

## World rules (cross-checked with `ledger_rules.md`)
Ledger items as they stand in v6:
- R-003 (landings) is fixed: L41 says a reader "every hundred steps", with no "six hundredth landing".
- R-004 is fixed: L585 reads "with the other humans'".
- R-006, R-007, R-008, R-010, R-011, R-012, R-013, R-015, R-019 and R-020 are kept.

**4. The chip scar is flat, then raised (LOW, factual)**
- **Earlier:** L19: "where the chip scar should have been flat and pale".
- **Later:**
  - L161: "The scar was warm under his palm, a raised ridge."
  - L299: "a pale ridge as long as a thumb".
- **Problem:** the norm is "flat", but Vosk's ordinary scar is a raised ridge.
- **Smallest fix:** L19 "should have been flat and pale" → "should have been pale".

**Watch items (not contradictions; just record them for ch02):**
- **"Leash is out"** (L315) versus the King still moving Vosk: "a step toward him that Eli doubted he'd meant to take" (L401). The network line (L341) covers it. Don't let ch02 say the King can command a leash-free chip outright.
- **The Ilder father's fob drove Vosk** (L519), though Vosk is Eli's house orc (L79, L105). That makes it a world fact that any Terrace fob can drive any orc. Hold it as a rule from now on, or have ch02 say Vosk was once an Ilder orc.

## Factual details

**5. The apple core goes out the door, then lies inside it (LOW)**
- **Earlier:** L115: "floated across the kitchen… out of the open yard door, and dropped on the step".
- **Later:** L145: "Vosk sat on the step inside the yard door… The apple core was by his boot".
- **Smallest fix:** L115 "out of the open yard door" → "to the open yard door".

**6. Teo's cut hand: "the hand that worked", then he uses it (LOW)**
- **Earlier:** L451: "got Eli by the collar with the hand that worked".
- **Later:**
  - L563: "slapped him… with the cut hand";
  - L605: he scrubs with the brush and "the cut across his palm had opened again".
- **Problem:** "worked" implies the cut hand doesn't.
- **Smallest fix:** L451 "with the hand that worked" → "with his good hand".

**7. Eli's headache: "always", or since he was about sixteen? (LOW)**
- **Earlier:** L195: "he'd stopped seeing the stalls at about sixteen, and the headache not long after."
- **Later:** L337: "His ears had the faint fullness they'd always had, which was the headache".
- **Smallest fix:** L337 "they'd always had" → "they'd had for years".

## Narrative style

**8. Eli's POV names "the King" before anyone says it (LOW-MEDIUM)**
- **Earlier:** nothing names him. Vosk's POV has only "something big" (L25) and "He's eating tonight" (L29). Eli's POV has "something came through the arch" (L397) and "He was the shape of an orc" (L399).
- **Later:** L403: "The King's eyes moved to Eli." The first spoken "The King'll have the new one" comes after it, at L405.
- **Smallest fix:** L403 "The King's eyes moved to Eli." → "His eyes moved to Eli."

**Watch (style):** Eli's POV uses Scald terms he may never have heard: "drift" (L223) and the name "Hookline" (L231). L7 makes drift common knowledge ("Everybody knew someone who had"), so this is acceptable. No fix needed.

**POV check:** the one break is clean. Vosk runs L3–81 and Eli runs from L85, with no head-hops found. L401 "that Eli doubted he'd meant to take" stays inside Eli's head.

---

## Notes housekeeping (not story text)
- **The NOTES fix log in `draft_v6.md` is stale.** It is headed "draft_v4 → draft_v5", and it quotes lines that aren't in the text:
  - "Nobody was between them and the bridge now"; the text has L465 "The bridge was open now."
  - "and nobody was looking at it"; the text has L469 "and no one was watching it."
  - "the white in front of it went thin"; the text has L435 "the white at his palm went thin."
- **`ledger_seeds.md` and `ledger_rules.md` still cite `draft_v1` lines.** v6 drops several items they track:
  - S-012 "Walk well" is no longer paid: it appears only at L37, and Vosk's last word is "Go" (L557).
  - R-016 "since he was six" isn't on the page; v6 says fifteen (L441).
  - R-022 and S-023, the Jon glimpse with the peach, are gone; the plan allows that.
  - S-008: the Queen ribbon now reads "THE QUEEN DECLINES TO COMMENT" (L119).
  - S-015 through S-017 and S-101 through S-106 (the shaved-head girl, the Stoop, Velk's tune, the 94-year-old dwarf) aren't in v6.
  - **The payoff-keeper should rebase both ledgers on v6.**
