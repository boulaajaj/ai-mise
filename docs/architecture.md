# Harnessmith Architecture (v2)

This is the working architecture, superseding `docs/history/blueprint-v1.md` after external review. The review's corrections and the responses to it are recorded in `docs/decisions/` (ADR-0001..0004). Research grounding and sources live in blueprint-v1's source list; claims below are labeled **[verified]** (survived adversarial verification against primary sources), *[prior art]* (fetched and extracted, not adversarially verified), or *[default]* (a configurable product choice, not a research finding).

## 1. Framing

Harnessmith is a **governed workspace compiler**: input = raw project materials + user decisions; output = an auditable, versioned, agent-ready workspace. The compiler may be probabilistic; the governance may not be.

Three founding constraints, inherited from the original product vision:

1. The user may be non-technical. Plain language is the product surface, in every phase.
2. The workspace must outlive any one AI platform. Platform artifacts are generated projections.
3. The agent must never be able to silently rewrite its own governing rules.

## 2. Control plane / data plane

### Control plane (`control-plane/`) — authority and enforcement

```
control-plane/
├── constitution/          # policy.yaml (user-owned) + schema
├── approval/              # proposal/receipt schemas + append-only receipt store
├── mutation/              # the gateway: stage / validate / apply / restore
├── validation/            # deterministic validators (path, frontmatter, link, provenance)
├── evaluation/            # capability + regression eval suites, baselines
├── threat-tests/          # attempted-bypass scenario suite
└── adapters/
    └── claude-code/       # compiles policy → CLAUDE.md, .claude/rules, settings, hooks
```

Installed **outside** any generated workspace. Protected by OS permissions and Claude Code permission deny-rules; normal editing tools are denied write access. Rationale: CLAUDE.md is context, not authority [verified — Anthropic: "context, not enforced configuration"], and a hook that lives in the same writable tree it protects is a circular defense (ADR-0001).

**Scope honesty:** this is a *drift-and-accident* boundary, not an adversarial security boundary. True guarantees require sandboxing. Threat tests are scoped to bypass-by-confused-agent, which is the realistic risk.

### Data plane (a generated workspace)

```
workspace/
├── workspace.yaml         # identity + configuration
├── sources/               # immutable inputs + hashed manifests (append-only)
├── knowledge/
│   ├── claims/            # atomic claims with provenance (see §4)
│   ├── concepts/          # OKF-style concept pages
│   └── relationships/
├── views/
│   ├── wiki/              # index.md, log.md, topic pages — rebuildable
│   └── reports/
├── memory/                # governed memory (see §7 auto-memory note)
├── skills/
├── decisions/
│   ├── records/           # lightweight decision notes
│   └── ADR/               # full ADRs (rare; see documentation tiers §6)
├── evaluations/
├── generated/
│   └── claude-code/       # CLAUDE.md, .claude/rules/, settings.json, projected skills
├── changes/
│   ├── proposals/  approvals/  manifests/
└── ops/
    └── index.db           # optional, derived, rebuildable, never in git
```

`generated/claude-code/` is one adapter output. Future adapters (codex, generic-markdown) read the same neutral workspace. This directory structure *is* the portability thesis, enforced.

## 3. The mutation gateway

An agent can mutate files via Write/Edit, bash, git, python/node, MCP filesystem tools, renames, symlinks, parent-directory replacement, permission changes, or by editing the protection scripts themselves. Blocking individual tools is whack-a-mole. Instead, **one gateway** and a protected-path validator:

```
Proposal → User approval (exact change set) → Approval receipt
        → Stage in temporary worktree → Deterministic validators + evals
        → Apply through gateway → Commit + restore tag + audit record
```

A transaction carries: affected files, before/after hashes, plain-language purpose, risk category, validation results, rollback identifier, approval expiry. Approval is per-transaction, not per-file-operation — the design response to the documented ~93% approval-fatigue rate *[prior art — Anthropic engineering]*.

Enforcement layers (defense in depth, weakest to strongest): generated instructions → PreToolUse hooks (fire regardless of model judgment [verified]) → Claude Code permission deny-rules → OS file permissions. Hooks alone are not a complete boundary; the stack is the design.

Rollback covers **rules and memory together** — reverting a rule does not undo memory written under it (the ratchet problem: ~68% of behavioral drift survived a rule revert in one study *[prior art]*), so restore tags snapshot the full governed tree, and `restore-change` must reproduce exact directory hashes.

## 4. Evidence → claims → views

Three layers, strict direction of derivation (ADR-0002):

- **sources/** — originals, never edited; manifests with SHA-256 hashes, append-only.
- **knowledge/claims/** — atomic claims: id, source reference or span, authority (user-stated | agent-inferred | external-source), status, confidence, valid-from/until, contradicts/supersedes links.
- **views/** — wiki and reports, rebuildable from claims at any time. A view is never cited as evidence for a claim (this single rule prevents synthesis decay).

Conventions: OKF-compatible frontmatter for knowledge and views (minimal `type` field, `index.md`, `log.md`) *[prior art — Google OKF v0.1, June 2026; early, deliberately minimal]*. OKF governs file shape only — it does not replace evidence handling or change governance.

Provenance targets *[default]*: 100% of safety-critical claims traceable; ≥95% of other factual claims.

## 5. Placement rubric

| The knowledge is… | It becomes… |
|---|---|
| Needed every session; user-ratified fact/convention/always-never | Constitution entry → projected into generated CLAUDE.md (<200 lines total [verified]) |
| Multi-step procedure used repeatedly | Skill (<500-line SKILL.md, references one level deep, trigger description with negative examples [verified]) |
| Must happen/never happen regardless of model judgment | Hook (narrow, deterministically checkable) + permission rule [verified mechanism] |
| Side-effecting action needing human timing | Slash command *[prior art]* |
| Fixed sequence, no judgment | Script (source never enters context merely by running; output still costs tokens [verified, qualified]) |
| Growing domain knowledge | Memory topic file behind an index [verified pattern] |
| Explanation/navigation/rationale | View (wiki page) *[prior art — Karpathy]* |
| Structured operational state | index.db — derived, rebuildable, never authoritative *[prior art]* |
| Record of a persistent change | Manifest / decision note / ADR per documentation tiers (§6) |

Meta-rules: ambiguity resolves to the **less powerful** home, or to an explicit "ambiguous — ask" outcome; every placement is logged; placement quality is measured as **cost-weighted precision and recall** (a false trigger and a missed trigger have different costs), not a single accuracy number.

## 6. Documentation tiers (anti-noise)

| Change | Record |
|---|---|
| Routine approved content update | Transaction manifest + git commit |
| Meaningful workflow/knowledge-structure change | Decision note (`decisions/records/`) |
| Long-lived architectural, governance, or safety decision | Full ADR (`decisions/ADR/`) |

Every artifact is inventoried automatically; narrative wiki pages exist only for concepts that need explanation. `index.md` is a map, not a museum catalog.

## 7. Lifecycle

1. **Acquire** — snapshot sources, hash, manifest, preserve originals.
2. **Inspect** — read-only subagent → detected purpose, stakeholders, constraints, repeated activities, safety-critical information, conflicts, unknowns, candidate capabilities.
3. **Ask** — only decision-changing questions. Each question states: the unresolved decision, possible answers, what artifact/behavior changes, cost of a wrong assumption. Stop when no unanswered question could materially change a high-risk placement, behavior, or workflow *[grounded in information-gain clarification research — prior art]*. Remaining unknowns become a visible assumptions ledger.
4. **Compile proposal** — what was learned, what will be generated, where each item lives, what will be enforced, what remains uncertain, what will deliberately *not* be built.
5. **Approve** — one transaction, accept/reject/modify.
6. **Stage & validate** — isolated worktree; deterministic validators before touching the live workspace.
7. **Commit + receipt** — receipt links proposal, approved scope, result hashes, validation evidence, restore point.
8. **Operate** — real tasks; record corrections and friction; do **not** immediately persist rules from single corrections.
9. **Retrospect (shadow mode initially, ADR-0003)** — classify repeated evidence, generate proposals, predict which eval should improve, apply **nothing** automatically. Graduation to prepared executable change-sets only after ~20–30 real sessions with stable regression tests *[default]*.
10. **Trajectory review** — periodically (*[default]* every 10th retrospective or monthly): "Would the user approve the complete present-day system if proposed all at once?" Counters compositional drift *[prior art]*.

Claude Code auto-memory note: native auto-memory lives outside the repo under `~/.claude/projects/.../memory` — during Harnessmith-controlled sessions it must be disabled or redirected into `workspace/memory/`, or rollback is incomplete.

## 8. Evaluation scorecard

| Area | Initial success criterion |
|---|---|
| Governance | Zero protected-path bypasses across the threat suite |
| Auditability | Every persistent mutation has an approval receipt + result hashes |
| Rollback | Restore reproduces the exact governed file tree (hash-identical) |
| Provenance | 100% safety-critical / ≥95% factual claims traceable |
| Placement | Cost-weighted precision & recall, including "ambiguous — ask" |
| Interview | Every question demonstrably changes a construction decision |
| Skill routing | Separate TP / FP / FN measurement (no single trigger-rate number) |
| Utility | Better completion / fewer corrections than both plain `/init` and the manual Arduino baseline |
| Improvement | Accepted retrospective changes improve their predicted eval without breaking regressions |
| Portability | Core workspace fully understandable with no Claude-specific tooling |

Two eval tiers throughout: capability evals (improvement frontier) and regression evals (do-not-break floor).

## 9. Build sequence

- **Phase 0 — Contract + threat model** (this repo): product boundary, canonical schemas, protected-asset list, ≥30 bypass scenarios, baselines (plain `/init` run + the manual Arduino workspace). Exit: you can state exactly what is authoritative, what is generated, and which process may change each item.
- **Phase 1 — Read-only bootstrapper**: source inventory, inspector subagent, unknowns ledger, decision-aware questions, workspace proposal. No writes, no wiki, no SQLite, no self-improvement. Exit: it examines the Arduino materials and produces a proposal you would seriously consider approving.
- **Phase 2 — Governed construction**: transaction format, receipts, scaffold scripts, validators, git commit/restore, protected-path enforcement. Exit: unauthorized writes fail, approved writes succeed, restore reproduces exact hashes.
- **Phase 3 — Claude Code adapter**: minimal CLAUDE.md, path-scoped rules, 1–2 useful skills, hooks + permissions, auto-memory redirect. Pin and wrap upstream skill-creator; fork only when composition can't deliver a required change. Exit: the Arduino workspace performs a useful task better than plain `/init`, without violating protected paths.
- **Phase 4 — Evidence-backed knowledge**: source manifests, claims with provenance, OKF-compatible concepts/views, citation-coverage validation, local contradiction checks. Exit: every important factual/safety claim traces to a source, user decision, or explicit inference.
- **Phase 5 — Retrospective shadow mode**: correction collection, proposal generation, rejection learning, predicted eval impact, no automatic application. Exit: accepted proposals improve measured performance; rejected proposals stop recurring.
- **Phase 6 — Controlled self-improvement + second pilot**: executable diffs behind transaction approval; then a very different domain (community-website management) as the true generality test.

The **Arduino golden thread** runs through every phase: the same end-to-end scenario must get better each week, so the platform never becomes sophisticated scaffolding around an empty lot.
