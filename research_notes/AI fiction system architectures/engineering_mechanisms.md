# Engineering mechanisms for reliable long multi-agent LLM pipelines

Scope: what decides whether a multi-stage agent pipeline finishes, stays consistent and stays cheap, with transfer notes for a fiction-writing engine (brief, planning, scene cards, drafting, revision loop, readers, delivery).

Labels: **PROVEN** = primary source reports a measured result or documents a stable API behaviour. **PROMISING** = a credible single-source or vendor-reported result, or a design recommendation without controlled evidence.

Sources fetched 2026-11-22. Dates are the page or paper date. Vendor pages carry no dates where noted.

Source list (primary unless marked):
- S1 Anthropic, "Building effective agents", 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- S2 Anthropic, "How we built our multi-agent research system", 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system
- S3 Anthropic, "Effective context engineering for AI agents", 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- S4 Anthropic API docs, Prompt caching. Undated page, read 2026-11-22. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- S5 Anthropic API docs, Rate limits. Undated page, read 2026-11-22. https://platform.claude.com/docs/en/api/rate-limits
- S6 Anthropic API docs, Message Batches API. Undated page, read 2026-11-22. https://platform.claude.com/docs/en/build-with-claude/batch-processing
- S7 Cognition (Walden Yan), "Don't Build Multi-Agents", 2025-06-12 (secondary: company blog, vendor of Devin). https://cognition.com/blog/dont-build-multi-agents
- S8 Mem0 team, arXiv:2504.19413, submitted 2025-04-28 (vendor-authored). https://arxiv.org/abs/2504.19413
- S9 Zep team, arXiv:2501.13956, submitted 2025-01-20 (vendor-authored). https://arxiv.org/abs/2501.13956
- S10 Ye et al., "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge", arXiv:2410.02736, submitted 2024-10-03. https://arxiv.org/abs/2410.02736 (abstract only; see gaps)

---

## 1. State and memory

### Takeaway
The strongest evidence favours explicit, external, structured state (plans, notes, traces, and typed records) over relying on a running summary. Vendor memory-graph systems report accuracy and cost gains, but these are vendor-reported and were checked only at abstract level.

### Cited Findings
- Context is a finite resource with diminishing returns; the goal is the smallest set of high-signal tokens. — **PROVEN (as guidance from a primary source)**, [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Structured note-taking: the agent writes notes to persistent storage outside the context window and reads them back (to-do lists, NOTES.md). Anthropic cites a Pokémon agent that kept tallies and maps across context resets. — **PROMISING** (one anecdote plus design advice), [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Lead agent saves its plan to external memory because context beyond ~200k tokens gets truncated. — **PROVEN as an operational practice in a production system**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- Compaction: summarise near the context limit and restart with the summary. Preserve architectural decisions, unresolved bugs and implementation details; discard redundant tool output. Tune for recall first, then improve precision. Clearing old tool results is described as the lightest form. — **PROMISING** (guidance, no ablation given), [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Pre-loading (embedding retrieval up front) versus just-in-time retrieval (keep identifiers such as paths and queries; load at runtime through tools). Claude Code uses a hybrid: CLAUDE.md is loaded up front, other files are fetched with glob and grep. The article suggests the hybrid suits less dynamic domains such as legal or finance. — **PROMISING**, [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Sub-agents may use tens of thousands of tokens internally but return condensed summaries of about 1,000–2,000 tokens to the lead. — **PROMISING** (design pattern), [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Mem0 (LOCOMO benchmark, LLM-as-judge accuracy): 26% relative improvement over an OpenAI memory baseline; 91% lower p95 latency than full-context; more than 90% token-cost saving versus full-context; graph variant about 2% higher overall. — **PROMISING** (vendor-authored; abstract only, absolute numbers and summary or RAG baselines not seen), [S8](https://arxiv.org/abs/2504.19413)
- Zep (temporal knowledge graph): Deep Memory Retrieval 94.8% vs 93.4% for MemGPT; LongMemEval accuracy up to 18.5% higher than baselines; 90% latency reduction. — **PROMISING** (vendor-authored; abstract only; baselines not named), [S9](https://arxiv.org/abs/2501.13956)
- Cognition's principle: share full agent traces, not single messages, and avoid parallel agents acting on unstated assumptions. — **PROMISING** (practitioner position with one worked example), [S7](https://cognition.com/blog/dont-build-multi-agents)

### Inferences
- For a fiction engine, the bible, brief, scene cards and continuity ledger should be **files or database rows with IDs**, not prose summaries. Summaries lose the exact facts that the continuity checker needs (names, dates, who-knows-what).
- Compaction is safe only for chat history. Decisions, rulings, and the scene-card plan must be persisted outside the summary.
- A knowledge graph of entities and time-stamped facts is the natural fit for continuity (who is where, when). The Zep result suggests that temporal graphs help retrieval, but there is no evidence here that they beat well-indexed flat records for a corpus of this size.

**Copy:** a run-state file (plan, status per scene, decisions made, open loops); typed records for entities and facts with source references; summaries of sub-agent output capped at a fixed length.
**Avoid:** rolling summaries as the only memory; memory retrieval that drops exact facts; parallel workers with unstated shared assumptions.

### Gaps
- No controlled head-to-head of "structured state" versus "plain summary" in a long-form generation task was found. Lost-in-the-middle style evidence (Liu et al., 2023) was not fetched in this run.
- Mem0 and Zep numbers are from abstracts and are vendor-authored. Baseline summary-memory results were not seen.
- Anthropic's file-based memory tool (beta, mentioned in S3) was not documented in detail.

---

## 2. Context budgeting and prompt caching

### Takeaway
Caching is the largest cost lever for a bible re-read on every call. Cache reads cost 0.1× base input (less on some newer models), and cache-read tokens do not count against input-tokens-per-minute limits. Put stable content first and changing content last, and mark a breakpoint after the stable block.

### Cited Findings
- Pricing multipliers relative to base input: 5-minute cache write 1.25×; 1-hour cache write 2×; cache read 0.1× by default, 0.05× for Opus 5.5 and Sonnet 5.5, and 0.025× for the Fable and Mythos 5.1/5.2 models. — **PROVEN (current API pricing)**, [S4](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Example per-MTok prices from that table: Haiku 5.5 base $0.10 (≤100k prompt tokens), write $0.125 (5m) or $0.20 (1h), read $0.01; Opus 5.5 base $4, read $0.20; Sonnet 5.5 base $2, read $0.10. — **PROVEN** (as listed on the page on 2026-11-22), [S4](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Minimum cacheable prompt length is model-dependent: 512 tokens for Haiku 5.5, Opus 5.5, Sonnet 5.5; 1,024 for Sonnet 5 and Sonnet 4.x; 2,048 for Opus 4.7; 4,096 for Haiku 4.5 and Opus 4.5/4.6. Shorter prompts are silently not cached. — **PROVEN**, [S4](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Cache prefix order is tools, then system, then messages. A change at one level invalidates that level and every later level. A change to tool definitions invalidates all three. Changing `tool_choice` or adding or removing images invalidates tools and system but not messages. — **PROVEN**, [S4](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Lookback: the system checks at most 20 positions per breakpoint. Up to 4 explicit breakpoints are allowed; automatic caching uses one slot, and 4 explicit breakpoints plus automatic caching returns a 400. Cache writes happen only at a breakpoint. — **PROVEN**, [S4](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- Cache-aware ITPM: `cache_read_input_tokens` do not count toward ITPM; `input_tokens` (after the last breakpoint) and `cache_creation_input_tokens` do. Example: 80% hit rate on a 2M ITPM limit gives about 10M effective input tokens per minute. Ramp limits also exclude cache reads. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)
- Batch and cache: the Message Batches API is 50% off (per the page description) and batches usually finish within 1 hour. The page recommends the 1-hour cache for batches with shared context, because a 5-minute entry may expire while the batch is processing. — **PROVEN** (page text), [S6](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- Anthropic's multi-agent run used about 4× the tokens of chat, and about 15× for multi-agent systems; token usage alone explained 80% of variance in BrowseComp performance. — **PROVEN** (self-reported eval in one system), [S2](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- Cost model for the engine: if the bible is B tokens and there are N calls per story, uncached cost is roughly N·B·base; cached cost is about B·write once plus N·B·0.1·base. For a bible of 100k tokens and 50 calls on Sonnet 5.5, that is roughly $10 uncached versus roughly $0.5 + $0.5 + small write cost cached, before counting output. Re-check this against the live price table before budgeting.
- Ordering: static rules and bible first, then per-story brief, then per-scene cards and the working text. Avoid putting timestamps, run IDs, or a varying "today" line in the early blocks, since any change there invalidates everything after it.
- Tool definitions are the most expensive thing to change: keep the tool list identical across all stages to keep the cache warm.
- Keep the cache alive during a run by reusing the same prefix within 5 minutes (or use 1h for slow stages).

**Copy:** stable-first prompt layout; one breakpoint after the bible; 1-hour cache for batch or slow review stages; a fixed tool list; monitor the cache-read rate on the usage page.
**Avoid:** time or ID stamps in the prefix; re-sending the bible inline in every user message; relying on a 5-minute cache for stages that run hours apart.

### Gaps
- The exact cache-hit rate achievable in a multi-stage fiction run was not measured here.
- The prompt-caching page is undated; prices were read on 2026-11-22 and must be re-checked before any budget is set.

---

## 3. Orchestration: fan-out, gates, checkpoints, resume

### Takeaway
Use an orchestrator-worker pattern where workers are fan-out for independent tasks and sequential gates for dependent ones. Checkpoint every stage and resume from the last good state rather than restarting. The published failure mode is conflicting unstated assumptions between parallel workers, which is avoided by sharing full context and by making decisions explicit.

### Cited Findings
- Workflow patterns: prompt chaining (with programmatic checks between steps), routing, parallelization (sectioning and voting), orchestrator-workers (when subtasks cannot be predicted), and evaluator-optimizer (when criteria are clear). Advice: find the simplest solution first; agentic systems trade latency and cost for performance. — **PROVEN (vendor guidance)**, [S1](https://www.anthropic.com/engineering/building-effective-agents)
- Multi-agent research system: Opus 4 lead with Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on an internal eval. — **PROMISING** (internal eval, self-reported), [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- The lead starts 3–5 subagents in parallel; each uses 3+ tools in parallel; this cut research time by up to 90% on complex queries. Synchronous subagent execution was named as a bottleneck. — **PROVEN as self-reported, PROMISING as generalisable**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- Resume: the team built systems that resume from the point of error, paired with retries and regular checkpoints. Rainbow deployment shifts traffic gradually from old to new versions while both run, because agents are mid-process. — **PROVEN as a practice in production**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- Production tracing and monitoring of decision patterns, without reading individual conversations. — **PROMISING**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- Failure mode: a task split into a background and a bird subtask produced a Super Mario-style scene and a mismatched sprite; the final agent had to reconcile them. Recommendation: share context and full traces; actions carry implicit decisions, and conflicting decisions produce bad results. — **PROMISING** (one worked example), [S7](https://cognition.com/blog/dont-build-multi-agents)
- Claude Code subagents are mostly used to answer narrow questions and are not used for writing code in parallel with the main agent, to avoid conflicting work. — **PROMISING** (author's account of a product design), [S7](https://cognition.com/blog/dont-build-multi-agents)

### Inferences
- The engine's sequential gates (brief, plan digest) map well to the evaluator-optimizer and prompt-chaining patterns. The scene drafting fan-out is safe only if scenes share a frozen plan and a written list of decisions.
- Parallel scene drafting is the main risk. Use parallel workers for independent checks (continuity, word counts, name collisions) but keep prose drafting sequential or limited to scenes with no shared state.
- Idempotence: each stage should write to a fixed path keyed by scene ID and stage, so a rerun overwrites rather than duplicates. This is an inference from the resume practice and is not a published result.

**Copy:** an orchestrator plus workers; a run log with stage status; a frozen plan file that every worker reads; per-stage outputs keyed by IDs; resume from the last completed stage; trace every worker's inputs.
**Avoid:** parallel prose writers with no shared decision log; subagents that receive only a message, not the context behind it; restarting whole runs after a failure.

### Gaps
- No published data was found on checkpoint granularity, or on idempotency-key designs from LangGraph, CrewAI or AutoGen. Those framework docs were not fetched in this run.

---

## 4. Rate limits, 429s and usage caps

### Takeaway
There are two different failure types. A 429 with `retry-after` is a transient rate limit, so wait that many seconds and retry. A spend-cap 429 has no `retry-after` and retrying does not help. Batch processing is the main lever for bulk work because it has its own limits and no ramp limit.

### Cited Findings
- Rate limits are RPM, ITPM and OTPM per model class, enforced with a token bucket. A 60 RPM limit may be enforced as 1 request per second, so bursts can fail. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)
- On 429, wait the `retry-after` seconds if the header is present. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)
- Monthly spend cap: once reached, requests return HTTP 429 with `rate_limit_error` and `error_code: enforced_spend_limit_reached`, with no `retry-after`. Retries, including SDK retries, fail until access resumes. Detect this code and stop; do not back off. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)
- Ramp limits: a sharp rise in usage can cause 429 `ramp_limit_exceeded` even under ITPM and OTPM. Advice: hold traffic at a level that succeeds, then rise by at most one step per minute; start bulk jobs slowly and spread requests. Batches are not subject to ramp limits. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)
- Message Batches: 50% discount; most batches finish in under 1 hour; results are available when all requests finish or after 24 hours; unfinished batches expire at 24 hours and expired requests are not billed. Each result carries a `custom_id` (1–64 characters, alphanumeric, hyphen, underscore). Batch limits by tier: 1,000–4,000 RPM for batch endpoints, up to 500,000 queued batch requests, 100,000 requests per batch. — **PROVEN**, [S6](https://platform.claude.com/docs/en/build-with-claude/batch-processing), [S5](https://platform.claude.com/docs/en/api/rate-limits)
- Monitoring: the Usage page shows rate-limit headroom and cache rate; response headers `anthropic-ratelimit-*` show remaining capacity. — **PROVEN**, [S5](https://platform.claude.com/docs/en/api/rate-limits)

### Inferences
- The retry policy should branch on `error_code`: ramp or RPM/ITPM (back off with `retry-after`, else exponential with jitter); spend cap (halt the run and checkpoint).
- Model tiering: use the cheapest model that passes for checkers, and reserve the strongest model for drafting and final judging. This is standard practice and the caching table supports it, but no controlled result was checked here.
- For a fiction run, a long batch of non-interactive checks (readers, continuity scans) belongs in the Batches API; the interactive gates stay synchronous.

**Copy:** branch on `error_code`; batch offline stages; a run budget in the run log; halt and checkpoint on spend-cap errors.
**Avoid:** retry loops on spend-cap errors; bursts of parallel calls at the start of a run (ramp limits); ignoring cache-read exemption when sizing jobs.

### Gaps
- Exponential backoff with jitter is not confirmed from the docs fetched here; the rate-limit page only says to honour `retry-after`.
- Tier-specific limits shown are as of 2026-11-22 and will change.

---

## 5. Checkers and judges

### Takeaway
A single-call rubric judge with a bounded score and a pass or fail grade is the most consistent design reported by a primary source, and it works best when the correct answer is clear. For mechanical checks (counts, cites, names, timelines), use scripts. Judge bias is documented but the specific bias effects were not verified in this run.

### Cited Findings
- Anthropic's research judge: one LLM call scores each output on a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency), returns a 0.0–1.0 score and pass or fail. This was the most consistent design and best aligned with human judgment, and worked best where the answer is clear. — **PROVEN (internal, self-reported)**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- The same source says humans still caught hallucinations on unusual queries, system failures and source-selection bias, such as favouring SEO content farms. — **PROVEN (as a reported limitation)**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)
- Anthropic advises programmatic checks between chained steps. — **PROVEN (guidance)**, [S1](https://www.anthropic.com/engineering/building-effective-agents)
- LLM-as-judge bias: "Justice or Prejudice" lists 12 potential biases, proposes the CALM framework to quantify them, and reports that significant biases persist on certain tasks even for advanced models. The abstract gives no bias list, effect sizes, judges tested or mitigation results. — **PROMISING** (abstract only, numbers not verified), [S10](https://arxiv.org/abs/2410.02736)

### Inferences
- Deterministic scripts should own: word counts per scene and chapter, required-cite presence and format, name collisions against the name ledger, timeline and date arithmetic, forbidden-term and banned-list scans, and schema validation of JSON outputs. A model is unreliable at these and a script is free.
- Models should own: whether a scene does what the plan says, whether a character's motive holds, whether a reader's experience works, and voice or style notes.
- Judge calibration: score against a fixed rubric with anchors, run the judge on a set of known good and known bad scenes before trusting it, and log the disagreement with human rulings. The position and length biases in S10 (not verified here) argue for randomised order and length-controlled comparisons if pairwise judging is used.
- Use a different model or a fresh context for judging, so that the drafter's assumptions do not bias the judge.

**Copy:** deterministic scripts first; rubric-based single-call judges with anchors; a gold set of scenes with human labels for calibration; a fresh context for each judge.
**Avoid:** trusting a judge without a calibration set; asking a judge to count words or check cites; pairwise judging without order randomisation.

### Gaps
- The MT-Bench paper (Zheng et al., 2023) and other judge-bias papers were not fetched in this run. Their numbers are not included.
- No calibration data for LLM judges on long-form fiction was found.

---

## 6. Human-in-the-loop

### Takeaway
Not researched in this run. Only indirect evidence is available: Anthropic's research system keeps humans in the loop for evaluation and tracing, and the batched-review pattern is consistent with the rate-limit guidance.

### Cited Findings
- Human testers caught failures the judge missed (hallucinations, system failures, source bias). — **PROVEN (as reported)**, [S2](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- Two gates (brief, plan digest) are a reasonable pattern. Place the human at points where a wrong decision is expensive to undo (canon, plan), not at every scene.
- Batch human review: present a set of decisions together, with options and cites, as one approval.

### Gaps
- No published data on approval-gate placement or review batching from production systems was checked in this run.

---

## 7. Tool use and schema checking

### Takeaway
Tools should be designed with the same care as prompts: clear names, examples, hard-to-misuse parameters, and tests against many inputs. Keep tool outputs small and structured, and validate them with a schema.

### Cited Findings
- Invest in agent-computer interface (ACI) design: thorough tool documentation and testing, test against many example inputs, and make parameters hard to misuse (for example, require absolute paths). — **PROVEN (vendor guidance)**, [S1](https://www.anthropic.com/engineering/building-effective-agents)
- Sub-agents return condensed summaries (1,000–2,000 tokens) rather than raw output. — **PROMISING**, [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Just-in-time retrieval needs good tool design and heuristics to avoid wasted context. — **PROMISING**, [S3](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Inferences
- Each stage should write a typed JSON record (scene ID, word count, cite list, entities, facts) that a script validates before the next stage starts. Validation failure is a retry with the error message, not a silent pass.
- Expose the bible through narrow tools (get entity by ID, list facts for scene) rather than dumping it in the prompt, if the bible grows beyond the cache budget.

### Gaps
- Structured-output and schema-enforcement features of the API were not fetched in this run.

---

## Summary of what to copy and avoid for the engine

Copy:
1. Persist everything that must survive (plan, decisions, open loops, entity facts) in files or rows with IDs. Do not rely on summaries.
2. Stable-first prompt layout with one cache breakpoint after the bible; 1-hour cache for slow or batch stages.
3. Orchestrator plus gated stages; parallel only for independent checks.
4. Checkpoint each stage; resume from the last completed stage; key outputs by scene and stage ID.
5. Branch retry logic on `error_code`; halt on spend cap; batch the offline checks.
6. Deterministic scripts for counts, cites, names and timelines; rubric judges with anchors and a gold set for prose.
7. Typed, validated outputs between stages.

Avoid:
1. Summary-only memory; parallel prose writers with unstated assumptions.
2. Timestamps or varying text in the cache prefix.
3. Retrying spend-cap 429s.
4. Judges that count or check cites; pairwise judging without order control.

## Evidence quality and conflicts
- Most measured numbers come from vendors (Mem0, Zep) or from Anthropic's own internal evals. None is independently replicated in this run.
- Anthropic's multi-agent research system is a read-heavy task with parallelisable search. Its results may not transfer to a sequential fiction pipeline, where Anthropic's own posts and Cognition both warn against parallel writing.
- Price and limit figures are snapshots from 2026-11-22.
- No conflicting sources were found on the caching or rate-limit mechanics.

## Not covered in this run (open gaps)
- Lost in the middle and long-context position effects (Liu et al., 2023).
- MT-Bench (Zheng et al., 2023) and full judge-bias results.
- LangGraph durable execution, CrewAI and AutoGen patterns (secondary; not fetched).
- Human-in-the-loop approval placement in production systems.
- Structured-output API features.
- Exponential backoff guidance beyond `retry-after`.
