# World Rules vs codex_v5 vs BANK: diff

*Claude's study note, 2026-11-07. **Not canon.** Compares `sources/world_rules/` (snapshot 2026-11-07; M-001–M-317, C-001–C-218, B-001–B-244, W-001–W-350, plus the open-questions appendix) against `codex_v5/` and `decisions/BANK.md` (2026-10-31 to 11-02). Nothing here has been applied anywhere.*

**Method.** Each World Rules (WR) claim was matched against the A–I notes and confirmed by grepping `codex_v5/`. Cites use `file Lnn` for codex lines and `BANK date [tag]` for bank entries.

**Headline.** WR is mostly a faithful distillation of the codex: about 95% of the claims have a direct codex source. What's genuinely new clusters in one area: **flesh-tech, the forge world, and Derrek's flesh-core business**. A few claims also already reflect BANK rulings (amplifier-only, the flesh-best rule). WR **predates or ignores most BANK rulings from 11-01 and 11-02**, so it still carries the old Jon-and-elves material, "time-fusion", the old Blight framing, soulless machines and the killable-Derrek lines.

---

## 1. NEW in World Rules (no basis in codex_v5)

### A. The materials ladder and flesh tech
| ID | Claim (one line) | Note |
|---|---|---|
| M-228 | Flesh is the material that holds Remnant best. | Not in the codex, which says only "body-like substrate holds best" (W12). Backed by BANK 2026-11-02 [machines]. |
| M-229 | Flesh cores, a.k.a. living metal, are made by warping living flesh and can hold a live, complete soul. | New term ("living metal"). Close to BANK 11-01 flesh weapons and 11-02 soul-cores. |
| M-230 | Young, healthy orcs are processed into flesh cores and living metal. | New. See the tension with BANK in §2. |
| M-231 | The old or recently dead become lesser enchanted metals, which need only latent potential. | New tier. |
| M-232 | The dead make walls; dead, inorganic structures (walls, ships) don't need living material. | New. Fits BANK 11-02 (grown structures are Convergence). |
| M-233 | The galaxy's electronic and enchanted might comes from infusing Remnant into matter. | New. **Conflicts with BANK** (§2). |
| W-222 | Through Convergence, the giants hold a monopoly on flesh cores and flesh materials. | New. **Conflicts with BANK** (§2). |
| W-344 | *Because* flesh holds Remnant best, the universe enslaves orcs and clones to harvest flesh en masse. | The enslavement is in the codex; the flesh-best reason is new (BANK-backed). |

### B. Focusing chambers and converged ships
| ID | Claim | Note |
|---|---|---|
| M-022 | Reaching past your own Remnant (taken souls, a focusing chamber) is an amplifier; nothing drains. | From BANK 10-31 [L1, L2 follow-up]. The codex still says "drain into batteries" (§3). |
| M-234 | A focusing chamber is an amplifier, not a drain or battery: the dragon inside reaches a wider pool. | New against the codex; aligned with BANK. |
| M-236 | A converged ship is a massive living-metal structure; a dragon firing from a chamber aboard one draws on all the Remnant infused into the city-ship. | New. |
| M-237 | That draw is why dragon beams can break planets. | New. |

### C. The giants' departure and the forge world
| ID | Claim |
|---|---|
| W-208 | The first giants left Earth on one great ship they converged: the first cathedral ship. |
| W-209 | They arrived at a world they had chosen ahead of time. |
| W-210 | The first crossing was slow, with no FTL; giants could afford the wait. |
| W-211 | Giant and elven colony voyages are crewed by largely the same people the whole way. |
| W-212 | Durability and size made giants excellent first space explorers, alongside the elves. |
| W-213 | "Forge world" is the galaxy's name; to giants it is simply home. |
| W-214 | After centuries of isolation on Earth, the giants retreated to the forge world and rebuilt: halls, shops, peace at last. |
| W-215 | The forge world was likely one of the first planets colonized. |
| W-216 | By the far future, giant families have lived there about 5,000 years. |
| W-217 | Giants keep their dead on the forge world for Convergence. (Partial: the codex has giants building from their dead, but not this location.) |
| W-218 | It is home to giant families, orc slaves, dwarven merchants and human diplomats. |
| W-219 | Ship-selling dominates its economy, hence the name. |
| W-220 | It sells ships to the whole galaxy, not only dragons. |
| W-221 | Its secret is where its ships come from and how they are made. |

### D. The forge-world strike and Derrek's flesh-core business
| ID | Claim |
|---|---|
| W-223 | In their second coup the dragons destroyed the giants' entire home world, not just a city. (The codex says "the heart of" the forge world; see §3.) |
| W-224 | No tower stands to remember the forge world's destruction. |
| W-225 | The strike also aimed to weaken the source of the material humans used to forge their dominance. |
| W-226 | It crippled the giants, one of Derrek's primary rivals, and left him no longer needing them. |
| W-227 | Weakening the human flesh-core supply costs Derrek nothing he cares about. |
| W-228 | Derrek has a deal with a coalition of opposition giant factions (the any-tactic and cashed-out camps), who are his secret factory, converging his personal flesh-core supply. |
| W-229 | With the competition destroyed, Derrek holds the flesh-core monopoly. |

(W-225–W-229 supply the *how* and *why* that the codex leaves unruled: "how he engineered it is not re-ruled", `08 L146`, `09 L97`.)

### E. Wording only
| ID | Claim |
|---|---|
| C-153 | "A single timeline, rewritten about 5,000 times." The codex has "a thousand or more runs" and treats ~5000 as a floor (§3). |

**Count: 34 claims** (A 8, B 4, C 14, D 7, E 1).

---

## 2. CONFLICTS WITH BANK (BANK overrides)

Format: **ID** → WR says → BANK says (date [topic]). "Soft" means a tension or wording clash, not a flat contradiction.

### Gods, absorption, demons
- **M-133** → "gods and changelings [absorb] by nature" → godhood is a level any being reaches with time and practice; "god" is an in-world title, not a kind (2026-11-01 [L16, W31, Law 4]; [NP#5]). Drop "by nature" for gods.
- **B-030** → humans reach godhood only by time-fusion or soul theft → "Any being of any size given enough time and enough practice can become a god"; theft and the keeper's pact are shortcuts only (2026-11-01 [L16, W31]).
- **B-035, B-036, B-037, M-180** (soft) → angels and demons are one *kind* of being, soul mages made like changelings → "demons and gods is an in-world name people give to beings who grow powerful enough… not a different race from another realm" (2026-11-01 [NP#5]). They're titles for any being powerful enough, not a soul-mage subtype.

### Machines and AI
- **C-033** → no machine, ASI included, holds a fragment or does magic → AI comes in three kinds; two hold Remnant (a held-Remnant being in the digital; an AI holding a chunk in focus). This answers "forever" whether AI have souls (2026-11-02 [machines set 1]).
- **C-035** → a machine's effect is never the same act as magic → an ensouled AI in a body, or a robot with receptors, "could likely use magic" (2026-11-02 [Q-B]).
- **M-233** → the galaxy's electronic and enchanted might comes from Remnant infusion → "electricity and shit would still power most machines"; Remnant is needed only for ensouled-AI machines (2026-11-02 [power]).
- **M-214** → a soul held in matter feels dread → only vague, general things, "maybe some strangeness"; sensation comes from sensory organs (2026-11-02 [Q-A]).
- **W-324** → only the elven bond can pool Remnant → amplifier rigs hold pooled Remnant for any wearer; Remnant wells are mined; everyone in the Tower draws on its pool (2026-11-02 [techs 1–8]; 2026-11-01 [L8 Tower]). It also clashes with WR's own M-236.

### Flesh-core supply
- **W-222, W-229** → giant and then Derrek flesh-core *monopolies* → "they can all be made by everyone like the real world. Ideas spread"; who makes what falls out of story (2026-11-02 [set 1, item 6]). A story-level monopoly might survive if Patrick wants it, but it needs his call.
- **M-229, M-230** (soft) → young orcs are processed into flesh cores holding a complete soul → the standard core is grown flesh around a measured draw of *pool* Remnant; orc-soul cores are the cheap "tainted" kind, sold mislabeled; the public doesn't know soul-tech uses souls (2026-11-02 [set 1], [techs 1–8], [what's banned]). Orcs as a source of *flesh* still fits ("flesh is both grown and harvested").
- **W-233, B-109, M-246** (soft) → metal "dwarven magic-infused cybernetics" let humans rival elders → metal augmentation may have adverse effects; flesh-grown augmentation keeps Remnant control (2026-11-02 [augmentation]).

### Time powers, immortality, the death-reset
- **C-097** → Jon and Derrek "borrow its magic" → their *only* given power is time; everything else they developed themselves; t196's "borrowed magic" is a 🚫 candidate (2026-11-01 [L4, Law 17]).
- **C-113, C-123, C-124, C-125, C-191, B-030** → "fused with time" / "the time-fusion" → "always wrong" wording; reword as plain description (one with time, in control of and bound to it through the keeper's pact) (2026-11-01 ["time-fusion" wording]; [NP#6a pact]).
- **C-191** → true immortality "through the time-fusion" → their bodies *can* die; the keeper instantly hard-resets them to where they died (2026-11-01 [L4]).
- **C-194, C-195, C-196** → a god can kill Derrek; Jon can kill Derrek; only a god with power from beyond the regress could threaten him → killing is pointless because of the death-reset; "Ya I dont think he can die lol"; a true-god ally would only cause an endless loop (2026-11-01 [L4 follow-ups]; [L4 window]).
- **C-157** (soft) → Jon's belief that this run is final is a lie → "jon has decided he wont reset anymore", left unrevealed in Book 1 (2026-11-01 [time travel showing]; [W50]). The "lie" (W42) may still stand for earlier runs, but needs a check.

### The keeper and the Blight
- **C-079, C-080, C-081** → every fractal level has a keeper, a consumer and a Blight as titles → that framing (W36) is replaced (2026-11-01 [L12]).
- **C-083** → the Blight seeks maximum dissolution → the Blight is the faction of the regress pressing on our barrier (including the keepers' own brother Unified Ones or greater). "Blight" is a placeholder for "enemies of our reality, those who wish to consume or destroy" (2026-11-01 [L12]; [L12 follow-up]).
- **M-171, M-195** (soft) → "Blight-favor" pacts and Blight-things as patrons → the Blight is outside the barrier and the keepers hold it out (2026-11-01 [L12]). It's unclear how a Blight pact reaches in; flag for Patrick.

### Cosmology scale
- **C-068, C-069** (soft) → "universe" means only planes of the regress and sibling worlds; smaller realms are never universes → every iota of Remnant is a whole universe further down; tiny beings build empires inside what we see as a quark (2026-11-02 [Law of the Regress]; [nested vs 0b/0c]). C-217 ("no alien peoples") holds only at our scale.

### The elven bond
- **M-167** → the bond doesn't track individuals; an elf who dies far away dies alone → the bond scales with Remnant and distance: a far lone elf is a near-invisible pinprick, up close you feel each other, and the homeworld shines like a beacon (2026-11-01 [L9, W08]). "Doesn't track" really means "can't feel at a distance".
- **M-169, B-135** (soft) → elves feel a member's disposition → BANK doesn't speak to disposition, but sensing is distance- and size-limited (same entry), so disposition-reading should be proximity-bound.

### Jon and the elves
- **W-126** → Jon is the elves' hidden god → "he isnt the actual secret master. Mika is very much in control" (2026-11-01 [W44, t550]).
- **W-127** → Jon asks devotion and breeds a warrior people → retired, along with the "gardening" framing (same entry).
- **W-130** → "the elven bloodline Jon led across the ages" is lore and Jon's side goal → Jon has no sway over the elves; he's an outsider who helped Mika as a boy (2026-11-01 [L10]; [W44]). Whether a bloodline side goal survives in any form needs Patrick.
- **W-204** → Jon led Mika and the elves away on the seedship → "I think mika alone" (2026-11-01 [L10, NP#71b]).
- **W-205** → Jon worked the elves toward fleeing over centuries → same, no sway (2026-11-01 [L10]).
- **W-243** → the Inquisition unknowingly hunts "its own god" → it still hunts whoever causes resets without knowing it's Jon, but Jon isn't its god (2026-11-01 [W44]).

### The Tower and betrayal day
- **W-159, W-160** (soft) → the emperor "converted himself into a giant stone tower"; the Tower *is* the converged emperor → he converged his *entire city* as a shield against the breath. He didn't survive as himself: every soul is merged into one centerless mass of Remnant in the walls (2026-11-01 [L7]; [L7 emperor alive]). M-205, M-206 and W-161 already fit.
- *(Missing from WR, not a conflict: the Tower is the largest Remnant source on Earth and a massive amplifier, the reason Derrek stays there and tore the dimensions there, and the place of the final peak sequence. 2026-11-01 [L8].)*

### Dragons
- **B-093** (soft) → dragons are a small, family-tied group → "dragon" is an umbrella: great winged dragons rule subjugated reptilian kin whose separate identity was erased (2026-11-01 [dragons umbrella, confirmed]).
- **B-117** (soft) → "a dragon's prepared stone" as a general trump card → only transmutation-studying dragons make stones; maybe an industry mass-producing them for sale 🌊 (2026-11-01 [dragon stones]).
- **B-203** (soft) → a dying dragon might detonate itself rather than be worn → dragon deaths vary; dragons don't self-destruct as a custom (2026-11-01 [dragon deaths]). Possibly fine as a rare individual act.

### Checked, no conflict
- **The "random" curse:** no WR claim uses it. It appears only in the open-questions appendix (World: "time powers seizing him at random"), which BANK settles (§4). C-148–C-151 already match the tether.
- **Lirael's window line, the rose cage, the son as "drywall", Book 1 window beats:** WR has no claims on these.
- **Soul-sensing machines:** WR has none. M-047–M-049 (rare, unreliable, never scanning) fit BANK 11-02 (no general machine soul-sensing; only spoof or reading-chip devices).
- **M-015** "not a pool" vs BANK's "latent pools": a word clash only. M-015 means a being's Remnant isn't a mana pool.

**Count: 32 entries covering 50 unique IDs** (21 flat conflicts, 11 soft).

---

## 3. CONFLICTS WITH CODEX (where BANK is silent or only partly speaks)

| WR | Codex says | Which looks newer |
|---|---|---|
| **M-234**, M-022: the focusing chamber is an amplifier, "not a drain or a battery" | It drains a captured dragon of "every iota of his energy" into batteries: `01 L223`, `06 L110`, `07 L134`, `11 L30`, `NEEDS_PATRICK L69`; the seam is "STILL OPEN" (`06 L111`). | **WR newer.** It follows BANK 10-31's spirit ("battery" retired), though BANK ruled on held souls, not chambers. Confirm it extends to chambers. |
| **M-230, M-231**: orcs and the dead are processed into flesh cores and metals | "a planet of slaves drained of their Remnant so the giants have endless energy" (`07 L298`, t54) | **WR newer**: it reframes drain-as-energy as flesh processing. |
| **W-223**: the dragons destroyed the giants' entire home world | The strike annihilated "the heart of the giants' forge world" (`07 L299`, t412) | **WR newer** (escalation). |
| **W-228**: the any-tactic and cashed-out camps are Derrek's secret flesh-core factory | Any-tactic giants are a league "who does whatever for money" for dragons; the cashed-out "quit the game entirely and just took seats of power" (`07 L134–135`, t48) | **WR newer.** It extends the camps rather than contradicting them, but "cashed-out quit the game" sits oddly with "secret factory". |
| **W-225–W-227**: the strike's motive was the human flesh-core supply | "How he engineered it is not re-ruled" (`08 L146`, `09 L97`) | **WR newer** (fills an open slot). |
| **C-153**: rewritten "about 5,000 times" | Each run ~10,000 years, "a thousand or more runs" (`01 L142`, `02 L165`); "~5000 is a floor; think 10× and up" (`09 L131`) | **Codex more precise.** WR turns a floor into an estimate. |
| **M-163**: enchantment is "set and left" (no concentration); also M-218 | "Objects hold souls without a holder's concentration" is 🌊 proposed, unconfirmed (`04 L118`, wk2 note) | WR states as settled what the codex marks 🌊. BANK 10-31 ("souls can sit inside certain materials") leans WR's way. WR's own appendix still lists it as open. |
| **W-031**: dwarves forge for humans in a "peaceful, mutually beneficial" relationship | The codex has this line (`10 L26`) but its own dwarves section says "Grimdark, not noble partnership". WR W-269 says computing knowledge "had to be coerced". | An internal codex tension that WR inherits. The older line is `10 L26`. |
| **W-032** "Giants are few" vs **B-075** "quietly more numerous than anyone thinks" | Both in the codex (`10 L32`, `07 L275`) | Inherited; B-075 (t418) is the newer read. |
| **B-155** (elves avoid heaven; it stays empty) vs **W-335** (elven ships enter heaven to travel) | Both in the codex (`10 L134`, `07 L158`) | Inherited; reconcilable (transit is not residence). |
| **W-005** (far future = rift at its widest, still breaking) vs **C-168** (by the late loops nothing is left to widen) | Both in the codex | Inherited tension. |

**Count: 11 rows** (5 where WR looks newer, 1 where the codex is more precise, 1 where WR states a 🌊 item as settled, 4 inherited internal tensions).

---

## 4. OPEN QUESTIONS already answered by BANK

**Settled (13)**
1. *Overreach as a named mechanic?* → **"Burnout"** is the in-world folk word for overuse destroying the body; Remnant is never used up (10-31 [NP#2, L8]).
2. *Dense unclaimed Remnant at great-death sites usable?* → Yes. Latent pools and wells are mined like oil, rift sites are richest, and the Tower is the largest pool and amplifier (11-01 [L8]; 11-02 [techs 1–8]).
3. *Bond monitoring disposition vs not tracking individuals?* → The bond scales with Remnant and distance (11-01 [L9]).
4. *"A god asks devotion; a demon offers a deal" vs one continuum?* → "God" and "demon" are in-world titles for powerful beings, not races (11-01 [NP#5]).
5. *Does "seeks maximum dissolution" still describe the Blight?* → No; it's replaced (11-01 [L12]).
6. *"Borrow the puppeteer's magic" vs "only given power is time"?* → Time only; "borrowed magic" is a 🚫 candidate (11-01 [L4]).
7. *How can Jon kill Derrek?* → He can't, meaningfully: the death-reset (11-01 [L4 follow-ups]).
8. *Do the limits on killing Derrek apply to Jon?* → Yes; both are reset on death (same).
9. *Is "hell" (human warp route, demon home, elven clone-pocket) one place?* → One hell, the elven prison realm, which is also the human FTL route; no demon home plane (11-01 [NP#5]).
10. *"Tether" names two tethers?* → One tether, the keeper's pact, running to both men (11-01 [NP#6a]).
11. *What does Jon carry across resets?* → His soul. The brain is rewound with the body, so he wakes blank (11-01 [time-travel mechanism]). The tension with the rose beat stays open (QUESTIONS 2.1).
12. *Derrek's conquest vs his powers seizing him "at random"?* → "Random" is deleted outright; he moves only when Jon jumps (11-01 [NP#6b]).
13. *Jon leading Mika vs the royal directive?* → Mika alone ordered the exodus (11-01 [L10]).

**Partly settled (21)**
14. *Pact overreach: burnout or exhaustion?* → Burnout covers any overuse that destroys the body (10-31). The pact case isn't named.
15. *Do objects hold souls without concentration?* → Souls "sit inside certain materials"; flesh weapons and soul-cores hold them (10-31 [L11]; 11-01; 11-02). Concentration isn't addressed.
16. *Which vessels need concentration?* → Flesh and living material hold best (living weapons, the rose); the rest is open.
17. *Older account of Convergence?* → The Tower is the emperor's city converged as a shield. Modern towers, buildings and hulls are Convergence. Flesh weapons use a Convergence-like ritual (11-01 [L7]; 11-02 [tech 7]). Its funerary origin and monetization aren't re-ruled.
18. *Convergence vs the three enchantment types?* → Flesh weapons and soul-cores tie Convergence to held-soul items; there's no full mapping.
19. *What a demon patron gains; how the tether feeds a god?* → "Demon" is only a title (NP#5); the gain is still open.
20. *The Orc King's patron?* → Not a demon from another realm, since demons are powerful beings of this world (NP#5). Who it is stays open.
21. *Can non-mages use reservoirs and enchanted items; do they degrade?* → Amplifier-only, "nothing drains" (10-31); the public uses ensouled machines (11-02). Degradation isn't stated.
22. *The amplifier principle case by case?* → The principle is settled (amplifier, never battery, 10-31). The cases (orc chips, captured dragon, slave planet) are open.
23. *The mechanism of a soul held in inert matter?* → Flesh holds best; complex machines need flesh to hold Remnant (11-02).
24. *The puppeteer's motive; is it coherent?* → It acts as pact patron, punisher and guardian of the barrier, and can reset the world itself (11-01 [L4], [L12]). That leans toward guardianship; the motive isn't formally chosen.
25. *Is the Tower rift the only entry, given rifts "in the sky"?* → Rifts are ground sites, "not the sky", each a reset scar; the Tower is where Derrek tore the dimensions (11-01 [time travel showing]; [L8]).
26. *Does a soul in a changeling feel being worn; does the dread extend?* → Held Remnant feels only vaguely, since sensation needs organs (11-02 [Q-A]). Changelings aren't addressed directly.
27. *Exact dragon population?* → "Dragon" is an umbrella over subjugated kin (11-01), which changes the headcount question.
28. *The Emperor's son: pawn or person?* → In Book 1, "drywall" to Derrek. He gathered Jon's team and brought them to the Tower; both men's lever plan failed (11-01 [L3], [W41]). His name and nature are open.
29. *Stock of the legal organ market?* → Clone flesh is sold, often passed off as real (11-02 [set 1]).
30. *Modern augmented humans fit the timeline?* → Augmentation rules: flesh-grown keeps Remnant control, metal has drawbacks (11-02). The era is open.
31. *Is the race roster thin?* → Adds dragon-kin and reptilian peoples (maybe frog-folk) and small trolls (11-01).
32. *Unbuilt: goblin/troll detail, demons?* → Troll size is set; demons are not a race (11-01).
33. *Authorless churn vs Jon and Derrek manufacturing everything?* → Jon has no sway over the elves and Mika runs his own people (11-01 [L10], [W44]). That weakens the "Jon controls" side.
34. *Heaven, dark prison and time-god society: fixed or provisional?* → Hell is settled as one realm (NP#5); the rest is open.

---

## 5. Summary

| Bucket | Count |
|---|---|
| NEW in WR (no codex basis) | **34 claims** (flesh tech 8 · chambers/ships 4 · forge world 14 · strike/Derrek 7 · wording 1) |
| Conflicts with BANK | **32 entries / 50 IDs** (21 flat, 11 soft) |
| Conflicts with codex (BANK silent) | **11 rows** (5 WR newer, 1 codex more precise, 1 🌊-as-settled, 4 inherited) |
| Open questions settled by BANK | **13 settled + 21 partly** (of 91 appendix items) |
| WR claims with a codex source | ≈ 1,090 of 1,129 (many of them now overridden by BANK) |

**Top 10 new items for Patrick to confirm as canon** (all 🌊 until he rules):
1. **M-228, M-229**: flesh holds Remnant best; "flesh cores / living metal" from warped living flesh hold a complete soul. (Name "living metal" is a placeholder unless he coined it.)
2. **M-230, M-231**: young orcs become flesh cores; the old and dead become lesser enchanted metals. (Square this with BANK's pool-Remnant cores and "tainted" orc cores.)
3. **M-232**: walls and ships are made from the dead; inorganic structures need no living material.
4. **M-236, M-237**: a dragon firing from a converged living-metal ship draws on the whole ship's Remnant, which is why beams break planets.
5. **M-234**: the focusing chamber is an amplifier, not a drain or battery (retires the codex's "drain into batteries").
6. **W-222**: giants' flesh-core monopoly via Convergence (clashes with BANK "ideas spread").
7. **W-228, W-229**: Derrek's secret deal with the any-tactic and cashed-out giant factions as his flesh-core factory, and his resulting monopoly.
8. **W-225–W-227**: the forge-world strike's motive was to cut the human flesh-core supply and cripple a rival Derrek no longer needs.
9. **W-223, W-224**: the dragons destroyed the giants' entire home world, and no tower remembers it.
10. **W-208–W-216**: the giants' departure on the first (converged) cathedral ship, a slow sub-light crossing to a pre-chosen world, and 5,000 years on the forge world.

Also worth a ruling: **M-233** (Remnant as the source of the galaxy's might) directly contradicts BANK 11-02 on power. Drop or reword it.
