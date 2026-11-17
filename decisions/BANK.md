# BANK: Patrick's rulings waiting for the next pass

**The pass of 2026-11-16/17 is done.** Everything banked from Oct 31 to Nov 17 went into the codex as R001–R147 (`decisions/RULINGS.md`). The old bank is kept word for word in `decisions/BANK_passed_2026-10-31_to_11-17.md`. Its process and engine rules still apply:
- Claude drafts the prose from Patrick's ideas, and his lines are protected.
- Ignore anything an AI added that Patrick didn't approve.
- Draft beat by beat, with the sense-checker, payoff-keeper and dialogue-editor.
- "freedom": Claude makes the story calls itself and asks only on world-level clashes.

**Open world questions** (26) are in `codex_v5/NEEDS_PATRICK.md` under "Pass 2026-11 · open calls". They block nothing.

## New since the pass
*(none yet)*
- 2026-11-17 · [ENGINE · seed density] Patrick: "You cant have 24 seeds in chapter 1 dude" → per chapter, keep about 6 Book 1 seeds and up to 3 light future-book seeds. Everything else is plain texture, mentioned once with no lingering. The payoff-keeper enforces this cap.
- 2026-11-17 · [ENGINE · outside readers] Patrick: "Im trusting you to know when grok has good ideas and whats settled. Your the author. These are just notes not hard requirements. Just consider it one of yiur agents. They have a job. Note taker and outsider reader. So you still get ultimate authority if you like it or not" (Grok and other outside readers are advisory, like any agent. Claude, as author, decides what to take. Canon and Patrick's words still win.)
- 2026-11-17 · [ENGINE · word choice] Patrick: "Another read of the old story from a new window showed some interesting notes about word usage being over done also. Maybe a new agent needs to run a word choice pass to make sure its varied" → built the `word-watch` agent and `scripts/wordcheck.py`. The outside read's counts: "didn't" 94, "Nobody" 54, "a long time" 17 across the 19k book. It also said "expand with scenes, not connective tissue"; expand Teo first; chapter 6's lord's ship. Notes in `stories/book1-emperors-son/v3/outside_reads.md`.
- 2026-11-17 · [ENGINE · v2] Patrick: "Maybe do some external research on like what the absolute bros of ai writing do. We need every check they make. Every agent they use. Each type of tool they use. Like lets build the absolute top end agentic pipeline we can" → `work/PIPELINE_V2.md`. New agents: `character-sim`, `forecaster`, `reader-panel`. `continuity-keeper` upgraded (5-category taxonomy, both passages quoted, Knowledge table). Added `scripts/slop_list.txt`, style anchors and provenance. Story skill: Pipeline v2.
- 2026-11-17 · [Book 1 · pacing] Patrick: "Id like you to split this into 2 parts and fill them in. Some of the pacing is still to fast. Maybe we do chapter 1 as a slower introduction and chapter 2 as the sort of quickening part into the underground" → `stories/book1-emperors-son/v3/split_plan.md`.
- 2026-11-17 · [Book 1 · Vosk's speech] Patrick on "I'm proud to die for the man that boy grew into": "It can be eloquent but also broken" → keep the eloquent content and words, but let breath and the body break the sentence (pauses, a restart, a word lost and found). It isn't delivered whole and clean.
