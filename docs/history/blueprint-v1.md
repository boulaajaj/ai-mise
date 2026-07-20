# Workspace Bootstrapper — Architecture Blueprint & Build Plan (v1 — SUPERSEDED)

> **Status: superseded by `docs/architecture.md` (v2) after external review, 2026-07-20.**
> Kept for history and for the research source list below. The review's corrections
> are recorded in `docs/decisions/ADR-0001..0004`. Do not build from this document.

**For Amine — July 20, 2026.** Target platform: Claude Code / Cowork. Governance stance: every persistent change requires explicit approval. First validation: the fresh-workspace Arduino Digger comparison test.

Built from a deep research pass (24 sources fetched, 120 claims extracted, 25 adversarially verified). **[verified]** = survived adversarial verification; *[prior art]* = fetched and extracted, not adversarially verified.

## Key verified findings (summary)

- **Placement rubric (partial, first-party):** every-session facts → CLAUDE.md under 200 lines (adherence degrades beyond); multi-step procedures → skills or path-scoped rules; guarantees → PreToolUse hooks (CLAUDE.md and memory are context, not enforcement).
- **Progressive disclosure is a spec:** ~100-token frontmatter always loaded; SKILL.md body (<500 lines / ~5k tokens) on trigger; bundled resources zero-cost until read; references exactly one level deep (nested chains cause partial reads).
- **Interview-and-inspect precedent:** `/init` with `CLAUDE_CODE_NEW_INIT=1` runs ask-which-artifacts → explore with subagent → follow-up questions → reviewable proposal before writing files.
- **Skill quality is measurable:** eval-first authoring (≥3 scenarios before writing docs, no-skill baseline, cross-model testing); skill-creator benchmark mode; description optimization improved triggering on 5 of 6 Anthropic document skills. (The 90% trigger figure and 73→85 routing figure were later downgraded — see ADR-0004.)
- **Memory pattern:** MEMORY.md index (first 200 lines / 25KB auto-loaded) + topic files read on demand.
- **Auto-memory location:** native auto-memory lives outside the repo; must be redirected for complete rollback.

## Key prior-art findings (summary)

- **Self-modification risks:** compositional drift (sequences of reasonable approved changes accumulating into unauthorized behavior → trajectory reviews needed); ratchet problem (~68% of behavioral drift survived a rule revert in one study → version memory with rules); optimizer-optimizee collapse (safety mechanisms inside the loop become optimization targets → constitution outside the loop); approval fatigue (~93% approval rate → batched transaction-level approval).
- **Working retrospective implementations:** BerriAI/self-improving-agent (PR-gated proposals; diff rejected unless target snippet matches exactly once; Claude Agent SDK support) and claude-improve (six-phase pipeline; nine feedback signal types; accept/reject/modify one at a time; meta-learnings file so rejected proposals do not recur).
- **Stopping problem:** no off-the-shelf answer; models learn spurious stopping proxies (dialogue length, confident tone); over-asking degrades results. Design response: questions must justify themselves by decision impact; explicit assumptions ledger; round caps. Information-gain clarification research supports asking only when belief would shift.
- **Memory substrate:** markdown as source of truth, SQLite as derived rebuildable index (memweave); files win for single-user transparency, databases only for concurrency/scale (Oracle analysis).
- **Wiki:** Karpathy LLM-wiki gist — interlinked markdown wiki, index.md + append-only log.md, periodic lint for contradictions/staleness/orphans; assign bookkeeping to the LLM.
- **Invisible git:** Bolt (plain-language rollback, documented ceiling, two-tier round-trip to real GitHub) and Abstract (kept git concepts, GUI re-presentation, deliberately lossy).
- **Reliability:** scripts for anything deterministic; verify early; assert on structured artifacts, not free text; two eval tiers (capability + regression); harness-only engineering moved a coding agent from rank 30 to top 5 on a public benchmark.

## v1 build plan (superseded by architecture.md §9)

Phase 0 study → Phase 1 placement rubric + scripts → Phase 2 interview engine → Phase 3 wiki + invisible git → Phase 4 retrospective loop → Phase 5 eval harness → Phase 6 Arduino experiment. The review moved Arduino to a golden thread from week one, demoted the wiki behind the claims layer, split control/data planes, and put self-improvement in shadow mode.

## Sources

**Verified (adversarial pass):**
Anthropic skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices · Agent Skills overview — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview · Equipping agents for the real world — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills · Complete Guide to Building Skills (PDF) — https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf · anthropics/skills repo + skill-creator — https://github.com/anthropics/skills · Claude Code memory docs (CLAUDE.md, MEMORY.md, /init) — https://code.claude.com/docs/en/memory · Hooks guide — https://code.claude.com/docs/en/hooks-guide · Steering Claude Code (placement rubric blog) — https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more

**Prior art (fetched and extracted, not adversarially verified):**
Karpathy, LLM knowledge bases gist — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f · Google Open Knowledge Format spec — https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md · memweave (markdown + SQLite memory) — https://towardsdatascience.com/memweave-zero-infra-ai-agent-memory-with-markdown-and-sqlite-no-vector-database-required/ · Oracle, files vs databases for agent memory — https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management · BerriAI/self-improving-agent — https://github.com/BerriAI/self-improving-agent · claude-improve — https://github.com/TerenceBristol/claude-improve · Compositional drift / mutable-layers paper — https://arxiv.org/html/2604.14717v2 · Self-evolving agent threat matrix — https://arxiv.org/pdf/2606.23075 · CaRT: knowing when to stop asking — https://arxiv.org/html/2510.08517v1 · Information-gain clarification — https://arxiv.org/abs/2606.03135 · Improving skill-creator (evals/benchmarks) — https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills · Agent harness survey — https://arxiv.org/html/2605.18747v1 · Agent behavioral consistency study — https://arxiv.org/html/2605.28840 · Bolt version history docs — https://support.bolt.new/concepts/version-history-github · Abstract (git for designers) — https://blog.prototypr.io/git-repository-for-designers-abstract-sketch-9138cf6ab9b1 · Slash commands vs skills vs hooks rubric — https://blog.laozhang.ai/en/posts/claude-code-hooks-slash-commands-skills · awesome-harness-engineering — https://github.com/ai-boost/awesome-harness-engineering
