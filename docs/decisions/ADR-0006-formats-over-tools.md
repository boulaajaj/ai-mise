# ADR-0006: Commit to formats, not tools

**Status:** Accepted · 2026-07-21
**Trigger:** Amine's directive via chat-session handoff (HANDOFF — AI-Mise, Jul 21): tool-agnostic architecture is FINAL.

## Decision

1. **Canonical data is plain Markdown + `[[wikilinks]]` + YAML frontmatter.** Nothing canonical may live in a proprietary app format or app database. (This tightens ADR-0002's OKF alignment into a hard rule.)
2. **Viewers are optional, never dependencies.** Obsidian, Logseq, Foam, VS Code — all are welcome renderers of the same files. The repo and every generated workspace must remain fully usable with grep, any editor, and any LLM. Issue #22 ("Obsidian-compatible views") is hereby refactored: the deliverable is a wikilink-linked markdown graph; Obsidian compatibility is a consequence, not the target.
3. **The mind map is a generated view, never hand-authored.** Derive Mermaid (`graph`/`mindmap`) blocks from the wikilink/link graph, commit the generated output (Mermaid renders natively on GitHub), regenerate on change. Generator: `tools/generate_mindmap.py`; output: `docs/mindmap.md`.
4. **Vendor-death test for every dependency:** "If this vendor disappears in six months, what do we lose?" The only acceptable answer: *a renderer — never the data.* Results recorded per dependency in `docs/dependencies.md`; new dependencies must add an entry in the same change.

## Consequences

- Issues #22 and #27 reworded to format-first language (flagged to Amine per the handoff directive).
- A views/wiki emitted by the compiler uses wikilinks as the canonical link syntax; adapters may additionally emit tool-specific conveniences, but only as projections.
- `docs/dependencies.md` becomes a standing artifact; the threat suite's scope note gains a sibling: data-liberation is testable (open the workspace with zero installed tools beyond a text editor).
