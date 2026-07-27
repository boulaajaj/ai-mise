# Baselines (issue #1)

The utility row of the scorecard compares a generated workspace against plain
`/init` **on the same materials** — whatever those materials are (ADR-0011). A
baseline that exists for exactly one project measures that project, so baselines
are captured per case, beside the case they belong to.

## Capturing a baseline

```bash
cd <the-folder-the-case-provides>
git stash                      # if needed, so /init sees a clean tree
claude                         # then run: /init   (also try CLAUDE_CODE_NEW_INIT=1 claude)
# copy what it generated — CLAUDE.md, .claude/ (if created) — into:
#   control-plane/evaluation/baselines/<case>/init/
```

Record in `<case>/NOTES.md`: date, Claude Code version, whether the interactive
NEW_INIT flow was used, wall-clock time, what the materials were, and your
one-paragraph impression of quality.

The blank-slate case has no folder to run `/init` in, and that is the point: with
nothing to read there is nothing to compare against, so the bar is the proposal
itself (#58).

## The hand-built workspace

The manually built workspace from the development project is a fixture, not a bar
(ADR-0011). Months of hand work is worth measuring against once there is
something worth measuring — snapshot it under `fixtures/` when the comparison in
#58 comes due. It does not set the scorecard.

## Status

- [ ] first case captured
- [ ] referenced from the Phase 3 utility eval
