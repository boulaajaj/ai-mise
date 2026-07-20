# ADR-0001: Separate control plane outside the agent-writable workspace

**Status:** Accepted · 2026-07-20
**Trigger:** External review of blueprint v1.

## Context

Blueprint v1 declared CLAUDE.md "immutable to the improvement loop" and relied on a PreToolUse hook, stored inside the workspace, to protect persistent paths. Review identified two flaws: (1) CLAUDE.md is delivered as context after the system prompt and cannot guarantee compliance — it is context, not authority (confirmed by Claude Code documentation); (2) a protection mechanism living in the same writable tree it protects is a circular defense — "this file protects itself from being changed."

## Decision

Split the product into a **control plane** (constitution policy, approval store, mutation gateway, validators, threat tests, adapters) installed outside any generated workspace and denied to normal editing tools, and a **data plane** (the workspace) where every persistent artifact is generated, replaceable, and restorable. The workspace's CLAUDE.md, hooks, and skills are compiled projections of control-plane policy, never the authoritative policy itself.

## Consequences

- Constitution changes become a manual, user-initiated act on the control plane — structurally outside the self-modification loop (also counters optimizer-optimizee collapse).
- Enforcement becomes a stack: generated instructions → hooks → Claude Code permission deny-rules → OS permissions. Hooks alone are explicitly not the boundary.
- The adapter directory (`generated/claude-code/` as one projection among future ones) turns the original portability thesis into enforced structure.
- **Scope honesty recorded:** on a personal machine this is an accident-and-drift boundary, not an adversarial security boundary; the threat suite is scoped to bypass-by-confused-agent.
