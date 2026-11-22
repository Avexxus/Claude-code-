# Commercial and Open AI Fiction Pipelines: Architecture Notes

Research date: 2026-11-22. Sources are dated where the page shows a date. Vendor claims are marked as such. "Documented" means the source describes it; "asserted" means the source claims a result without evidence shown.

Coverage limits up front: GitHub API access was not available in this session, so repo star counts, licenses and commit dates come from web-rendered pages and are approximate. "Book-Agent" did not match any named system in search; the closest work is listed under the epistemic-control question. Sudowrite and NovelCrafter docs were read at snippet or summary level, not in full.

---

## Key Question 1: How does NousResearch/autonovel work end to end?

### Takeaway
autonovel is a staged, script-driven pipeline (foundation, draft, automated revision, Opus review, export) built on a set of markdown prompt files and Python judges. Its README reports outputs (a 19-chapter, ~79k-word novel plus art and audio) but reports no before-and-after quality metrics, so its quality claim rests on the process, not on measured results.

### Cited Findings
- Five phases: foundation (world, characters, outline, voice, canon from a seed; "Loop until `foundation_score > 7.5`"), first draft (write and evaluate each chapter; "Keep if `score > 6.0`, retry if not"), automated revision (adversarial edits, reader panel, revision briefs, rewrites; "Plateau detection stops the loop"), Opus review loop (full manuscript, dual-persona review, repeated rounds), export (LaTeX, art, ePub, audiobook scripts). README, fetched 2026-11-22 — [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- Five co-evolving layers (voice, world, characters, outline, chapters) with canon as a cross-cutting layer; changes propagate up and down, and propagation debts are tracked in `state.json`. Same README — [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- Prompt and instruction files: `program.md` (per-phase agent instructions), `CRAFT.md`, `ANTI-SLOP.md` (word-level AI tells), `ANTI-PATTERNS.md` (structural AI patterns), `PIPELINE.md`, `WORKFLOW.md`, and templates `voice.md`, `world.md`, `characters.md`, `outline.md`, `canon.md`, `MYSTERY.md` — [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- Checks: `evaluate.py` (mechanical scorer for banned words, clichés, show-don't-tell, sentence uniformity, plus a separate LLM judge); `adversarial_edit.py` ("Cut 500 words" analysis); `compare_chapters.py` (head-to-head Elo tournament); `reader_panel.py` (four-persona novel-level evaluation); `review.py` (Opus dual-persona review with stopping conditions) — [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- Reported results: first novel *The Second Son of the House of Bells*, "19 chapters, 79,456 words"; drafting went "24 → 19 chapters through 4 merges"; "6 automated cycles and 6 Opus review rounds, with all major items resolved"; art (linocut cover, 19 woodcut ornaments) and 4,179 speaker-attributed audiobook segments — [NousResearch/autonovel](https://github.com/NousResearch/autonovel)
- Repo metadata (web page): ~1.7k stars, 333 forks, 3 commits on master, most recent commit dated Mar 20, 2026 (commit history page, fetched 2026-11-22) — [commits](https://github.com/NousResearch/autonovel/commits/master). License not visible in captured content.

### Inferences
- The thresholds (7.5, 6.0) are design parameters. The README does not show whether they were tuned or whether scores correlate with reader judgment.
- The novel's own numbers are self-reported. Only 3 commits on master for a repo with ~1.7k stars suggests history was squashed or imported; this makes it hard to audit how the pipeline evolved.
- The mechanical scorer (banned words, uniformity) plus an LLM judge is a two-layer check. The README does not say how often the two disagree.

### Gaps
- No per-chapter score distributions, judge-vs-human agreement, or before/after revision metrics in the README. (Not found.)
- Prompt file contents were not read directly; descriptions above come from the README. Next step if needed: read `program.md` and `evaluate.py` raw.
- License and exact last-commit date for the repo page were not confirmed beyond the commit-history snippet.

---

## Key Question 2: How do Inkfluence, Sudowrite, NovelCrafter store and retrieve story knowledge?

### Takeaway
All three converge on a small set of always-on reference facts plus a rolling or retrieved window of prose. Inkfluence is the most explicit about memory layers (bible, verbatim last-3, generated running record, held-back future events). NovelCrafter uses a manually curated codex with per-entry AI-context rules. Sudowrite's Story Bible is a field-based source of truth with stated dependency rules. None publishes evaluation data of its own memory design.

### Inkfluence (vendor help page, updated Nov 2026)
- **Story bible** (always sent before each chapter, "does not age out"): story goal, audience, POV, character names and spellings, key objects, "non-negotiable" rules, open threads, timeline anchors, plus summaries of the latest three chapters. Set from the idea and story setup; editable — [How Inkfluence AI keeps a long book consistent](https://www.inkfluenceai.com/learn/how-inkfluence-ai-keeps-a-book-consistent)
- **Verbatim context**: full text of the three preceding chapters plus the last two paragraphs of the previous chapter; for very long chapters, the later part — same page.
- **Running record**: written after each chapter by reading it back; five entry types tagged with source chapter (who knows what; each person's latest location and state; key objects and condition; events already shown; story clock). Only the latest position per person is kept. Not hand-editable — same page.
- **Planned future events**: next three chapters' planned events held back as context so the current chapter sets them up without paying them off. A plan-check rewrites lines the book has already fulfilled; a rewrite that changes too much is discarded — same page.
- **Series carry-over**: "Continue as a series" carries bible (with edits), running record marked as earlier, prior ending, a plan built from the prior book, language and chapter count — same page.
- **Stated limits** (vendor's own list): hand edits do not update the record; record keeps facts not prose; "the oldest entries give way on long books" with no size stated; bible edits apply only to later chapters; finished chapters are not rewritten, so errors persist until regenerated; imported manuscripts have no bible or record; "not perfect memory."
- A search snippet described the bible as 5,000–12,000 words for a full arc, built incrementally. This is a secondary/search-summary claim; not confirmed on the primary page. — [For Series Authors](https://www.inkfluenceai.com/for/series-authors)
- Asserted, not evidenced: 23,565 novels (self-reported); "repeated reveals falling from 2 in 9 to 0 in 9" (one novel, nine regenerations, internal); "1-in-175 baseline" and "1,509 of 2,406" flags (internal sampling; accuracy of the generated record itself not measured). Page itself flags that one test cannot yield a rate. Its cited research (Liu et al., Hsieh et al., Kim et al.) concerns long-context models generally, not this product.

### NovelCrafter (vendor help docs)
- **Codex**: author-curated entries (characters, locations, objects, etc.) attached to a book. Series Codex is "the same as the standard codex, with the additional bonus of the entries being shared over every book in the series" (help page last updated Jan 31, 2025) — [Series Codex](https://novelcrafter.com/help/docs/codex/series-codex)
- Entries can be moved between book and series codex; separate tabs for all, series-only, and book-only entries — same page.
- **AI Context setting** per entry: "Always" (sent regardless of mention), "Only when detected" (sent when name or alias appears in the project), or "Never." Detection is case-insensitive by default, with optional case-sensitive matching and an exclusion list; acronyms are kept separate from common nouns. Tags are not visible to the AI; information must be in a codex field or details section. "Research content is also excluded from prose generation." Last updated Aug 15, 2026 — [Anatomy of a codex entry](https://www.novelcrafter.com/help/docs/codex/anatomy-codex-entry)
- Gives no token counts or budgets; only advice to be "fairly descriptive, while being concise to not overload the AI." (Documented.)
- Progressions (documenting how characters change over time) are described in a Jenova comparison as citing NovelCrafter's docs; not confirmed in the official pages read. Treat as unverified. — [Jenova comparison](https://www.jenova.ai/en/resources/which-ai-novel-writing-assistant-remembers-character-arcs-timelines-and-worldbuilding-best) (competitor content).

### Sudowrite (vendor docs and blog)
- **Story Bible**: per-project reference hub that the AI reads; fields shown beneath prose; "source of truth that both you and the AI can refer back to." Sections: Braindump, Synopsis, Genre and Style, Characters, Worldbuilding, Outline, Scenes. — [What is Story Bible](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/what-is-story-bible/jmWepHcQdJetNrE991fjJC), last updated Jan 13, 2026
- Dependency rules (documented on the same page): Braindump feeds Synopsis (fallback if empty); Genre feeds Synopsis, Outline, Scenes, Draft; Style feeds Beat and Draft; Synopsis feeds Characters, Worldbuilding, Outline, Scenes; Characters and Worldbuilding feed Outline, Scenes, Draft; Scenes feed Draft. Key constraint quoted: "Scene and Prose Generation (in Draft) will only look at explicitly mentioned Characters and Worldbuilding elements." This means an unnamed character is invisible to prose generation.
- Character data can be imported from existing text ("smart import"); worldbuilding stored on cards.
- Context: a vendor-affiliated blog says Write reads up to 20,000 words of context plus all Story Bible data. Not confirmed on primary docs.
- Conflict: a blog says Story Bible holds 2,000 characters per bible; the May 21, 2024 changelog ("Worldbuilding, Unlimited Characters") says unlimited. The changelog is the more recent primary source; current limit not verified.
- The official Draft or Write pages do not state a character or word limit (checked on the Story Bible page).

### Cross-tool comparison (retrieval mechanism)
| Tool | Always-on facts | Recent prose | Future/plan | Retrieval of older text |
|---|---|---|---|---|
| Inkfluence | Story bible | Last 3 chapters verbatim + last 2 paragraphs | Next 3 chapters' plans, checked against record | Running record (generated), not retrieval |
| NovelCrafter | Codex entries with "Always" | Scene context (not detailed in sources read) | Not described | Codex entries detected by name in text |
| Sudowrite | Story Bible fields | Scenes/outline fields feed Draft | Outline and Scenes | Not described on sources read |

### Inferences
- Four of five retrieval designs in the sources are **explicit, human-checkable state** (bible, codex, fields, running record) rather than embedding search. Inkfluence's running record is closest to a structured, per-entity state store.
- NovelCrafter's "only when detected" mode is name-matching retrieval, which will miss characters referred to only by pronoun or role. The docs do not address this.

### Gaps
- No primary document for Inkfluence's record format beyond the help page; no test data.
- NovelCrafter per-scene context budget and how Progressions are sent to the model: not found.
- Sudowrite Write/Beat context limit: unconfirmed.

---

## Key Question 3: What does the "Book-Agent" community pipeline do (epistemic control, character knowledge)?

### Takeaway
No pipeline named "Book-Agent" surfaced. The closest and most relevant work is the June 2026 arXiv paper "Staying In Character" (ReverieMem), which formalizes what a character may know and reports a large gain on a knowledge-boundary benchmark. The benchmark and metric are the authors' own, so the number is a strong paper claim, not an independent result.

### Cited Findings
- ReverieMem (arXiv 2606.25632v2, stamp 09 Nov 2026; authors Tang, Zhang, Yang, Tang, Li, Lai, Yang). Three layers: episodic (first-person scene summaries), semantic (five-element SPOCV tuples: subject, predicate, object, cause, visibility set, so retrieval only returns facts the character can see), personality (behavioral patterns and emotion-transition records). — [arXiv 2606.25632](https://arxiv.org/html/2606.25632)
- Benchmark KBF-QA: 4,386 multiple-choice questions over eight novels (2,442 recall, 1,944 refusal). Metric KBF is the harmonic mean of recall and refusal accuracy. — same
- Reported KBF (%): ReverieMem 73.3; BookWorld 38.7; ComoRAG 37.7; Direct prompting 37.2; HippoRAG 20.9; Naive RAG 18.9; RAPTOR 16.8. — same
- The "34.6 percentage points" claim is against BookWorld (73.3 − 38.7 = 34.6); the abstract does not name the baseline. Pairwise judging: 78.86% mean win rate vs BookWorld across five generator LLMs, two modes, five dimensions. — same
- Authors' stated limits: KBF-QA covers plausible knowledge, not multi-witness contradictions, information-asymmetric mysteries, or unreliable narrators (future work); no modelling of one character's model of another's knowledge; benchmark items validated by the authors, no independent re-annotation or inter-annotator agreement. — same
- ICLR 2026 MemAgents workshop poster, "Epistemic Memory Failures in Long-Form Narrative Agents" (Xiwei Chen, sole author): 90-chapter, 180k+ token deployment; failure mode "known-information forgetting" (characters re-ask or rediscover facts); root cause naive recency-based injection excluding mid-chapter key facts; fix Key Facts Injection with "already knows" markers; stated result: 73% reduction in known-information forgetting. Model not named; abstract only. — [ICLR virtual page](https://iclr.cc/virtual/2026/10021229)
- BookWorld (ACL 2025, Fudan): builds role agents from novels plus a world agent; aimed at creative simulation, not strict knowledge control. — [arXiv 2504.14538](https://arxiv.org/html/2504.14538v1)
- InkOS (Narcooo/inkos, GitHub; README fetched 2026-11-22): 11.4k stars, AGPL-3.0; "Story Creation AI Agent"; README treats structured state (current state, hooks, chapter summaries, Zod-validated) as authoritative, with `story/memory.db` (SQLite FTS5/BM25) explicitly "not the authority for story facts." A continuity auditor checks each draft against the state, with the example of a character knowing something they never witnessed. Each chapter gets a state snapshot; prose, index and state are committed as an atomic file set. Read from the Chinese README; English README not checked. Commit date not shown. — [Narcooo/inkos](https://github.com/Narcooo/inkos)

### Inferences
- Two independent groups (the ICLR poster and ReverieMem) identify the same problem: recency or similarity retrieval misses facts that matter to a character's knowledge. This is a real signal, though both are single-group work.
- InkOS's split (structured state is authority; search index is a projection) is the same pattern as Inkfluence's record and the SPOCV visibility set: the knowledge should be a **typed store with visibility**, not text chunks.

### Gaps
- No "Book-Agent" system found under that name. If Patrick means a specific repo or post, the name or link is needed.
- ReverieMem's comparison to Inkfluence-style structured state was not tested; none of the baselines is that design.
- The 73% and 34.6-point numbers are not independently reproduced.

---

## Key Question 4: How do these tools handle context budgets, long-run consistency, and cost?

### Takeaway
Sources give very little on budgets or cost. The concrete numbers are: Inkfluence sends 3 full chapters plus bible and record; Sudowrite's Write reads up to 20k words (secondary source); autonovel uses LLM judge loops with plateau stops. Cost is handled by stopping rules (plateau detection, caps), not by published token budgets.

### Cited Findings
- Inkfluence chapter caps: 40 on paid plans, 5 on free (page updated Nov 2026) — [Inkfluence](https://www.inkfluenceai.com/learn/how-inkfluence-ai-keeps-a-book-consistent)
- autonovel: "Plateau detection stops the loop when scores stabilize"; review rounds capped by stopping conditions in `review.py` (description only) — [autonovel](https://github.com/NousResearch/autonovel)
- NovelCrafter: no token counts; advises conciseness to avoid overloading the AI — [Anatomy of a codex entry](https://www.novelcrafter.com/help/docs/codex/anatomy-codex-entry)
- Epistemic deployment: 90 chapters, 180k+ tokens over 3 months; a naive full-context approach is not the solution the author proposes; recency injection is the named failure — [ICLR page](https://iclr.cc/virtual/2026/10021229)

### Inferences
- Consistency cost is paid by re-reading state, not by re-reading all prose. Inkfluence and InkOS both keep a compact typed state and send verbatim text only for voice and the immediate scene. This keeps per-chapter context roughly constant as the book grows.
- Cost control via judge loops is real but unmeasured in these sources; autonovel's loops multiply LLM calls per chapter, and no cost figure is given.

### Gaps
- No published per-chapter token cost for any tool.
- How the running record is trimmed on long books (Inkfluence "oldest entries give way") is not specified.

---

## Key Question 5: Which ideas are used by several independent tools (strong signal) versus only one?

### Takeaway
Strong signal (three or more independent sources): a **separate, typed state store** (bible/codex/state) that is always sent, with recent text sent verbatim in small amounts, and an automated consistency check against that state. Weaker (one or two): visibility-scoped character knowledge, per-entry AI-context rules, held-back future plans, LLM-judge revision loops with plateau stops.

### Cited Findings and Classification
- **Typed always-on state store**: Inkfluence (bible + record), NovelCrafter (codex, "Always" setting), Sudowrite (Story Bible), InkOS (structured state authoritative), autonovel (`canon.md`, `state.json`, `world.md`, `characters.md`). **Strong: five sources.**
- **Verbatim recent text plus compact state**: Inkfluence (last 3 chapters), InkOS (chapter summaries in state; prose kept), Sudowrite (Draft reads Scenes/Characters). **Strong: three.**
- **Automated continuity check against state**: InkOS (continuity auditor), autonovel (`evaluate.py`, judge, reader panel), Inkfluence (plan-check against record). **Strong-moderate: three.**
- **Visibility-scoped character knowledge** (who knows what): Inkfluence (running record "who knows what"), ReverieMem (SPOCV visibility set), ICLR poster (already-knows markers), InkOS (example of a character knowing an unwitnessed thing). **Moderate: four, but two are the same research line.**
- **Held-back future plans**: Inkfluence only (in the sources read). **Single.**
- **Per-entry AI-context switch (always / when detected / never)**: NovelCrafter only. **Single.**
- **LLM-judge revision with plateau stop**: autonovel only among the primary sources read; Agents' Room and StoryWriter not checked. **Single.**
- **Elo or head-to-head chapter comparison**: autonovel only. **Single.**

### Inferences
- The most-used idea is the one least likely to be novel for us: a typed, human-editable bible read on every call. Any saga-engine design already has this shape.
- The visibility idea is the strongest unique lead for a series with secrets, because two separate efforts converge on it and the fix is concrete (store a visibility set with each fact).

### Gaps
- Independence: Inkfluence and NovelCrafter may both draw on common LLM-app patterns; "independent" here means separate codebases or vendors, not separate invention.

---

## Open-source multi-agent novel and story repos

Access note: GitHub API calls were refused for these repos in this session (not enabled). Metadata below is from rendered GitHub pages or secondary listings, as dated.

| Repo | Stars (page) | License | Last commit (page) | Architecture (README) |
|---|---|---|---|---|
| [NousResearch/autonovel](https://github.com/NousResearch/autonovel) | ~1.7k | not visible | Mar 20, 2026 (3 commits on master) | Staged pipeline with judges (see Q1) |
| [Narcooo/inkos](https://github.com/Narcooo/inkos) | 11.4k | AGPL-3.0 | not shown | Structured state authoritative, auditor, atomic commits (Chinese README read) |
| [google-deepmind/tell_me_a_story](https://github.com/google-deepmind/tell_me_a_story) | 53 | Sidebar: Apache-2.0; README: CC-BY-4.0 for dataset (conflict) | not shown (3 commits) | This is the **dataset** repo for Agents' Room; README does not describe the agent roles |
| [THU-KEG/StoryWriter](https://github.com/THU-KEG/StoryWriter) | not checked | not checked | not checked | Three-agent outline/plan/write pipeline per arXiv 2506.16445 (secondary listing) |
| [Austinggg/CreAgentive](https://github.com/Austinggg/CreAgentive) | not checked | not checked | not checked | Three-stage workflow, knowledge graph for story state, per arXiv 2509.26461 (secondary) |
| [abhishekmishragithub/novelai](https://github.com/abhishekmishragithub/novelai) | not checked | not checked | not checked | Four-agent fantasy system with RAG, per listing (secondary; low confidence) |

Agents' Room (arXiv 2410.02603) is the research reference for planning and writing agents with an orchestrator; the GitHub repo is the dataset only, so the implementation is not publicly confirmed from the repo. Stars and commit dates for StoryWriter, CreAgentive and novelai were not checked; treat them as unverified leads until checked on GitHub.

---

## Per-pipeline: what it does, stated results, copy, avoid

### autonovel (open source, NousResearch)
- **Does:** staged generation with judge loops, revision, Opus review, export.
- **Stated results:** 19-chapter, ~79k-word novel; 6 revision cycles and 6 review rounds. No quality metrics.
- **Copy:** explicit per-phase prompt files; mechanical "AI tell" scorer alongside an LLM judge; plateau-based stopping; reader-panel persona review.
- **Avoid:** thresholds without calibration; scores presented as quality evidence; a single-author self-report as a benchmark.

### Inkfluence (commercial)
- **Does:** story bible, verbatim last-3 chapters, generated running record with who-knows-what, held-back future plans, series carry-over.
- **Stated results:** vendor counts and internal test rates only (see Q2 for caveats).
- **Copy:** the layered memory (bible / verbatim / generated record / held-back plans); the explicit "hand edits don't reach the record" limit; the stated list of what it can't do.
- **Avoid:** relying on the generated record without a human check; their internal "1-in-175" figures as a rate.

### NovelCrafter (commercial)
- **Does:** author-curated codex (series and book scope) with per-entry AI-context rules.
- **Stated results:** none on quality in sources read.
- **Copy:** the three-state AI-context switch (always / when detected / never); tags invisible to the model, so put facts in fields.
- **Avoid:** name-matching retrieval for characters referred to by role or pronoun.

### Sudowrite (commercial)
- **Does:** Story Bible with dependency-tracked fields feeding Outline, Scenes, Draft.
- **Stated results:** none on quality in sources read.
- **Copy:** explicit dependency map for which fields feed which step; import from existing text.
- **Avoid:** the documented rule that prose only sees "explicitly mentioned" characters and worldbuilding. An unnamed character can be missing from a scene.

### ReverieMem / "Staying In Character" (research, June 2026)
- **Does:** per-character episodic, visibility-scoped semantic (SPOCV) and personality memory for role-play agents over novels.
- **Stated results:** KBF 73.3 vs 38.7 (BookWorld); 78.86% pairwise win rate vs BookWorld. Authors' benchmark.
- **Copy:** visibility set on every fact; refusal items in the benchmark (the agent should decline what it cannot know).
- **Avoid:** treating the margin as settled before independent re-annotation, which the authors say is still pending.

### Epistemic memory poster (ICLR 2026 workshop)
- **Does:** Key Facts Injection with "already knows" markers.
- **Stated results:** 73% reduction in known-information forgetting (one deployment, one author).
- **Copy:** explicit "already knows" marker in context, so the model does not re-discover facts.
- **Avoid:** taking the 73% figure as general.

### InkOS (open source, AGPL-3.0)
- **Does:** structured state as authority; continuity auditor; atomic commits of prose and state.
- **Stated results:** none on quality in README read; star count only.
- **Copy:** the rule that a search index is a projection, not the source of facts; the auditor checking drafts against state; atomic commit of state with prose.
- **Avoid:** AGPL-3.0 if we ever want to embed code; read the English README before relying on it.

---

## Overall gaps for the report writer
- No "Book-Agent" found by that name. Ask Patrick for the link if this refers to a specific project.
- No independent evaluation of any commercial tool's consistency. All quality claims are vendor-internal.
- GitHub metadata for several repos is unverified (API access refused for this session).
- Sudowrite Write/Beat context limit and the 2,000 vs unlimited character conflict are unresolved; the 2024 changelog is the better primary source.
- No per-chapter cost data for any tool.
