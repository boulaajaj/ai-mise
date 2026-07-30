# ADR-0015: The work stays undivided until a division earns its place

**Status:** Proposed · 2026-07-30 (merge = agreement)
**Trigger:** Amine's message, 2026-07-30, relaying an exchange with another assistant that proposed a durable kernel principle — "choose the least complex arrangement capable of doing the work reliably" — and warned against writing today's component names into the kernel. The instruction with it: "Keep the method and kernel as principal as possible without being tied to any specific concept that might change within a month or two."

## Context

[[ADR-0014-whether-an-assistant-is-warranted|ADR-0014]] settled whether a standing assistant is warranted and what it must be good at. It did not settle how many parts the answer has. That is the next question down, and it is the one the surrounding ecosystem answers for you if you do not answer it first.

The repository already has the restraint idea, but only in scoped forms. [[METHOD]]'s orientation step 5 bounds how much gets codified. [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 4 bounds AI-Mise's own supporting skills — they appear when a real need appears, never in anticipation of one. Both are about AI-Mise. Neither is a general rule about dividing work, and neither reaches the thing AI-Mise builds for a person.

The pressure to split is not hypothetical, and it is already in this repository. [[prior-art]] records revfactory/harness, which turns a domain description into a complete agent team by choosing from six architectural patterns. A tool whose input is a description and whose output is a team has answered the question before anyone asked it. Doing that would make AI-Mise a generator of arrangements rather than a judge of them — the same failure [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] exists to prevent one layer up.

The current evidence is genuinely split, and a decision that pretended otherwise would not survive contact with it *[prior art]*. Anthropic, OpenAI and Microsoft each default to one worker and add on evidence; Anthropic reports teams spending "months building elaborate multi-agent architectures only to discover that improved prompting on a single agent achieved equivalent results." Google's ADK guidance says the opposite — reliability comes from decentralization and specialization. Weeks later Google Research measured 260 configurations across six benchmarks and found the effect swinging from +80.8% to -70.0% depending on how well the architecture fits the task, with sequential-reasoning tasks worse under every multi-agent variant tried. The measured answer is that it depends on the work. That is what a test is for, and what a default cannot do.

The durable form of the rule is much older than any of that *[prior art]*, and it points the same way: Parnas (1972) argued about where seams fall rather than how many there are; Ashby (1958) sets the floor, since a regulator cannot exceed its own capacity as a channel for variety; Stevens, Myers and Constantine (1974) named the failure mode as coincidental binding. The lineage and the sources are in [[foundations]].

## Decision

All decisions below are *[default]* — chosen product behavior. The prior art they draw on is *[prior art]*, named and linked in [[foundations]]; none of it settles the choice on its own.

1. **The kernel carries the restraint.** [[METHOD]]'s orientation step 5 gains it, in the same breath as codifying the minimum: *divide the work as little as it allows: a division earns itself by different knowledge, different authority, or a judgment that cannot review itself, and stands only while it beats the undivided version on real work. Having a name is not a reason to be separate.*

2. **Three grounds, and they are the whole list.** *Different knowledge* — the part knows something the whole cannot act correctly without. *Different authority* — the part may do what the whole may not, or may not do what the whole may. *A judgment that cannot review itself* — the work and the check on it cannot be the same act. Anything else is not a reason, however sensible it sounds: not tidiness, not that a step has a name, not that the diagram reads better with another box in it.

3. **The comparison is against the undivided version, on the person's real work.** The three grounds justify proposing a division; only the comparison keeps it. The baseline is the same work done by one whole, not a version built to lose. This is [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 5 turned outward: that one holds AI-Mise's own scorecard to plain `/init` on the same materials; this one holds every division AI-Mise proposes to the same standard on the person's materials.

4. **However it is divided, one whole answers to the person.** The person deals with one thing that owns the conversation and answers for all of it. How the work is divided behind that is an internal fact. It never becomes something they have to route around, and it never becomes their vocabulary.

5. **The kernel names none of the current forms.** Not instruction, skill, workflow, tool, specialist, or any coordination pattern with a name this quarter. Those are adapter vocabulary and live in [[architecture]], which is rewritten when the words change. This is [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 5 applied to the layer most crowded with product names.

## Consequences

- [[METHOD]] goes from 72 lines to 78, the second consecutive ADR to add to it. The standing of that figure is unchanged from [[ADR-0014-whether-an-assistant-is-warranted|ADR-0014]]: #44's under-40 is this repository's acceptance criterion for its own page, nothing validates it, and the page has been over budget since it was written. #44 is where the cut happens; this is one of the things that should survive it.
- [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 4 becomes a special case of decision 1 — the same rule applied to AI-Mise's own supporting skills. Nothing in it changes; it stops standing alone as a preference.
- [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] decision 5 gains a product-side twin. That decision governs how AI-Mise is measured; decision 3 governs how what AI-Mise builds is measured. Same discipline, pointed the other way.
- [[ADR-0005-builder-vs-workspace|ADR-0005]]'s split survives the new test, on different authority: the Builder can change how the work works and the assistant cannot. The rule proving operable on the repository's most exposed existing division is part of why it is safe to adopt.
- The README needs no change, and gains a reason. "The person using AI-Mise meets exactly one thing — an assistant they name" is now a projection of decision 4, and the line below the fold — internal separation "the user benefits from without ever seeing" — is decision 4 from the other side.
- Nothing here forbids division or fixes a number. Work that needs four parts, and can show it, gets four.
- One thing is now owed that does not exist yet: decision 3's comparison. Phase 1 reaches a proposal before there is any real work to compare on, so what ships first is the grounds and a stated intent to compare. Building the comparison is evaluation work and is not in Phase 1.

## Alternatives not taken

All five are *[default]* — product-choice reasoning, not research findings.

**Name the forms in the kernel — instruction, skill, workflow, tool, specialist** — rejected: these are the fastest-moving words in the field, and [[ADR-0012-philosophy-is-the-product|ADR-0012]] decision 5 already rules product names out of instruction. The instinct behind it, that a rule has to be applicable and not merely admirable, is kept by decision 2: three grounds a person can check are more applicable than six nouns that expire.

**"One assistant, always"** — rejected: it is a number, and the rule is not about numbers. Ashby's floor says the regulator cannot be smaller than the work; Google Research measured +80.8% where the architecture fit the task. A rule that forbids that win is as wrong as one that assumes it.

**Adopt the manager pattern by name** — rejected: right shape, wrong durability. Its content — one thing owns the conversation and calls on the rest — is kept by decision 4, phrased to outlive the name. The name belongs in [[architecture]], where names are allowed to expire, and the credit belongs in [[foundations]].

**Require a measured comparison before any division may be proposed** — rejected: Phase 1 reaches a proposal from nothing, before there is real work to measure on, so the requirement would make the rule unusable exactly where it first applies. The instinct behind it, that a claim of improvement must be earned rather than asserted, is kept by decision 3 — the comparison keeps a division rather than permitting it — and by the kernel's existing rule that every important claim carries its condition.

**Split step 5 into two steps, one for how much and one for how divided** — rejected: the split does not pass its own test. Deciding how much to codify and deciding how to divide the work are one act of restraint at one moment, and separating them would be a division made because two things had names.
