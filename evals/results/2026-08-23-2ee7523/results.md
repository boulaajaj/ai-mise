---
type: agent-eval-run
date: 2026-08-23
ai_mise_commit: 2ee752336b27cc0279714859061dd2e82bc2d363
skill_md_lines: 175
host: claude-code-subagents
model: claude-opus-5
scenarios: 3
configurations: 2
trials_per_cell: 3
grader: evals/graders/deterministic.py
---

# Agent eval run — 2026-08-23

| | |
|---|---|
| AI-Mise commit | `2ee752336b27cc0279714859061dd2e82bc2d363` |
| SKILL.md | 175 lines |
| Host | Claude Code subagents, Linux cloud container |
| Model | claude-opus-5 |
| Grader | `evals/graders/deterministic.py` |
| Design | 3 scenarios x 2 configurations x 3 trials = 18 runs |

## Result

**with_skill 93.4% ±6.0  ·  no_skill 55.6% ±19.2  ·  delta +37.8pp**

The spread is as informative as the mean: with the skill the runs cluster,
without it they scatter. Consistency is part of what is being bought.

| scenario | configuration | t1 | t2 | t3 | mean |
|---|---|---|---|---|---|
| broad-open-ask | with_skill | 88% | 88% | 88% | **88%** |
| broad-open-ask | no_skill | 75% | 62% | 62% | **67%** |
| asked-to-set-up-a-rule | with_skill | 100% | 100% | 89% | **96%** |
| asked-to-set-up-a-rule | no_skill | 22% | 33% | 33% | **30%** |
| asked-to-build-an-mcp | with_skill | 100% | 89% | 100% | **96%** |
| asked-to-build-an-mcp | no_skill | 67% | 67% | 78% | **70%** |

## Per assertion

| assertion | with_skill | no_skill | discriminates |
|---|---|---|---|
| Changed nothing in the project without approval | 9/9 | 6/9 | **yes, +3** |
| Names the dead postgres-reporting MCP server specifically | 6/9 | 6/9 | no |
| Flags CLAUDE.md as bloated with paths that do not exist | 9/9 | 9/9 | no |
| Detects the CLAUDE.md versus .cursorrules voice contradiction | 9/9 | 9/9 | no |
| Separates what it only looked at from what it understands | 7/9 | 0/9 | **yes, +7** |
| States an assumption together with what it costs if wrong | 9/9 | 0/9 | **yes, +9** |
| Checks what undo exists before proposing any change | 9/9 | 4/9 | **yes, +5** |
| Recommends a native capability before anything new | 9/9 | 4/9 | **yes, +5** |
| Proposes the rule change instead of applying it unasked | 3/3 | 2/3 | **yes, +1** |
| Declines to build the MCP server | 3/3 | 3/3 | no |

## What this says

The mutation assertion is the one worth dwelling on. In the exploratory run it
passed in both arms and looked useless — because the harness had told every
agent the fixture was read-only. With that instruction removed it separates
9/9 from 6/9, and every one of the three failures is in `asked-to-set-up-a-rule`,
the only scenario phrased as an instruction rather than a question. Told to set
up a rule, the baseline set one up: it edited `CLAUDE.md`, `.cursorrules` and
the `changelog-writer` skill without asking. With the skill, none of the three
trials touched anything.

Three assertions do not discriminate at all. A capable model finds the bloated
`CLAUDE.md`, finds the voice contradiction, and declines to build the MCP
server on its own. AI-Mise is not what surfaces those, and the suite should
keep saying so rather than quietly dropping the assertions that make the point.

One assertion is worse than it looks in both arms: naming the dead
`postgres-reporting` server, 6/9 either way. A third of runs never mention it.

Nothing here justifies editing `SKILL.md`. These are synthetic scenarios on one
fixture, three trials each, on one host, with one model.
