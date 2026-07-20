# The meta-harness: how harnessmith evolves itself

A tool that compiles governed, self-improving workspaces must be developed
inside one. This document defines harnessmith's own harness — deliberately the
same shape as the product, one level up. It is also the product's first test
fixture: every mechanism we impose on user workspaces gets tried here first.

## Mapping (product concept → dev-repo implementation)

| Product concept | In this repo |
|---|---|
| Constitution (user-owned, agent-untouchable) | `control-plane/constitution/policy.yaml` + the rules block of `CLAUDE.md` |
| Generated projection | `CLAUDE.md` (projection of docs/; docs win on conflict) |
| Decision records | `docs/decisions/` ADRs (append-only) + issue threads |
| Placement rubric | architecture.md §5, applied to our own knowledge: recurring dev procedure → skill or script; every-session fact → CLAUDE.md; evolving understanding → docs/meta/retro-log.md |
| Mutation gateway | PRs/commits referencing issues; protected paths listed in policy.yaml apply to us too |
| Retrospective (shadow mode) | `retro-log.md` entries — observations and proposals only; changes land only as reviewed commits |
| Trajectory review | Every ~10 retro entries or monthly: re-read the ADRs + retro log and ask "would Amine approve today's repo proposed all at once?" File findings as a `meta-harness` issue |
| Eval harness | The threat suite + validator self-tests are our own regression tier; phase exit tests are our capability tier |

## Dev-retrospective entry format (append to `retro-log.md`)

```
## YYYY-MM-DD — <session focus>
- What was attempted / what shipped:
- Corrections received (from Amine, from tests, from reality):
- Diagnosis (which artifact was wrong or missing — cite the file):
- Proposals (each → an issue labeled `meta-harness`; placement per rubric):
- Rejected previously, do not re-propose:
```

## Rules

1. Shadow mode applies to us too: a retrospective entry never directly changes
   the harness; it produces issues, and issues produce reviewed commits.
2. Rejected proposals are recorded and must not recur (same as the product's
   rejection-learning rule).
3. The meta-harness itself is versioned: changes to this file or CLAUDE.md are
   `meta-harness`-labeled, ADR-worthy when structural.
4. Honesty rule: when we violate our own process (we will), the retro entry
   says so plainly. The gap list is the most valuable output — every gap here
   is a gap users will hit too.

## Bootstrap status

Created 2026-07-20 alongside Phase 0. First retrospective is due at the end of
the first Claude Code working session (see the standing meta-harness issue).
