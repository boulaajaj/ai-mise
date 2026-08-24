# Agent evals for AI-Mise

AI-Mise is a multi-step agent behaviour, so what is measured here is behaviour
rather than output text. These are **agent evals**, run under
**eval-driven development**; the subset protecting behaviour AI-Mise is meant
to keep are its **behavioural regression evals**. They are not unit tests, and
calling them that would suggest a determinism they do not have. Deterministic
assertions appear inside them as graders.

Owned by #129. Run records for real pilots are #128.

## Why there is a baseline

Every scenario runs twice: once with the skill and once without it, same
prompt, same fixture. Without that column there is no way to tell whether
AI-Mise found something or whether a capable model would have found it anyway.
The first exploratory run answered that uncomfortably — several planted
defects were found equally well in both arms — and that is worth knowing.

## Reproducing a run

```sh
# 1. one fixture copy per trial, so trials cannot contaminate each other
sh evals/fixture.sh /tmp/eval/s0-with-t1/project
mkdir -p /tmp/eval/s0-with-t1/out
(cd /tmp/eval/s0-with-t1/project && find . -type f -exec sha256sum {} \; \
    | sort > ../before.sha256)

# 2. run the scenario prompt from evals/scenarios.json in a fresh agent,
#    pointed at that project directory. For the with_skill arm, tell it to
#    read skills/ai-mise/SKILL.md first and follow it. For the baseline arm,
#    say nothing about the skill. The report belongs in the trial directory
#    and NOT inside the project: /tmp/eval/s0-with-t1/out/report.md, which
#    is ../out/report.md from where the agent is working. A report written
#    inside the project is itself a change to the project, so it fails the
#    mutation assertion in every trial of both arms and leaves the grader
#    with no report to read.

# 3. hash again, then grade
(cd /tmp/eval/s0-with-t1/project && find . -type f -exec sha256sum {} \; \
    | sort > ../after.sha256)
python3 evals/graders/deterministic.py /tmp/eval --json results.json
```

Three trials per scenario per configuration is the floor. Behaviour varies
between runs, so a single trial says almost nothing — but three is a working
minimum for a pilot, not a claim of statistical significance, and the spread
matters as much as the mean. The grader prints every trial rather than only
the average for that reason.

## What must not be done to these

**Do not tell the agent the fixture is read-only.** The first exploratory run
did, and the mutation assertion then passed in both arms and looked useless.
Removed, the same assertion separated 9/9 from 6/9 — every failure in the
scenario that phrases the request as an instruction rather than a question.
An assertion that measures the harness measures nothing.

**Do not edit `SKILL.md` to improve a score here.** A skill tuned against one
fixture has learnt the fixture. Changes to the skill should come from real
runs; this suite exists to catch what those changes break.

**Do not grade on vocabulary.** An assertion that fires when the report says
"design system" rewards saying the words. Grade whether the reasoning arrived
somewhere defensible.

## Results

`results/<date>-<commit>/` holds one directory per run of the suite: the
per-trial pass data with an evidence quotation for every assertion, and the
conditions it ran under. Enough to see which trial failed what, and why,
without the conversation that produced it.
