# Baselines (issue #1)

Two comparison targets for the utility scorecard row ("better than both plain
/init and the manual baseline"). Both require Amine's machine and the Arduino
Digger repository — capture them as follows and commit the snapshots here.

## 1. Plain /init baseline

```bash
cd <arduino-digger-repo>
git stash                      # if needed, so /init sees a clean tree
claude                         # then run: /init   (also try CLAUDE_CODE_NEW_INIT=1 claude)
# after it finishes, copy the generated artifacts:
#   CLAUDE.md, .claude/ (if created)
# into: control-plane/evaluation/baselines/init-baseline/
```

Record in `init-baseline/NOTES.md`: date, Claude Code version, whether the
interactive NEW_INIT flow was used, wall-clock time, and your one-paragraph
impression of quality.

## 2. Manual workspace baseline

Snapshot the hand-built Arduino workspace (the wiki, architecture docs, safety
rules, issues/PR conventions built manually over months):

```bash
# from the manual workspace root:
git archive HEAD | tar -x -C <ai-mise>/control-plane/evaluation/baselines/manual-baseline/
# or, if not a git repo, copy the relevant folders and note what was excluded
```

Record in `manual-baseline/NOTES.md`: what this workspace contains, roughly how
many hours it took to build by hand, and which parts you consider its strongest
assets (the bar AI-Mise must meet).

## Status

- [ ] init-baseline captured
- [ ] manual-baseline captured
- [ ] both referenced from the Phase 3 utility eval
