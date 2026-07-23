---
type: glossary
title: AI-Mise ubiquitous language
---

# Glossary — the ubiquitous language

One word, one meaning, everywhere ([[ADR-0009-domain-language-and-structure|ADR-0009]]).
Entries are definitions, not claims — authority lives in the linked ADRs.
If you need a new term, add it here or reuse the existing one.

## Method/Kernel context

- **Kernel** — what stays true regardless of platform, model, or decade ([[METHOD]]). Everything else is an adapter.
- **Adapter** — a replaceable translation of the kernel and a workspace to one platform's files (CLAUDE.md, hooks, settings — Claude Code today; Codex, others later). One term, one meaning: adapters translate; they never hold canonical data.
- **Invariant** — a rule that must always hold; changed only by its own deliberate process.

## Governance context

- **Constitution** — the user-owned policy (`control-plane/constitution/policy.yaml`); never edited by an agent ([[ADR-0001-control-plane-separation|ADR-0001]]).
- **Control plane** — authority: constitution, approval, validation, threat tests. Lives outside any workspace.
- **Proposal** — the one unit of persistent change: files, before/after hashes, plain purpose, risk tier, rollback id.
- **Receipt** — the record that a proposal was approved/rejected and applied; the approval's audit trail.
- **Mutation gateway** — the single path every persistent change flows through: propose → approve → stage → validate → apply → restore point.
- **Risk tier** — routine / structural / governance / safety; sets whether a change applies instantly or waits ([[ADR-0008-no-modes-tiered-application|ADR-0008]]).

## Construction context

- **Builder** — the persona that sets up and changes a workspace; distinct from the user's assistant ([[ADR-0005-builder-vs-workspace|ADR-0005]], [[ADR-0008-no-modes-tiered-application|ADR-0008]]).
- **Setup change** — a change to how the workspace works, badged and undoable; not a mode ([[ADR-0008-no-modes-tiered-application|ADR-0008]]).

## Knowledge context

- **Workspace / data plane** — the per-project world the agent works in; all generated, replaceable, restorable.
- **Source** — immutable evidence, hashed, append-only. Never edited ([[ADR-0002-evidence-claims-views|ADR-0002]]).
- **Claim** — an atomic fact with provenance (source, authority, confidence, validity). Traceable.
- **View** — rebuildable synthesis (wiki page, report, mind map). Never cited as evidence for a claim.
- **Memory** — governed, growing domain knowledge behind an index; read on demand.
- **Skill / Hook** — a reusable procedure / a deterministic lifecycle guard, per the placement rubric.
- **Completeness** — the set of things that make a workspace ready (profile, mission, constraints…), each known / assumed / missing; gates construction.

## Meta context

- **Meta-harness** — the repo governing its own development by the same rules it compiles for users (issue #19).
- **Self-hosting ladder** — the repo adopts each practice in the same phase that ships it.
- **Retrospective** — event-triggered reflection that proposes improvements; applies nothing on its own (shadow mode, [[ADR-0003-shadow-mode-self-improvement|ADR-0003]]).
- **Loyal dissent** — flag concerns before complying; never silently refuse, never silently comply ([[ADR-0007-challenge-before-compliance|ADR-0007]]).
