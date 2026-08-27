#!/usr/bin/env python3
"""Plugin-manifest validator — the things claude.ai's sync refuses, checked here first.

The CLI and the account sync do not enforce the same rules. `claude plugin
install` resolved this repo happily while adding the same marketplace through
claude.ai failed three times with "Marketplace sync failed", leaving an empty
marketplace on the account (#141). The CLI reads a real clone and is lenient
about where things sit; the server-side fetch is not.

So the rules the stricter path enforces are checked here, on every change,
rather than discovered by a person on a phone:

    manifest-missing    no .claude-plugin/plugin.json — it is the plugin
                        manifest location, and under the default strict mode
                        it is the authority for what the plugin contains
    name-mismatch       the manifest and the marketplace entry disagree about
                        the plugin's name, so the entry resolves to nothing
    version-mismatch    same, for a pinned version
    bad-relative-source a relative source that does not start with "./"
    source-escapes-repo a relative source that climbs out of the marketplace
                        root, and so points at something not shipped here
    reserved-bin        a top-level bin/ directory, which the account
                        distribution path rejects outright
    skills-missing      the plugin declares a skill directory that is not there

Deterministic by design: this runs as code, never as model judgment. It cannot
prove the sync succeeds — only this repo's owner can run that — but every rule
here is one the published plugin reference states, and each was failing or at
risk when it was written.

Usage:
    check_plugin_manifests.py [--repo <dir>]

Exit codes: 0 = pass, 1 = violations found, 2 = invalid input.
"""
import argparse
import json
import posixpath
import sys
from pathlib import Path


VALIDATOR = "plugin_manifests"


def fail(message: str) -> None:
    """Invalid input: the repo's validator shape, and exit 2."""
    print(json.dumps({"validator": VALIDATOR, "passed": False, "detail": message}, indent=2))
    raise SystemExit(2)


def load_json(path: Path, label: str) -> dict:
    """Parse a manifest, or fail as invalid input. Never returns a non-mapping."""
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{label} is not valid JSON: {exc}")
    # A list or a bare string parses fine and then meets .get() further down,
    # which would answer with an AttributeError rather than a result.
    if not isinstance(data, dict):
        fail(f"{label} must be a JSON object, found {type(data).__name__}")
    return data


def is_repo_local(source) -> bool:
    """True for a plugin shipped from this repository rather than fetched.

    Only ever asked about a source already known to be a string or an object,
    so an absent or malformed one cannot reach here and be read as "remote".
    """
    return isinstance(source, str)


def check(repo: Path) -> list[dict]:
    violations = []

    marketplace_path = repo / ".claude-plugin" / "marketplace.json"
    if not marketplace_path.is_file():
        fail("no .claude-plugin/marketplace.json")
    marketplace = load_json(marketplace_path, "marketplace.json")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        fail("marketplace.json must declare a non-empty plugins array")
    for position, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(f"marketplace.json plugins[{position}] must be an object, "
                 f"found {type(entry).__name__}")
        # Both fields are required by the schema. Left unchecked, a missing
        # source reads as "not a string" and the entry would be waved through
        # as remote — the validator skipping exactly what it is here to catch.
        if not isinstance(entry.get("name"), str) or not entry["name"]:
            fail(f"marketplace.json plugins[{position}] must have a name")
        if not isinstance(entry.get("source"), (str, dict)):
            fail(f"marketplace.json plugins[{position}] ({entry['name']}) must have a "
                 f"source that is a relative path or an object, found "
                 f"{type(entry.get('source')).__name__}")

    manifest_path = repo / ".claude-plugin" / "plugin.json"
    manifest = load_json(manifest_path, "plugin.json")

    for entry in entries:
        source = entry.get("source")
        name = entry["name"]

        if not is_repo_local(source):
            # Fetched from elsewhere; its manifest is not ours to validate.
            continue

        if not source.startswith("./"):
            violations.append({
                "kind": "bad-relative-source",
                "plugin": name,
                "found": source,
                "message": 'a relative source must start with "./"',
            })

        # A relative source resolves against the marketplace root, so one that
        # climbs out of it points at something this repository does not ship.
        #
        # Compared as path segments rather than as a string prefix: ".." is a
        # segment that climbs, while "..foo" is an ordinary directory whose
        # name happens to begin with dots, and startswith("..") cannot tell
        # them apart.
        normalised = posixpath.normpath(source)
        if normalised == ".." or normalised.startswith("../"):
            violations.append({
                "kind": "source-escapes-repo",
                "plugin": name,
                "found": source,
                "message": "a relative source must stay inside the repository",
            })
            continue

        # "./" means the plugin root is the repository root, which is the only
        # layout this repo uses. Anything deeper would need its own manifest
        # beside it, and that is a different check than this one.
        #
        # Compared exactly rather than with strip("./"), which removes any
        # run of "." and "/" from both ends and so would read "./.." — a
        # traversal out of the repository — as the repository root.
        if source not in ("./", "."):
            continue

        if not manifest:
            violations.append({
                "kind": "manifest-missing",
                "plugin": name,
                "found": None,
                "message": (
                    "no .claude-plugin/plugin.json — the CLI tolerates its "
                    "absence, the account sync does not"
                ),
            })
            continue

        if manifest.get("name") != name:
            violations.append({
                "kind": "name-mismatch",
                "plugin": name,
                "found": manifest.get("name"),
                "message": "plugin.json name does not match the marketplace entry",
            })

        entry_version, manifest_version = entry.get("version"), manifest.get("version")
        if entry_version and manifest_version and entry_version != manifest_version:
            violations.append({
                "kind": "version-mismatch",
                "plugin": name,
                "found": manifest_version,
                "message": f"plugin.json version {manifest_version} != marketplace {entry_version}",
            })

        if not (repo / "skills").is_dir():
            violations.append({
                "kind": "skills-missing",
                "plugin": name,
                "found": None,
                "message": "plugin root has no skills/ directory",
            })

    if (repo / "bin").is_dir():
        violations.append({
            "kind": "reserved-bin",
            "plugin": None,
            "found": "bin/",
            "message": "a top-level bin/ directory is rejected by account distribution; use scripts/",
        })

    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: the repo this script lives in)")
    args = parser.parse_args()

    repo = args.repo.resolve()
    if not repo.is_dir():
        fail(f"--repo is not a directory: {repo}")

    violations = check(repo)
    print(json.dumps({
        "validator": VALIDATOR,
        "passed": not violations,
        "detail": (
            "; ".join(f"{v['kind']}: {v['message']}" for v in violations)
            if violations else
            "manifests satisfy the rules the account sync enforces"
        ),
        "repo": repo.name,
        "violations": violations,
    }, indent=2))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
