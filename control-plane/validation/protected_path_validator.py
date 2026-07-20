#!/usr/bin/env python3
"""Protected-path validator — the first working control-plane validator.

Given a proposal JSON (proposal.schema.json) and the policy's protected-asset
globs, reject any transaction that touches a protected path, escapes the
workspace root via traversal or symlinks, or mixes governance/safety-tier
changes into a routine transaction.

Deterministic by design: this runs as code, never as model judgment.

Usage:
    protected_path_validator.py --workspace <dir> --policy <policy.yaml> --proposal <proposal.json>

Exit codes: 0 = pass, 1 = violations found, 2 = invalid input.
"""
import argparse
import fnmatch
import json
import sys
from pathlib import Path

try:
    import yaml  # pyyaml
except ImportError:  # minimal fallback: parse only the globs we need
    yaml = None

GOVERNANCE_TIERS = {"governance", "safety"}


def load_protected_globs(policy_path: Path) -> list[str]:
    text = policy_path.read_text(encoding="utf-8")
    if yaml is not None:
        data = yaml.safe_load(text)
        pa = data.get("protected_assets", {})
        return [g for group in pa.values() for g in group]
    # Fallback: naive extraction of "- path/**" lines under protected_assets
    globs, active = [], False
    for line in text.splitlines():
        if line.startswith("protected_assets:"):
            active = True
            continue
        if active and line and not line.startswith(" "):
            break
        s = line.strip()
        if active and s.startswith("- "):
            globs.append(s[2:].split("#")[0].strip())
    return globs


def is_protected(rel_path: str, globs: list[str]) -> bool:
    p = rel_path.replace("\\", "/").lstrip("./")
    for g in globs:
        if fnmatch.fnmatch(p, g) or fnmatch.fnmatch(p, g.rstrip("/**") + "/*") or p == g.rstrip("/**"):
            return True
        # match directory prefix for `dir/**` style globs
        base = g[:-3] if g.endswith("/**") else None
        if base and (p == base or p.startswith(base + "/")):
            return True
    return False


def escapes_root(workspace: Path, rel_path: str) -> bool:
    """True if rel_path resolves outside the workspace root (traversal or symlink escape)."""
    candidate = (workspace / rel_path)
    try:
        resolved = candidate.resolve()
    except OSError:
        return True
    try:
        resolved.relative_to(workspace.resolve())
        return False
    except ValueError:
        return True


def validate(workspace: Path, policy: Path, proposal: dict) -> list[str]:
    violations: list[str] = []
    globs = load_protected_globs(policy)
    risk = proposal.get("risk_category", "routine")

    for ch in proposal.get("changes", []):
        rel = ch.get("path", "")
        if not rel:
            violations.append("change with empty path")
            continue
        if escapes_root(workspace, rel):
            violations.append(f"path escapes workspace root: {rel}")
        if is_protected(rel, globs):
            violations.append(f"protected path: {rel}")
        target = workspace / rel
        if target.is_symlink():
            violations.append(f"target is a symlink (write-through forbidden): {rel}")
        rename_to = ch.get("rename_to")
        if rename_to and (is_protected(rename_to, globs) or escapes_root(workspace, rename_to)):
            violations.append(f"rename target protected or escaping: {rename_to}")

    # Mixed-tier smuggling (threat scenario 29): a routine transaction must not
    # touch paths whose tier is governance-adjacent.
    if risk == "routine":
        sensitive_prefixes = ("generated/", "changes/", "decisions/ADR/")
        for ch in proposal.get("changes", []):
            p = ch.get("path", "").replace("\\", "/")
            if p.startswith(sensitive_prefixes):
                violations.append(
                    f"tier mismatch: '{p}' requires structural/governance risk category, transaction is 'routine'"
                )
    return violations


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, type=Path)
    ap.add_argument("--policy", required=True, type=Path)
    ap.add_argument("--proposal", required=True, type=Path)
    args = ap.parse_args()

    try:
        proposal = json.loads(args.proposal.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"INVALID INPUT: {e}", file=sys.stderr)
        return 2

    violations = validate(args.workspace, args.policy, proposal)
    result = {
        "validator": "protected_path_validator",
        "passed": not violations,
        "detail": "; ".join(violations) if violations else "no protected-path violations",
    }
    print(json.dumps(result, indent=2))
    return 0 if not violations else 1


if __name__ == "__main__":
    sys.exit(main())
