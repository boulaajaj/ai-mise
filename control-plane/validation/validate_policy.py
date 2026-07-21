#!/usr/bin/env python3
"""Validate policy.yaml against policy.schema.json (issue #2).

Requires pyyaml + jsonschema when available; degrades to structural checks
(required top-level keys, shadow-mode invariants) when they are not, so the
validator never silently passes on a machine without the libraries.

Usage: validate_policy.py --policy <policy.yaml> --schema <policy.schema.json>
Exit codes: 0 = pass, 1 = violations, 2 = invalid input / cannot validate fully.
"""
import argparse
import json
import sys
from pathlib import Path

REQUIRED_TOP = ["meta", "identity", "protected_assets", "approval", "interview",
                "placement", "self_improvement", "review", "provenance", "platform"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy", required=True, type=Path)
    ap.add_argument("--schema", required=True, type=Path)
    args = ap.parse_args()

    try:
        import yaml
    except ImportError:
        print(json.dumps({"validator": "validate_policy", "passed": False,
                          "detail": "pyyaml not installed; cannot parse policy — install pyyaml"}))
        return 2

    try:
        policy = yaml.safe_load(args.policy.read_text(encoding="utf-8"))
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001 - report any parse failure
        print(json.dumps({"validator": "validate_policy", "passed": False, "detail": f"parse error: {e}"}))
        return 2

    violations = []

    try:
        import jsonschema
        v = jsonschema.Draft202012Validator(schema)
        for err in sorted(v.iter_errors(policy), key=lambda e: list(e.absolute_path)):
            path = "/".join(str(p) for p in err.absolute_path) or "<root>"
            violations.append(f"{path}: {err.message}")
        mode = "full-jsonschema"
    except ImportError:
        for key in REQUIRED_TOP:
            if key not in policy:
                violations.append(f"missing top-level key: {key}")
        mode = "structural-fallback (install jsonschema for full validation)"

    # Cross-field invariants the schema cannot express
    si = policy.get("self_improvement", {})
    ap_ = policy.get("approval", {})
    if si.get("mode") == "shadow" and ap_.get("auto_approve"):
        violations.append("self_improvement.mode is 'shadow' but approval.auto_approve is non-empty (ADR-0003 violation)")

    result = {"validator": "validate_policy", "mode": mode, "passed": not violations,
              "detail": "; ".join(violations) if violations else "policy validates clean"}
    print(json.dumps(result, indent=2))
    return 0 if not violations else 1


if __name__ == "__main__":
    sys.exit(main())
