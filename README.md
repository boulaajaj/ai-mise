# AI-Mise

## AI moves fast. Your workspace should remember.

AI-Mise is an experiment in giving AI a durable place to work: one that keeps
the context you choose, learns how you like to work, and helps you move a
project forward without making you repeat yourself every time.

> Less time managing AI. More time doing the work.

## What it is being built to do

### Keep the context

- Carry the useful parts of a project across conversations instead of making
  you repeat yourself.
- Organize material around *your* words and categories, not a template imposed
  by the software.
- Turn a growing body of work into clear priorities and useful views when you
  need them.

### Keep up with AI

- Research the tools, approaches, and ideas that are relevant to the work in
  front of you.
- Explain findings at the right level: detailed when you want detail, plain
  language when you do not.
- Help create focused assistance for recurring work, rather than treating every
  task like a blank chat.

### Make it yours

- Start with the project you actually have, whether that is software, an
  Arduino build, a practice, or something nobody has named yet.
- Ask before assuming how you want things grouped, named, or shown.
- Keep the workspace in your hands instead of trapping your work inside a
  single conversation.

### Show its work

- Make important changes visible, explain why they were proposed, and keep a
  readable history of how the setup evolved.
- Let your decisions shape the assistant over time without letting it quietly
  rewrite the rules.
- Make experiments safe to review, keep, discard, or undo.

## The point

Most people should not need a second career in AI tools, prompts, or whatever
new acronym appears next week just to get useful help from AI. The goal is an
assistant that becomes more useful as it learns the work — while you remain in
control.

This starts as a personal experiment. I keep seeing the same pattern in every
project: research the space, learn the vocabulary, compare options, collect the
useful context, and decide what matters. AI-Mise is an attempt to make that
careful process easier to repeat and easier to trust.

---

*Everything below this line is how it works inside. The person using AI-Mise
never needs any of it.*

**The kernel:** [METHOD.md](METHOD.md) — one page that stays true regardless of
platform, model, or decade. Everything else is an adapter.

## Product boundary (one sentence)

AI-Mise works out what you are doing — from your materials when you have them,
from the conversation when you don't — asks a small number of justified
questions, describes in plain language the workspace it would set up for your
assistant, builds only what you approve, and can put anything back exactly as
it was.

**Explicitly out of scope for the first release:** automatic self-improvement,
SQLite, full wiki generation, multi-platform adapters, scheduled retrospectives,
voice UX, marketplace distribution.

## One assistant — you name it

This is the promise being built (see Status below for what runs today): the
person using AI-Mise meets exactly one thing — an assistant they name at the
first hello. Small help is applied at once and can always be undone; changes to
how the assistant works are announced in plain words and wait for a good
moment. Nobody is asked to switch modes, and words like "builder" or
"compiler" never reach them.

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
