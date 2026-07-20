# ADR-0002: Three-layer knowledge — immutable sources, atomic claims, rebuildable views

**Status:** Accepted · 2026-07-20
**Trigger:** External review of blueprint v1; also a return to the original product synthesis, which required "raw evidence preserved separately from generated interpretation."

## Context

Blueprint v1 made the wiki the primary explanatory layer without a provenance substrate. Review identified synthesis decay as the failure mode: an AI-written summary becomes the source for another AI-written summary until the original fact is unrecoverable. Karpathy's LLM-wiki gist is a high-level pattern and intentionally leaves schemas and safeguards open — it cannot serve as the safety design.

## Decision

- `sources/` — immutable or append-only evidence with hashed manifests.
- `knowledge/claims/` — atomic claims carrying: source reference/span, authority (user-stated | agent-inferred | external-source), status, confidence, valid-from/until, contradicts/supersedes links.
- `views/` — wiki and reports, rebuildable from claims; **a view is never citable as evidence for a claim.**

OKF v0.1 conventions (minimal `type` frontmatter, index.md, log.md, links, citations) adopted for the knowledge and views layers only — OKF does not replace evidence handling or change governance.

## Consequences

- Every important factual or safety statement is traceable to a source, a user decision, or an explicit inference — the Phase 4 exit test.
- Wiki generation is demoted from Phase 3 to Phase 4+ and the first release ships without it.
- Provenance validation (citation coverage, contradiction checks around changed concepts) becomes a deterministic validator in the mutation gateway.
