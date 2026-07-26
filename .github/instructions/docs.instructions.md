---
applyTo: "docs/**/*.md"
---

# Review instructions: documentation and knowledge base

- Verify claim labels ([verified] / [prior art] / [default]) on factual assertions
  about platform behavior, research findings, or third-party projects (ADR-0004).
  Exemption: a page whose stated purpose is a plain-language surface for a
  non-specialist — README, skill outputs, proposal templates, and pages that say so
  under their title — carries no inline labels; its authority lives in the decisions
  it links to, so flag a missing link, not a missing label. **The exemption is per
  page, never per paragraph:** a design document does not become exempt by containing
  a friendly section, and ADR-0004 continues to govern it in full.
- Cross-references: prefer `[[wikilinks]]` or standard markdown links over bare
  prose mentions so the generated mind map stays connected (ADR-0006). If links
  changed, `docs/mindmap.md` must be regenerated in this PR.
- `docs/decisions/` is append-only. A PR touching an existing ADR must be flagged
  unless it only changes Status via an explicit superseding ADR added alongside.
- `docs/meta/retro-log.md`: entries are append-only and dated; flag rewrites of
  prior entries.
- `docs/dependencies.md`: any PR introducing a tool, library, or service must add
  its vendor-death row here; flag if missing.
- Watch for scope drift: docs describing enforcement the code does not implement
  yet must say so plainly (the "discipline vs machinery" honesty rule) — flag
  aspirational text presented as current fact.
