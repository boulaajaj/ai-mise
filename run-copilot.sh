#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

# dependency register row (same-PR rule from our own instructions)
python - <<'PYEOF'
from pathlib import Path
p = Path("docs/dependencies.md")
t = p.read_text(encoding="utf-8")
row = "| GitHub Copilot code review | automated PR reviewer | a reviewer, never data - instructions are plain markdown in-repo; reviews are advisory | PASS |\n"
anchor = "| gh CLI | GitHub automation | convenience; replaceable by API/web | PASS |\n"
assert anchor in t and row not in t
p.write_text(t.replace(anchor, anchor + row), encoding="utf-8")
print("dependency row added")
PYEOF

git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'meta: Copilot review instructions encoding repo governance as review criteria'
git push -q -u origin meta/copilot-review
gh pr create -R "$R" --base main --head meta/copilot-review \
  --title "meta: automated AI review - Copilot instructions encode our governance" \
  --body "Adds Copilot code review custom instructions so every PR gets an AI reviewer that knows our rules:

- .github/copilot-instructions.md - repo-wide: governance invariants (policy.yaml untouchable, ADRs append-only), claim hygiene (ADR-0004), formats-over-tools + vendor-death test (ADR-0006), knowledge-base maintenance (mind-map regeneration, retro-log append-only, size limits), validator conventions, prompt-injection review for skills, plain-language product voice, and tier-smuggling detection in PR shape.
- .github/instructions/validators.instructions.md - path-scoped for control-plane Python (determinism, path safety, failure honesty, fixture requirement).
- .github/instructions/docs.instructions.md - path-scoped for docs (labels, wikilinks, append-only zones, aspirational-vs-actual honesty).
- docs/dependencies.md - Copilot added with vendor-death verdict PASS (a reviewer, never data).

Another free rung on the self-hosting ladder (#19): the reviewer now enforces mechanically what was previously discipline. Note Copilot review is advisory - it cannot block merges; the required-status-check rung arrives with mini CI (#27/#28)."
echo PR-CREATED
git checkout -q main
