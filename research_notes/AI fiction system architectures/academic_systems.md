# Academic systems and benchmarks for long-form narrative generation

Scope: multi-agent and staged LLM pipelines for long fiction (novels, novellas, serialized fiction), plus the benchmarks and reader/judge methods used to evaluate them. Compiled 2026-11-22 from arXiv abstract pages and HTML full text.

## Method and reliability notes

- **Sourcing.** arXiv abstract pages were read directly. HTML full texts were read through a summarizing fetch tool, so every number below comes from that extraction and should be checked against the PDF or HTML before it goes into the codex or any report. Where the extraction was internally inconsistent, that is noted.
- **Truncation.** Several HTML papers were longer than the tool's read window. Appendices and late sections were not read for: Agents' Room (read to ~100k of 170k chars), ConWriter (appendices partly read), ConStory-Bench, DOME, FlawedFictions, Spoiler Alert, StoryScope, Fair-play detective, Suspense. Appendix-only results may be missing.
- **Proven vs promising.** The brief asks for "proven" = replicated or strong ablations. No finding here has been replicated by an independent group. Applying the rule strictly, nothing reaches "proven". The labels below therefore mean:
  - **Proven (benchmark-level):** a measurement finding reported across several models or datasets within one paper, with stated statistics. Still single-paper, so treat as strong but unreplicated.
  - **Promising:** a system result, or a single-paper ablation, with no replication.
- **Not checked:** the "Atlas" half of arXiv 2607.00918 (see Section 1), and any post-2026-09 work beyond the search hits in Section 9.

Source dates below are arXiv v1 submission dates unless stated.

---

## 1. Systems that generate long stories (multi-agent or staged)

### 1.1 Agents' Room (Huot et al., arXiv 2410.02603; ICLR 2025)
- **Date:** v1 2024-10-03; v2 2025-03-14. Verified as the ICLR 2025 paper. Source: [arXiv abs](https://arxiv.org/abs/2410.02603), [HTML v2](https://arxiv.org/html/2410.02603v2).
- **What it does.** Decomposes narrative writing into subtasks. Four planning agents (conflict, character, setting, plot) run first, then five writing agents (exposition, rising action, climax, falling action, resolution), then an optional finalizer. A deterministic, centralized orchestrator calls them in order: conflict → character → setting → plot, then the writers.
- **State.** One shared scratchpad, initialized with the prompt. Each call appends its label and output. Agents read it to avoid redundancy. No critic, no editor, no revision loop.
- **Reported numbers** (Table 2, "Tell Me a Story" test set, 55 items):
  - Average words: humans 1,439; E2EZS 1,207; ARZS write 3,278; ARFT plan+write 3,006; ARFT plan 856.
  - Rouge-L: E2EZS 20.71 (highest); ARFT plan+write 17.60.
  - Unique-word %: humans 15.53; ARFT write 46.39.
  - Intra-story trigram repetition: humans 0.0020; ARFT plan+write 0.0019.
  - Human pairwise: 9,900 ratings, Bradley-Terry. Fleiss κ = 0.46 (N=150, k=3). Human stories are preferred overall; longer-story preference rate ~0.51.
  - LLM judge (Gemini 1.5 Pro): Spearman ρ = 0.62 by system (N=45), ρ = 0.41 by item (N=9,900). Highest agreement on Development (ρ=0.83) and Creativity (ρ=0.85). Self-consistency 90.2%.
- **Ablations.** No formal table. Variants compared: plan, write, plan+write, each zero-shot or fine-tuned. Fine-tuned beats zero-shot. Plan-only is weak (the authors blame the simple finalizer). Write-containing variants are longer.
- **Limits stated.** Small dataset (123/52/55 train/val/test). Outputs run shorter than requested, and asking for more tokens did not help. Fixed orchestrator. One backbone (Gemini 1.5 Flash). BertScore does not discriminate between systems.
- **Label:** Promising (single paper; human-judged; not long-form in the sense of chapters).
- **Copy:** role decomposition by narrative function; a shared scratchpad as a simple state store; pairwise human eval with Bradley-Terry.
- **Avoid:** treating "more words" as quality (its own length numbers show this); relying on BertScore or Rouge for story quality; a no-critic pipeline if consistency matters, since the paper has no consistency check at all.

### 1.2 MAGNET: "From Personas to Plot" (Ho, Aluru et al., arXiv 2607.00918)
- **Date:** v1 2026-07-01; v2 2026-10-03. Source: [arXiv abs](https://arxiv.org/abs/2607.00918), [HTML v2](https://arxiv.org/html/2607.00918v2).
- **Title discrepancy.** The brief lists this paper as "MAGNET and Atlas." The arXiv title is "From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives". MAGNET is the system. **"Atlas" does not appear in the HTML text I read.** A search snippet describes ATLAS as a graph-based hallucination checker used for evaluation. That claim is unverified and conflicts with the full text. Check the PDF before relying on either.
- **What it does.** Goal-driven narrative engine.
  - Character agents (Gemma-4-31B-it) receive persona, goal, recent history, and world variables, and propose an action.
  - Critic (Gemini 2.5 Flash) checks each action for relevance, specificity, and consistency. It returns revision feedback, or it accepts and emits world-state updates and a `goal_reached` flag.
  - Narrator (Opus 4.7) selects actions and writes the paragraph.
  - Goal generator (Opus 4.7) produces follow-up goals and transitions. A goal is replaced when it has stalled for 15 steps. A domain-shift goal fires when t mod 40 = 0.
  - Evaluators: GPT-5.4 mini and Claude Haiku 4.5, as editors and rubric scorers.
- **State.** Directed graph (world root, character nodes, state-variable nodes). Flattened to a dict for agents. Overwrite-style updates, committed only for selected actions after narration.
- **Critic loop.** Algorithm 1: regenerate each character action until `revise=False` or MAX_REVISIONS.
- **Reported numbers.**
  - Editor annotations, lower is better (Table 1): 20 pages: single model 208.0, StoryBox 104.9, StoryWriter 120.3, **MAGNET 84.0**. 100 pages: 200.7, 105.4, 106.4, **86.4**. Paired t-test p-values vs MAGNET: 0.0002 to 0.0382.
  - Rubric, higher is better (Table 2): 20 pages: 76.8, 76.0, 78.2, **82.6**. 100 pages: 71.0, 78.7, 74.1, **79.6**. MAGNET is highest in both columns. The margin over StoryBox at 100 pages is small (0.9 points). Reported p-values 0.0003 to 0.0424.
  - Annotator agreement with evaluators: GPT-5.4 mini 82.5% and Haiku 4.5 85.0% on annotations.
- **Ablations** (20 pages, Table 5). Annotations / rubric:
  - No critic: 109.0 / 78.1
  - No goal shift: 119.5 / 78.4
  - No structured state: 116.9 / 76.4
  - Full: 84.0 / 82.6
  - The rubric p-value mapping for the three ablations is inferred (the extraction lists three values in order). Verify.
- **Label:** Promising. Single paper, with component ablations and paired tests. The evaluators are LLM editors, and the paper's own agreement check is about 85%.
- **Copy:** persona-grounded actors plus a critic that gates actions; world state as a graph of variables with explicit commit-after-selection; goal stalling and forced domain shifts to prevent plateaus; ablation design that removes one component at a time.
- **Avoid:** the baselines are weak (single-model prompting, StoryBox, StoryWriter), so the margin over them is not the margin over strong modern pipelines. The evaluators are LLM judges from the same model families. Length scales are 20 and 100 pages, not novel-length.

### 1.3 ConWriter (arXiv 2608.05169; Findings of EMNLP 2026)
- **Date:** v1 2026-05-27; v2 2026-09-04. Source: [arXiv abs](https://arxiv.org/abs/2608.05169), [HTML v2](https://arxiv.org/html/2608.05169v2).
- **What it does.** Training-free, scene-level generation. Each scene passes through: transition check → draft → verification → accept or repair. Only accepted scenes update memory.
- **State.**
  - Static memory M^s: premises, world rules, character attributes, style constraints.
  - Dynamic memory M^d_t: events, entity states and relations, temporal information, unresolved future constraints.
  - Transition operator o_t = (Pre, Post, Forbid). A scene is feasible only if its preconditions hold.
  - Commit only when the blocking violation count is zero. Merge with conflict-aware merging.
- **Verification.** V_t = V_Pre + V_Post + V_Forbid + V_Facet (timeline, characterization, basic facts, commonsense, style). Accept only if V_t = 0.
- **Risk monitoring.** Token log-probs when available. Otherwise a proxy based on lexical dispersion and punctuation density. Risk sets a verification budget. Per the paper, high risk alone does not trigger repair. α, β, γ are not given in the extraction.
- **Repair.** Sentence-level, with a repair spec (violated constraints, evidence, content to keep, forbidden changes), under a retry budget. If repair fails, the scene is rejected and memory is unchanged.
- **Reported numbers** (Table 1, CED = consistency errors per 10k words, lower is better; averages over four ConStory-Bench tasks; 20 cases in total):
  - Qwen3.5-Plus, 3K: direct 0.1657, DOME 0.8546, **ConWriter 0.0352**. At 6K: 0.4109 / 0.4709 / **0.0728**. At 12K: 0.3303 / 0.3272 / **0.1629**.
  - DeepSeek-V4-Flash, 3K: 1.0662 / 0.6971 / **0.1335**. 6K: 0.6421 / 0.3572 / **0.2968**. 12K: 0.6602 / 0.7386 / **0.3261**.
  - GPT-5.4-nano, 3K: 0.0000 / 0.1291 / **0.0000**. 6K: 0.2525 / 0.1522 / **0.0546**. 12K: 0.0793 / 0.0419 / **0.0324**.
  - ConWriter has lower CED than DOME in all nine base-model/length cells. Reductions vs direct range 50.6% to 87.5%, with a ceiling at 3K for GPT-5.4-nano.
  - Cost (Table 4, Task 1 per story): ConWriter uses 53 to 80 API calls, vs 10 to 27 for direct. Tokens rise several-fold, for example 1.16M vs 376K for Qwen3.5-Plus.
- **Ablation** (Table 2, 3K, DeepSeek-V4-Flash, CED): full 0.1335; w/o dynamic memory 0.7499; w/o structured validation 0.6843; w/o uncertainty monitoring 0.5463. Word count rises to 6,737 to 7,724 without validation.
- **Limits stated.** 20-case subset (first five per task). Overhead is "a natural trade-off". Needs capable base models; some are "less repair-compliant", and repeated feedback can fight length control.
- **Label:** Promising. Single paper, but with ablations and a multi-model grid.
- **Copy:** explicit transition constraints as data, not prose; commit-on-zero-violations memory; tiered verification; sentence-level repair with a retry budget; the memory-update-only-on-accept rule.
- **Avoid:** CED counts errors by an LLM checker, so the metric and the method share a judge family. The evaluation uses 20 cases. Cost is 2 to 5 times the direct baseline in calls and several times in tokens. At 12K with Qwen3.5-Plus, DOME (0.3272) and direct (0.3303) are nearly tied.

### 1.4 DOME: Dynamic Hierarchical Outlining with Memory-Enhancement (Wang et al., arXiv 2412.13575)
- **Date:** v1 2024-12-18. Source: [arXiv abs](https://arxiv.org/abs/2412.13575), [HTML v1](https://arxiv.org/html/2412.13575v1).
- **What it does.** Interleaves outline planning with writing.
  - Rough outline: five stages, generated once.
  - Each stage is expanded into M=3 detailed outlines, alternating with writing.
  - Memory-Enhancement Module (MEM): a temporal knowledge graph. An LLM extracts a `<subject, action, object, chapter>` quadruple from each sentence. Retrieval is by entity, then LLM relevance scoring on a 1 to 5 rubric, with a cosine filter of 0.75 (bge-large-en-v1.5).
  - Temporal Conflict Analyzer: groups quadruples by five rules, asks the LLM to describe each group, then asks for a conflict judgment. Conflict rate CR = m/N.
- **Reported numbers** (Table 1, 20 DOC premises, Qwen1.5-72B generator, human rankings by three graduate students; lower is better except Ent-2):
  - CR: Llama3-70B 6.78; Qwen1.5-72B 0.66; Re3 0.77; DOC 1.21; **DOME 0.56**.
  - Ent-2: 9.25 / 9.06 / 11.56 / 11.55 / **12.29**.
  - Words: DOME 7,114 vs 3,802 (Re3) and 496 (Qwen1.5 direct).
  - Human average ranks (plot completeness etc.): DOME 1.15 to 1.77 vs 2.4 to 4.9 for the others.
  - Table 2 gives different DOME human scores (1.20 to 1.32) than Table 1. The extraction flags this and the paper should be checked.
- **Ablation** (Table 2): w/o MEM: CR 4.52 (vs 0.56). w/o DHO: 1,472 words, Ent-2 11.50. The MEM ablation used a limit of two chat rounds, which the authors note as a compute reduction.
- **Cost.** About 200 API calls and about 4 hours for a 7,000-word story. Stated in the paper.
- **Limits stated.** 20 premises. Human evaluation is expensive. Hand-designed prompts. Heavy API use.
- **Label:** Promising. Single paper, 20 premises, a 2024 generator.
- **Copy:** temporal KG with chapter-indexed quadruples as memory; retrieval by entity plus LLM relevance filter; the conflict analyzer as a separate consistency check.
- **Avoid:** using ConWriter's results as a DOME ranking. ConWriter re-tested DOME with newer models and found it worse than direct generation in several cells (for example Qwen3.5-Plus at 3K, CED 0.85 vs 0.17). These are different setups. Note also that DOME's own results are on a 2024 generator with 20 premises.

### 1.5 CreAgentive (arXiv 2509.26461)
- **Date:** v1 2025-09-30 (only version). Source: [arXiv abs](https://arxiv.org/abs/2509.26461), [HTML v1](https://arxiv.org/html/2509.26461v1).
- **What it does.** Three stages: initialization (user skeleton), generation (short- and long-term goals drive multi-agent dialogue), writing (rendering from the prototype with retrospection and foreshadowing).
- **Story Prototype.** Genre-agnostic, two linked graphs.
  - Role Graph: characters with static attributes; relations with strength, direction, and chapter labels.
  - Plot Graph: events and scenes, with consequences and emotional impact per participant.
  - Chapter-level snapshots for versioning and flashbacks.
- **Agents.** Initialization agent; short-term goal agent (one distinct plot path per chapter); role agents auto-built from the prototype, in a relay ("PlotWeave") where each builds on the last, with "limited cognition" (each sees only its own character's information); scorer agent (general and story-specific rules; highest score is written back); exit agent (checks whether the long-term goal is met); recall and thread agents (pull past events and foreshadowing); writer agent.
- **Reported numbers** (Table 2, Sq composite score):
  - CreAgentive 8.28 (human) / 8.17 (auto).
  - Agents' Room 8.07 / 7.75.
  - Direct 7.50 / 7.84.
  - LongWriter-ChatGLM4-9B 7.76 / 6.65.
  - DOC v2 7.38 / 5.76.
  - Dramatron 7.36 / 6.61.
  - Human-authored Worm 8.71 / 8.37.
  - Ablation (Table E.1): full 8.48 (conflicts with 8.28 in Table 2; flagged); w/o multiple short-term goals 8.17; w/o PlotWeave 8.20; w/o Recall and Thread 7.93 (largest drop, Coherence 7.52, Empathy 6.67).
  - Cost (Table G.1): $0.015 to $0.15 per chapter. The abstract claims under $1 per 100 chapters.
- **Limits and issues.**
  - The abstract says 10 narrative indicators. The paper defines 9 (seven quality dimensions plus word and chapter count).
  - Judges: five "literature enthusiasts" as human raters, and DeepSeek-R1 as the automatic judge.
  - Most baselines use DeepSeek-V3. Worm is the only human reference.
  - No dedicated limitations section.
- **Label:** Promising. Single paper, weak evaluation design (few raters, one auto judge, inconsistent numbers). Ablations exist but small margins (8.48 vs 7.93).
- **Copy:** the prototype as a two-graph state (characters and plot), chapter-stamped relations, recall and thread agents that read both past and future state, the "limited cognition" rule for role agents.
- **Avoid:** the cost claim is a per-chapter figure from a few models; the "thousands of chapters" claim has no count. The prototype-as-prompt approach is not shown to beat plain retrieval over the same content.

### 1.6 Other systems found while checking (not read in full)
- **StoryWriter** (arXiv 2506.16445, June 2025): multi-agent with an outline agent that checks event consistency, plus the LongStory dataset. Not read.
- **SuperWriter-agent** (arXiv 2506.04180, 2025): planning, writing, and checker/refiner stages, evaluated on WritingBench. Not read.
- **WSE-bench** (arXiv 2608.15654): benchmark for storytelling across agent architectures in open-ended world simulation. Not read.
- **Shadow-Loom** (arXiv 2605.02475; see Section 3.4).

---

## 2. State tracking and knowledge stores (cross-system summary)

| System | State store | Update rule | Consistency use |
|---|---|---|---|
| Agents' Room | Text scratchpad | Append | None |
| MAGNET | Directed graph of variables | Overwrite, after narrator selects | Critic gates actions |
| ConWriter | Static + dynamic memory, transition ops | Commit only if zero blocking violations | Verify, then repair |
| DOME | Temporal KG of quadruples | Append per generated part | Conflict analyzer (LLM group-judge) |
| CreAgentive | Two graphs (role, plot), chapter snapshots | Consequences recorded per event | Scorer agent; recall/thread agents |
| Shadow-Loom | Versioned graphical world model | Validation with auto-repair | LLM audit for "miracle steps" |

Read-across: the systems that gate writes on a check (MAGNET, ConWriter) report the largest consistency gains. The text-only scratchpad (Agents' Room) has no consistency mechanism. This is an observation across papers, not a controlled comparison.

---

## 3. Evaluation and consistency checking

### 3.1 ConStory-Bench / "Lost in Stories" (Li et al., arXiv 2603.05890)
- **Date:** v1 2026-03-06. Source: [arXiv abs](https://arxiv.org/abs/2603.05890), [HTML v1](https://arxiv.org/html/2603.05890v1). Project: https://picrew.github.io/constory-bench.github.io/. Note: the brief calls this "ConStory-Bench"; the arXiv title is "Lost in Stories: Consistency Bugs in Long Story Generation by LLMs". Both names are used.
- **Benchmark.** 2,000 prompts, four scenarios: generation 751, continuation 432, expansion 422, completion 395. Target 8,000 to 10,000 words.
- **Error taxonomy** (5 categories, 19 subtypes):
  - Timeline & plot logic (6): absolute time, duration, simultaneity, causeless effects, causal logic violations, abandoned plot elements.
  - Characterization (4): memory, knowledge, skill fluctuations, forgotten abilities.
  - World-building (3): core rules, social norms, geography.
  - Factual & detail (3): appearance, nomenclature, quantitative.
  - Narrative & style (3): perspective, tone, style shifts.
- **Judge: ConStory-Checker.** o4-mini, four stages: category-guided extraction, contradiction pairing, evidence chains, JSON report.
  - Validation: 200 stories with 1,000 injected errors (Qwen3-235B-Thinking). Two professional web-novel writers annotated.
  - Checker: recall 0.550, precision 0.884, F1 0.678.
  - Human experts (table): recall 0.139, precision 0.660, F1 0.229. The text gives different numbers (recall 17.1%, F1 0.281). Flagged as an inconsistency.
  - No human inter-annotator agreement reported.
- **Metrics.** CED = errors / (words / 10,000). Group Relative Rank: within each prompt, rank models by Q = words / (1 + errors).
- **Per-model CED** (Table 3): GPT-5-Reasoning 0.113; Gemini-2.5-Pro 0.305; Claude-Sonnet-4.5 0.520; GLM-4.6 0.528; Qwen3-32B 0.537; LongWriter-Zero 0.669; SuperWriter 0.674; MiniMax-M1-80k 3.447. Text and table disagree on some GRR values (GPT-5 3.05 vs 2.80; Claude 4.9 vs 4.54).
- **Findings (proven-level, benchmark statistics, single paper).**
  - Factual & detail and timeline dominate.
  - Errors cluster at 40 to 60% of the narrative; fact errors at 15 to 30%.
  - Error-bearing text has higher token entropy (+19.2% Qwen3-4B; +12.0% Qwen3-30B).
  - Error count grows with length: r = 0.478 (Claude-Sonnet-4.5), r = 0.973 (DeepSeek-V3.2-Exp).
  - Generation tasks have the highest CED for most models.
- **Label:** Proven (benchmark-level statistics, multiple models). The judge is validated only against injected errors, so recall is low (0.55): the benchmark undercounts real errors.
- **Copy:** the five-category, 19-subtype taxonomy as the error vocabulary; CED per 10k words as the length-normalized metric; the position-of-error analysis for targeting checks.
- **Avoid:** using the o4-mini judge alone without a human check (recall 0.55, and humans disagree with each other). Ranking models on raw error counts without normalizing for length.

### 3.2 Finding Flawed Fictions (Ahuja, Sclar, Tsvetkov; arXiv 2504.11900)
- **Date:** v1 2025-04 (April 2025). Source: [HTML v1](https://arxiv.org/html/2504.11900v1).
- **Task.** Binary detection of plot holes (continuity errors), plus sentence-level localization. Metric CEEval-Full.
- **Data.**
  - FlawedFictions: 414 stories (207 positive), from Project Gutenberg, about 730 words.
  - FlawedFictionsLong: 200 stories (97 positive), fairy tales, about 2,700 words.
  - Positives built by a five-stage pipeline (three-act extraction, proposition scoring, counterfactual generation, patching, filtering) with GPT-4o, then Prolific verification (at least three annotators, majority). About 70% accepted.
- **Results** (FlawedFictions, accuracy / CEEval-Full):
  - Always "no error" 0.50 / 0.50.
  - Llama-3.3-70B 0.57 / 0.38.
  - GPT-4o (CoT) 0.64 / 0.58.
  - o1 (low) 0.71 / 0.65.
  - Claude 3.5 Sonnet 0.76 / 0.67.
  - Claude 3.5 Sonnet with verifier 0.74 / 0.68.
  - Claude 3.7 Sonnet (extended thinking) 0.73 / 0.66.
  - Human 0.76 / 0.68 (9 undergraduates, 50 samples).
- **Long set** (FlawedFictionsLong): best o1 (medium) 0.61 / 0.53. Near baseline (0.51 / 0.51).
- **Length effect** (Table 7): point-biserial correlation of word count with CEEval-Full is negative for all 14 models, from -0.029 to -0.196; 13 of 14 significant.
- **Generator-induced errors** (Figure 2): summarizing raises GPT-4o's error rate from 0.31 to 0.45. Contemporary adaptation raises Claude 3.5 Haiku from 0.14 to 0.27, and GPT-4o-mini from 0.14 to 0.53.
- **Limits.** One inserted flaw per story. Only continuity errors. CEEval-Full is lenient. Small human sample. Inter-annotator agreement not reported in the visible text.
- **Label:** Proven at benchmark level (multiple models; length effect with many models). The long set is weak and mostly fairy tales.
- **Copy:** the length-effect check as a sanity test for any judge; plot-hole detection as an audit task for a critic.
- **Avoid:** using this as a measure of long-form quality. The stories are short, the errors are planted, and detection is not repair.

### 3.3 Spoiler Alert: narrative forecasting for tension (Sui et al., arXiv 2604.09854)
- **Date:** v1 2026-04-10. Source: [HTML v1](https://arxiv.org/html/2604.09854v1).
- **Metric: 100-Endings.** At each sentence boundary (10% to 99%), Qwen3-32B generates 100 candidate endings. Qwen3-8B judges each as Y/N against the true continuation. The no-rate is the fraction that fail. Plus late-stage no-rate, post-spike retention, and inflection rate at vertex-angle thresholds.
- **Findings.**
  - Human corpora (New Yorker, n=261) have mean no-rate 0.765, late NR 0.607.
  - Top-10 LLMs on EQ-Bench (n=319): mean NR 0.630, late NR 0.215. LLMs score higher on EQ-Bench rubric (about 82 vs 79) but lower on 100-Endings.
- **Pipeline** (Step 0: 7-beat sheet from a reference story; Step 1: thick plan; Step 2: write). Pipeline on 32 EQ-Bench prompts:
  - Sonnet 4.6: vanilla late NR 0.139, pipeline 0.339. Rubric 82.04 to 85.03.
  - Opus 4.6: 0.185 to 0.296. Rubric 82.88 to 81.82.
  - GPT-5.2: 0.329 to 0.443. Rubric 83.80 to 81.24.
  - Internal inconsistency: section 6.2 reports 0.702 and 0.577; Table 2 reports 0.747 and 0.606. Flagged.
- **Stability.** Across 4 repeats, SD of mean NR ≤ 0.001.
- **Limits stated.** Predictability is necessary but not sufficient, so incoherent text can score high. Circular: LLM generator and LLM judge (mitigated by separate families). The pipeline closes "roughly half" the gap. 32 prompts. The New Yorker corpus is private. No component ablations.
- **Label:** Promising. The metric is novel and stable, but the pipeline result is small (32 prompts) and has internal inconsistencies.
- **Copy:** the tension metric as a check on whether a draft is too predictable; the beat-sheet-then-plan-then-write pipeline as a baseline to test against.
- **Avoid:** using NR alone as a quality score (the authors' own caveat). Note the pipeline lowered rubric scores for two of three models.

### 3.4 StoryScope (Russell, Rajendhran, Iyyer, Wieting; arXiv 2604.03136)
- **Date:** v1 2026-04-03. Source: [HTML v1](https://arxiv.org/html/2604.03136v1). Univ. of Maryland and Google DeepMind.
- **What it measures.** Whether AI fiction can be told apart from human fiction by narrative-discourse choices (agency, chronology, etc.), not style. Uses rarity in a 304-feature narrative space.
- **Pipeline.** GPT-5.1 converts each story into a template across ten NarraBench dimensions. Feature discovery and deduplication to 304. Gemini 3 Flash fills values. XGBoost with SHAP picks 30 core and 75 fingerprint features.
- **Data.** 10,272 Books3 human stories, each with mirror AI stories from five LLMs (61,608 total). Average about 4,750 words.
- **Results.**
  - Binary human vs AI macro-F1: narrative 93.2; narrative + style 96.0; core only 84.8; ModernBERT 99.9; Binoculars 55.9.
  - Six-way attribution: narrative 68.4 (chance 16.7); text baselines at least 99.5.
  - Human stories are the rarest of six versions for a prompt 57.8% of the time (chance 16.7%).
  - Attribution is weak among Gemini, DeepSeek, and Kimi (F1 0.55 to 0.67).
- **Validation.** Gemini 3 Flash repeatability Krippendorff α = 0.88 (the paper also reports 0.90 and κ 0.89; not fully consistent). Human-model κ = 0.84 on 240 items over 12 stories.
- **Limits.** Raw-text detectors beat the narrative features on accuracy. Human validation is only 12 stories. Copyright limits human text release. Pipeline depends on specific LLMs.
- **Label:** Proven at benchmark level for the detection gap (large corpus, many generators); promising for the feature set as a tool.
- **Copy:** narrative-discourse features (agency, chronology, perspective) as diagnostics for "AI sameness" in a draft, and the rarity-vs-prompt-mates design.
- **Avoid:** using it as a detector. Its own result says raw text classifiers win. Also avoid the 2026-era generator mix as a fixed reference.

### 3.5 Synthetic Reader Panels (Zimmerman; arXiv 2602.14433)
- **Date:** v1 2026-02-16. Source: [HTML v1](https://arxiv.org/html/2602.14433v1). Single author, affiliated with the deploying publisher.
- **Method.** LLM personas (demographic, reading, psychographic, with consistency and reliability scores). Panel composition 40% target, 30% adjacent, 20% wild cards, 10% experts. Tournament selection with thresholds (aggregate ≥ 6.5/10, ≥ 60% of panelists above 5, ≥ 40% "would read"). Anti-slop gate with five checks (accept s<0.4; review 0.4 to 0.6; reject ≥0.6).
- **Numbers.**
  - Filtered vs unfiltered concepts (8 champions vs 20 concepts): mean 4.8 vs 7.1; share ≥7: 15% vs 62%.
  - Case A (N=270): aggregate 7.9; reluctant readers 5.9; tech-savvy 8.4.
  - Case B (N=5): military specialists 9.0 vs general readers 7.0.
- **Validation.** None against real readers or sales. Calibration and anti-bias effects are described but not quantified. The anti-slop detector has no accuracy or false-positive rate.
- **Failure modes reported.** Positivity bias (LLM readers score higher). Recency bias. Articulation premium (better-written pitches score higher). Cultural and community gaps.
- **Label:** Promising at best. No validation, tiny samples, no significance tests, one deployment.
- **Copy:** the panel-composition idea (anchor, adjacent, wild card) and the explicit positivity-bias warning as a checklist item.
- **Avoid:** treating panel scores as reader predictions. Use it only as a relative ranking within one run, and check against real readers before trusting it.

### 3.6 Reader simulation and judge reliability (cross-paper)
- **Agents' Room:** LLM pairwise judge agreed with humans at ρ = 0.62 (systems) and 0.41 (items). Self-consistency 90%.
- **MAGNET:** LLM editors agreed with human annotations 82.5 to 85.0%.
- **StoryScope:** LLM feature annotation κ = 0.84 with humans on 12 stories.
- **ConStory checker:** recall 0.55, precision 0.88. Undercounts errors.
- **Synthetic Reader Panels:** no validation.
- **Suspense (Xie and Riedl):** human pairwise only, with no numeric agreement reported.

Read-across: judges agree with humans most on coarse system-level rankings and least on item-level calls. Recall of error detectors is the weak point. No paper here reports a reader-simulation method validated against real readers' ratings over time.

---

## 4. Plot holes, suspense and fair play (narrower methods)

### 4.1 Suspense via iterative planning (Xie and Riedl; arXiv 2402.17119)
- **Date:** v1 2024-02-27. Source: [HTML v1](https://arxiv.org/html/2402.17119v1). Georgia Tech.
- **Method.** Zero-shot, ChatGPT (gpt-3.5-turbo-0613). Generate protagonist, goal, and dire situation. Then iterate: propose an action toward the goal, then a reason it fails, conditioned on earlier failures. The final iteration succeeds. Each action-failure pair becomes a chapter summary, then an event sequence, then prose. Optional clues of the coming failure, and timing of the reveal.
- **Results** (human pairwise, Prolific, 90 participants, 30 pairs):
  - vs ChatGPT baseline: suspense 84.9% win; novelty 76.6%; enjoyment 67.9%; logic 49.2%; naturalness 25.3% win, 56.1% tie.
  - Ablation 1 (no detail elaboration) vs baseline: suspense 79.8%. Ablation 2 (also no outline planning): suspense 72.3%.
  - Full vs Ablation 1: suspense 75.0%. Full vs Ablation 2: suspense 80.4%.
  - Clues: 57.9% preferred the version with clues vs 10.9% without.
  - Outline checks (30 stories): action relevant 96.5%; failure reason plausible 89.8%; likelihood decreasing 55.1%.
- **Agreement.** Fleiss κ computed; only "fair average" reported, no number.
- **Limits.** English only; Western narrative theory; thin character setup weakens empathy and suspense.
- **Label:** Promising. Strong pairwise effects, but single paper, gpt-3.5-era model, and short stories.
- **Copy:** the planned-failure outline (each beat is an attempted action that fails, with decreasing likelihood) as a suspense generator; clue planting; the relative-preference eval.
- **Avoid:** using pairwise "which is more suspenseful" as a metric without anchoring. The method's suspense claims have no automated measure. Spoiler Alert (3.3) offers one.

### 4.2 Fair-play detective fiction (Wagner, Keydar, Abend; arXiv 2507.13841)
- **Date:** v1 2025-07-18. Source: [HTML v1](https://arxiv.org/html/2507.13841v1). Hebrew University of Jerusalem.
- **Correction to the brief.** This paper does **not** propose a fair-play generation method. It proposes a probabilistic framework and metrics for fair play, and applies them to LLM-generated detective stories. Generation is plain paragraph-by-paragraph prompting (25 paragraphs), with no clue planning and no checker.
- **Metrics.** Gullible-reader and know-it-all-reader probabilities. Surprise S_S (lower = more surprise). Coherence S_C (upper bound, since it uses the know-it-all reader). Fair play S_FP = S_C − S_S. Expected revelation content (ERC) via paragraph filling.
- **Findings.** Real Holmes stories reveal the culprit earlier than Poirot stories (surprisal 0.466 vs 0.634). Small Llama models mostly fail to get positive fair-play scores. Several models converge on the culprit early, which can make scores unreliable. Name and style repetition (about 90% of Llama stories use "Jameson").
- **Table 1 extraction is garbled**, so the S_S, S_C, S_FP and ERC values per model are not reliable from the tool output. Check the PDF before citing them.
- **Label:** Promising. The framework is interesting; the empirical table could not be read cleanly.
- **Copy:** the surprise-vs-coherence decomposition as a test that a mystery reveals fairly. The early-convergence failure as a check on generated mysteries.
- **Avoid:** citing this as a generator. It is an evaluation framework with LLM-judged probabilities, validated against no humans.

---

## 5. Revision loops: what helps and what adds churn

| Mechanism | Evidence | Strength |
|---|---|---|
| Critic gating actions before commit (MAGNET) | Ablation: 109.0 vs 84.0 annotations; rubric 78.1 vs 82.6 | Promising (single paper, ablated) |
| Verify-then-repair with commit-on-zero-violations (ConWriter) | Ablation: CED 0.13 vs 0.68 without structured validation | Promising, but CED is judge-based |
| Scene-level verification gate (ConWriter) | Above | Promising |
| Temporal KG memory (DOME) | CR 0.56 vs 4.52 without MEM | Promising; 20 premises |
| Scorer and recall/thread agents (CreAgentive) | 8.48 full vs 7.93 without recall/thread | Promising; small margins |
| Plan-level iterative failure (Suspense) | Pairwise suspense 80.4% vs ablation | Promising |
| Extra planning-only stages (Agents' Room plan-only) | Plan-only underperforms | Churn signal, weak |
| Tension pipeline (Spoiler Alert) | Late NR up for two of three models; rubric down for two | Mixed; rubric cost |
| Repeated feedback loops in general (ConWriter limits) | "Repeated feedback can conflict with length control" | Churn risk |

Read-across: gains that come from a gate on writes (no commit without a check) and from memory the writer reads back show up in ablations. Pure planning stages without a check do not reliably help. Revision budgets are capped in every system here, and the papers do not report a sweep over the number of revision rounds. That is a gap.

---

## 6. Failure modes (collected)

- **Length vs quality confound.** Agents' Room: word count and human preference are not the same. FlawedFictions: error rate rises with length for 13 of 14 models. ConStory: error count grows roughly linearly with length. Normalize by length.
- **Judge positivity and self-preference.** Synthetic Reader Panels report positivity bias and articulation premium. MAGNET and CreAgentive use judges from the same family as the generator.
- **Judge recall.** ConStory checker recall 0.55: many errors are missed. Plot-hole detectors are measured on planted errors, not natural ones.
- **Predictability is not tension.** Spoiler Alert: low predictability is necessary but not sufficient.
- **Early convergence.** Fair-play detective: models pick the culprit early, which makes fair-play scores unreliable.
- **Mid-story drift.** ConStory: errors cluster at 40 to 60% of the narrative.
- **Plan-only without writing.** Agents' Room: plan-only output is short (856 words) and underperforms.
- **Repair compliance.** ConWriter: some strong models are less repair-compliant.
- **Reported-number mismatches.** ConStory (human F1, GRR), CreAgentive (8.28 vs 8.48), DOME (Table 1 vs 2), Spoiler Alert (0.702 vs 0.747), MAGNET (rubric text vs table). Check before citing.

---

## 7. What we should copy (summary)

1. A state store that is written only after a check passes (ConWriter; MAGNET). Commit on zero blocking violations.
2. Explicit transition constraints per scene (pre, post, forbidden), checked before drafting (ConWriter).
3. Chapter-stamped relation and event graph as the memory (DOME; CreAgentive). Retrieval by entity and relevance.
4. A critic that can reject and regenerate an action before it becomes a story beat (MAGNET).
5. Planned failure per beat for suspense (Suspense), with clues.
6. Consistency error taxonomy from ConStory (five categories, 19 subtypes) as the checker vocabulary; CED per 10k words as the metric.
7. Length-controlled evaluation: report per-length results and normalize errors.
8. Pairwise human eval (Bradley-Terry) for system ranking, with the LLM judge used only for system-level ranks.

## 8. What we should avoid

1. Text-only scratchpads with no consistency check (Agents' Room) for anything that must hold over chapters.
2. Ranking systems on word count, Rouge, or BertScore.
3. Trusting LLM judges for item-level calls (Agents' Room ρ = 0.41) or for error recall (ConStory 0.55).
4. Reader-panel scores as a stand-in for real readers (Synthetic Reader Panels; no validation).
5. Predictability as a tension score on its own (Spoiler Alert).
6. Extra planning or revision stages with no measured gain (Agents' Room plan-only).
7. Unbounded revision. Every system caps retries, and no paper sweeps the cap.

## 9. Gaps and newer work

- **Replication:** none of these results is replicated. All are single-paper.
- **Unverified "Atlas":** the MAGNET paper's HTML text does not mention Atlas. A search snippet describes an ATLAS hallucination checker. Verify against the PDF.
- **Not read:** StoryWriter (arXiv 2506.16445), SuperWriter-agent (arXiv 2506.04180), WSE-bench (arXiv 2608.15654). These came up in search and may be relevant. Read them next.
- **Missing evaluation:** no paper here reports a reader-simulation method validated against real reader ratings over time, or a sweep of revision-round counts. These are the two most useful gaps for us.
- **Length:** most systems stop at 10 to 100 pages or ~7,000 words. Novel-length (80k+) evidence is absent from this set.
- **Language:** all systems are English-only (Suspense explicitly). No cross-language evidence.
- **Reproducibility:** several rely on private corpora (New Yorker in Spoiler Alert), copyrighted human stories (StoryScope), or single-author deployments (Synthetic Reader Panels).

## 10. Source list

- Agents' Room: https://arxiv.org/abs/2410.02603 (v1 2024-10-03, v2 2025-03-14; ICLR 2025). HTML: https://arxiv.org/html/2410.02603v2
- MAGNET / "From Personas to Plot": https://arxiv.org/abs/2607.00918 (v1 2026-07-01, v2 2026-10-03). HTML: https://arxiv.org/html/2607.00918v2
- ConWriter: https://arxiv.org/abs/2608.05169 (v1 2026-05-27, v2 2026-09-04; Findings of EMNLP 2026). HTML: https://arxiv.org/html/2608.05169v2
- CreAgentive: https://arxiv.org/abs/2509.26461 (v1 2025-09-30). HTML: https://arxiv.org/html/2509.26461v1
- ConStory-Bench / Lost in Stories: https://arxiv.org/abs/2603.05890 (v1 2026-03-06). HTML: https://arxiv.org/html/2603.05890v1
- DOME: https://arxiv.org/abs/2412.13575 (v1 2024-12-18). HTML: https://arxiv.org/html/2412.13575v1
- Finding Flawed Fictions: https://arxiv.org/html/2504.11900v1 (2025-04)
- Spoiler Alert: https://arxiv.org/html/2604.09854v1 (v1 2026-04-10)
- StoryScope: https://arxiv.org/html/2604.03136v1 (v1 2026-04-03)
- Synthetic Reader Panels: https://arxiv.org/html/2602.14433v1 (v1 2026-02-16)
- Shadow-Loom: https://arxiv.org/html/2605.02475v1 (v1 2026-05-04)
- Fair-play detective: https://arxiv.org/html/2507.13841v1 (v1 2025-07-18)
- Suspense via iterative planning: https://arxiv.org/html/2402.17119v1 (v1 2024-02-27)
- Search-only leads: StoryWriter https://arxiv.org/pdf/2506.16445; SuperWriter-agent https://arxiv.org/pdf/2506.04180; WSE-bench https://arxiv.org/pdf/2608.15654

## Section 3.4 addendum: Shadow-Loom (arXiv 2605.02475; David Wilmot; v1 2026-05-04)
- **What it is.** An open-source framework (not benchmarked) that turns a narrative into a versioned graphical world model. Causal engine (Pearl's three rungs over an ancestral multi-world network) and narrative-physics engine (scores four reader states: mystery, dramatic irony, suspense, surprise, plus six emotional trajectories). LLMs are used only for extraction, rendering, and audit.
- **Pipeline.** Five agents build a register; three specialist agents per chunk; validation with auto-repair. Causal and narrative scoring. Top candidate packed as a brief. Only the brief reaches the creative LLM. Audit for "miracle steps".
- **Results.** None. No external dataset, no ablations, no reader-data validation. The author says so.
- **Label:** Not evidence. A design artifact.
- **Copy (as ideas only):** the "only the brief reaches the writer" boundary; an audit step that flags unmotivated events.
- **Avoid:** treating its reader-state scores as validated.
