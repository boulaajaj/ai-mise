---
applyTo: "control-plane/**/*.py"
---

# Review instructions: control-plane Python

- These scripts are the deterministic backbone (ADR-0001: enforcement must not depend
  on model judgment). Review for determinism: sorted iteration, no wall-clock or
  random dependence in outputs, byte-stable regeneration.
- Every validator: JSON result object (validator/passed/detail), exit codes 0/1/2,
  stdlib-first, graceful degradation with an explicit non-passing result when an
  optional library is missing (see validate_policy.py) — never a silent pass.
- Path safety is load-bearing: any new file access must resolve paths and verify
  containment (pattern: escapes_root in protected_path_validator.py); reject
  symlinks in write paths.
- Failure honesty: a validator that cannot validate must say so and exit 2 —
  flag any code path that could return success without having checked anything.
- Tests: a new validator needs at least one passing fixture and one
  deliberately-failing fixture in the same PR.
