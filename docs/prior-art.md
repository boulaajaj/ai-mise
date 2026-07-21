# Prior-art watchlist — repos moving in our direction

**Purpose:** projects that already learned something by trial and error that we should reuse or copy rather than rediscover. Reviewed 2026-07-20. Re-check quarterly (the standing meta-harness issue is the reminder). Convention: each entry says what they built, how reputable, and *exactly what we take*.

**The strategic read:** the field splits into harness *runtimes* (many, some huge) and harness *generators* (few, small). Nobody found combines: generation + enforced governance + provenance + a non-technical surface. That combination remains our lane. The April 2026 snapshot repo states it plainly: "most projects function as harness runtimes rather than harness generators."

---

## Tier 1 — direct overlap, study before building the corresponding phase

### revfactory/harness — the closest generator (~3.6k stars)
A meta-skill that turns a domain description into a complete agent team: domain analysis → team architecture → agent definitions → skill generation → integration → validation, choosing from six architectural patterns (pipeline, fan-out/fan-in, expert pool, producer-reviewer, supervisor, hierarchical delegation). Author-measured +60% quality in A/B tests (unreplicated).
**Take:** the six architectural patterns as composition templates for generated workspaces; the six-phase generation pipeline as a checklist against our Phase 1–3 flow. **What it lacks (our lane):** no approval gateway, no provenance, no rollback, aimed at developers.
**Phase relevance:** 1, 3.

### aiming-lab/AutoHarness — governance pipeline (~337 stars)
Governance framework wrapping every tool call: parse/validate → risk-classify → permission check → execute → sanitize → audit. YAML constitution, risk pattern matching (secrets, path traversal, dangerous ops), per-agent permission profiles, JSONL audit trail, cost attribution.
**Take:** the 6-step per-call pipeline as the inner loop of our mutation gateway; their risk patterns as seed rules for our validators; JSONL audit format. Their YAML-constitution convergence independently validates our policy.yaml design.
**Phase relevance:** 2.

### HKUDS/OpenHarness — the reputable runtime (~14.8k stars, University of Hong Kong)
Full harness runtime + personal agent (ohmo): markdown skills compatible with anthropics/skills, MEMORY.md persistence, layered permissions (path rules, command filtering, pre/post hooks, approval dialogs), subagents, plugin architecture.
**Take:** their layered permission framework as reference for our adapter's generated settings; their skill-discovery hierarchy. **Strategic:** the strongest candidate for a *second adapter target* someday — compiling the same workspace to OpenHarness would prove the portability thesis against a non-Anthropic runtime.
**Phase relevance:** 3, and the future portability milestone.

### tigerless-labs/autoharness — shadow-mode learning, implemented (~18 stars)
Self-learning skill layer for Claude Code: capture (with redaction) → reflect (add/merge/patch/remove decisions) → **promoter as the sole writer** → daemon-free lifecycle ranking by real usage → per-skill ledger recording why each skill was created/changed. Validates "through adherence in use" rather than benchmarks.
**Take:** promoter-as-sole-writer is our gateway principle independently reinvented — copy their atomic-write discipline; the per-skill ledger maps to our decision notes; usage-frequency pruning is the answer to skill sprawl we hadn't designed yet. Small project, but the mechanics are exactly our Phase 5.
**Phase relevance:** 5.

## Tier 2 — specific mechanisms worth lifting

### ruvnet/metaharness (~185 stars, prolific maintainer, 18+ npm packages)
Scaffolds branded harnesses with CLI, MCP server, memory, learning loop. Two standout mechanisms: **witness-signed releases** (Ed25519-signed manifest attestation, byte-deterministic across CI) and **default-deny MCP policy** with a static `mcp-scan` threat check.
**Take:** signing our approval receipts and restore tags (Ed25519 over the receipt JSON) would make the audit trail tamper-evident — a cheap, large upgrade to Phase 2. Default-deny tool policy belongs in the generated settings projection.

### kayba-ai/autoharness (~19 stars)
Closed-loop harness optimization: proposal backends → benchmark each candidate → champion/challenger promotion → persistent resumable campaigns.
**Take:** the champion/challenger benchmark loop is precisely the graduation mechanism our Phase 6 needs — a self-improvement change must beat the current champion on evals before it may even be *proposed* for approval.

### Already in our ADRs (recorded earlier, listed for completeness)
- **BerriAI/self-improving-agent** — PR-gated self-modification; exact-match diff guard (ADR-0003 lineage).
- **TerenceBristol/claude-improve** — six-phase retrospective, nine feedback signal types, rejection memory (ADR-0003 lineage).
- **anthropics/skills** — skill-creator, spec, templates; we pin and wrap (issue #14).

## Tier 3 — context and radar (not competitors)

Runtimes that show where the ecosystem is going, useful as adapter targets or pattern sources, not as models to copy: **bytedance/deer-flow** (~57k stars, long-horizon SuperAgent), **langchain-ai/deepagents** (~19k stars, planning + subagents on LangGraph), **aden-hive/hive** (~10k stars, outcome-driven with human oversight), **code-yeongyu/oh-my-openagent** (~48k stars, multi-provider abstraction).

Curated lists to re-check quarterly for new generators: **danielrosehill/AI-Harnesses** (point-in-time snapshots), **ai-boost/awesome-harness-engineering**, **RyanAlberts/best-of-Agent-Harnesses** (rescored weekly).

---

## Reuse decisions to file as issues

1. Adopt AutoHarness-style per-call pipeline stages inside the mutation gateway (Phase 2 issue).
2. Sign approval receipts + restore tags, metaharness-style Ed25519 (Phase 2 issue).
3. Champion/challenger eval gate for graduated self-improvement, kayba-style (amend Phase 6 issue).
4. Usage-frequency skill pruning + promoter-as-sole-writer, tigerless-style (amend Phase 5 issue).
5. Evaluate revfactory's six architecture patterns as workspace composition templates (Phase 1/3 issue).
6. Long-term: OpenHarness as second adapter target to prove portability (backlog issue).

## Links

revfactory/harness — https://github.com/revfactory/harness · aiming-lab/AutoHarness — https://github.com/aiming-lab/AutoHarness · HKUDS/OpenHarness — https://github.com/HKUDS/OpenHarness · tigerless-labs/autoharness — https://github.com/tigerless-labs/autoharness · ruvnet/metaharness — https://github.com/ruvnet/agent-harness-generator · kayba-ai/autoharness — https://github.com/kayba-ai/autoharness · BerriAI/self-improving-agent — https://github.com/BerriAI/self-improving-agent · claude-improve — https://github.com/TerenceBristol/claude-improve · anthropics/skills — https://github.com/anthropics/skills · AI-Harnesses snapshot — https://github.com/danielrosehill/AI-Harnesses · awesome-harness-engineering — https://github.com/ai-boost/awesome-harness-engineering · best-of-Agent-Harnesses — https://github.com/RyanAlberts/best-of-Agent-Harnesses
