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
