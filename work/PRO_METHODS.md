# How others use AI for fiction, and what we adopt (2026-11-09)

## Sources
- **Agents' Room** (Google DeepMind, ICLR 2025): planning agents (character, conflict, plot, setting) write to a shared scratchpad. Writing agents then draft each section, and an orchestrator coordinates. Human readers preferred its stories over single-pass baselines.
- **Novelcrafter's workflow** (the tool Patrick's old codex was compiled for): codex (story bible, one entry per subplot) → chapter and scene summaries → scene beats (often 6+ per scene: who is there and what they do) → prose.
- **Author revision loops** (practitioner reports): developmental edit → line edit → a separate beta-reader prompt (catches pacing and structure) → reverse outline; fact-check every chapter against the bible. AI can't judge whether a scene works emotionally; that needs human readers.
- **Craft frameworks** (Claude's own knowledge, not from this search):
  - Swain's scene/sequel: goal, conflict, disaster / reaction, dilemma, decision
  - Story Grid's five beats per scene, with a value shift
  - Sanderson's promises, progress, payoffs
  - Weiland's want, need, ghost, lie (already in use)

## What we already do
- story bible / codex
- a canon checker
- adversarial critics
- line edits and polish
- a story guard and a consistency check
- outside readers (Grok, a fresh Claude, Patrick)

## Gaps to adopt
1. **A planning layer before prose** (Agents' Room). Character dossiers, a conflict map and relationship vectors, before any drafting. This is the story-layer work Patrick asked for.
2. **Scene cards** (Swain + Novelcrafter beats). Every scene gets a goal, a conflict and a disaster (or a reaction, dilemma and decision), plus its value shift. This structurally fixes "the characters cooperate with the plot": every scene must contain a failure or a hard choice.
3. **A promise/payoff ledger** (Sanderson). Every setup gets a tracked payoff, and every payoff a setup.
4. **A reverse outline after each draft:** what each scene actually does, compared with the card.
5. **A cold beta reader:** an agent with NO codex access, reading like a stranger.
6. **Human readers for emotional truth:** Patrick, plus outside AIs as extra eyes.
