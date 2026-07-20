# Handoff — continuing Harnessmith in Claude Code

This repo is the Phase 0 deliverable (contract + threat model) plus the Phase 1
read-only inspector skeleton. This file tells a Claude Code session (or you)
exactly how to push it and what to do next.

## 0. GitHub setup — one command (first action)

```bash
cd harnessmith
bash setup/setup-github.sh
```

The script is idempotent: it creates the private repo (if missing), pushes
main, and creates all 7 phase milestones, labels, and 19 tracking issues with
full bodies and milestone assignments. Requires `gh` authenticated with repo
scope. Re-running never duplicates milestones or issues.

## 0.5 This repo governs itself

harnessmith is self-hosting: read `CLAUDE.md` (the dev-harness rules) and
`docs/meta/dev-harness.md` (how this repo evolves under its own governance —
shadow-mode retrospectives in `docs/meta/retro-log.md`, `meta-harness` issues,
periodic trajectory reviews). End every working session by appending a
retro-log entry. Every gap we hit in our own process is product intelligence.

## 1. Ground rules for every future session

- `control-plane/constitution/policy.yaml` is user-owned. No agent edits it. Ever. Propose changes in conversation; Amine applies them by hand.
- Design changes require a decision record in `docs/decisions/` (see ADR-0001..0004 for the format and for why the architecture is shaped this way).
- Claim hygiene (ADR-0004): label design assertions [verified] / [prior art] / [default]. Numbers that are product choices go in policy.yaml, not prose.
- The plain-language surface is a first-class exit criterion in every phase. If a non-technical professional couldn't understand the output, the phase isn't done.
- Read `docs/architecture.md` before writing code. `docs/history/blueprint-v1.md` is superseded context, kept for the research source list.

## 2. Current state

| Piece | State |
|---|---|
| Product boundary, planes, lifecycle, scorecard | `docs/architecture.md` (v2, post-review) |
| Authoritative policy + configurable defaults | `control-plane/constitution/policy.yaml` |
| Transaction schemas | `control-plane/approval/*.schema.json` |
| Threat suite | 34 scenarios defined, 0 automated (`control-plane/threat-tests/scenarios.md`) |
| First validator | `protected_path_validator.py` — working; self-tested against traversal, protected paths, symlinks, tier smuggling |
| Inspector skill (Phase 1) | `skills/inspector/` — SKILL.md + working `inventory.py` (hashing, symlink-refusing) |
| Dev harness (self-hosting) | `CLAUDE.md`, `docs/meta/dev-harness.md`, `docs/meta/retro-log.md` |
| Mutation gateway, adapters, evals | Directories exist; not implemented (Phase 2–3) |

## 3. Phase 0 — remaining items (do these first)

1. **Baselines** (needs Amine's machine): run plain `/init` (try `CLAUDE_CODE_NEW_INIT=1`) on the Arduino Digger repo; snapshot the output. Snapshot the manually built Arduino workspace as the second baseline. Store both under `control-plane/evaluation/baselines/` (or record paths if too large).
2. **Validate the schemas**: write 3 example proposals (routine / structural / safety) and 2 receipts; check them against the schemas with a JSON-schema validator; fix schema friction now, not in Phase 2.
3. **Policy schema**: write `control-plane/constitution/policy.schema.json` and validate policy.yaml against it.

Phase 0 exit: you can state exactly what is authoritative, what is generated, and which process may change each item. (The architecture doc states it; the baselines make it testable.)

## 4. Phase 1 — read-only bootstrapper (next build work)

Build order:
1. Run the inspector skill against the real Arduino Digger materials (golden thread starts here — week one, per the review).
2. Iterate on findings quality: every finding must cite manifest paths; safety-critical constraints (ESC temperatures, current limits, mechanical stops) must surface prominently.
3. Implement the unknowns ledger → four-part question contract → assumptions ledger flow exactly as `skills/inspector/SKILL.md` specifies; enforce the round cap from policy.yaml.
4. Produce `proposal.md` and show it to Amine.

Phase 1 exit: the proposal is good enough that Amine would seriously consider approving it. No writes, no wiki, no SQLite, no self-improvement.

## 5. Phase 2 preview (do not start until Phase 1 exit passes)

Mutation gateway (`stage-change`, `validate-change`, `apply-change`, `restore-change` in `control-plane/mutation/`), remaining validators (frontmatter, link, provenance, path — reuse `protected_path_validator.py` as the pattern), receipt issuance, and automation of the 34 threat scenarios. Phase 2 exit: unauthorized writes fail, approved writes succeed, restore reproduces exact directory hashes.

## 6. Known open questions (inherited, unresolved)

- Interview stopping quality is the least-grounded area of the whole design — expect Phase 1 iteration.
- Anthropic platform guidance moves fast (200-line CLAUDE.md figure is from June 2026; `CLAUDE_CODE_NEW_INIT` is env-gated). Thresholds live in policy.yaml so drift is a one-line fix.
- Auto-memory redirect mechanics (policy `platform.claude_code.auto_memory`) need a concrete implementation in Phase 3.
