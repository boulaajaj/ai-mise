#!/usr/bin/env bash
set -uo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

git checkout -q meta/challenge-rule
git fetch -q
git merge origin/main -m "Merge main into meta/challenge-rule (resolve squash-merge divergence)" || true
echo "--- conflicts: ---"
git diff --name-only --diff-filter=U

# CLAUDE.md: branch version == main's content + ADR-0007 rule line -> keep ours
if git diff --name-only --diff-filter=U | grep -q '^CLAUDE.md$'; then
  git checkout --ours CLAUDE.md && git add CLAUDE.md && echo "CLAUDE.md: kept branch version (main + rule)"
fi
# any other conflicted file the branch does not intentionally change -> take main
for f in $(git diff --name-only --diff-filter=U); do
  git checkout --theirs "$f" && git add "$f" && echo "$f: took main"
done
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q --no-edit || true
# sanity: rule present and no conflict markers
grep -q "Challenge before compliance (ADR-0007)" CLAUDE.md && echo RULE-PRESENT
! grep -rq "<<<<<<<" CLAUDE.md docs/ && echo NO-MARKERS
python tools/generate_mindmap.py >/dev/null 2>&1 || true
git add -A && git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m "Regenerate mindmap after merge" 2>/dev/null || true
git push -q
gh pr merge 33 -R "$R" --merge --body "Merged on Amine's explicit instruction (session, Jul 21): ADR-0007 challenge before compliance. Conflict from #29 squash-merge resolved by keeping main + the new rule." && echo MERGED-33
git checkout -q main && git pull -q
echo "== final =="
gh pr list -R "$R" --state open --json number,title -q '.[] | (.number|tostring) + " " + .title'
git log --oneline -3
rm -- "$0"
