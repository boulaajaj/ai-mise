#!/usr/bin/env bash
set -uo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"
git checkout -q meta/adr-0008-no-modes
git fetch -q
git merge origin/main -m "Merge main (mindmap conflict; regenerated)" || true
if git diff --name-only --diff-filter=U | grep -q .; then
  git checkout --theirs docs/mindmap.md 2>/dev/null || true
  git add -A
  git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q --no-edit
fi
python tools/generate_mindmap.py
git add docs/mindmap.md
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Regenerate mindmap after main merge' 2>/dev/null || true
git push -q && echo PUSHED
gh api -X POST "repos/$R/pulls/45/requested_reviewers" -f 'reviewers[]=copilot-pull-request-reviewer[bot]' >/dev/null 2>&1 && echo RE-REVIEW-REQUESTED
git checkout -q main
rm -- "$0"
