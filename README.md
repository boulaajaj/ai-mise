# Harnessmith

**A governed workspace compiler.** Harnessmith converts raw project materials and user decisions into an auditable, versioned, agent-ready workspace — without ever allowing the agent to silently rewrite its own governing rules.

> Tell it what you do. It forges the AI workspace that helps you do it — and it can never quietly change the rules you gave it.

## Product boundary (one sentence)

Given a folder of real project materials, Harnessmith inspects it, asks a small number of justified questions, proposes an agent workspace in plain language, builds the approved version through a controlled transaction, and can restore any prior state exactly.

**Explicitly out of scope for the first release:** automatic self-improvement, SQLite, full wiki generation, multi-platform adapters, scheduled retrospectives, voice UX, marketplace distribution.

## The two planes

| | Control plane (`control-plane/`) | Data plane (`workspace-template/` → a user's workspace) |
|---|---|---|
| Owns | Authority: policy, approval, mutation gateway, validators | Work: sources, knowledge, views, skills, decisions, generated artifacts |
| Written by | The user, manually and rarely | The agent — but **only through the mutation gateway** |
| Trust stance | Outside the agent's writable area; protected by OS + Claude Code permissions | Everything here is replaceable, restorable, and generated |

The workspace's `CLAUDE.md`, hooks, and skills are **generated platform projections** compiled from the control plane's policy — never the authoritative constitution itself. This is what keeps the accumulated knowledge portable: swap the adapter, keep the workspace.

**Honesty note:** on a personal machine this boundary is protection against *accident and drift* — a confused or drifting agent — not against a determined adversary. A true security boundary requires OS-level sandboxing. The threat suite in `control-plane/threat-tests/` is scoped accordingly.

## The mutation gateway

Every persistent change follows one path:

```
Proposal → User approval of exact change set → Approval receipt
        → Stage in temporary worktree → Deterministic validators
        → Apply through gateway → Commit + restore tag + audit record
```

Approval covers a **transaction** (files, before/after hashes, plain-language purpose, risk category, validation results, rollback id, expiry) — not individual file operations. This is the design answer to approval fatigue: fewer approvals, each one meaningful.

## Knowledge has three layers

```
sources/     immutable evidence — originals + hashed manifests, append-only
knowledge/   atomic claims with provenance (source span, authority, status,
             confidence, valid-from/until, contradicts/supersedes links)
views/       rebuildable synthesis — wiki pages, reports; never the source of truth
```

A wiki page may say "the left ESC temperature spike is probably telemetry-related." The claim beneath it must say which log supports it, whether the user said it or the agent inferred it, and what superseded it. This prevents synthesis decay — AI summaries feeding AI summaries until nobody remembers the original fact.

## Non-technical surface (first-class requirement, every phase)

The person using a Harnessmith workspace never sees git, YAML, schemas, or hashes. They see: **Save Version · What Changed? · Safe Experiment · Keep It / Discard · Restore** — and proposals written in plain language. Any phase whose exit test can't be explained to a non-technical professional isn't done.

## Status

Phase 0 (contract + threat model) — **this repository is the Phase 0 deliverable**, plus the Phase 1 read-only inspector skeleton. See `HANDOFF.md` for the build sequence and next actions, `docs/architecture.md` for the full design, and `docs/history/blueprint-v1.md` + `docs/decisions/` for how we got here.

## The golden thread

The Arduino Digger project is the end-to-end test fixture from the first working week: every phase must improve the same run — inspect → constrain → ask → propose → build → perform a real task → absorb a correction → restore safely. The clean *generalization* test is the second pilot (a community-website domain), since Arduino doubles as the development fixture.
