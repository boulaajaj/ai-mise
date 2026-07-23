# Glossary — the ubiquitous language

One word, one meaning, everywhere (ADR-0009). If you need a new term, add it
here or reuse the existing one. Contexts group the terms by where they live.

## Method context

- **Kernel** — what stays true regardless of platform, model, or decade ([[METHOD]]). Everything else is an adapter.
- **Adapter** — a replaceable translation of the kernel to one platform (Claude Code today; Codex, others later).
- **Invariant** — a rule that must always hold; changed only by its own deliberate process.

## Governance context

- **Constitution** — the user-owned policy (`control-plane/constitution/policy.yaml`); never edited by an agent.
- **Control plane** — authority: constitution, approval, validation, threat tests. Lives outside any workspace.
- **Proposal** — the one unit of persistent change: files, before/after hashes, plain purpose, risk tier, rollback id.
- **Receipt** — the record that a proposal was approved/rejected and applied; the approval's audit trail.
- **Mutation gateway** — the single path every persistent change flows through: propose → approve → stage → validate → apply → restore point.
- **Risk tier** — routine / structural / governance / safety; sets whether a change applies instantly or waits (ADR-0008).

## Construction context

- **Builder** — the persona that sets up and changes a workspace; distinct from the user's assistant (ADR-0005/0008).
- **Setup change** — a change to how the workspace works, badged and undoable; not a mode (ADR-0008).
- **Adapter (construction)** — compiles the neutral workspace into one platform's files (CLAUDE.md, hooks, settings).

## Knowledge context

- **Workspace / data plane** — the per-project world the agent works in; all generated, replaceable, restorable.
- **Source** — immutable evidence, hashed, append-only. Never edited.
- **Claim** — an atomic fact with provenance (source, authority, confidence, validity). Traceable.
- **View** — rebuildable synthesis (wiki page, report, mind map). Never cited as evidence for a claim.
- **Memory** — governed, growing domain knowledge behind an index; read on demand.
- **Skill / Hook** — a reusable procedure / a deterministic lifecycle guard, per the placement rubric.

## Cross-cutting

- **Completeness** — the set of things that make a workspace ready (profile, mission, constraints…), each known / assumed / missing; gates construction.
- **Retrospective** — event-triggered reflection that proposes improvements; applies nothing on its own (shadow mode).
- **Meta-harness** — the repo governing its own development by the same rules it compiles for users.
