# ADR-0011: An exit test names a capability, not a project

**Status:** Proposed · 2026-07-27 (merge = agreement)
**Trigger:** #58 defers the Arduino comparison and makes a blank-slate bootstrap the first trial. Phase 1's recorded exit test is "it examines the Arduino materials and produces a proposal you would seriously consider approving." The trial we intend to run has no definition of passing, and the definition we do have describes a pilot that is not happening.

## Context

Arduino Digger was the first real project on hand, so it became the fixture, then the baseline, then the acceptance criterion — three jobs, acquired one at a time and never separately decided. That is how the domain lean of #57 reached the place it does the most damage: the criteria that say when we are done.

A fixture that is also the exit test cannot fail in the way that matters. If the product only ever has to satisfy the project it was built beside, "it works" and "it works here" are indistinguishable, and the first person from another profession becomes the experiment we never ran.

The correction is not to delete the pilot. Concrete material is how shapes get checked against something real rather than against our imagination of it — the same reason the approval fixtures keep their content (#57). The correction is to stop letting the fixture set the bar.

## Decision

All decisions below are *[default]* — chosen product behavior, not derived from research.

1. **An exit test names a capability, never a project.** A phase is done when the product does the thing for a case it has not met, in words the person understands. A named project may illustrate a phase; it may not define the phase's exit.

2. **Phase 1's exit test is the empty room.** From nothing — no folder, no domain, no materials — the product reaches a proposal the person would seriously consider approving, and shows no lean toward any profession (#57, #58). This is the harder case and the more honest one: with nothing to read, everything the product says came from the product.

3. **First contact has two cases, and each exit test says which it means.** Starting from nothing and starting from something that already exists are different flows with different failure modes ([[ADR-0010-where-workspaces-live|ADR-0010]]). An exit test that does not say which case it covers is not an exit test.

4. **The golden thread is a fixture and is named as one.** It stops being a requirement running through every phase and becomes what it always was: concrete material to measure against, kept for the later comparison #58 preserves. A fixture earns its place by catching things. It does not get to say when we are finished.

5. **Baselines compare like with like.** The utility row of the scorecard measures against plain `/init` on the same materials, whatever those materials are — not against one hand-built workspace. A baseline that exists for exactly one project measures that project.

## Consequences

- Phase 1 gains an exit test that can be run today (#58) and loses one that could not be run at all.
- Phase 3 needs the same treatment and gets it here: a generated workspace performs a useful task better than plain `/init` on the same materials, without violating protected paths.
- The blank-slate flow now has a bar to clear before it is written. That order is what keeps a trial honest — voice, question discipline and patience are all easy to rate generously once you have already seen the transcript.
- The Arduino comparison is not lost. It returns as a measurement against baselines when there is something worth measuring (#4, #58).
- Nothing in [[ADR-0010-where-workspaces-live|ADR-0010]] changes. This decides how the two workflows it describes are judged, not what they are.
- [[architecture]] sections 8 and 9 are updated to match, [[HANDOFF]] stops pointing the next session at a deferred pilot, and `control-plane/evaluation/baselines/README.md` now describes one baseline captured per case rather than two captured once.

## Alternatives not taken

**Keep the golden thread as the exit test and add a blank-slate test beside it** — rejected: two exit tests, one of them a project we are not currently working on, is a phase that never exits. The instinct behind it, not losing the end-to-end discipline, is kept by decision 4.

**Write exit tests per domain as pilots arrive** — rejected: it makes generality the thing we verify last, after the architecture has already been shaped around whoever came first. #57 exists because that had begun happening.
