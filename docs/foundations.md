---
type: reference
title: Foundations — where the Method comes from
---

# Foundations

**Standing rule** *[verified]*: every idea adopted from someone else is named and, where it lives online, linked
here or in [[prior-art]]. Borrowing without credit is a defect, reviewable
like any other.

Scholarly grounding for [[METHOD]]. The ideas below are *[prior art]*, adapted
here (July 2026) from classical philosophy and cognitive
science. The kernel uses plain words (truth,
craft, judgment); this page records the lineage.

## The triad (Aristotle, Nicomachean Ethics VI)

| Classical term | Plain word | AI-Mise responsibility |
|---|---|---|
| Epistēmē — reliable knowledge of what is true and why | **Truth** | Evidence, sources, claims with provenance, uncertainty, freshness ([[ADR-0002-evidence-claims-views|ADR-0002]], issue #43) |
| Technē — craft; reasoned ability to produce | **Craft** | Skills, tools, procedures, quality standards, verification (placement rubric; strong-skill standard below) |
| Phronēsis — practical wisdom about the particular case | **Judgment** | Priorities, exceptions, escalation, why-the-rule-exists, loyal dissent ([[ADR-0007-challenge-before-compliance|ADR-0007]]; the rules-carry-reasons invariant) |

Only truth → an encyclopedia. Only craft → an automation script.
Judgment without evidence → dangerous confidence. Competence is all three.

## Metacognition — but external

*[prior art — self-reflection and calibration literature; task- and
prompting-dependent results; specific citations attach when #43 ships]*
Models show something like self-monitoring, yet research finds it
undependable: confident critique of correct answers into wrong ones,
superficial reflection, miscalibrated confidence. AI-Mise therefore does
not try to write the model's thoughts; it provides an **external operating
environment for reflection**: the person's identity and mission, trusted
evidence, decisions with rationale, quality definitions, unresolved
questions, change history, verification requirements, and feedback from
real outcomes. The model reasons; the workspace gives it something
coherent to reason *from* and something meaningful to reason *toward*.

A practical consequence — the **knowledge-condition ledger** *[default —
design requirement, not yet built; feeds #24]*: the workspace is to track not only what is known but its condition — confidence,
assumptions, contradictions, verification status, and the reasons behind
decisions (feeds the completeness model, #24, and the dashboard).

## The strong-skill standard

A weak skill is steps. A strong skill also knows: the decision it
supports, its prerequisites, what "good" means, common failure modes, how
to verify, and the conditions under which it does not apply. This is the
generation bar for every skill AI-Mise produces (issue #14).

## Dividing the work

*[prior art]* The kernel's rule — divide as little as the work allows, and
let a division earn itself — is older than the field now arguing about it,
and that field currently disagrees with itself.

**Where seams belong, not how many.** Parnas (1972) is the source, and he
is routinely read backwards. His argument is about *where* a boundary
falls: a five-module and a six-module decomposition of the same system
"could conceivably be identical after assembly," and the criterion is that
each module hides a design decision from the others. Stevens, Myers and
Constantine (1974) named the failure the kernel's last sentence prevents —
**coincidental binding**, a module whose elements have no meaningful
relationship. A split made because something had a name is that failure,
and it has had a name for fifty years.

**The floor.** Ashby (1958) bounds the rule from below: a regulator's
"capacity as a regulator cannot exceed its capacity as a channel for
variety." How little the work allows is set by the work. A rule that
always answered "one" would be wrong.

**The three grounds.** Different knowledge is the end-to-end argument
(Saltzer, Reed and Clark, 1984) — a function belongs where the knowledge
to do it correctly is. Different authority is least privilege (Saltzer and
Schroeder, 1975), "the least set of privileges necessary to complete the
job." A judgment that cannot review itself is the audit profession's
**self-review threat**: a party who "will not appropriately evaluate the
results of previous judgments made or services provided." Fagan (1976) is
the measured version — an inspection moderator "from an unrelated project"
to preserve objectivity.

**Three criteria, then elimination.** The shape of the test comes from
design for assembly (Boothroyd and Dewhurst, 1983): a part is necessary
only if it moves relative to what is already assembled, must be of a
different material, or must be separate or assembly becomes impossible.
Everything else is "a candidate for elimination." Three checkable
criteria, and the rest goes — the same shape the kernel's three grounds
take.

**The comparison.** Kohavi et al. (2009) name the baseline: "the Control,
which is commonly the 'existing' version." The undivided version is the
control; the divided one has to beat it, on the same work.

**The counter-case.** Simon (1962) argues the other way, and the rule is
better for answering him than for ignoring him: nearly-decomposable
systems assemble and evolve faster. Two limits. His mechanism is
interruption-and-collapse, which version control makes false in software;
and he describes where seams *already lie* in evolved systems rather than
licensing their invention. His own caveat is the load-bearing part — the
interactions between subsystems are "weak, but not negligible."

**Today, and the disagreement.** Anthropic says start with the simplest
approach and add complexity only when evidence supports it. OpenAI says
start with one and add specialists only when they materially improve
isolation, clarity or legibility. Microsoft says not to assume role
separation requires separate agents. Google's ADK guidance says the
opposite — reliability comes from decentralization and specialization.
Google Research then measured it — 260 configurations, six benchmarks —
and found the effect swinging from +80.8% to -70.0% with how well the
architecture fits the task, sequential-reasoning tasks worse under every
multi-agent variant tried. That spread is why the kernel carries a test
rather than a number, and why it borrows none of their vocabulary.

## The loop's lineage

Understand the person and mission → determine what is known, missing,
uncertain → select knowledge, skills, standards → let the model reason and
act → verify against evidence and purpose → explain plainly → learn and
update. This is the Method's loop *[prior art — kin to deliberate practice and
organizational learning cycles]*, centered on one person over time.

## Machine tempo

*[prior art — Lilian Weng, "Harness Engineering for Self-Improvement"
(2026); agent-development-lifecycle (ADLC) literature]* Agent loops run until-done at machine speed, not in
fixed planning cycles; learning-reflection fires when evidence accumulates rather
than on a calendar; the slow interval guard for whole-trajectory review
([[architecture]] section 7) remains — it is governance, not a calendar.
Principles adopted into the design direction (implementation tracked as issues; not all enforced yet): evidence-paired edits carrying falsifiable
predictions checked next round; the judge is read-only to the improver;
improvements accepted only with zero regression on held-in and held-out
sets; quality measured as distributions against thresholds; failures
clustered and mapped to a component before any fix; memory as structured
items merged deterministically.

Our addition *[default]*: the third tempo. The literature accelerates
truth and craft and silently drops judgment. In AI-Mise, judgment runs on
the human clock by design — the human is the metronome for judgment, not
latency to remove. And the fast loop inherits the kernel's purpose test:
verification against checks alone lets speed mass-produce work that
passes and misses the point.


## Credits and sources

- **Lilian Weng** — *Harness Engineering for Self-Improvement* (Jul 2026): until-done loops, evidence-paired edits with checked predictions, read-only judges, held-in/held-out acceptance, failure clustering, durable file state. https://lilianweng.github.io/posts/2026-07-04-harness/
- **Andrej Karpathy** — Software 3.0 framing and the LLM-wiki pattern our knowledge views descend from. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Aristotle** — *Nicomachean Ethics*, Book VI: epistēmē, technē, phronēsis.
- **Eric Evans** — *Domain-Driven Design*: ubiquitous language (ADR-0009).
- **Tiago Forte** — *Building a Second Brain*: the second-brain framing the README borrows to place AI-Mise for a new reader. We depart from it deliberately — this workspace exists to get a project done, not to keep notes. https://www.buildingasecondbrain.com/book
- **Anthropic** — Agent Skills guidance, memory/hooks documentation, skill-creator: the placement limits and eval-first authoring our adapter follows.
- **Google Cloud** — Open Knowledge Format: the minimal frontmatter conventions our files use.
- **Atlan** — ADLC-vs-SDLC: continuous calibration, eval distributions, inner/outer loops. https://atlan.com/know/ai-agent/adlc-vs-sdlc/
- **Open-source authors** whose implementations we deliberately reuse — BerriAI (self-improving-agent), Terence Bristol (claude-improve), Tigerless Labs (autoharness), Kayba (autoharness), aiming-lab (AutoHarness), ruvnet (metaharness), HKUDS (OpenHarness), revfactory (harness) — each with specifics and links in [[prior-art]].
- **Bolt (StackBlitz)** and **Abstract** — the hide-the-version-control UX lineage behind "Save Version / Restore".
- **David Parnas** — *On the Criteria To Be Used in Decomposing Systems into Modules* (1972): information hiding, and the argument that decomposition is about where seams fall rather than how many there are. https://dl.acm.org/doi/10.1145/361598.361623
- **Wayne Stevens, Glenford Myers and Larry Constantine** — *Structured Design* (1974): coincidental binding — the name, since 1974, for a split made because something had a name. https://doi.org/10.1147/sj.132.0115
- **W. Ross Ashby** — *Requisite Variety and its Implications for the Control of Complex Systems* (1958): the floor under "as little as the work allows." https://pespmc1.vub.ac.be/books/AshbyReqVar.pdf
- **Jerome Saltzer, David Reed and David Clark** — *End-to-End Arguments in System Design* (1984): the different-knowledge ground — a function belongs where the knowledge to do it correctly is. https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf
- **Jerome Saltzer and Michael Schroeder** — *The Protection of Information in Computer Systems* (1975): least privilege, the different-authority ground; and economy of mechanism, whose stated rationale is verifiability. https://web.mit.edu/Saltzer/www/publications/protection/
- **U.S. Government Accountability Office** — *Government Auditing Standards* (GAO-21-368G), the self-review threat: the audited name for a judgment that cannot review itself. https://www.gao.gov/products/gao-21-368g
- **Michael Fagan** — *Design and Code Inspections to Reduce Errors in Program Development* (1976): the measured case for a reviewer from outside the work. https://doi.org/10.1147/sj.153.0182
- **Geoffrey Boothroyd and Peter Dewhurst** — *Design for Assembly: A Designer's Handbook* (1983): three criteria and elimination — the shape the kernel's three grounds take.
- **Herbert Simon** — *The Architecture of Complexity* (1962): the strongest case against the rule, kept and answered rather than left out.
- **Ronald Kohavi, Roger Longbotham, Dan Sommerfield and Randal Henne** — *Controlled Experiments on the Web* (2009): the control is the existing version — the undivided baseline the divided one has to beat. https://doi.org/10.1007/s10618-008-0114-1
- **Anthropic** — *Building effective agents* (2024): start with the simplest approach and add complexity only when evidence supports it. https://www.anthropic.com/engineering/building-effective-agents
- **Anthropic** — *Building multi-agent systems: When and how to use them* (2026): the same advice restated for the multi-agent case — multi-agent systems are often applied where a single agent would do better. https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
- **OpenAI** — orchestration guidance: start with one, add specialists only when they materially improve capability isolation, policy isolation, prompt clarity or trace legibility; and the manager pattern — one assistant owns the conversation and calls on the rest — whose content the kernel keeps without its name. https://developers.openai.com/api/docs/guides/agents/orchestration
- **Microsoft** — Cloud Adoption Framework guidance on one agent versus several: do not assume role separation requires separate agents. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents
- **Google (Agent Development Kit)** — *Developer's guide to multi-agent patterns in ADK* (2025): the clearest statement of the opposing view — reliability comes from decentralization and specialization. Credited because the disagreement is real and the kernel has to survive it. https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/
- **Google Research** — *Towards a Science of Scaling Agent Systems* (2025): 260 configurations across six benchmarks, +80.8% to -70.0% depending on task-architecture alignment — the measurement behind carrying a test instead of a number. https://arxiv.org/abs/2512.08296

## The center, in one sentence

AI-Mise turns general model intelligence into situated competence: it
maintains an evolving understanding of the person, mission, evidence,
capabilities, and decisions, so the model can determine not only what it
*can* do, but what is true, what should be done, how to do it well, and
how to know it worked.
