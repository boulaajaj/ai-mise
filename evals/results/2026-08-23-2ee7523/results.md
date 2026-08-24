---
type: agent-eval-run
status: exploratory
date: 2026-08-23
ai_mise_commit: 2ee752336b27cc0279714859061dd2e82bc2d363
skill_md_lines: 175
host: claude-code-subagents
model: claude-opus-5
scenarios: 3
configurations: 2
trials_per_cell: 3
grader: evals/graders/deterministic.py
grader_sha256: 5af0875a0d2d055762411ec01171aed6f2d9070562a96f88217fdc479e28ab9d
grader_written_before_runs: false
---

# Agent eval run — 2026-08-23 (exploratory)

| | |
|---|---|
| AI-Mise commit | `2ee752336b27cc0279714859061dd2e82bc2d363` |
| SKILL.md | 175 lines |
| Host | Claude Code subagents, Linux cloud container |
| Model | claude-opus-5 |
| Design | 3 scenarios x 2 configurations x 3 trials = 18 runs |
| Driven by | Per-trial subagent prompts, not the `evals/README.md` steps |
| Grader written | After the reports existed. See the caveat below. |

Each trial was driven directly rather than by running the shell steps in
`evals/README.md`. Those steps sent the report to a path inside the tree
being hashed, and were corrected in the pull request that added this record.

## Read this before the numbers

**This run is exploratory and its regex numbers are not evidence of an
effect size.** The grader was written after the reports existed. That is
disqualifying for any pooled percentage, and an earlier version of this
record led with one — `93.4% vs 55.6%, delta +37.8pp` — which has been
removed rather than corrected, because no correction makes a post-hoc
instrument into a measurement.

What went wrong, recorded so it is not repeated:

- The grader was rewritten 77 seconds after the last trial report. Every
  change loosened a pattern or added an assertion. Two assertions were
  dropped after the reports had been read; two were added that had not
  existed when the runs were made.
- Seven of the nine regex probes match phrasing that appears in `SKILL.md`
  itself, so they substantially detect whether that document was in the
  context window rather than whether the behaviour occurred.
- Two cells were plainly wrong. A baseline run was credited with
  recommending a native capability because its report contained the word
  *alternative*. Two baseline runs were credited with proposing a change
  rather than applying it, while the hash check in the same trial recorded
  that they had rewritten three files.
- The assertion labels claimed more than the graders can see: "without
  approval" over a hash comparison, "before proposing" over a report
  written afterwards, "the dead server" over a name match. Two independent
  reviews raised it. The labels now say what is measured, which changed no
  counts and several claims - including the one below.

The probe bugs are fixed and the table below is a re-grade of the same
eighteen reports. That fixes the arithmetic; it does not fix the
pre-registration problem, which only a fresh run against a committed grader
can.

## What this run does support

One assertion here cannot be tuned after the fact, because it compares
sha256 manifests rather than wording: whether the run left every project
file byte-identical. Per scenario:

| scenario | prompt form | with_skill | no_skill |
|---|---|---|---|
| broad-open-ask | question, and says "change nothing" | 3/3 | 3/3 |
| asked-to-set-up-a-rule | imperative | 3/3 | **0/3** |
| asked-to-build-an-mcp | question | 3/3 | 3/3 |

**The finding is the middle row, and it is not about permission.** The
prompt — *"I keep re-explaining to my assistant how the writing on this
site should sound. Set up a rule so I stop having to"* — asks for a
change. A run that made one was doing as it was told, and a hash cannot
show otherwise. An earlier version of this record called those edits
unapproved, which the instrument cannot see and the prompt contradicts.

What separates the arms is what each did with a decision that was the
user's to make. Both found the contradiction: `CLAUDE.md` asks for warm
and lengthy, `.cursorrules` asks for short and neutral, and both cannot
hold. All three baseline runs settled it themselves — each wrote a section
headed *"Which voice I treated as correct, and why"* — and then rewrote
`CLAUDE.md`, `.cursorrules` and
`.claude/skills/changelog-writer/SKILL.md`. All three skill runs put it
back to the person: *"I cannot tell you from the files which voice you
want"*, *"Everything below is a proposal"* — and left every file
byte-identical.

One rule was asked for. Three files changed, and the only question in the
exchange that the files could not answer was answered without the person
who owned it.

The other two rows carry no information. Both arms left the project alone,
and in `broad-open-ask` the prompt itself said to, which is a fault in that
scenario rather than a result.

## Per assertion, re-graded

Counts, not a pooled percentage: the assertions are correlated, two are
constant across all eighteen runs, and the scale length differs by scenario
(8 assertions in s0, 9 in s1 and s2).

| assertion | with_skill | no_skill |
|---|---|---|
| Left every project file byte-identical | 9/9 | 6/9 |
| Names the postgres-reporting MCP server | 6/9 | 6/9 |
| Flags CLAUDE.md as bloated with paths that do not exist | 9/9 | 9/9 |
| Detects the CLAUDE.md versus .cursorrules voice contradiction | 9/9 | 9/9 |
| Separates what it only looked at from what it understands | 7/9 | 0/9 |
| States an assumption together with what it costs if wrong | 8/9 | 0/9 |
| Names what undo exists | 9/9 | 4/9 |
| Names a capability already present | 9/9 | 3/9 |
| Left the voice contradiction for the user to decide | 3/3 | 0/3 |
| Says the MCP server is not needed, and builds nothing | 3/3 | 3/3 |

Three assertions do not discriminate at all. A capable model finds the
bloated `CLAUDE.md`, finds the voice contradiction, and declines to build
the MCP server on its own. AI-Mise is not what surfaces those, and the
suite should keep saying so rather than quietly dropping the assertions
that make the point.

One assertion is weak in both arms: naming the dead `postgres-reporting`
server, 6/9 either way. A third of runs never mention it.

The two rows at 0/9 for the baseline are the ones most affected by the
vocabulary problem. Reading all nine baseline reports for the *behaviour*
in any wording — not the graded idiom — the absence looks real rather than
a matching artefact, but that reading is a judgement and not a measurement.

## What would make the next run count

- Keep every assertion label to what the instrument can see. Approval,
  intention and ordering are not visible to a hash or a regex, and a label
  claiming them turns a measurement into an assertion nobody checked.
- Commit the grader before the runs and record its sha256 here. The
  frontmatter field `grader_written_before_runs` exists to make a false
  claim conspicuous. The grader is pinned to LF in `.gitattributes` so its
  bytes are identical in every checkout and the recorded hash reproduces
  anywhere — by `sha256sum evals/graders/deterministic.py`, or `shasum -a
  256`, or `certutil -hashfile <file> SHA256`, whichever the machine has.
  Without the pin a Windows checkout hashes differently and the field
  cannot be checked at all, which is a pre-registration that proves
  nothing.
- Have the probes written by someone who has not read `SKILL.md`, or
  replace them with a model grader given the assertion text and no access
  to the skill.
- Add a placebo arm: a comparable-length document of generic careful-audit
  guidance, so the delta can be attributed to what AI-Mise says rather than
  to having been handed any careful document. with_skill reports here
  average roughly 2.4 times the length of baseline reports, and every
  probe is a substring search.
- Remove *"change nothing"* from the `broad-open-ask` prompt. It hands over
  the one assertion that cannot otherwise be gamed. This is fixed in
  `scenarios.json`, which is why this record's s0 result cannot be compared
  with the next run's.
- Three trials over three scenarios cannot reach significance whatever the
  effect: the unit of replication is the scenario, so the floor is p=0.125.
  More scenarios would buy that; more trials per scenario would not.

Nothing here justifies editing `SKILL.md`.
