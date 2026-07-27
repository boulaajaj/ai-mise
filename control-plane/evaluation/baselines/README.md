# Baselines (issue #1)

The utility row of the scorecard compares a generated workspace against plain
`/init` **on the same materials**, whatever those materials are *[default]*
(ADR-0011). A baseline that exists for exactly one project measures that
project, so baselines are captured per case, beside the case they belong to.
Everything on this page is that one chosen behavior, applied.

## Capturing a baseline

Give `/init` exactly what the bootstrapper is given. Do not stash or tidy the
tree first: a baseline that ran on different materials is not a baseline.

```bash
cd <the-folder-the-case-provides>
claude                         # then run: /init
# copy what it generated — CLAUDE.md, .claude/ (if created) — into, in this repo:
#   control-plane/evaluation/baselines/<case>/init/
```

`CLAUDE_CODE_NEW_INIT=1` is a different flow, so it is a different baseline:
capture it under `control-plane/evaluation/baselines/<case>/init-new/` rather
than over the top of the first one.

Record in `<case>/NOTES.md`: date, Claude Code version, which flow was run,
wall-clock time, exactly what materials were present, and your one-paragraph
impression of quality.

The blank-slate case has no folder to run `/init` in, and that is the point
(#58): with nothing to read there is nothing to compare against, so the bar is
the proposal itself.

## The hand-built workspace

The manually built workspace from the development project is a fixture, not a
bar (ADR-0011). Months of hand work is worth measuring against once there is
something worth measuring — snapshot it under
`control-plane/evaluation/fixtures/` when the comparison in #58 comes due,
creating that directory then; nothing lives there yet. It does not set the
scorecard.

## Status

- [ ] first case captured
- [ ] referenced from the Phase 3 utility eval
