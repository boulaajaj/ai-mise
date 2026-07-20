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
