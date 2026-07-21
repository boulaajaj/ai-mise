# Dependency register — vendor-death test (ADR-0006)

Question per dependency: *if this vendor disappears in six months, what do we lose?*
Only acceptable answer: a renderer — never the data. New dependencies must add a row in the same change that introduces them.

| Dependency | Role | If it vanishes, we lose | Verdict |
|---|---|---|---|
| Markdown + YAML frontmatter | canonical data format | nothing — open standards, plain text | PASS (foundation) |
| git | version history, restore | nothing proprietary — local repos are self-contained; any git implementation reads them | PASS |
| GitHub | remote hosting, issues, Mermaid rendering | hosting + issue tracker; all data (repo, decisions in-files) survives locally; issues are the only GitHub-resident data → mitigate later with periodic issue export | PASS with note |
| Mermaid | mind-map renderer | the picture, not the graph — edges live in markdown links; regenerate to any other renderer | PASS |
| Obsidian / Logseq / Foam | optional viewers | a nicer view; zero data | PASS |
| Python (stdlib) | validators, generators | tooling convenience; scripts are replaceable; data untouched | PASS |
| pyyaml / jsonschema | full-strength validation | strict validation; validators degrade gracefully (validate_policy.py fallback mode) | PASS |
| Claude Code | primary runtime (adapter target) | the runtime — workspace remains readable/usable as plain files; adapter thesis (ADR-0001) exists precisely for this | PASS by design |
| gh CLI | GitHub automation | convenience; replaceable by API/web | PASS |
| GitHub Copilot code review | automated PR reviewer | a reviewer, never data — instructions are plain markdown in-repo; reviews are advisory | PASS |
| GitHub Actions (CI) | runs validators/scanners on every change | automation convenience — all checks are runnable locally (same scripts) | PASS |
| CodeQL | security scanning (free, public repos) | a scanner — findings are advisory copies, code untouched | PASS |
| Semgrep (OSS rules) | pattern scanning, tokenless, advisory | a scanner — nothing canonical | PASS |
| Dependabot | dependency update alerts | an alerting service — nothing canonical | PASS |
| SonarCloud (pending setup) | code-quality dashboard, free for public repos | a dashboard — requires SONAR_TOKEN (see issue); data stays in repo | PASS (pending) |

Standing rule: anything that would flip a row to FAIL (canonical data inside an app database, a format only one vendor reads) is rejected at proposal time by the provenance/format validators (Phase 2+).
