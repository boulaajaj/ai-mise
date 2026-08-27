#!/usr/bin/env python3
"""Documented-trigger validator — the docs may not name a command that does not exist.

Claude Code namespaces a plugin's components as `plugin:component`, so a skill
shipped inside a plugin is reached as `/<plugin>:<skill>` and never as
`/<plugin>`. The install docs said the latter, which resolved to
`Unknown command` for anyone following them (#140).

This derives the real trigger from the manifests rather than from prose — the
marketplace's plugin name plus the skill's own frontmatter name — and then
holds the documentation to it. Two failure modes are reported separately:

    bare-name        a doc names `/<plugin>` where no such command is registered
    trigger-missing  a doc explains the plugin install route but never says
                     what to type afterwards

Deterministic by design: this runs as code, never as model judgment. The bare
name stays legal in `install.sh` prose, where the skill really is installed
under a chosen folder name and the bare word really is the trigger — so the
check looks for the plugin's own name, not for any bare word.

It objects to the bare form even where the surrounding sentence is disowning
it, and that is deliberate rather than a limitation: a reader scanning the
page for something to type finds the token, not the clause around it. Warn
about the mistake by describing it — "the plugin name on its own" — rather
than by printing it.

There is one legitimate exception. The two non-plugin routes — `install.sh`
and `gh skill install` — place the skill folder directly, so on those a bare
word really is the trigger, and documenting one of them with the default
folder name produces a correct `/ai-mise` that the rule above would reject.

Rather than guess from surrounding text which route a passage describes, the
prose says so, in a marked region:

    <!-- trigger-ok-start: why the bare name is correct here -->
    | gh skill install … | `/ai-mise` | everywhere |
    <!-- trigger-ok-end -->

Bare names inside such a region are allowed. The reason is required and is
read by nobody — it exists so that opening a region is a decision somebody
made and signed, rather than a way to silence the check. An unterminated
region, or one opened without a reason, is itself a violation: otherwise the
escape hatch could quietly swallow the rest of the file.

Usage:
    check_documented_trigger.py [--repo <dir>] [--doc <path> ...]

Exit codes: 0 = pass, 1 = violations found, 2 = invalid input.
"""
import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_DOCS = ("README.md", "INSTALL.md")

# The claude plugin install route, as the docs spell it. A doc that contains
# this is claiming the plugin route works, and therefore owes the reader the
# trigger that route produces.
PLUGIN_ROUTE = re.compile(r"claude plugin install", re.IGNORECASE)


def fail(message: str) -> None:
    print(json.dumps({"result": "error", "error": message}, indent=2))
    raise SystemExit(2)


def read_plugin_name(repo: Path) -> str:
    manifest = repo / ".claude-plugin" / "marketplace.json"
    if not manifest.is_file():
        fail(f"no marketplace manifest at {manifest.relative_to(repo)}")
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{manifest.name} is not valid JSON: {exc}")
    plugins = data.get("plugins") or []
    # Only a plugin sourced from this repository is one whose trigger these
    # docs are entitled to describe.
    local = [p for p in plugins if str(p.get("source", "")).strip("/.") == ""]
    if len(local) != 1:
        fail(f"expected exactly one repo-local plugin in {manifest.name}, found {len(local)}")
    name = local[0].get("name")
    if not name:
        fail(f"repo-local plugin in {manifest.name} has no name")
    return name


def read_skill_names(repo: Path) -> list[str]:
    names = []
    for skill_md in sorted((repo / "skills").glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            fail(f"{skill_md.relative_to(repo)} has no YAML frontmatter")
        name = re.search(r"^name:\s*(\S+)\s*$", match.group(1), re.MULTILINE)
        if not name:
            fail(f"{skill_md.relative_to(repo)} frontmatter has no name")
        names.append(name.group(1))
    if not names:
        fail("no skills found under skills/*/SKILL.md")
    return names


ALLOW_START = re.compile(r"<!--\s*trigger-ok-start:\s*(.*?)\s*-->")
ALLOW_END = re.compile(r"<!--\s*trigger-ok-end\s*-->")


def allowed_spans(text: str, rel: str) -> tuple[list[tuple[int, int]], list[dict]]:
    """Character ranges where a bare name is signed off, plus any misuse of the marker."""
    spans, violations = [], []
    ends = [m.start() for m in ALLOW_END.finditer(text)]
    for start in ALLOW_START.finditer(text):
        reason = start.group(1)
        line = text.count("\n", 0, start.start()) + 1
        if not reason:
            violations.append({
                "doc": rel, "line": line, "kind": "allow-without-reason",
                "found": start.group(0), "expected": None,
                "message": "trigger-ok-start must carry a reason",
            })
        after = [e for e in ends if e > start.end()]
        if not after:
            violations.append({
                "doc": rel, "line": line, "kind": "allow-unterminated",
                "found": start.group(0), "expected": None,
                "message": "trigger-ok-start with no matching trigger-ok-end",
            })
            continue
        spans.append((start.end(), after[0]))
    return spans, violations


def check_doc(path: Path, repo: Path, plugin: str, triggers: list[str]) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(repo).as_posix()
    spans, violations = allowed_spans(text, rel)

    # `/<plugin>` as a command, i.e. not preceded by a path or package
    # segment (`boulaajaj/ai-mise`, `~/ai-mise/…`) and not continuing into
    # `:skill` or a longer path.
    bare = re.compile(rf"(?<![\w.~-])/{re.escape(plugin)}(?![:\w/-])")
    for match in bare.finditer(text):
        if any(lo <= match.start() < hi for lo, hi in spans):
            continue
        line = text.count("\n", 0, match.start()) + 1
        violations.append({
            "doc": rel,
            "line": line,
            "kind": "bare-name",
            "found": f"/{plugin}",
            "expected": triggers[0] if len(triggers) == 1 else triggers,
            "message": (
                f"/{plugin} is not a registered command — a plugin's skills are "
                f"namespaced plugin:skill"
            ),
        })

    if PLUGIN_ROUTE.search(text) and not any(t in text for t in triggers):
        violations.append({
            "doc": rel,
            "line": None,
            "kind": "trigger-missing",
            "found": None,
            "expected": triggers[0] if len(triggers) == 1 else triggers,
            "message": (
                "doc documents the claude plugin install route but never names "
                "the trigger it produces"
            ),
        })

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: the repo this script lives in)")
    parser.add_argument("--doc", type=Path, action="append", dest="docs",
                        help="documentation file to check; repeatable "
                             f"(default: {', '.join(DEFAULT_DOCS)})")
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not repo.is_dir():
        fail(f"--repo is not a directory: {repo}")

    plugin = read_plugin_name(repo)
    triggers = [f"/{plugin}:{skill}" for skill in read_skill_names(repo)]

    docs = args.docs or [repo / name for name in DEFAULT_DOCS]
    violations = []
    for doc in docs:
        doc = doc if doc.is_absolute() else repo / doc
        if not doc.is_file():
            fail(f"no such documentation file: {doc}")
        violations.extend(check_doc(doc, repo, plugin, triggers))

    print(json.dumps({
        "result": "fail" if violations else "pass",
        "plugin": plugin,
        "valid_triggers": triggers,
        "docs_checked": [
            (d if d.is_absolute() else repo / d).relative_to(repo).as_posix() for d in docs
        ],
        "violations": violations,
    }, indent=2))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
