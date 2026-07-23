# AI-Mise

**Your AI *mise en place*.** In a professional kitchen, *mise en place* means everything prepped, in its place, and ready before the cooking starts — so the chef can just cook. AI-Mise does that for AI: it converts raw project materials and your decisions into an auditable, versioned, agent-ready workspace — without you having to keep up with the latest AI setup, and without ever allowing the agent to silently rewrite the rules you gave it.

> Tell it what you do. It sets everything in place — and it can never quietly change the rules you gave it.

**The kernel:** [METHOD.md](METHOD.md) — one page that stays true regardless of platform, model, or decade. Everything else is an adapter.

## Product boundary (one sentence)

Given a folder of real project materials, AI-Mise inspects it, asks a small number of justified questions, proposes an agent workspace in plain language, builds the approved version through a controlled transaction, and can restore any prior state exactly.

**Explicitly out of scope for the first release:** automatic self-improvement, SQLite, full wiki generation, multi-platform adapters, scheduled retrospectives, voice UX, marketplace distribution.

## One assistant — you name it

This is the promise being built (see Status below for what runs today):
the person using AI-Mise meets exactly one thing — an assistant they name at
the first hello. Small help is applied at once and can always be undone;
changes to how the assistant works are announced in plain words and wait for
a good moment. Nobody is asked to switch modes, and words like "builder" or
"compiler" never reach them.

---

*Everything below this line is the mechanic's manual — how it works inside.
The person using AI-Mise never needs any of it.* Internally, the machinery
that changes the setup is separate from the machinery that does the work
([[ADR-0005-builder-vs-workspace|ADR-0005]], [[ADR-0008-no-modes-tiered-application|ADR-0008]]) — separation the user benefits from
without ever seeing.

## The two planes

| | Control plane (`control-plane/`) | Data plane (`workspace-template/` → a user's workspace) |
|---|---|---|
| Owns | Authority: policy, approval, mutation gateway, validators | Work: sources, knowledge, views, skills, decisions, generated artifacts |
| Written by | The user, manually and rarely | The agent — but **only through the mutation gateway** |
| Trust stance | Outside the agent's writable area; protected by OS + Claude Code permissions | Everything here is replaceable, restorable, and generated |

The workspace's `CLAUDE.md`, hooks, and skills are **generated platform projections** compiled from the control plane's policy — never the authoritative constitution itself. Swap the adapter, keep the workspace: that's the portability promise.

**Honesty note:** on a personal machine this boundary is protection against *accident and drift* — a confused or drifting agent — not against a determined adversary. A true security boundary requires OS-level sandboxing. The threat suite in `control-plane/threat-tests/` is scoped accordingly.

## The mutation gateway

Every persistent change follows one path:

```
Proposal → User approval of exact change set → Approval receipt
        → Stage in temporary worktree → Deterministic validators
        → Apply through gateway → Commit + restore tag + audit record
```

Approval covers a **transaction** (files, before/after hashes, plain-language purpose, risk category, validation results, rollback id, expiry) — not individual file operations. Fewer approvals, each one meaningful.

## Knowledge has three layers

```
sources/     immutable evidence — originals + hashed manifests, append-only
knowledge/   atomic claims with provenance (source span, authority, status,
             confidence, valid-from/until, contradicts/supersedes links)
views/       rebuildable synthesis — wiki pages, reports; never the source of truth
```

A view is never citable as evidence for a claim. This single rule prevents synthesis decay — AI summaries feeding AI summaries until nobody remembers the original fact.

## Non-technical surface (first-class requirement, every phase)

The person using an AI-Mise workspace never sees git, YAML, schemas, or hashes. They see: **Save Version · What Changed? · Safe Experiment · Keep It / Discard · Restore** — and proposals written in plain language. Any phase whose exit test can't be explained to a non-technical professional isn't done.

## Status

Phase 0 (contract + threat model) — **this repository is the Phase 0 deliverable**, plus the Phase 1 read-only inspector skeleton. See `HANDOFF.md` for next actions, `docs/architecture.md` for the design, `docs/prior-art.md` for what we deliberately reuse from other projects, and `docs/decisions/` for why the architecture is shaped this way.

## The golden thread

The Arduino Digger project is the end-to-end test fixture from the first working week: every phase must improve the same run — inspect → constrain → ask → propose → build → perform a real task → absorb a correction → restore safely. The clean *generalization* test is the second pilot (a community-website domain), since Arduino doubles as the development fixture.
