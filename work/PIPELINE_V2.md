# Story engine v2: what the best AI-fiction pipelines do, and what we add
🌊 Claude research note, 2026-11-17. Sources are at the end. Earlier research is in `work/PRO_METHODS.md`.

## What the field does now
1. **Separate the logic from the prose.** Plan the story's structure first, then write (Agents' Room; CreAgentive). *We have this:* the planning room, then drafting.
2. **A shared, structured story state, compared scene by scene.** MAGNET keeps a shared world state, and its evaluator Atlas compares the current scene's world state with earlier scenes'. Another paper keeps a temporal knowledge graph of the story so far and reports 88% fewer conflicts. *We now have:* `continuity-keeper` with `story_state.md`. **Upgrade:** a state snapshot for every scene, not every chapter.
3. **A taxonomy of consistency errors, with evidence chains.** ConStory-Bench sorts errors into five kinds: timeline and plot logic, characterization, world-building rules, factual details, and narrative style. Its checker quotes both conflicting passages as evidence. **Upgrade:** the continuity check uses those five categories and must quote both lines.
4. **Don't trust one model to find plot holes.** "Finding Flawed Fictions" found that frontier models are near random at detecting plot holes, and that LLM summaries and drafts *introduce* holes. **Upgrade:** for any plot logic, run two independent checkers (sense-checker and continuity-keeper) plus an outside reader (Grok), and act only on findings that cite the text.
5. **Characters as agents.** MAGNET has persona-grounded character agents that propose their own next action from the shared state. This fixes "people acting for the plot." **New:** `character-sim` runs before a key scene. Each main character, from their dossier and the current state, says what they would do and want there, and the writer must honour it or give a cause.
6. **Schedule who knows what and when it's revealed.** Book-Agent schedules revelations: what the reader knows, and what each character knows, at each point. That's essential for Jon's opacity. **Upgrade:** `story_state.md` gets a *Knowledge* table (reader / Eli / each character) and a reveal schedule.
7. **Measure tension by forecasting.** "Spoiler Alert" uses narrative forecasting as a tension metric: if a model can easily predict what happens next, the tension is low. **New:** `forecaster` reads up to the end of each scene and predicts the next one. If it's right too often, the writer adds a turn. If it's wildly wrong, check whether the turn was earned.
8. **Synthetic reader panels.** LLM personas with different tastes react to the text and mark where they'd quit (DNF). There's no validation against real readers, so treat it as a smoke test. **New:** `reader-panel` runs 5 personas: grimdark veteran, casual fantasy reader, hater, literary reader, and a teen sci-fi fan. Each gives where they'd stop, what confused them, and what they'd tell a friend.
9. **Anti-slop, done with data.** Antislop (ICLR 2026) profiles words and phrases a model over-uses compared with human text, then bans them. The authors say to build your own list. **Upgrade:** `wordcheck.py` gets a project slop list (`scripts/slop_list.txt`) built from our own drafts. The writer gets that list *before* drafting, as prevention, not only cure.
10. **Style anchors.** Keep a small set of the best approved passages as the voice reference (style memory). **Upgrade:** `v3/style_anchors.md` collects 5–8 passages Patrick approves, and the writer and line-editor read it.
11. **Record human authorship.** The U.S. Copyright Office's January 2025 report (Part 2) says AI-assisted works are registrable where the author made substantial creative choices, so keep records of outlines, bibles and revisions. *We have this:* BANK, RULINGS and git history. **Upgrade:** a `PROVENANCE.md` per book listing Patrick's own beats, lines and rulings.
12. **The human sits at the gates.** Every pro workflow puts the author at approval points, with the AI as a partner, not an automatic novelist. *We have this:* Patrick approves each chapter, and outside reads are advisory.

## The pipeline per chapter (v2)
1. **Prep:**
   - The writer reads `story_state`, the summaries, voice notes, the ledgers, style anchors and the slop list.
   - `character-sim` runs for the chapter's key scenes.
2. **Draft:** `story-writer`, at full size, scene by scene.
3. **Check, in parallel:**
   - `sense-checker` (does it make sense);
   - `payoff-keeper` (seeds and rules, with the seed cap);
   - `continuity-keeper` (state diff, 5-category taxonomy, evidence pairs);
   - `forecaster` (tension).
4. **Fix:** the writer fixes what the checks flag, and Claude as author decides which flags to take.
5. **Polish:**
   - `dialogue-editor`;
   - then `word-watch` (after `wordcheck.py` and the slop list);
   - then the `line-editor` natural pass;
   - then `story-guard`.
6. **Read:**
   - `reader-panel` runs 5 personas on a STORY_ONLY copy.
   - Patrick and Grok read too.
7. **Approve:** Patrick approves. Then `continuity-keeper` updates the state files, and the chapter goes into the ledgers.

## Sources
- Agents' Room, arXiv 2410.02603: https://arxiv.org/pdf/2410.02603
- MAGNET (character-grounded multi-agent stories) and Atlas, arXiv 2607.00918: https://arxiv.org/abs/2607.00918
- ConWriter, arXiv 2608.05169: https://arxiv.org/pdf/2608.05169
- CreAgentive, arXiv 2509.26461: https://arxiv.org/pdf/2509.26461
- Lost in Stories / ConStory-Bench, arXiv 2603.05890: https://arxiv.org/html/2603.05890v1
- Dynamic hierarchical outlining with memory (temporal KG), arXiv 2412.13575: https://arxiv.org/pdf/2412.13575
- Finding Flawed Fictions (plot-hole detection), arXiv 2504.11900: https://arxiv.org/pdf/2504.11900v3
- Spoiler Alert (narrative forecasting as tension), arXiv 2604.09854: https://arxiv.org/pdf/2604.09854
- StoryScope (idiosyncrasies in AI fiction), arXiv 2604.03136: https://arxiv.org/pdf/2604.03136
- Antislop, ICLR 2026 / arXiv 2510.15061: https://arxiv.org/abs/2510.15061 ; sampler: https://github.com/sam-paech/antislop-sampler
- Synthetic Reader Panels, arXiv 2602.14433: https://arxiv.org/abs/2602.14433 ; Readers sim: https://github.com/Eeman1113/Readers
- Book-Agent pipeline (community): https://forum.level1techs.com/t/my-ai-powered-novel-writing-pipeline-book-agent-generating-epistemically-controlled-long-form-fiction/243193
- Tool comparisons (secondary): https://revise.io/blog/best-ai-for-novel-writing ; https://blog.chapter.pub/sudowrite-vs-novelcrafter/ ; https://www.timtis.com/blog/the-best-ai-tools-for-writing-a-book-and-where-they-cant-help/
