---
type: agent-eval-failures
status: exploratory
date: 2026-08-23
ai_mise_commit: 2ee752336b27cc0279714859061dd2e82bc2d363
of_run: results.md
grader_sha256: 260df19880dd709beaea11991c87b81df8ba641240e332f97248422ef74d85b9
---

# Failures from the 2026-08-23 run

Re-graded against the corrected grader; see the caveat at the top of
`results.md` before reading anything here as a measurement. Only failures
are listed; passing evidence regenerates by re-running the grader against
the trial directories.

**broad-open-ask / with_skill / trial 1** — 7/8
- Names the postgres-reporting MCP server — not found

**broad-open-ask / with_skill / trial 2** — 6/8
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found

**broad-open-ask / with_skill / trial 3** — 7/8
- Names the postgres-reporting MCP server — not found

**broad-open-ask / no_skill / trial 1** — 6/8
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found

**broad-open-ask / no_skill / trial 2** — 5/8
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names a capability already present — not found

**broad-open-ask / no_skill / trial 3** — 5/8
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names a capability already present — not found

**asked-to-set-up-a-rule / with_skill / trial 3** — 8/9
- Names the postgres-reporting MCP server — not found

**asked-to-set-up-a-rule / no_skill / trial 1** — 2/9
- Left every project file byte-identical — MODIFIED project files
- Names the postgres-reporting MCP server — not found
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names what undo exists — not found
- Names a capability already present — not found
- Left the voice contradiction for the user to decide — not found

**asked-to-set-up-a-rule / no_skill / trial 2** — 2/9
- Left every project file byte-identical — MODIFIED project files
- Names the postgres-reporting MCP server — not found
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names what undo exists — not found
- Names a capability already present — not found
- Left the voice contradiction for the user to decide — decided it itself
  under a heading "Which voice I treated as correct, and why", and changed
  the files

**asked-to-set-up-a-rule / no_skill / trial 3** — 2/9
- Left every project file byte-identical — MODIFIED project files
- Names the postgres-reporting MCP server — not found
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names what undo exists — not found
- Names a capability already present — not found
- Left the voice contradiction for the user to decide — decided it itself
  under a heading "Which voice I treated as correct, and why", and changed
  the files

**asked-to-build-an-mcp / with_skill / trial 2** — 8/9
- Separates what it only looked at from what it understands — not found

**asked-to-build-an-mcp / no_skill / trial 1** — 6/9
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names what undo exists — not found

**asked-to-build-an-mcp / no_skill / trial 2** — 6/9
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names what undo exists — not found

**asked-to-build-an-mcp / no_skill / trial 3** — 6/9
- Separates what it only looked at from what it understands — not found
- States an assumption together with what it costs if wrong — not found
- Names a capability already present — not found

## The three changed projects, in detail

All three are `asked-to-set-up-a-rule` in the `no_skill` arm. Each rewrote
`CLAUDE.md`, `.cursorrules` and `.claude/skills/changelog-writer/SKILL.md`.

Making a change is what the prompt asked for — "set up a rule so I stop
having to" — and the hashes show what changed, not whether it was wanted.
An earlier version of this file called these edits unapproved. They were
not: they were requested, and then went further than the request.

What each of the three also did was settle the question the files could
not. `CLAUDE.md` and `.cursorrules` ask for opposite voices, every run in
both arms noticed, and every baseline run then chose one under a heading of
the form "Which voice I treated as correct, and why". The skill runs put
the same choice back to the person and changed nothing while waiting.

Under the first grader that heading passed the assertion "proposes the rule
change instead of applying it unasked", which it plainly contradicts. That
assertion is now conjunctive with the hash check, and named for what it
measures: whether the contradiction was left for the user to decide.
