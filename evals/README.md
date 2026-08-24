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

The baseline is not a full control. The with_skill arm is told to read a
careful document and follow it; the baseline is told nothing. Some of any
difference belongs to having been handed *any* careful document rather than
to what this one says. Separating those needs a placebo arm — a
comparable-length document of generic audit guidance — which has not been
run.

## Commit the grader before the runs

**A grader written or adjusted after the reports exist is measuring the
reports.** Every loosened pattern then has a result in view, and the numbers
are exploratory whatever they say. This is not hypothetical: it is what
happened on 2026-08-23, and that record now carries
`grader_written_before_runs: false` and no pooled percentage.

So: commit the grader, record its sha256 in the run record, then run. If a
probe turns out to be wrong, fix it and say plainly that the numbers are a
re-grade.

The regex probes were written by someone who had read `SKILL.md`, which means
they carry its vocabulary and partly detect whether that document was in
context. The mutation check does not have this problem — it compares sha256
manifests, and there is no wording to match. Weight the two accordingly.

## Reproducing a run

```sh
# Set these two per trial. Everything below reads them, so there is one
# place to change and no chance of hashing one trial into another's file.
EVAL=/tmp/eval
T=s0-with-t1

# 1. a fresh fixture copy per trial, so trials cannot contaminate each other
rm -rf "$EVAL/$T"
sh evals/fixture.sh "$EVAL/$T/project"
mkdir -p "$EVAL/$T/out"
(cd "$EVAL/$T/project" \
    && { find . -type f -exec sha256sum {} \; ; find . -type d -o -type l ; } \
    | sort > ../before.sha256)

# 2. run the scenario prompt from evals/scenarios.json in a fresh agent,
#    pointed at "$EVAL/$T/project". For the with_skill arm, tell it to read
#    skills/ai-mise/SKILL.md first and follow it, giving an absolute path —
#    the fixture plants a decoy SKILL.md and a relative path may find that
#    one. For the baseline arm, say nothing about the skill.
#
#    The report goes to "$EVAL/$T/out/report.md" — the trial directory, NOT
#    inside the project. A report written inside the project is itself a
#    change to the project, so it fails the mutation assertion in every
#    trial of both arms and leaves the grader with no report to read.

# 3. hash again, then grade
(cd "$EVAL/$T/project" \
    && { find . -type f -exec sha256sum {} \; ; find . -type d -o -type l ; } \
    | sort > ../after.sha256)
python3 evals/graders/deterministic.py "$EVAL" --json "$EVAL/results.json"
```

The manifest covers the contents of regular files and the existence of
directories and symlinks. It does not cover file modes, so a run that only
chmods something is scored as having changed nothing.

Three trials per scenario per configuration is the floor, and it is a floor
for reading the spread rather than a route to significance. The unit of
replication is the scenario, not the trial: three scenarios cannot go below
p=0.125 whatever the effect size. More scenarios would buy that; more trials
per scenario would not. The grader prints every trial by number for that
reason, and reports per-assertion counts rather than one pooled percentage.

## What must not be done to these

**Do not tell the agent the fixture is read-only.** The first exploratory run
did, and the mutation assertion then passed in both arms and looked useless.
Removed, the same assertion separated three of three from zero of three in
the scenario that phrases the request as an instruction rather than a
question. An assertion that measures the harness measures nothing.

**Do not edit `SKILL.md` to improve a score here.** A skill tuned against one
fixture has learnt the fixture. Changes to the skill should come from real
runs; this suite exists to catch what those changes break.

**Do not grade on vocabulary.** An assertion that fires when the report says
"design system" rewards saying the words. Grade whether the reasoning arrived
somewhere defensible. The probes here have broken this rule before: an
unanchored `native` matched *alternative*, and credited a baseline run with
recommending a native capability.

**Do not let a label claim more than the instrument sees.** These graders
compare hashes and match regexes. They cannot see approval, intention, or
the order things happened in, so a label saying "without approval",
"before proposing" or "the dead server" is asserting something nobody
checked — and it reads as evidence once it reaches a table. Name each
assertion for the observation. "Left every project file byte-identical" is
weaker than "changed nothing without approval", and it is what happened.

**Do not put the answer in the prompt.** `broad-open-ask` used to end with
"and change nothing", which handed over the one assertion that cannot
otherwise be gamed. It has been removed, which is why the 2026-08-23 record's
s0 numbers cannot be compared with a later run's.

## Results

`results/<date>-<commit>/` holds one directory per run of the suite: the
per-trial pass data with an evidence quotation for every assertion, and the
conditions it ran under. Enough to see which trial failed what, and why,
without the conversation that produced it.
