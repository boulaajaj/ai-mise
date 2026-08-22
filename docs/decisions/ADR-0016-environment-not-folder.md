# ADR-0016: AI-Mise starts from the environment, not from a folder

**Status:** Accepted · 2026-08-21 (proposed 2026-08-05)
**Trigger:** Amine's message, 2026-08-05, relaying an extended design exchange with another assistant and narrowing the product's scope by hand: it generates the best supporting arrangement it can for the person's problem, it is triggered rather than ambient, and it keeps track of everything it has built. Not all of that is decided here. Review of a first draft found it deciding five things at once; this record keeps the two that are genuinely one decision, and the rest is listed under *What this record does not decide* and settled elsewhere.

## Context

The constitution's `identity.boundary` opens *"Given a folder of real project materials"* **[verified]**. Every downstream document inherits that opening, and it decides more than it looks like it decides: it says the first thing AI-Mise meets is content. Read a folder, infer a domain, propose a workspace.

That was true of the product as first conceived and it is no longer true of the product being built. [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 2 already made the empty room — no folder, no domain, no materials — the exit test for Phase 1, on the grounds that it is the harder and more honest case. [[ADR-0010-where-workspaces-live|ADR-0010]] already treats starting from nothing and starting from something as two flows, not one flow with an optional input. #85 already puts capability discovery before reading anything **[verified]**. The repository moved; the sentence that governs it did not.

The gap matters because of what it licenses. A product that starts from a folder can propose anything that sounds right for the domain it inferred, and discover at build time that the host cannot do it. A product that starts from the environment knows what it may promise before it promises anything. The difference is not emphasis. It is the order of two operations, and getting it backwards is how a plan becomes an apology.

## Decision

Both decisions below are *[default]* — chosen product behavior, not derived from research.

1. **The starting point is the environment, not a folder.** The first thing AI-Mise establishes is what this setup can actually do; materials, when there are any, are read after that and in light of it. Capability is a state rather than a fact — something may be unsupported, detected, available, configured, authorized, tested or failing, and *detected is not tested*. A tool that is installed and has never run here is not yet proven, and anything proposed on its strength says so. AI-Mise never runs a tool merely to demonstrate that the tool exists: a probe must be safe and free, or the capability stays unproven and the person is told which one it is. Existing materials remain a first-class case, not a special one — [[ADR-0010-where-workspaces-live|ADR-0010]]'s two flows both still hold, and this decision governs which question comes first in each of them, not whether folders are allowed.

2. **It is summoned, and it does nothing unbidden.** The person calls it by name. It does not watch, does not act on its own initiative, and is not present between invocations. Recurring work is not excluded by this and is not decided here (#110); wherever it exists, it exists because a person declared it.

## What this record does not decide

Three things travelled with the trigger and are decided elsewhere, because each is a separate argument that would otherwise have hidden inside this one.

- **What AI-Mise promises, and how the promise is checked.** Raised as #80, since folded into the first pilot (#18) and now the subject of the evaluation work. The existing baseline stands: a proposal is compared against plain `/init` on the same materials, with the task, baseline, metric and target fixed before the run. No global threshold belongs in `policy.yaml` yet.
- **What is remembered across workspaces.** Raised as #109, since folded into #23. [[ADR-0013-local-history-by-default|ADR-0013]] governs history inside a workspace; the index across them is not built and is not decided here.
- **Standing requests, and what a run may never change.** Raised as #110, since folded into #23.

## What has happened since it was proposed

Both decisions shipped before this record was merged, which is the wrong way
round and worth saying plainly rather than tidying away. #124 rewrote the
skill so that it orients to the host before it reads anything belonging to
the person, and #125 made it an explicitly invoked skill, installed by name
on every host that takes one. So this record documents behaviour that already
exists rather than authorising behaviour that does not.

It is merged anyway. The decision is still the decision, and the alternative
is a product whose central choice is written down nowhere.


## Consequences

- `control-plane/constitution/policy.yaml`'s `identity.boundary` no longer describes the product, and nothing now reads it. The skill stopped resolving policy when it became the concierge (#124), and the control plane left the install altogether (#125). The sentence is still the person's to write and this ADR does not change it. What changed is the stake: a disagreement between that file and these decisions no longer compiles into anything.
- `docs/meta/direction.md` says AI-Mise *"quietly sets everything in place… and then gets out of your way"* **[verified]**. Decision 2 contradicts it directly. That page is not protected and can be corrected; the correction belongs with the documentation pass in #99.
- #85 gains the capability record decision 1 implies, rather than that record becoming an issue of its own.
- Nothing here requires a new phase scheme. The existing milestones already order this work; what they lacked was assignments, not structure.
- The word for decision 1's underlying model is deliberately absent from every surface a person sees. The model may be typed and explicit internally; the vocabulary for it belongs in [[architecture]], and [[METHOD]]'s rule about plain language everywhere the user looks governs the rest.

## Alternatives not taken

All five are *[default]* — product-choice reasoning, not research findings.

**Decide all five things here** — rejected on review: they arrived together but they are not one decision. Orientation and invocation are a single argument about what happens first. Measurement, cross-workspace memory and recurring work each carry their own trade-offs, and folding them in would mean agreeing to all five by merging one.

**Treat capability as a boolean** — rejected: installed and working are different, and collapsing them loses the difference exactly where it costs something. The cheaper version — record `true` once a tool is found — is what produces a plan that fails at build time, and that failure is what decision 1 exists to prevent.

**Prove capability by running the tool** — rejected: it is the reliable test and it is not free. Running something to see whether it runs can spend money, send a message, or change state the person did not agree to change. Where a probe is safe and free it is taken; otherwise the honest answer is that the capability is unproven, and saying so costs less than the alternative.

**Let it run in the background and surface when it has something** — rejected: it is the most requested shape and the one this product is least entitled to. Everything here is built on the person having said yes to a specific thing; a system that decides when to speak has already taken the first decision away. What is useful in it survives in #110: work can recur, if a person declared it and set the date it expires.

**Rewrite the boundary sentence in this ADR** — rejected: the control plane is protected, and a decision record that edits the constitution it answers to inverts the hierarchy. Proposing the wording in conversation and letting the person apply it costs one round trip and keeps the ordering intact.
