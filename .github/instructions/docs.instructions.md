---
applyTo: "docs/**/*.md"
---

# Review instructions: documentation and knowledge base

- Verify claim labels on factual assertions about platform behavior, research
  findings, or third-party projects (ADR-0004). Two things this file deliberately
  does not reproduce, because both apply here in full and a rule written twice is a
  rule that will eventually disagree with itself: the label vocabulary and its exact
  written form, defined in the opening paragraph of `docs/architecture.md`, and the
  plain-language exemption, defined in `.github/copilot-instructions.md` §2.
- Cross-references: prefer `[[wikilinks]]` or standard markdown links over bare
  prose mentions so related documents stay reachable from one another (ADR-0006).
- `docs/decisions/` is append-only. A PR touching an existing ADR must be flagged
  unless it only changes Status via an explicit superseding ADR added alongside.
- `docs/meta/retro-log.md`: entries are append-only and dated; flag rewrites of
  prior entries.
- `docs/dependencies.md`: any PR introducing a tool, library, or service must add
  its vendor-death row here; flag if missing.
- Watch for scope drift: docs describing enforcement the code does not implement
  yet must say so plainly (the "discipline vs machinery" honesty rule) — flag
  aspirational text presented as current fact.
