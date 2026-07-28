# A second brain that works with you — not one more thing to learn

Before any real work I kept running the same loop by hand: find the current
research, find whoever already solved this, learn which methods actually
hold, then search the same idea under four different names because the good
answer was filed under the fourth. Then I noticed I was running it
identically every time. If I go looking for *how to research*, there's a
pattern in there — empirically proven, repeatable, obeying the same laws
everything else obeys. A pattern like that can be written down once. And
once it's written down, I shouldn't be the one running it by hand.

That's all this is: a process that runs in my head as me, Amine Boulaajaj,
that I'd rather stop re-running manually.

> Tell it what you do. It sets everything in place — and it can never quietly
> change the rules you gave it.

## Who it's for

People with one brain and a lot on it — a family, a job, real work — who
want to use AI seriously and have no interest in becoming an AI engineer to
do it. You shouldn't need to know what an MCP server is, how model memory is
layered, or what an Agent Skill does. That's a profession. It isn't yours.

Using AI well takes separate contexts that don't bleed into each other, and
skills that do things your way rather than the average way. Building that is
a job — the harness engineer, the information organizer, the researcher, the
PhD in whatever you need this week. This does that job, and none of them
need managing.

## The tools keep moving

Prompting. Then MCP servers, so you stop pasting API documentation at a model
that would rather be told once. Then Agent Skills, which at my day job went
from a curiosity to something we can't work without — next to hooks, prompts,
decisions recorded as issues, architecture written down where an agent will
find it. That is what keeps our agents organized and the application running.

They'll keep moving, fast. The pattern underneath doesn't: know what's true,
learn from whoever did it before you, write down the minimum that makes the
work repeatable, treat every correction as evidence. That pattern is one
page — [METHOD.md](METHOD.md). Everything else, including whichever platform
wins this year, is an adapter.

## What it does

Works out what you're doing — from your materials when you have them, from
the conversation when you don't — asks the few questions whose answers change
the outcome, describes in plain language the setup it would build, builds
only what you approve, and can put anything back exactly as it was.

You meet one assistant, named by you at the first hello. Small help lands
immediately and is always undoable; anything that changes how the assistant
itself works is announced in plain words and waits for a good moment. No
modes to switch between, and no vocabulary to learn.

*That is the promise being built — [Status](#status) is what runs today.*

**Not in the first release:** self-improvement, SQLite, wiki generation,
multi-platform adapters, scheduled retrospectives, voice, marketplace
distribution.

## Guardrails, honestly

Your rules are written down, versioned, and can't be edited by the thing they
govern. Anything it changes, you can put back exactly as it was.

Will that contain something smarter than every human combined? No. Nothing
will, and anyone promising otherwise is selling. What guardrails do is
smaller and far more useful: nothing changes without being written down, and
nothing written down can't be undone.

---

*Everything below this line is how it works inside.
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

Phase 0 (contract + threat model) — **this repository is the Phase 0 deliverable**, plus the Phase 1 read-only first-contact skill. See `HANDOFF.md` for next actions, `docs/architecture.md` for the design, `docs/prior-art.md` for what we deliberately reuse from other projects, and `docs/decisions/` for why the architecture is shaped this way.

## The end-to-end scenario

One project runs end to end as the development fixture: every phase must improve the same run — inspect → constrain → ask → propose → build → perform a real task → absorb a correction → restore safely. The fixture is not the bar: what the product must clear is written without naming a profession ([[ADR-0011-exit-tests-name-capabilities|ADR-0011]]), and the generality test is a second pilot in a domain unlike the first.
