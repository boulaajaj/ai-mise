# Run record — <short name>

Owned by #128. One file per deliberate run. Plain Markdown, kept by whoever
ran it. No database, no schema validator, no server: the first question is
whether these are the right fields, and that is answered by writing a few real
records and seeing which stayed empty and which were wanted and missing.

**Fill the three sections in order, and do not move material between them.**
What AI-Mise was shown, what the evaluator expected, and what was noticed
afterwards are different kinds of evidence. Collapsed together, a run that
merely repeated something we told it reads as a run that worked it out.

---

## A — What AI-Mise had (visible to it during the run)

| | |
|---|---|
| AI-Mise commit | |
| Host and model | |
| Date | |
| Opening prompt, verbatim | |
| Files, folders and connectors it could reach | |
| Anything it was told beyond the prompt | |

Nothing from section B may appear here. If it does, the run is contaminated,
and recording that is better than quietly discarding it.

## B — What the evaluator expected (hidden from it)

Written **before** the run. Hypotheses to inspect behaviour against — not a
marking scheme, and not the correct answer.

- What we think the real problem is:
- What would count as recognising it:
- Behaviours we are watching for:
- What would make us call the run a failure:

## C — What actually happened (observed after)

**Its understanding of the goal**, in its words:

**Orientation** — what it established about the host before asking anything:

**Scans** — what it mapped, and which parts it went deep on:

**Coverage versus understanding** — which areas it only looked at, and which
it claimed to understand. Take this from its own report. If it did not
distinguish them, say so: that is itself a finding.

**Questions it asked** — and for each, what decision the answer would change:

**Assumptions** — and what each costs if wrong:

**Contradictions found, and evidence it could not get:**

**Recommendations:**

**Corrections the person had to make:**

**Outcome:**

**Failures and surprises:**

---

## D — What this suggests

One improvement hypothesis, at most two. Each becomes an eval case in
`evals/scenarios.json`, an existing issue, or nothing at all.

Prefer turning a failure into an eval case **before** changing `SKILL.md`. A
real failure fixed only in the instruction leaves nothing behind to catch it
coming back.

- Hypothesis:
- Where it goes (eval case / issue / nowhere):
