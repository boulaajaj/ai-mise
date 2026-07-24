---
type: reference
title: Foundations — where the Method comes from
---

# Foundations

Scholarly grounding for [[METHOD]]. All of this is *[prior art]* — a
synthesis contributed through Amine (July 2026) from classical philosophy
and cognitive science, adapted here. The kernel uses plain words (truth,
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

## The loop's lineage

Understand the person and mission → determine what is known, missing,
uncertain → select knowledge, skills, standards → let the model reason and
act → verify against evidence and purpose → explain plainly → learn and
update. This is the Method's loop *[prior art — kin to deliberate practice and
organizational learning cycles]*, centered on one person over time.

## Machine tempo

*[prior art — Lilian Weng, "Harness Engineering for Self-Improvement"
(2026); ADLC literature]* Agent loops run until-done in minutes, not in
sprints; reflection fires when evidence accumulates, not on a calendar.
Reusable principles adopted: evidence-paired edits carrying falsifiable
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

## The center, in one sentence

AI-Mise turns general model intelligence into situated competence: it
maintains an evolving understanding of the person, mission, evidence,
capabilities, and decisions, so the model can determine not only what it
*can* do, but what is true, what should be done, how to do it well, and
how to know it worked.
