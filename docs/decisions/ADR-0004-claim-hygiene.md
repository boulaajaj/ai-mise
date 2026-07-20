# ADR-0004: Claim hygiene — downgraded assertions from blueprint v1

**Status:** Accepted · 2026-07-20
**Trigger:** External review of blueprint v1.

## Decision

The following v1 assertions are downgraded and must be presented accordingly anywhere they appear:

1. **"90% skill-trigger rate"** — our product target, not an Anthropic standard. Skill routing is measured as separate true-positive / false-positive / false-negative rates, because a false trigger and a missed trigger have different costs.
2. **"73% → 85% routing improvement from negative examples"** — anecdotal until located in a primary source or reproduced by our own evals.
3. **"60% of run divergence originates in the first two steps" and "near-zero free-text reproducibility"** — plausible findings from a real consistency paper, but not verified at those exact figures; treated as design hints (verify early; assert on structured artifacts), not verified claims.
4. **"Markdown vs databases resolves cleanly"** — markdown-as-authority with SQLite-as-derived-index is our architectural choice, well-motivated for a single-user product; it is not a universally settled result.
5. **"Every 10th retrospective is a trajectory review" and placement-accuracy thresholds** — sensible starting policies; they live in `control-plane/constitution/policy.yaml` as configurable defaults.
6. **"Zero-token scripts"** — script *source* does not enter context merely by running; script *output* still consumes context. Phrase accordingly.

## Consequences

Verified/prior-art/default labeling is mandatory in all design documents (see architecture.md §1). Numbers that are product choices live in policy.yaml, not in prose.
