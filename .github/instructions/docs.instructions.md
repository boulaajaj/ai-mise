---
applyTo: "docs/**/*.md"
---

# Review instructions: documentation and knowledge base

- Verify claim labels ([verified] / [prior art] / [default]) on factual assertions
  about platform behavior, research findings, or third-party projects (ADR-0004).
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
