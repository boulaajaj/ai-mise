# ADR-0016: AI-Mise starts from the environment, not from a folder

**Status:** Proposed · 2026-08-05 (merge = agreement)
**Trigger:** Amine's message, 2026-08-05, relaying an extended design exchange with another assistant and narrowing the product's scope by hand: it generates the best supporting arrangement it can for the person's problem, it is triggered rather than ambient, and it keeps track of everything it has built, "logged in a repository sort of thing or a decision log of how everything changed and when." Two further instructions came with it — that recurring work should be possible only at the person's consent and only after establishing that the environment permits it, and that research already done should be recorded so the next session continues rather than restarts.

## Context

The constitution's `identity.boundary` opens *"Given a folder of real project materials"* **[verified]**. Every downstream document inherits that opening, and it decides more than it looks like it decides: it says the first thing AI-Mise meets is content. Read a folder, infer a domain, propose a workspace.

That was true of the product as first conceived and it is no longer true of the product being built. [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 2 already made the empty room — no folder, no domain, no materials — the exit test for Phase 1, on the grounds that it is the harder and more honest case. [[ADR-0010-where-workspaces-live|ADR-0010]] already treats starting from nothing and starting from something as two flows, not one flow with an optional input. #85 already puts capability discovery before reading anything **[verified]**. The repository moved; the sentence that governs it did not.

The gap matters because of what it licenses. A product that starts from a folder can propose anything that sounds right for the domain it inferred, and discover at build time that the host cannot do it. A product that starts from the environment knows what it may promise before it promises anything. The difference is not emphasis. It is the order of two operations, and getting it backwards is how a plan becomes an apology.

There is a second thing the folder framing quietly hid. If the unit of work is a folder, then history is history *within* one workspace, and [[ADR-0013-local-history-by-default|ADR-0013]] plus #8 and #11 already deliver that. If the unit of work is a person's environment over time, then AI-Mise builds more than one thing and something has to know what it has built. Nothing currently does **[verified]**.

And a third. The product's own promise has been *"the best possible"* arrangement, in various phrasings. That cannot be checked. [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 5 already refuses this at the level of AI-Mise's own scorecard — baselines compare like with like, against plain `/init` on the same materials. The same refusal has never been applied to what AI-Mise says about itself.

## Decision

All decisions below are *[default]* — chosen product behavior, not derived from research.

1. **The starting point is the environment, not a folder.** The first thing AI-Mise establishes is what this setup can actually do; materials, when there are any, are read after that and in light of it. Capability is established by running, not by finding: a tool that is installed and has never run is not yet a capability, and nothing may be proposed on the strength of one. Existing materials remain a first-class case, not a special one — [[ADR-0010-where-workspaces-live|ADR-0010]]'s two flows both still hold, and this decision governs which question comes first in each of them, not whether folders are allowed.

2. **It is summoned, and it does nothing unbidden.** The person calls it by name. It does not watch, does not act on its own initiative, and is not present between invocations. Where recurring work exists (decision 5), it exists because a person declared it, with a stop condition and a date on which it must be re-approved rather than quietly continuing.

3. **The promise is falsifiable, and "best" is not.** What AI-Mise claims is that what it proposes beats doing nothing, on the person's own work, against a measure chosen before the run. Not optimal, not best possible, not best-supported-under-current-evidence — those cannot be checked and every competitor claims them already. This is [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 5 turned outward, and #80's rule that a metric chosen after seeing the run is not a metric **[verified]**.

4. **What it builds is remembered across workspaces, not only within one.** An append-only record of every workspace produced: when, for what, on which host, under which policy version, and what has happened to it since. [[ADR-0013-local-history-by-default|ADR-0013]] governs history inside a workspace; this governs the index across them. It answers a question the product currently cannot: *what have you built me, and is any of it still alive.*

5. **Recurring work is possible, declared, and still only proposes.** Whether this environment can run anything on a schedule is discovered before the person is asked for permission to use it — asking consent for something the host cannot do wastes the person's attention while looking capable. What runs is declared in advance and separately from what it accumulates: a person writes the goal, trigger, sources, permissions, budget, expected output, verification, stop condition and review date; the system writes last run, next run, history, failure state and pause switch, and never the other way round. [[ADR-0003-shadow-mode-self-improvement|ADR-0003]] is unchanged and now load-bearing: a scheduled run produces proposals, and `auto_approve: []` still holds **[verified]**.

## Consequences

- `control-plane/constitution/policy.yaml`'s `identity.boundary` no longer describes the product. This ADR does not change it and cannot: the control plane is a protected asset and that sentence is the person's to write. Until it is rewritten by hand, the repository's own law and its decisions disagree, and the law wins wherever anything compiles from it.
- `docs/meta/direction.md` says AI-Mise *"quietly sets everything in place… and then gets out of your way"* **[verified]**. Decision 2 contradicts it directly. That page is not protected, so unlike the boundary sentence it can be corrected — by a separate pull request, not this one.
- #47's north-star sentence gains nothing and loses nothing; its qualifier *"through visible, reversible changes"* was already the right one **[verified]**.
- [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 5 gains a product-level twin, the same way [[ADR-0015-division-earns-its-place|ADR-0015]] decision 3 did. Three layers now compare against a like baseline: AI-Mise's own phases, the divisions AI-Mise proposes, and now the product's claim about itself.
- Four things are owed and none is built today: the capability record, the build log, the research ledger, and the job contract. All four were asked for by name. None is large.
- Nothing here requires a new phase scheme. The existing milestones already order this work; what they lacked was assignments, not structure.
- The word for decision 1's underlying model is deliberately absent from every surface a person sees. The model may be typed and explicit internally; the vocabulary for it belongs in [[architecture]], and [[METHOD]]'s rule about plain language everywhere the user looks governs the rest.

## Alternatives not taken

All five are *[default]* — product-choice reasoning, not research findings.

**Keep "the best possible harness"** — rejected: it is unfalsifiable, and the repository already knows it. The instinct behind it, that the ambition should be high, is kept by decision 3 — beating the person's real baseline on a measure fixed in advance is a harder promise than "best," not a softer one, because it can be lost.

**Let it run in the background and surface when it has something** — rejected: it is the most requested shape and the one this product is least entitled to. Everything here is built on the person having said yes to a specific thing; a system that decides when to speak has already taken the first decision away. Decision 5 keeps what is useful in it — work can recur — by requiring that a person declared it and set the date it expires.

**Rewrite the boundary sentence in this ADR** — rejected: the control plane is protected, and a decision record that edits the constitution it answers to inverts the hierarchy. Proposing the wording in conversation and letting the person apply it costs one round trip and keeps the ordering intact.

**Adopt the seven-phase scheme the exchange proposed** — rejected: a second phase vocabulary running beside Phase 0–6 gives every work item two possible homes and no required one. The ordering it proposed was good and is largely the existing ordering; it is recorded as a mapping rather than as a structure.

**Make the internal model a named product concept** — rejected: naming it invites the person to learn it, and the whole point of the surface is that they do not have to. The instinct behind it, that being explicit about how things relate beats guessing from surface plausibility, is kept — it is decision 1's second sentence, and it is enforced internally where accuracy costs the person nothing.
