#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Add deployment model (Claude Code first, v0 Personal Preview slice)'
git push -q
echo PUSHED

gh api "repos/$R/milestones" -f title="v0 Personal Preview" -f description="The earliest slice on Amine's machine for daily use: inspector skill + Obsidian-vault mind map views + validator hook (mini CI) + shadow-mode self-review. Exit: one week of real daily use, friction filed as issues. See docs/deployment.md." >/dev/null && echo MILESTONE-CREATED

gh issue create -R "$R" --title "Auto-research: the Builder researches its own improvements (shadow mode)" --milestone "Phase 5 — Retrospective Shadow Mode" --body "From Amine: in addition to retrospectives on corrections, the system should proactively research ways to improve itself — new checks, better patterns, platform changes, anything that improves response quality — and bring findings back as proposals. This is the original synthesis section 8 'controlled upgrade-review workflow' made concrete: a scheduled research pass over the prior-art watchlist, official platform changelogs, and curated lists; each finding becomes a shadow-mode proposal with predicted eval impact. Never silently rebuilds itself; same gateway, same approval." >/dev/null
gh issue create -R "$R" --title "Response-style customization: generate variants, ask for feedback, learn preferences" --milestone "Phase 5 — Retrospective Shadow Mode" --body "From Amine: the assistant should occasionally offer different ways of responding (structure, length, tone, format), ask which the user prefers, and persist the preference over time. Placement per rubric: learned preferences are personal-layer memory (weakest home first), promoted to rules only with repeated evidence. Feedback requests must be rare and batched — same anti-fatigue principle as approvals. Ties into claude-improve's nine feedback signal types (prior-art.md)." >/dev/null
gh issue create -R "$R" --title "Ship v0 Personal Preview on Amine's machine" --milestone "v0 Personal Preview" --body "Assemble the four-piece slice from docs/deployment.md: (1) inspector skill installed user-level; (2) views emitted as an Obsidian-compatible vault (wikilinks, plain markdown) so graph view = mind map; (3) a hook that runs existing validators on every change (mini CI); (4) end-of-session shadow retrospective writing observations + proposals to a file. Sequence: after issue #7 (first proposal) and issue #9 (validators). Exit: Amine uses it daily for a week on a real project and files the friction as issues — that list is the requirements input for Phases 2–5." >/dev/null
echo NEW-ISSUES-FILED

rm -- "$0"
git add -A && git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Remove one-time script' && git push -q
echo CLEAN
