# harnessmith — development harness

This repo builds a governed workspace compiler. It governs its own development
the same way: this file is the *projection* of the authoritative docs below —
if they conflict, the docs win.

## Non-negotiable rules

- NEVER edit `control-plane/constitution/policy.yaml`. It is user-owned. Propose changes in conversation; Amine applies them by hand.
- NEVER edit files under `docs/decisions/` — ADRs are append-only; supersede with a new ADR.
- Design changes require a decision record in `docs/decisions/` before or with the implementing commit.
- Label design assertions [verified] / [prior art] / [default] (ADR-0004). Product-choice numbers live in policy.yaml, never hardcoded in prose or code.
- Plain-language surface is an exit criterion of every phase: if a non-technical professional couldn't understand the output, the phase is not done.
- Do not start a phase until the previous phase's exit test passes (phases and exit tests: `docs/architecture.md` §9).

## Read before working

- `docs/architecture.md` — the design (v2, authoritative)
- `HANDOFF.md` — current state, next actions, ground rules
- `docs/meta/dev-harness.md` — how this repo evolves itself (retrospectives, proposals)
- `docs/history/blueprint-v1.md` — superseded; kept for the research source list

## Conventions

- Python: stdlib-first, no dependencies unless an ADR justifies one; validators print a JSON result object and use exit codes 0/1/2 (see `protected_path_validator.py` as the pattern).
- Threat scenarios: new bypass ideas are added to `control-plane/threat-tests/scenarios.md` *before* being tested.
- Commits: reference the issue; one coherent change per commit.
- Skills follow the platform limits recorded in policy.yaml (`placement.limits`).

## Self-evolution (dogfooding)

After each working session, append a dev-retrospective entry per
`docs/meta/dev-harness.md`. Improvements to this repo's own harness (this file,
the skills, the validators, the process) are proposed as issues labeled
`meta-harness` and land like any other change — reviewed, recorded, reversible.
This file stays under 200 lines, per our own rubric.
