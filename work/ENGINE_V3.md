# Engine v3: the Foundry
🌊 Claude design doc, 2026-11-21. Draft for talking through with Patrick. Nothing is built yet.
Inputs: Patrick's direction (BANK 2026-11-21), `work/PIPELINE_V2.md`, `work/RECURRING_ISSUES.md` (the mined notes catalogue), and new research (sources at the end).

## 0. The shift in one paragraph
Until now the engine has been a **workshop**: one book, Patrick reading every chapter, catching the gaps by hand. Patrick is stepping back. The engine has to become a **foundry**: many stories across four eras, and Patrick sees only a one-screen digest per story plus a short queue of world questions. So the job Patrick did by reading (catching what's wrong, what feels false, what isn't *his*) has to move into the machine. Three things make that possible:
1. **A firm world**, thick enough that writers stop guessing (the World Kernel plus four Era Bibles).
2. **Shared memory across stories** (the Registry), so story #40 knows what story #12 did.
3. **Prevention before cure**, so the writer never makes the notes we keep getting. Today the checkers catch them after the fact.

## 1. What we have, honestly
**Works**
- The planning room (slice → cast → conflict → cards → audit) and the per-chapter v2 loop.
- continuity-keeper + `story_state.md`: it caught nine plan-vs-state clashes before drafting.
- character-sim: it stops characters acting for the plot.
- The seed cap, wordcheck.py + slop list, and originality-check: it caught Hollin, Garro and the Yoda lift.
- The BANK → pass → RULINGS loop for canon.

**Breaks at scale**
- **Patrick is the main gap-catcher.** Doc being owned, Returned ship too early, the button-chip Orc King, Eli reading cold, Jon returning, 24 seeds: each one was caught by Patrick or Grok, not by the engine.
- **Everything is story-local.** story_state, ledgers and voice notes live inside one book. A second story would start blind.
- **World answers are invented mid-draft.** When a chapter needs "how does a comm work in this era," the writer guesses. That guess either quietly becomes canon or contradicts it later.
- **Too many agents, run in series.** 24 agents and about 12 calls per chapter. That hits rate limits (we had three 429 stalls). There's no resume runbook, and agents can't commit.
- **Taste lives in Patrick's head and the BANK prose.** No agent reads it as a rubric.
- **The checkers catch symptoms.** The writer keeps making the same classes of mistake because the fixes go into reviews, not back into the writer's brief.

## 2. The architecture: three layers
```
WORLD LAYER (Patrick's, firm)        REGISTRY (shared, grows)          FOUNDRY (per story)
 codex_v5 + BANK                     characters / places / events      commission → brief → plan
 └ World Kernel (rules sheet)        names (all races, all eras)       → draft → checks → polish
 └ Era Bibles ×4                     inventions (LOCAL → promote?)     → readers → digest
 └ Power & Scale table               timeline of all story events      
 └ World Gap Queue → Patrick         cross-story continuity            
```

### 2a. World Layer: make it firm enough to write blind
- **World Kernel** (`world/KERNEL.md`): the codex boiled down to **hard rules a writer must not break**, one line each with a cite.
  - Magic: Remnant / Will / Skill; burnout means the suit burns; the capacity cap; flesh holds and metal must be bound; enchantment is held Remnant; the Tower amplifies; the elven bond is an organ.
  - Race sheets: lifespan, Remnant, body, senses, what they eat, how they die, how they talk.
  - The 🚫 retired tripwires.

  Every writer and checker reads this, not the 230k-word codex. This is the biggest single fix.
- **Era Bibles ×4** (`world/eras/B1…B4.md`), one per timeline (far future / space wild west / late Darkest Age / cosmic). Each is a *texture* bible, not a plot one:
  - tech level and what's common vs rare (comms, weapons, ships, medicine);
  - money, prices and wages; food, drink and drugs;
  - travel times; who rules where; what ordinary people believe about magic;
  - slang and oaths, by race;
  - what a street smells like; what kills poor people; what the rich do for fun;
  - the faction clocks (who is rising or falling in that era).

  This is "build the world thicker." It is built by a **thickening sprint** (§5), not mid-story.
- **Power & Scale table** (`world/POWER_SCALE.md`): what each tier of power can actually do, in scenes. Examples: a street mage lifts a loader; a master stops a fall; a dragon does X. Checkers use it for the "why doesn't X just…" audit and to stop power creep across stories.
- **World Gap Queue** (`world/GAP_QUEUE.md`): the key new mechanism. When a story needs an answer the Kernel and the Era Bible don't have, a **gap-detector** classifies it:
  - **World-level** (how magic works, what a race is, era tech, big history): the story *does not invent it*. It writes around the gap, or uses a clearly flagged provisional answer marked 🌊 HOLD. The question goes into the queue as a phone-short A/B/C with Claude's pick. Patrick answers in batches, whenever he likes. Answers flow through the normal bank → pass.
  - **Story-level** (a town, a minor person, a custom, a ship): invent freely, tag it LOCAL, log it in the Registry.

  This is how Patrick stays out of the reading but stays the owner of the world.

### 2b. The Registry: memory across stories
`registry/` holds plain markdown tables, one row per thing:
- `characters.md`: name, race, era, born/died, stories they appear in, status, the voice card link.
- `places.md`, `events.md`: dated on a **single master timeline** across all four eras.
- `names.md`: every name used, by race and era. The **name engine** (§4) checks against it so we never reuse or collide.
- `inventions.md`: every LOCAL invention, with a "used in N stories" count. Anything used in 3+ stories, or that a story leans on hard, is offered to Patrick for promotion in the batched digest.
- **Voice cards** (`registry/voices/<name>.md`): one per recurring character, built from their best lines plus calibration notes. Example: the Eli card holds "loving but absent-minded; loves the idea of his friends; the softness is the point". A character who "gets big" gets a full **dossier** (want, wound, lie, arc across stories). That is "explain every character who gets big."

continuity-keeper gains a second job. At story end it **writes the story's facts into the Registry**. At story start, world-slicer **pulls** every Registry row the story touches.

### 2c. The Foundry: the per-story pipeline, rebuilt
**Commission layer (new).** `foundry/SLATE.md` is a queue of story pitches. They are generated by an idea agent across four axes:
- era;
- scale (vignette, short, novella, novel);
- angle (character spinoff, historical event, ordinary life, faction war, mystery, horror, heist, romance, comedy-grim);
- whose story (a Registry character who's "gotten big," or someone new).

Claude picks a balanced batch. Patrick can veto or star items, or say nothing.

**Per-story pipeline (v3):**
1. **Brief + pre-flight.**
   - Brief from the pitch.
   - The **gap-detector** reads the brief against the Kernel, Era Bible and Registry, and lists every world question the story will touch. World-level questions go to the queue (the story waits or writes around them). Story-level ones get invented now.
   - **Gate A (optional, by autonomy level).**
2. **Planning room, merged.**
   - world-slicer (now also pulls the Registry).
   - cast-builder + conflict-mapper (can run together).
   - scene-carder.
   - plan-auditor. It now also runs: the **reader-knowledge plan** (what the reader, each POV and each character knows, scene by scene, and the reveal schedule); the **suspense plan** (in each tense stretch, the protagonist's options shrink); the **fair-play check** for mysteries (two readers, one naive and one detective: the twist must surprise the first and be gettable by the second); and the **stakes and deaths ledger**.
   - continuity-keeper plan-check (as now).
   - **Gate B (optional).**
3. **Writer pre-flight (new; prevention).** Before every chapter, the writer gets one page, `WRITER_PREFLIGHT.md`, generated from `RECURRING_ISSUES.md`. It holds:
   - the ten mistakes we keep making, as don'ts with one-line examples;
   - the voice cards for everyone on stage;
   - the slop list and tic caps;
   - the seed cap;
   - the style anchors.

   This is the main lever. The catalogue becomes rules *before* the draft instead of notes *after* it.
4. **Draft** (scene by scene, character-sim for choice scenes).
5. **Checks, merged into 3 parallel agents** instead of about 7 in series:
   - **logic-check** = sense-checker + continuity (5 categories, quoting both lines) + Kernel rules + power scale + calendar, travel, wound and money clocks.
   - **craft-check** = payoff-keeper (seeds) + forecaster (tension) + dialogue notes + "telling not showing" + theme.
   - **taste-check (new)** = a **Patrick-proxy**: a rubric built from every note Patrick has ever given, plus originality-check.
6. **Fix pass** (the writer, driven by author_calls).
7. **Polish:** wordcheck.py (free; a script, not an agent), then one combined dialogue + word-watch pass, then story-guard.
8. **Readers:** reader-panel (5 personas) on STORY_ONLY. A cold-reader for shorts.
9. **Deliver:**
   - FINAL + STORY_ONLY + a **one-screen DIGEST**: the story in 5 lines, what it adds to the world, new LOCAL inventions, world questions raised, and the reader-panel score.
   - Registry write-back. Commit.

**Speed tiers:**
- **Vignette / short** (under 8k): one merged check round, no forecaster, cold-reader instead of the panel.
- **Novella:** the full chapter loop.
- **Novel:** the full loop plus whole-book passes (arc, theme, sag in the middle, ending).

## 3. Complex-narrative coverage checklist
Everything a deep story can contain, and which part of v3 owns it. ✅ = covered today · 🆕 = new in v3.

| Need | Owner |
|---|---|
| Canon and magic rules | Kernel + logic-check 🆕 (was canon-checker) |
| Power scaling, "why doesn't X just" | Power table 🆕 + plan-auditor ✅ |
| Motive and cooperation (no one acts for the plot) | character-sim ✅ + plan-auditor ✅ |
| Who-knows-what, dramatic irony, reveal schedule | reader-knowledge plan 🆕 (state Knowledge table ✅) |
| Mystery fair play | two-reader check 🆕 |
| Suspense (shrinking options) | suspense plan 🆕 + forecaster ✅ |
| Seeds and payoffs, seed density | payoff-keeper ✅ |
| Timeline, calendar, travel time, wound clocks, money | continuity-keeper ✅ → generalised clocks 🆕 |
| Offscreen faction moves | conflict-mapper ✅ + Era faction clocks 🆕 |
| Deaths and stakes that stick (grimdark) | stakes ledger 🆕 |
| Multi-POV (each POV knows only its own) | reader-knowledge plan 🆕 |
| Nonlinear / frame narratives (e.g. Barnaby as historian) | scene-carder story-order vs telling-order fields 🆕 |
| Subplots braided, none forgotten | scene-carder thread map 🆕 |
| Theme (what it's about underneath) | brief ✅ + craft-check theme line 🆕 |
| Character arcs across stories | voice cards + dossiers in Registry 🆕 |
| Voice consistency per character | voice cards 🆕 (voice_notes ✅) |
| Dialogue that sounds human | dialogue pass ✅ |
| Setting texture, era-true detail | Era Bibles 🆕 |
| Prose tics, slop | wordcheck + slop list ✅, pre-flight 🆕 |
| Originality and name collisions | originality-check ✅ + name engine 🆕 |
| Cross-story contradictions | Registry + master timeline 🆕 |
| Patrick's taste | Patrick-proxy 🆕 |
| Tension and pacing | forecaster ✅ + reader-panel ✅ |
| Endings that land | whole-book pass + panel ✅ |

## 4. Supporting builds
- **Name engine** (`scripts/names.py` + `world/NAMES.md`): per-race sound rules (syllables, consonant clusters, endings), drawn from the canon names. It generates candidates, filters them against the Registry and a list of famous fictional names, and logs the choice as LOCAL.
- **Patrick-proxy rubric** (`foundry/PATRICK_TASTE.md`): mined from the BANK and every correction. It lists:
  - what he loves: grit, the grotesque, eloquent-but-broken, softness under menace, earned scale, concrete texture;
  - what he hates: op reality-shifting tech too early, buttons-and-gimmicks, too many seeds, characters made too revered, AI additions he didn't approve, summary instead of scene.

  It's scored per chapter.
- **Run manifest and resume** (`stories/<slug>/RUN.md`): each stage gets a status line (done / running / failed) and its output file. After a 429 or a context reset, the next session reads RUN.md and resumes. Claude commits after each agent, since agents can't.
- **Model tiering.**
  - The strongest model for writer, Patrick-proxy and final judge.
  - A mid model for the logic and craft checks and the planners.
  - Scripts (no model) for word counts, tics, slop and name collisions.
  - Merging about 12 calls per chapter down to about 6 cuts rate-limit stalls by roughly half.

## 5. Build order (what I'd do, in sequence)
1. **Catalogue → pre-flight + script gate.** Turn RECURRING_ISSUES into `WRITER_PREFLIGHT.md`, `PATRICK_TASTE.md` and `DECLINED.md`, and extend wordcheck.py into the gate. *(Cheap, biggest quality win.)*
2. **World Kernel.** Distil the codex into the hard-rules sheet, then canon-check it against the codex.
3. **Registry seed.** Load everything Book 1 has established (characters, names, places, inventions, timeline).
4. **Merge agents.** Write logic-check, craft-check and taste-check; retire the overlaps into modes. Rewrite `story/SKILL.md` as v3; add RUN.md.
5. **Gap-detector + queue**, and the name engine.
6. **Thickening sprint, one era at a time.** idea-scout drafts the Era Bible from the codex. canon-checker vets it. Gaps become the first batch of A/B/C questions for Patrick. Start with **Book 2's era** (space wild west), the least built and the most fun to mass-print.
7. **Calibration run.** Three short stories, one each in B1, B2 and B3, through the full v3 pipeline. Measure: which notes still slip through? Feed them back into pre-flight. *Then* open the tap.

## 6. What the catalogue changes (from `work/RECURRING_ISSUES.md`, 25 kinds ranked)
The catalogue confirms the design and adds five things it lacked:
1. **The plan must be drafted from `story_state.md`.** Every plan check found 11–14 breaks (kind 3) because the planner works from memory. Fix: scene-carder and the writer both open the state file first, and the plan check becomes a script-assisted diff.
2. **A script gate after every draft, before any agent.** It runs wordcheck.py and checks verbatim repeats, cite and quote resolution in NOTES and ledgers, tracked-object mentions, chapter-closer similarity and overdue seeds. Four agents were counting the same tics by hand (waste c2), and wordcheck was often left unrun.
3. **One merged, de-duplicated review.** The same flag was raised by 2–4 agents and merged by hand (waste c1). The logic and craft checks write to a single `review.md`, keyed by line number. "Checked and clean" items go to the ledger, not the report (waste c3).
4. **A provenance filter on blind readers.** The panel, forecaster, cold reader and Grok/Gemini notes all hit Patrick's protected lines, settled calls, or rules they couldn't see (catalogue b). Their notes pass through a filter against `PROVENANCE.md` and the declined register before reaching the writer. The forecaster's fixes are checked against the Jon and Doc rules (R-034, R-047).
5. **A shared "declined, and why" register** (`foundry/DECLINED.md`). The Eli softness was argued six times before the calibration, "break the speech" was raised three times after Patrick's "eloquent", and the nosebleeds came back three times. Every reviewer and every outside paste is checked against it.

**Reintroduction is the sneakiest failure** (catalogue a): Vosk's proud line swung back and forth over 5 passes, a new Yoda image appeared after the first was removed, and Garro was coined right after the Hollin fix. Fix: once a decision is made it goes into the pre-flight as a hard **DON'T** with an example, and the script gate greps for it.

**Provenance gap:** nothing marks Patrick's real lines apart from AI-added "protected" ones (kind 24). Fix: `PROVENANCE.md` cites every [P] line to a BANK date. Without a BANK cite, a line is not protected.

## 7. Recurring issues → where each is prevented
| # | Kind (catalogue rank) | Prevention in v3 | Script? |
|---|---|---|---|
| 1 | Word tics and motifs | pre-flight caps + script gate | ✅ |
| 2 | Neat, explaining dialogue | pre-flight DON'Ts + dialogue pass | partial |
| 3 | Plans and notes contradicting the text | plan drafted from state; cite resolution | ✅ |
| 4 | Broken on-page rules | `ledger_rules` in the pre-flight packet ("rules touched") | partial |
| 5 | Object, injury and hand drift | inventory and clocks in the packet; tracked-object grep | ✅ |
| 6 | Geography and timeline slips | calendar from day one; travel times in the Era Bible | partial |
| 7 | Convenient arrivals | conflict-mapper offscreen clocks | — |
| 8 | Acting for the plot | character-sim + Power table | — |
| 9 | Telling | pre-flight + craft-check | — |
| 10 | Interpreting Jon (and Doc) | rules R-034 and R-047 in the packet + declined register | partial |
| 11 | Seed overload | seed budget in the packet | ✅ (count) |
| 12 | Clue stacking | pointer budget per seed | partial |
| 13 | Repeated beats and scene shapes | scene-carder shape field; book-level shape log | partial |
| 14 | Rhythm on autopilot, buttoned closers | closer comparison across chapters | ✅ |
| 15–16 | Stock phrases, repeated openings | script gate | ✅ |
| 17–18 | Trope echoes, name collisions | name engine + Registry + originality-check | ✅ (names) |
| 19 | Reader lost (unanchored terms) | term registry: first use must be anchored | ✅ |
| 20 | POV and knowledge slips | Knowledge table + reader-knowledge plan | — |
| 21 | Pacing sags | forecaster + panel; travel budget per chapter | — |
| 22 | Overdue seeds | script gate flags them | ✅ |
| 23 | Misreading the soft protagonist | voice card calibration + declined register | — |
| 24 | AI lines treated as Patrick's | provenance with BANK cites | ✅ |
| 25 | Stale ledgers | ledger update moves into the merged review step | — |

## Sources (new this round; v2 sources are in PIPELINE_V2.md)
- NousResearch autonovel (autonomous novel pipeline: world bible, characters, outline, drafting with evaluation, revision cycles): https://github.com/NousResearch/autonovel
- Inkfluence series bible (persistent series memory: last 3 chapters plus a running record): https://www.inkfluenceai.com/for/series-authors
- Shadow-Loom (graph world model scoring reader states: mystery, dramatic irony, suspense, surprise), arXiv 2605.02475: https://arxiv.org/pdf/2605.02475.pdf
- Fair-play detective stories (two reader models: surprised vs brilliant detective), arXiv 2507.13841: https://arxiv.org/html/2507.13841v1
- Suspense via iterative planning (diminishing escape options), arXiv 2402.17119: https://arxiv.org/pdf/2402.17119
- Expectation modelling via imagined continuations, arXiv 2412.15239: https://arxiv.org/pdf/2412.15239
- Uncertainty and creativity in generation, arXiv 2602.16162: https://www.arxiv.org/pdf/2602.16162
