# ADR-0014: Whether an assistant is warranted is decided, not assumed

**Status:** Proposed · 2026-07-30 (merge = agreement)
**Trigger:** #103 left open whether deciding *whether*, *which*, and *with what* belongs in the kernel. Amine's answer, 2026-07-30: yes. The directive it comes from: "It can also sense and conclude whether or not you need assistance and which assistant with which skills you need for a specific task, because this is really what AI-mise is about."

## Context

#103 put the claim on the README: some work does not need an assistant, saying so is a real answer, and where one would help the question is what it should be good at. It sits in `## What it sets out to do`, the section that says what the product is for.

[[METHOD]] does not say it. The orientation list runs from naming the domain, through learning the craft, to codifying the minimum and executing — and every step presumes something is being stood up. The one question whose answer could be "nothing" is not on the page.

The repository has the restraint version of this idea in three places, and it is easy to mistake that for the same thing. "Codify the minimum ... No more" bounds how much gets built. [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 2 bounds what becomes code. The voice section bounds what gets asked. All three assume the build is happening and argue about its size; none of them permits zero.

The gap is not academic. [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] exists because a fixture became the acceptance criterion one job at a time, with nobody ever deciding it. "This person needs an assistant" is the same shape of assumption one layer further in, and it is the one that would turn AI-Mise into something that builds workspaces because building workspaces is what it does.

## Decision

All decisions below are *[default]* — chosen product behavior, not derived from research.

1. **The kernel carries the judgement.** [[METHOD]]'s orientation list gains a step, placed before anything is codified: *decide whether a standing assistant is warranted at all, and if so what it must be good at. "None" is an answer. Work that judgement out rather than handing it back as a question.*

2. **It names a capability, never a product.** What the assistant must be *good at* — a careful reader of research and a careful drafter are different jobs — is the whole of the answer. Which vendor, model or feature provides it is an adapter's problem. This is [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 5 applied to the decision most likely to attract a product name.

3. **The person approves; they do not specify.** They say what they do. Working out what that needs is AI-Mise's job, not a menu handed back to them — and what comes back is a proposal they can decline.

## Consequences

- [[METHOD]] goes from 69 lines to 72, against the under-40 budget in #44. The page has been over since it was written and this does not fix it. #44 is where the kernel gets cut; this step is one of the things that should survive the cut.
- [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 2 asks Phase 1 to reach "a proposal the person would seriously consider approving." A proposal of "nothing standing yet, here is what to do instead" satisfies it — a phase that can only exit by building could not test this decision. Nothing in ADR-0011 changes.
- [[ADR-0005-builder-vs-workspace|ADR-0005]] gives the Builder and the assistant distinct identities and assumes both exist. Where none is warranted there is no second identity to name and no handoff to style. That ADR is not wrong; its scope is now stated.
- #46 has the person name their assistant. That step now sits behind this judgement rather than at the start of every setup.
- The README needs no change. #103 already says this, and the effect here is that the product page becomes a projection of the kernel rather than a claim the kernel does not carry.

## Alternatives not taken

**Leave it on the README** — rejected: the README says what the product does now, and is rewritten whenever that changes. The kernel is what an adapter gets checked against. A claim this central, living only on the most frequently rewritten page, has nothing holding it.

**Use the directive's own words, "which assistant with which skills"** — rejected: "which assistant" invites a vendor's name, which [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 5 rules out of all instruction. "What it must be good at" is the same judgement, expressed so that next month's launches do not date it.

**Ask the person which assistant they want** — rejected: it hands the hardest judgement to the person least equipped to make it, which is the premise the product exists to deny. The instinct behind it, that the person stays the authority, is kept by decision 3: they approve the proposal, they do not have to author it.
