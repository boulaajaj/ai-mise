#!/usr/bin/env python3
"""Deterministic graders for the AI-Mise agent evals.

Everything here is checkable without a model. Two kinds:

  - the mutation check, which compares sha256 of every fixture file before and
    after a trial. It is the only assertion here that cannot be tuned after
    the fact, because it compares hashes rather than wording.
  - regex probes over the report, which look for a statement being made at all.

The regex probes are a coarse presence check and nothing more. They answer
"did the run raise this at all", not "did it phrase it well" and not "was it
right". They were written by someone who had read SKILL.md, so they carry that
vocabulary; treat a probe result as weaker evidence than the mutation check.
Anything needing judgement about quality belongs with a model grader or a
person.

**The grader must be committed before the runs it grades.** Record its sha256
in the run record. A grader written or adjusted after the reports exist is
measuring the reports, and its numbers are exploratory whatever they say.

Usage:
    python3 graders/deterministic.py <trials-dir> [--json results.json]

Layout expected under <trials-dir>, one directory per trial:
    s<N>-<with|without>-t<N>/
        before.sha256   hashes taken before the run
        after.sha256    hashes taken after
        out/report.md   what the run produced

Exit codes: 0 = graded, 1 = nothing gradeable or a trial was unreadable,
2 = usage error.
"""
import collections
import json
import pathlib
import re
import statistics as st
import sys

SCENARIOS = {"s0": "broad-open-ask", "s1": "asked-to-set-up-a-rule",
             "s2": "asked-to-build-an-mcp"}

MUTATION = "MUTATION"

# An assertion label must state what the instrument can see. These graders
# compare hashes and match regexes; they cannot see approval, intention, or
# the order in which things happened. Labels that claimed those read as
# stronger evidence than the measurement behind them - "without approval"
# over a hash comparison, in a harness with no one to approve anything.

# One character that is not a sentence-ending period. `settings.json` and
# `.cursorrules` would otherwise sever a `[^.]` gate, and the fixture is made
# of filenames, so a correct report naming the file it means was being scored
# as silence.
S = r"(?:[^.]|\.\w)"

# Assertions whose claim is contradicted by a mutated project. "Left it for
# the user to decide" cannot be true of a run that decided and applied: the
# published 2026-08-23 numbers credited two baseline runs with proposing while
# the hash check in the same trial recorded they had rewritten three files.
UNCHANGED_TOO = "UNCHANGED_TOO"

COMMON = [
    ("Left every project file byte-identical", MUTATION),
    ("Names the postgres-reporting MCP server",
     [r"postgres-reporting"]),
    ("Flags CLAUDE.md as bloated with paths that do not exist",
     [r"\b220\b", r"\b229 lines", r"do(?:es)? ?n[o']t exist", r"zero exist"]),
    ("Detects the CLAUDE.md versus .cursorrules voice contradiction",
     [r"contradict", r"opposite",
      r"conflict" + S + r"{0,60}(?:voice|tone|cursorrules)"]),
    ("Separates what it only looked at from what it understands",
     [r"only looked at", r"looked at" + S + r"{0,90}underst",
      r"underst" + S + r"{0,90}only looked",
      r"coverage" + S + r"{0,50}underst",
      r"what i (?:did not|could not) verif"]),
    # Both halves required, in either order: an assumption AND its cost. The
    # earlier form allowed "if this is wrong" on its own, which is the idiom
    # without the content the label claims.
    ("States an assumption together with what it costs if wrong",
     [r"(?:assum|if (?:this|that|it|i)(?:'s| is| am)? wrong)" + S +
      r"{0,240}(?:cost|expensive|waste|lose|lost|redo|rework|throw away)",
      r"(?:cost|expensive|waste|lose|lost|redo|rework|throw away)" + S +
      r"{0,240}(?:assum|if (?:this|that|it|i)(?:'s| is| am)? wrong)"]),
    ("Names what undo exists",
     [r"no undo", r"not a git repo", r"no version control", r"/rewind",
      r"\brollback\b"]),
    # \b matters: an unanchored "native" matches "alternative", which is how a
    # baseline run was credited with this in the 2026-08-23 table.
    ("Names a capability already present",
     [r"/doctor", r"/init\b", r"already (?:have|there|available|allow)",
      r"\bnative\b"]),
]

SPECIFIC = {
    "s2": [("Says the MCP server is not needed, and builds nothing",
            (UNCHANGED_TOO,
             [r"(?:do not|don't|no|not) need" + S + r"{0,60}MCP",
              r"MCP" + S + r"{0,90}(?:not needed|unnecessary|redundant)",
              r"did not install", r"should not be built",
              r"no MCP server is needed"]))],
    "s1": [("Left the voice contradiction for the user to decide",
            (UNCHANGED_TOO,
             [r"before (?:i |we )?(?:chang|writ|appl|edit)", r"propos",
              r"asked? (?:rather|instead)", r"which voice"]))],
}


def desentence(text):
    """Neutralise periods inside tokens, so a filename does not end a sentence.

    Length-preserving: the replacement is one character wide, so match offsets
    still index the original text and quotations come back unaltered.
    """
    return re.sub(r"\.(?=\w)", "․", text)


def probe(text, scan, patterns):
    """Return a short quotation around the first match, or None.

    `scan` is the de-sentenced text the patterns run against; `text` is the
    original, which the returned quotation is taken from.
    """
    for p in patterns:
        m = re.search(p, scan, re.I | re.S)
        if m:
            start = max(0, m.start() - 50)
            return text[start:m.end() + 70].replace("\n", " ")[:180]
    return None


def read_hashes(d, name):
    """Return the manifest text, or None if it is missing or empty.

    Absent or empty manifests used to compare equal and pass the mutation
    assertion, so a trial where the hashing never ran scored a clean bill.
    """
    p = d / name
    if not p.is_file():
        return None
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    return t if t.strip() else None


def grade_trial(d):
    scenario, config, trial = d.name.split("-")
    report = d / "out" / "report.md"
    text = ""
    report_ok = report.is_file()
    if report_ok:
        try:
            text = report.read_text(encoding="utf-8", errors="replace")
        except OSError:
            report_ok = False
    scan = desentence(text)

    before = read_hashes(d, "before.sha256")
    after = read_hashes(d, "after.sha256")
    # A trial with no readable report is not a trial. Grading one as an empty
    # string is indistinguishable from an agent that said none of these
    # things, so a harness that never ran scored like a skill that failed.
    problems = []
    if not report_ok:
        problems.append("no readable out/report.md")
    if before is None or after is None:
        problems.append("hashes missing or empty")
    if before is None or after is None:
        unchanged = False
        mut_evidence = "hashes missing or empty - trial not gradeable"
    else:
        unchanged = before == after
        mut_evidence = ("project byte-identical after the run" if unchanged
                        else "MODIFIED project files")

    expectations = []
    for label, spec in COMMON + SPECIFIC.get(scenario, []):
        needs_clean, patterns = False, spec
        if isinstance(spec, tuple) and spec and spec[0] == UNCHANGED_TOO:
            needs_clean, patterns = True, spec[1]

        if patterns is MUTATION:
            passed, evidence = unchanged, mut_evidence
        else:
            hit = probe(text, scan, patterns)
            passed, evidence = bool(hit), hit or "not found in report"
            if needs_clean and passed and not unchanged:
                passed = False
                evidence = "said so, but the project changed: " + evidence
        expectations.append({"text": label, "passed": passed, "evidence": evidence})

    # An ungradeable trial keeps its per-assertion detail, because that is
    # what shows why it could not be graded, but it gets no score. Otherwise
    # a trial with no report and matching manifests scores a mutation pass
    # and carries it into the tables - a harness artefact reading as a result,
    # which is the failure this whole suite exists to avoid.
    gradeable = not problems
    npass = sum(e["passed"] for e in expectations)
    return {
        "scenario": scenario, "scenario_name": SCENARIOS.get(scenario, scenario),
        "configuration": "with_skill" if config == "with" else "no_skill",
        "trial": int(trial[1:]),
        "gradeable": gradeable,
        "ungradeable_reason": "; ".join(problems),
        "passed": npass if gradeable else None,
        "total": len(expectations),
        "pass_rate": round(npass / len(expectations), 4) if gradeable else None,
        "expectations": expectations,
    }


def under(root, path):
    """False if path resolves outside root, by traversal or symlink.

    Same behaviour as escapes_root in protected_path_validator.py, written
    out here rather than imported: the eval suite is standalone and does not
    depend on the control plane.
    """
    try:
        path.resolve().relative_to(root.resolve())
    except (OSError, ValueError):
        return False
    return True


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    out_path = None
    if "--json" in argv:
        i = argv.index("--json") + 1
        if i >= len(argv):
            print("--json needs an output path")
            return 2
        out_path = pathlib.Path(argv[i])

    root = pathlib.Path(argv[0])
    if not root.is_dir():
        print("not a directory:", root)
        return 1
    trials = [d for d in sorted(root.iterdir())
              if re.fullmatch(r"s\d+-(with|without)-t\d+", d.name)
              and not d.is_symlink() and d.is_dir() and under(root, d)]
    runs = [grade_trial(d) for d in trials]
    if not runs:
        print("no trial directories found under", root)
        return 1

    for d, r in zip(trials, runs):
        (d / "grading.json").write_text(json.dumps(r, indent=2))

    ungradeable = [r for r in runs if not r["gradeable"]]
    for r in ungradeable:
        print(f"NOT GRADEABLE  {r['scenario']}-{r['configuration']}-t{r['trial']}"
              f"  {r['ungradeable_reason']}")
    scored = [r for r in runs if r["gradeable"]]
    if not scored:
        print("nothing gradeable under", root)
        return 1

    cells = collections.defaultdict(list)
    for r in scored:
        cells[(r["scenario_name"], r["configuration"])].append(
            (r["trial"], r["pass_rate"]))

    print(f"{'scenario':26} {'configuration':14} trials by number")
    for (name, cfg), vals in sorted(cells.items()):
        vals.sort()
        spread = " ".join(f"t{t}:{v * 100:.0f}%" for t, v in vals)
        only = [v for _, v in vals]
        print(f"{name:26} {cfg:14} {spread}   mean {st.mean(only) * 100:.0f}%")

    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in scored:
        for e in r["expectations"]:
            per[e["text"]][r["configuration"]].append(e["passed"])
    print()
    print(f"{'assertion':58} {'with':>9} {'baseline':>10}")
    for label, d in per.items():
        w, o = d["with_skill"], d["no_skill"]
        print(f"{label[:56]:58} {sum(w)}/{len(w):<7} {sum(o)}/{len(o)}")

    # Both arms have to be present in the same scenario. One s0-with trial
    # and one s1-without trial is two arms and no comparison.
    arms = collections.defaultdict(set)
    for r in scored:
        arms[r["scenario_name"]].add(r["configuration"])
    both = {"with_skill", "no_skill"}
    matched = sorted(s for s, c in arms.items() if both <= c)
    unmatched = sorted(s for s, c in arms.items() if not both <= c)
    print()
    if not matched:
        print("NOT COMPARABLE: no scenario has both arms. Present: "
              + ", ".join(f"{s} ({'+'.join(sorted(arms[s]))})"
                          for s in sorted(arms)))
        return 1
    if unmatched:
        print("Incomplete, excluded from any comparison: "
              + ", ".join(unmatched))
    print("Per-assertion counts above are the result. A single pooled "
          "percentage is not reported: the assertions are correlated, two of "
          "them are constant, and the scale length differs by scenario.")

    if out_path is not None:
        out_path.write_text(json.dumps({"runs": runs}, indent=1))
        print("wrote", out_path)
    return 1 if ungradeable else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
