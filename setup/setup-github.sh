#!/usr/bin/env bash
# ai-mise one-shot GitHub setup: repo + push + milestones + issues.
# Requirements: gh (authenticated, repo scope), git. Run from the repo root.
# Idempotent-ish: safe to re-run; existing milestones/issues are not duplicated.
set -euo pipefail

OWNER="$(gh api user -q .login)"
REPO="ai-mise"
FULL="$OWNER/$REPO"
echo "==> GitHub account: $OWNER"

# --- 1. Create private repo (if missing) and push ---------------------------
if gh repo view "$FULL" >/dev/null 2>&1; then
  echo "==> Repo $FULL already exists"
else
  gh repo create "$FULL" --private --description "Governed workspace compiler: turns raw project materials + user decisions into an auditable, versioned, agent-ready workspace." >/dev/null
  echo "==> Created private repo $FULL"
fi
git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$FULL.git"
git push -u origin main
echo "==> Pushed main"

# --- 2. Milestones ----------------------------------------------------------
declare -a MS=(
  "Phase 0 — Contract & Threat Model|Product boundary, schemas, protected assets, 34 bypass scenarios, baselines. Exit: what is authoritative vs generated, and which process may change each item, is stated and testable."
  "Phase 1 — Read-Only Bootstrapper|Inventory, inspector, unknowns ledger, decision-aware questions, proposal. No writes. Exit: an Arduino proposal Amine would seriously consider approving."
  "Phase 2 — Governed Construction|Mutation gateway, receipts, validators, restore. Exit: unauthorized writes fail, approved writes succeed, restore reproduces exact hashes."
  "Phase 3 — Claude Code Adapter|Compile policy into CLAUDE.md/rules/settings/hooks; auto-memory redirect. Exit: Arduino workspace beats plain /init without protected-path violations."
  "Phase 4 — Evidence-Backed Knowledge|Source manifests, claims with provenance, OKF views, citation validation. Exit: every important claim traces to source, user decision, or explicit inference."
  "Phase 5 — Retrospective Shadow Mode|Correction collection, proposals, rejection learning, predicted eval impact, no auto-apply. Exit: accepted proposals improve metrics; rejected ones stop recurring."
  "Phase 6 — Controlled Self-Improvement & Second Pilot|Executable diffs behind transaction approval; community-website pilot as the true generality test."
)
existing_ms=$(gh api "repos/$FULL/milestones?state=all" -q '.[].title')
for entry in "${MS[@]}"; do
  title="${entry%%|*}"; desc="${entry#*|}"
  if grep -qxF "$title" <<<"$existing_ms"; then
    echo "==> Milestone exists: $title"
  else
    gh api "repos/$FULL/milestones" -f title="$title" -f description="$desc" >/dev/null
    echo "==> Milestone created: $title"
  fi
done

# --- 3. Labels --------------------------------------------------------------
gh label create meta-harness -R "$FULL" --description "The repo's own evolving dev harness (dogfooding)" --color 5319e7 2>/dev/null || true
gh label create golden-thread -R "$FULL" --description "Arduino end-to-end fixture" --color 0e8a16 2>/dev/null || true

# --- 4. Issues --------------------------------------------------------------
existing_issues=$(gh issue list -R "$FULL" --state all --limit 200 --json title -q '.[].title')
make_issue() {
  local title="$1" milestone="$2" body="$3" labels="${4:-}"
  if grep -qxF "$title" <<<"$existing_issues"; then
    echo "==> Issue exists: $title"; return
  fi
  if [ -n "$labels" ]; then
    gh issue create -R "$FULL" --title "$title" --milestone "$milestone" --label "$labels" --body "$body" >/dev/null
  else
    gh issue create -R "$FULL" --title "$title" --milestone "$milestone" --body "$body" >/dev/null
  fi
  echo "==> Issue created: $title"
}

M0="Phase 0 — Contract & Threat Model"
M1="Phase 1 — Read-Only Bootstrapper"
M2="Phase 2 — Governed Construction"
M3="Phase 3 — Claude Code Adapter"
M4="Phase 4 — Evidence-Backed Knowledge"
M5="Phase 5 — Retrospective Shadow Mode"
M6="Phase 6 — Controlled Self-Improvement & Second Pilot"

make_issue "Capture baselines: plain /init run + manual Arduino workspace snapshot" "$M0" \
"Run /init (also try CLAUDE_CODE_NEW_INIT=1) on the Arduino Digger repo and snapshot the output. Snapshot the manually built Arduino workspace as the second baseline. Store under control-plane/evaluation/baselines/ (or record locations if too large).

Exit: both baselines stored and referenced from the evaluation README. These are the comparison targets for the Phase 3 utility scorecard row." golden-thread

make_issue "Write policy.schema.json and validate policy.yaml against it" "$M0" \
"Author control-plane/constitution/policy.schema.json covering every key currently in policy.yaml. Add a validation script (stdlib-first; pattern: protected_path_validator.py).

Exit: policy.yaml validates clean; a deliberately broken copy fails loudly."

make_issue "Exercise proposal/receipt schemas with worked examples" "$M0" \
"Write 3 example proposals (routine / structural / safety) and 2 receipts; validate against the schemas. Fix schema friction now, not in Phase 2.

Exit: examples committed under control-plane/approval/examples/ and validating clean."

make_issue "Run inspector on Arduino Digger materials (golden thread kickoff)" "$M1" \
"Point skills/inspector at the real Arduino materials (raw materials only — NOT the hand-built harness). Produce manifest.json, findings.md, unknowns ledger.

Exit: findings cite manifest paths; the unknowns ledger is honest (includes what inspection could not determine)." golden-thread

make_issue "Findings quality: manifest-cited provenance + safety-critical surfacing" "$M1" \
"Iterate on inspector output: every finding cites manifest entries; safety-critical constraints (ESC temperatures, current limits, mechanical stops) surface prominently and are never buried.

Exit: Amine reviews findings.md and confirms nothing safety-critical is missing or diluted." golden-thread

make_issue "Implement question contract + assumptions ledger flow" "$M1" \
"Enforce the four-part question contract (unresolved decision / possible answers / what changes / cost of wrong assumption), batch and round caps from policy.yaml, and the stopping rule. Unasked or unanswered unknowns become explicit assumptions.

Exit: every asked question demonstrably changes a construction decision (scorecard row: Interview)."

make_issue "First full workspace proposal for review" "$M1" \
"Produce proposal.md per the inspector SKILL.md output contract: plain language, placement per rubric, enforced items, assumptions ledger, deliberate non-goals.

Exit (Phase 1 gate): Amine would seriously consider approving it. No writes happen." golden-thread

make_issue "Build mutation gateway: stage / validate / apply / restore" "$M2" \
"Implement control-plane/mutation/: stage into an isolated worktree, run validators, apply on receipt, tag restore point. Approval covers the transaction; receipts follow receipt.schema.json; approved_scope_hash checked at apply time.

Exit: the lifecycle in architecture.md section 3 runs end to end on a toy workspace."

make_issue "Remaining deterministic validators: frontmatter, link, provenance" "$M2" \
"Same pattern as protected_path_validator.py (JSON result, exit codes 0/1/2). Frontmatter: platform limits from policy.yaml. Link: wiki/skill references resolve, one level deep. Provenance: claims cite sources; views never cited as evidence.

Exit: each validator has a passing and a deliberately-failing fixture."

make_issue "Automate the 34 threat scenarios" "$M2" \
"Turn control-plane/threat-tests/scenarios.md into automated tests: run each bypass attempt, assert it is blocked, assert an audit record exists. Update scenario statuses.

Exit (scorecard row Governance): zero protected-path bypasses across the suite."

make_issue "Hash-exact restore test (rules AND memory together)" "$M2" \
"Build a workspace, apply 3 transactions, corrupt something, Restore. Assert the restored tree is hash-identical to the tagged state, including memory/ (the ratchet problem — ADR-0003 context).

Exit (scorecard row Rollback): restore reproduces the exact governed file tree."

make_issue "Claude Code adapter: compile policy into CLAUDE.md, rules, settings, hooks" "$M3" \
"control-plane/adapters/claude-code/ compiles policy.yaml + workspace knowledge into generated/claude-code/ artifacts (CLAUDE.md under 200 lines, path-scoped rules, settings.json deny-rules, PreToolUse hooks). Generated files carry a do-not-edit-directly header pointing at the policy.

Exit: regenerate-and-diff is clean; hand-editing a projection is caught by threat scenario 34's test."

make_issue "Auto-memory redirect/disable during governed sessions" "$M3" \
"Implement policy platform.claude_code.auto_memory: disable or redirect native auto-memory into workspace/memory/ so rollback is complete.

Exit: after a governed session, no workspace-relevant memory exists outside the governed tree."

make_issue "Pin and wrap upstream skill-creator (do not fork yet)" "$M3" \
"Pin a version of anthropics/skills skill-creator; wrap it for generating workspace skills (evals-first, negative examples in descriptions). Fork only when composition cannot deliver a required change — record that decision as an ADR if it happens.

Exit: one Arduino workspace skill generated through the wrapper, with evals."

make_issue "Claims layer with provenance + citation-coverage validator" "$M4" \
"Implement knowledge/claims per ADR-0002: id, source span, authority (user-stated / agent-inferred / external-source), status, confidence, validity window, contradicts/supersedes. Citation-coverage validator enforces policy thresholds (100% safety-critical, >=95% factual).

Exit (scorecard row Provenance): thresholds met on the Arduino workspace."

make_issue "Shadow-mode retrospectives: collection, proposals, rejection learning" "$M5" \
"Implement the retrospective pipeline per ADR-0003: collect corrections/friction, classify, diagnose, propose with predicted eval impact, record rejections so they never recur. Apply NOTHING automatically.

Exit: accepted proposals improve their predicted eval; a rejected proposal does not reappear."

make_issue "Executable diffs behind transaction approval (graduation)" "$M6" \
"After the graduation criteria in policy.yaml (min real sessions + stable regressions), allow retrospectives to prepare executable change-sets — still through the full gateway (proposal, receipt, stage, validate, apply).

Exit: one real self-improvement lands end-to-end with a complete audit trail."

make_issue "Second pilot: community-website domain (true generality test)" "$M6" \
"Run the full bootstrap on the Spraker East neighborhood website domain. Arduino has been the dev fixture, so THIS is the clean generalization experiment. Score with the architecture.md section 8 scorecard; write the comparison report.

Exit: written report; decision on whether the method generalizes."

make_issue "meta: run dev retrospectives and evolve the repo's own harness" "$M0" \
"ai-mise is self-hosting: the repo follows the same governance it compiles for users (see CLAUDE.md and docs/meta/dev-harness.md). At the end of each working session, append a retro-log entry; file improvement proposals as meta-harness issues; every ~10 entries or monthly, run a trajectory review (would Amine approve today's repo proposed all at once?).

This issue stays open as the standing meta-harness anchor. Exit: never (recurring); close only if the meta-harness design is superseded by ADR." meta-harness

echo
echo "==> Done. Repo: https://github.com/$FULL"
echo "==> Milestones: https://github.com/$FULL/milestones"
echo "==> Issues:     https://github.com/$FULL/issues"