# ADR-0009: Domain language first, structure follows (DDD applied to ourselves)

**Status:** Proposed · 2026-07-21 (merge = agreement)
**Trigger:** Amine: organize the repo by domain-driven design and good practice — "self-improve."

## Context

DDD's value is not folders; it is **ubiquitous language** — one vocabulary shared by the domain, the docs, and the code, so a word means exactly one thing everywhere. AI-Mise already uses such a vocabulary across ADRs, but it is never defined in one place. A disruptive folder move now would rewrite paths in every doc, break the generated mind map, and churn history immediately before Phase 2 depends on those paths. Loyal dissent (ADR-0007) against the literal "reorganize the folders now" request: do the durable part first.

## Decision

1. **Ship a glossary** — `docs/GLOSSARY.md`, the ubiquitous language: Kernel, Control Plane, Data Plane / Workspace, Constitution, Proposal, Receipt, Mutation Gateway, Claim, View, Source, Memory, Skill, Hook, Adapter, Builder, Setup change, Completeness. One line each, cross-linked. This is the DDD backbone; folders are downstream of it.
2. **Name the bounded contexts** (already physically separated — DDD by accident, now on purpose): **Governance** (control-plane/constitution, approval, validation), **Construction** (mutation, adapters), **Knowledge** (sources, claims, views, memory), **Method/Kernel** (METHOD.md, docs/decisions), **Meta** (dev-harness, the repo governing itself). Record the map in the glossary; do not move files yet.
3. **Migrate incrementally.** When a phase first touches a context, align that context's folders to the map in the same PR — never a big-bang move. The mind map regenerates; CI keeps it honest.
4. **The glossary is enforced.** Copilot instructions gain: flag new terms that duplicate an existing glossary concept under a different word (the anti-synonym rule — the practical test of ubiquitous language).

## Consequences

- One small PR now (glossary + context map), not a churn. Structure improves as a side effect of work already scheduled.
- New standing check: a PR introducing a domain term not in the glossary either adds it or reuses the existing word.
- This is the self-improvement Amine named: the repo applies its own placement/where-does-this-live discipline to its own layout.
