#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/harnessmith
git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Rename to AI-Mise; add prior-art watchlist and ADR-0005 (Builder vs Workspace)'
git push -q
echo PUSHED
body=$(gh issue view 19 -R boulaajaj/ai-mise --json body -q .body)
gh issue edit 19 -R boulaajaj/ai-mise --body "${body//ai-mise is self-hosting/AI-Mise is self-hosting}" >/dev/null 2>&1 || true
fixed=$(gh issue view 19 -R boulaajaj/ai-mise --json body -q .body | sed 's/harnessmith/AI-Mise/g')
gh issue edit 19 -R boulaajaj/ai-mise --body "$fixed" >/dev/null
echo ISSUE19-FIXED
gh repo view boulaajaj/ai-mise --json url -q .url
rm -- "$0"
