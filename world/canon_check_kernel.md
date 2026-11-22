# Canon check of world/KERNEL.md (2026-11-22, canon-checker)

I couldn't write /home/user/Claude-code-/world/canon_check_kernel.md because I have no Write or Edit tool in this session. The full numbered list is below; it can be pasted into that file as written.
The check found 17 issues in /home/user/Claude-code-/world/KERNEL.md: 3 high, 5 medium, 9 low. I spot-checked world/ref/characters_eras.md fully; I did not check world/ref/magic.md, cosmos.md or beings_world.md.
Worst 1: §1 law 7 says "One scale, no immortals", but 🔒 Law 4b keeps a separate true-immortal group (Jon, Derrek, rule-beasts), and how that sits beside R105 is still open (L36).
Worst 2: §1 law 10 stamps 🔒 on "no one in-world learns the faceless Emperor is Derrek" and "no lesser being… seriously beats Derrek". The first comes from t364, not a law, and the Book 3 reveal is open; nothing in the codex says the second.
Worst 3: §4 and §7 put "the brightness is the horror… we fixed everything except what beings are" in quote marks as Patrick's words. It is Claude's wording and is still waiting for his yes (FLAGGED_ADDITIONS F128).

**canon_check_kernel.md**

1. **HIGH · §1 law 7 "One scale, no immortals."**
   - Problem: wrong. It erases 🔒 Law 4b.
   - Evidence: 02 Law 4b: "TRUE IMMORTALITY IS A SEPARATE CATEGORY — by MECHANISM… Jon and Derrek… and the RULE-BEASTS… 'cannot die, but can feel,' which the sacrifice scene relies on." Beside it, R105 says "nothing stops them dying", and the clash is open (NEEDS_PATRICK L36). world/ref/characters_eras.md line 129 states this correctly.
   - Fix: "No immortals among the aging (4a). True immortality is a separate category by mechanism: Jon, Derrek (⚠️ vs R105, L36) and rule-beasts within their domain (4b)."

2. **HIGH · §1 law 10 "no lesser being kills or seriously beats Derrek; no one in-world learns the faceless Emperor is Derrek before the window."**
   - Problem: overstated, wrongly locked, and the cite is bad.
     - "Seriously beats" has no source. The codex has the bishop seeming "to score a serious blow" and Derrek "weakened by the barrage" (09 ascent, items 6 and 8).
     - The Emperor clause comes from t364 ("noone knows who the emperor is"). That is v5 text about the far future, not a 🔒. The past-era reveal is open: 09 RETIRED says "(Still bears on the past-era Derrek-reveal question, Book 3.)" And Jon and the Historian know who the Emperor is.
     - R123 is about the Tower being an amplifier, not about the Emperor's identity.
   - Fix:
     - Split the line. Keep the 🔒 on Law 17 (time is their only given power; the tether) and Law 4b ("no MORTAL can kill him"; W38 with Patrick's t317 condition).
     - Move "neither dies on the page" to ✅ as a story rule (R105).
     - Make the faceless Emperor ✅: "in Book 1's era no ordinary person knows (t364); Book 3 is open".
     - Drop "seriously beats" and the R123 cite.
     - Propagate to characters_eras.md line 181.

3. **HIGH · §4 Book 1 "Feel" column and §7 "The eras": "the brightness is the horror… we fixed everything except what beings are" (09 tone).**
   - Problem: an AI line presented in quote marks as Patrick's.
   - Evidence: FLAGGED_ADDITIONS F128: "Claude's wording (jul08 t27), backed in substance by your t480… Needs: your yes to the wording." 09 PER-ERA TONE: "This bold line is Claude's wording (jul08 t27, never confirmed then)."
   - Fix: remove the quote marks, label it "Claude's line, pending F128", or replace it with Patrick's t480 substance.

4. **MED · §1 law 11 and the §6 tripwire "Books 1–3 show no jumps or resets on the page."**
   - Problem: an extension Patrick didn't rule.
   - Evidence: wk W53 covers Book 1 only: "Book 1… no plea, no time travel shown" (09 line 36). R100 says only "Books 1–3 sit inside the current run and each ends at the window." Law 19 says erased loops are "never planned or dramatized", with a 🌊 tension beside W54 and W55.
   - Fix: "Book 1 shows no time travel (W53). Books 2–3 sit in the same run (R100), so no reset is expected, but that is a reading, not a ruling." Mark it ⚖️. Same fix in characters_eras.md line 38.

5. **MED · §2 soul magic (🔒): "Changelings: 1–2 souls at a time, the original self drives."**
   - Problem: the qualifier is dropped, and ✅ material sits under a 🔒.
   - Evidence: 02 Law 14: "Changelings take 1–2 souls at a time (wk W16); 'one driver always in control' holds only for changelings who keep a sustainable pace (wk W22)." 08 adds the failure modes: decay and rupture (W20).
   - Fix: "1–2 souls is the sustainable pace; one driver holds only at that pace; past it they decay or rupture (W16, W20, W22)." Mark it ✅.

6. **LOW · §2 "The grip… transmutation… the mythic top" marked 🔒, citing 02 Law 7b.**
   - Problem: overlocked. Law 7b is ⚖️: "The nuclear arts are the mythic top — by scale and prestige, NOT by audited mechanism."
   - Fix: lock the grip (Law 1, W01). Mark the mythic-top clause ⚖️.

7. **MED · §5 "Heaven and hell are lifeless pocket worlds the elves found."**
   - Problem: silently picks a side of an open item.
   - Evidence: 01/07/09: "whether they created or found the worlds is debated… 🌊 open (wk W28)"; "'elves built heaven' is the in-world belief, not the truth (wk W29)."
   - Fix: "…pocket worlds the elves reached with a rift device; created or found is open (W28)."

8. **MED · Missing 🔒 laws (c).**
   - Absent:
     - Law 3: "Everything is a grade/scale; nothing is fixed".
     - Law 10: "No temperament-gating of access".
     - Law 20: No-Formula / Multi-Scale.
     - Law 14: soul-binding and soul-harvesting are "the deepest violations"; override without absorption.
     - Law 0c: "The brain is body, not soul" (✅ under a 🔒).
   - Fix: add one line each to §1 or §2. They can merge with law 5 (no types) to keep the count at 12.

9. **MED · Missing 🚫 tripwires (c).**
   - Absent:
     - "the thief drives their grip" (R132; 02 Law 2 / 14).
     - Burnout's "husk/thrall" version and burnout as Remnant combustion (02 RETIRED: "Still retired").
     - The founder-soul / "original changeling" (07 RETIRED).
     - "Jon saved young Derrek" as saga history (R114).
     - "The last friendly giant" as a special figure, and the queen as Jon's rival (R116).
     - The chip's Book-3 bait clause (R143).
     - "Book 3 is the final loop" (02 RETIRED v5).
     - A god "supercharging" a lesser being with its Remnant (02 RETIRED v5-jul).
     - "Your own soul pays for every use" (02 RETIRED v5-jul).
   - Fix: append them to §6.

10. **LOW · §7 R038 quote.**
    - Problem: two separate quotes are spliced into one, and the wording is altered.
    - Evidence: R038 has two quotes: "these are wizards. Big and tough doesnt mean throws punches" · "Try not to make it so slingy… describe how that would look more than just he hurled ot at him". The Kernel joins them with "…" and changes the ending to "he hurled it."
    - Fix: quote them as two separate lines, verbatim.

11. **LOW · §7 "Ghosts are bound out of love."**
    - Problem: narrowed.
    - Evidence: 04 GHOSTS: "Ghosts may be bound as guardians, servants, power sources, punishment — or out of love."
    - Fix: "Ghosts are bound for many reasons, love among them."

12. **LOW · §7 Tower: "radiation, deformation, animals that won't go near", hung on BANK 11-16 [STORAGE].**
    - Problem: bad cite (d). This is the betrayal-day blast's aftermath, not the Tower-as-mass quote.
    - Evidence: R061 ("The radiation left overs… Deformation and such", [CAPITAL · wrongness]); 10, t88: "another reason animals avoid the Tower."
    - Fix: cite R061 and t88.

13. **LOW · §2 Dragons: "supreme in bursts, then drained."**
    - Problem: risky word. 07 means stamina ("drags the fight long *drains* them"), but law 2 bans "drained" for Remnant.
    - Fix: "then spent and tired" or "can't hold peak". Mark it as stamina, never Remnant.

14. **LOW · §7 "the younger the flesh the better" cited t349.**
    - Problem: bad cite (d). It comes from BANK 11-08 (R144).
    - Fix: cite R144 / BANK 11-08.

15. **LOW · §2 Enchantment line marked 🔒.**
    - Problem: overlocked, and the cite doesn't cover the whole line. Only "Remnant held inside something" sits inside 🔒 0c (R099). "Organics hold best / metal bound" is R148, which is ✅. "Book 1 tech runs on flesh" isn't in R148's text; it's in BANK 11-16 [STORAGE]: "That's why in book 1 they use flesh".
    - Fix: split into 🔒 (R099) and ✅ (R148; BANK 11-16).

16. **LOW · §1 law 12 "every race came from the one shatter."**
    - Problem: needs an exception. In-betweeners "PRE-DATE the One — NOT descended from it" (02 Law 15), and higher-plane beings come from "an even more ancient breaking" (jul23 t100).
    - Fix: add "on our plane; in-betweeners and higher-plane beings are not of it."

17. **LOW · world/ref/characters_eras.md overlocks.**
    - Problem: three lines carry a 🔒 their sources don't give.
      - Line 32: "The Tower is fused into all eras" under 🔒 Law 19. Law 19 doesn't say this.
      - Line 108: Derrek "can't reset or jump on his own" 🔒. The source is 09 t713, not Law 17.
      - Line 19: "Under dragon rule…" 🔒. It cites 07 narrative, not a law.
    - Fix: change all three to ✅.

**Verified clean (sample):**
- The AURA "Its grimdark…" quote matches BANK 11-21.
- The BANK 11-16 quotes match the passed bank ("Your body is what is spent", "tiny explosions in every cell of your body", "Organics just hold it better").
- The quotes cited t380, t466, t638, t604, t458, jul08 t24 and jul23 t52 are all in the codex.
- R148 and R149 exist.
- No stale rules: nothing in the Kernel has been overridden by a later ruling or by BANK.md since the pass.