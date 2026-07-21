#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

# update the dev-harness mapping row (mutation gateway -> PR flow)
python - <<'PYEOF'
from pathlib import Path
p = Path("docs/meta/dev-harness.md")
t = p.read_text(encoding="utf-8")
old = "| Mutation gateway | PRs/commits referencing issues; protected paths listed in policy.yaml apply to us too |"
new = "| Mutation gateway | protected main + PR-only merges: the PR is the proposal, Amine's merge is the approval receipt; protected paths in policy.yaml apply to us too |"
assert old in t, "mapping row not found"
p.write_text(t.replace(old, new), encoding="utf-8")
print("dev-harness updated")
PYEOF

python tools/generate_mindmap.py
git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'meta: PR-only flow — protect main, PR = proposal, merge = approval (#19)'
git push -q -u origin meta/pr-only-flow
gh pr create -R "$R" --base main --head meta/pr-only-flow \
  --title "meta: PR-only flow — main is protected; the PR is the proposal, your merge is the approval" \
  --body "Correction from Amine: ai-mise must do as it says others should do — no direct commits to main.

What changed:
- Branch protection on main (already applied via API): PRs required, enforced for admins, no force-pushes, no deletions.
- CLAUDE.md: new top rule — every change lands via PR from a typed branch; the PR is the proposal, your merge is the approval (the product's transaction model on GitHub primitives).
- dev-harness.md: mutation-gateway mapping updated accordingly.
- retro-log: correction recorded, with the generalized lesson — when an enforcement rung is free (settings, not machinery), climb it immediately.
- Follow-up noted: when mini CI ships (#27/#28), add it as a required status check.

**Merging this PR is the first act of the new governance — the approval gate approving its own creation.**"
echo PR-CREATED
git checkout -q main
rm -- "$0"
