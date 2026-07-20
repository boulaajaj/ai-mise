# ADR-0003: Self-improvement starts in shadow mode

**Status:** Accepted · 2026-07-20
**Trigger:** External review of blueprint v1; self-modification risk literature.

## Context

Blueprint v1 activated the full retrospective loop (propose → approve → apply) as soon as it was built. Research on self-evolving agents documents compositional drift, revert hysteresis (rules roll back; memory written under them does not), and safety mechanisms becoming optimization targets. These papers are recent — directionally informative, not settled engineering law — which argues for conservatism, not confidence.

## Decision

The retrospective system initially: observes corrections and friction, generates proposed improvements, scores them against evals with a **predicted eval impact**, learns from rejections (a rejected proposal must not recur), and applies **nothing** automatically. Graduation to preparing executable change-sets (still behind transaction approval and deterministic application) requires roughly 20–30 real sessions with stable regression tests — a configurable default, not a research finding.

## Consequences

- Phase 5 exit test becomes measurable: accepted proposals improve their predicted eval; rejected proposals stop recurring.
- We collect ground truth on proposal quality before any proposal can touch the workspace, converting the riskiest feature into the best-instrumented one.
- Trajectory review ("would the user approve the present-day system proposed all at once?") is scheduled from the first live retrospective, not added later.
