# Dev retrospective log (append-only)

Format: see `dev-harness.md`. Shadow mode: entries propose, never change.

## 2026-07-20 — Phase 0 scaffold (Cowork session)

- What shipped: repo skeleton; policy.yaml; proposal/receipt schemas; 34 threat
  scenarios; protected-path validator (self-tested); inspector skill +
  inventory script (self-tested); ADRs 0001–0004; architecture v2; meta-harness.
- Corrections received: external review (friend) — adopted via ADRs 0001–0004.
  Cowork sandbox GitHub proxy blocks repo creation → GitHub setup moved to a
  handoff script (`setup/setup-github.sh`).
- Diagnosis: blueprint v1 lacked a real control boundary (fixed, ADR-0001);
  base64 file transfer between environments is corruption-prone — prefer
  text-exact writes or git as the transfer medium.
- Proposals: none beyond filed issues yet; first working session should append
  the next entry.
- Rejected previously, do not re-propose: applying retrospective changes
  automatically (ADR-0003); wiki as source of truth (ADR-0002).

## 2026-07-20 — Rename to AI-Mise + prior-art intake + ADR-0005 (Cowork session)

- What shipped: repo renamed from the original working name to ai-mise (GitHub
  redirect active); full internal reference sweep; docs/prior-art.md
  (12-project watchlist with 6 reuse decisions to file as issues); ADR-0005
  (Builder vs Workspace as two enforced conversational identities, from
  Amine's observation).
- Corrections received: Amine rejected two rounds of naming (craft-metaphor,
  then developer-jargon) — lesson recorded: names must pass the "any human,
  first read" test, which is also the product's own plain-language rule.
- Diagnosis: we named the product before applying its own non-technical-surface
  principle to the name itself. The principle was in the README the whole time.
- Proposals: file the 6 reuse-decision issues from prior-art.md; add threat
  scenario 35 (workspace session acts on structural instruction without
  handoff) to scenarios.md next session.
- Rejected previously, do not re-propose: metaphor names; jargon names;
  base64 cross-environment file transfer.

## 2026-07-21 — Old-name purge (user-directed history edit)

- Amine directed a full purge of the pre-rename working name from the repo
  (chose purge over archive when asked). This entry's predecessor was reworded
  accordingly — a user-initiated exception to append-only, recorded here so
  the history edit is itself in the history.


## 2026-07-21 — PR-only flow (correction from Amine)

- Correction received: Amine caught the repo committing directly to main —
  "ai-mise should do as it says others should do." A textbook self-hosting
  ladder violation: we preached no-unreviewed-mutations while pushing straight
  to the trunk.
- Fix shipped: branch protection on main (PRs required, enforced for admins,
  no force-push, no deletion); CLAUDE.md rule added; dev-harness mapping
  updated — the PR is the proposal, Amine's merge is the approval receipt.
  This entry itself lands via the first PR.
- Diagnosis: the gap existed because the dev harness was discipline, not
  enforcement (already noted in issue #19's ladder comment) — but this rung
  needed no new machinery, only GitHub settings, so there was no excuse to
  wait for Phase 2. Lesson for the product: when an enforcement rung is free,
  climb it immediately; "later" is only legitimate when machinery is missing.
- Proposals: when mini CI ships (#27/#28), add it as a required status check
  on main so validators gate merges mechanically.

## 2026-07-21 — Review loop live + free scanners (Cowork session)

- What shipped: Copilot review instructions (PR #30) + auto-review ruleset;
  mini CI with validator self-test and mind-map freshness (PR #31, closes the
  automation half of #28); CodeQL, Semgrep (advisory), Dependabot; secret
  scanning + push protection enabled; SonarCloud setup filed (needs Amine).
- Corrections received: Amine — activate the full review loop (request →
  wait → fix → reply → resolve → re-review) and keep the record in threads.
  Done: PR #30's em-dash finding fixed, replied with root cause, thread
  resolved; same class fixed proactively on #31 before review.
- Corrections from reality: one-time helper scripts got committed into PR
  branches twice (git add -A before cleanup). Lesson: helper scripts live
  outside the worktree or in .gitignore. Also: retro-log appends now require
  a PR since main is protected — the ladder creating exactly the friction it
  predicted; acceptable, batch entries with session-end PRs.
- Arduino-DiggerSetup inspected (found on GitHub, public): 13 workflows,
  self-testing wiki-lint, advisory/strict convention — two patterns reused
  into our CI same-day. It is the manual baseline in living form (issue #1).
- Proposals: make ci.yml a required status check once green on main;
  gitignore one-time scripts.


## 2026-07-23 — Direction review 1 (triggered by Amine: "we are already failing at our own repository")

- What was attempted / what shipped: direction retrospective as a procedure
  (mission / constraints / opportunities); docs/meta/direction.md created as
  the living executive summary; repo description rewritten in plain language;
  persona-first extensions recorded on #46 and #20; recurrence issue filed (#52).
- Corrections received (from Amine): repo description spoke compiler jargon
  to humans; session reports used insider words ("canon"); retrospectives
  redefined as daily-orientation procedures — the set-everything-in-place
  ritual the product is named for.
- Diagnosis: the voice rule was enforced on product surfaces but not on our
  own public description and reporting — the gap was ours, not the rules'.
- Proposals: direction reviews recur at trigger points (tracked in the new
  issue); the any-human bar applies to every outward-facing sentence,
  including session reports.
- Rejected previously, do not re-propose: modes; per-merge human approval
  (standing delegation + re-review rule); calendar retrospectives.

## 2026-07-24 — self-attribution, and the wrong fix for it

- Correction: the credits register named the repo owner. Removed. Authorship in
  your own repo is the default — a credit line for the owner is labeling every
  room of your own house with your name.
- Second correction, same day: the first fix was worse than the defect. It wrote
  the absurdity down as a rule — a clause in the standing rule, a reviewer check
  — so this exact case would be caught forever. Amine: "If something goes
  without saying, that means we don't encode it." A repo that adds a line per
  obvious thing ends at millions of lines and still misses the next one. Both
  additions were reverted; only the deletion stands.
- Class: rules substituting for judgment. First as literal compliance against
  obvious context, then as encoding obvious context. Same root — treating the
  kernel as where understanding is stored, when it holds only what must be true.
- No rule was added. This entry is evidence, not policy: material for failure
  clustering and the judge/eval work, where a judgment miss belongs — measured
  as whether general judgment improved, not patched case by case.

## 2026-07-28 — one skill instead of two, and two reviewers being right differently

- What shipped: PR #90 (claim labels); PR #95 — `skills/ai-mise` replaces
  `skills/inspector` and `skills/blank-slate` (ADR-0012 decision 4), every live
  pointer updated, `inventory.py` moved across unchanged; issue #96 filed for
  what the review found in it.
- Diagnosis worth keeping: the two skills were split on whether a folder
  exists, which forced the model to choose a skill at the one moment it could
  not know — before it had looked. The merge was not a concatenation: two rules
  that existed twice became one that says more. Provenance stopped being a
  property of the circumstance and became a property of every sentence, which
  is what it always was; the injection guard stopped being about files and
  became about instructions, which now also covers entry points neither
  original anticipated.
- Correction from review: CodeRabbit caught the skill restating "four-part"
  from policy.yaml in the same sentence that told the reader not to work from
  memory. Same class as the 07-24 entry from the other direction — not encoding
  the obvious, but keeping a second copy of the kernel and calling it a
  pointer. A pointer that repeats the value is a copy.
- Copilot caught a script path that could not resolve, and proposed a fix that
  would have hardcoded a repo layout the skill stops living in the moment
  anyone installs it. The observation was right and the direction was wrong;
  taking the whole comment would have shipped a defect that only appears in the
  deployment we have not tested yet.
- Friction, recorded not solved: CodeRabbit's per-developer limit turned two of
  five review cycles into no-ops, and three of its four findings failed to post
  as threads — the review existed only inside a summary body. A finding with no
  thread has no disposition unless someone writes one by hand, and nothing in
  the flow notices that it is missing.
- Proposals: pause CodeRabbit's automatic incremental review so the allowance
  goes to substantive pushes rather than three-line doc corrections; consider
  whether a review whose comments failed to post should block a merge, given
  that today it merely looks like a quiet review.
