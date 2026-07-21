#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

# dependency rows (same-PR rule)
python - <<'PYEOF'
from pathlib import Path
p = Path("docs/dependencies.md")
t = p.read_text(encoding="utf-8")
anchor = "| GitHub Copilot code review | automated PR reviewer | a reviewer, never data - instructions are plain markdown in-repo; reviews are advisory | PASS |\n"
if anchor not in t:
    anchor = "| gh CLI | GitHub automation | convenience; replaceable by API/web | PASS |\n"
rows = (
 "| GitHub Actions (CI) | runs validators/scanners on every change | automation convenience; all checks are runnable locally (same scripts) | PASS |\n"
 "| CodeQL | security scanning (free, public repos) | a scanner; findings are advisory copies, code untouched | PASS |\n"
 "| Semgrep (OSS rules) | pattern scanning, tokenless, advisory | a scanner; nothing canonical | PASS |\n"
 "| Dependabot | dependency update alerts | an alerting service; nothing canonical | PASS |\n"
 "| SonarCloud (pending setup) | code-quality dashboard, free for public repos | a dashboard; requires SONAR_TOKEN - see issue; data stays in repo | PASS (pending) |\n"
)
assert anchor in t
p.write_text(t.replace(anchor, anchor + rows), encoding="utf-8")
print("dependency rows added")
PYEOF

git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'meta: free-tier scanning - mini CI (validators, self-test, mindmap freshness), CodeQL, Semgrep advisory, Dependabot (#27 #28)'
git push -q -u origin meta/free-scanners
gh pr create -R "$R" --base main --head meta/free-scanners \
  --title "meta: mini CI + free-tier scanners (CodeQL, Semgrep, Dependabot)" \
  --body "Free-tier quality stack for a public repo, patterns borrowed from Arduino-DiggerSetup (advisory-vs-strict via continue-on-error; self-testing checks - every failure mode must fire):

- ci.yml (STRICT): policy schema validation, approval-example validation, protected-path validator self-test against a deliberately violating proposal, mind-map freshness (regenerate + diff - closes the automation half of #28), CLAUDE.md size limit. Candidate for required status check once green.
- codeql.yml: GitHub semantic security scanning, python + actions, weekly sweep. Free for public repos.
- semgrep.yml (ADVISORY): OSS rules, tokenless.
- dependabot.yml: weekly GitHub Actions version updates, labeled meta-harness.
- dependencies.md: vendor-death rows for all five (all PASS - scanners and dashboards, never data).

NOT included: SonarCloud - free for public repos but needs a SonarCloud account + SONAR_TOKEN secret only Amine can create. Setup steps will be filed as an issue.

Self-hosting ladder: this is the workspace-CI rung running on the compiler itself first." >/dev/null
echo PR-CREATED
PRNUM=$(gh pr list -R "$R" --head meta/free-scanners --json number -q '.[0].number')
gh api -X POST "repos/$R/pulls/$PRNUM/requested_reviewers" -f 'reviewers[]=copilot-pull-request-reviewer[bot]' >/dev/null 2>&1 && echo "COPILOT-REQUESTED-$PRNUM" || echo "COPILOT-REQ-FAILED-$PRNUM"

# enable secret scanning + push protection (free for public repos)
gh api -X PATCH "repos/$R" --input - >/dev/null <<'JSONEOF' && echo SECRET-SCANNING-ON || echo SECRET-SCANNING-FAILED
{"security_and_analysis":{"secret_scanning":{"status":"enabled"},"secret_scanning_push_protection":{"status":"enabled"}}}
JSONEOF

gh issue create -R "$R" --title "Set up SonarCloud (free for public repos) - needs Amine's account + SONAR_TOKEN" --milestone "v0 Personal Preview" --body "SonarCloud is free for public repos and adds maintainability/duplication/coverage dashboards on every PR. Needs steps only Amine can do: (1) sign in at sonarcloud.io with GitHub; (2) import boulaajaj/ai-mise; (3) create SONAR_TOKEN and add as a repo Actions secret; (4) then a session adds the sonarcloud workflow + updates the pending row in docs/dependencies.md. Verdict expected: PASS (a dashboard, never data)." >/dev/null
echo ISSUE-CREATED
git checkout -q main
rm -- "$0"
