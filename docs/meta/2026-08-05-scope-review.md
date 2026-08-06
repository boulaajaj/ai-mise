# 2026-08-05 — Scope review and transfer note

*What was decided on 5 August 2026, and what the next session needs to know.
This is a record, not a plan; the reasoning lives in the linked decisions and
work items.*

## Why this exists

An extended design exchange with another assistant produced a long brief:
a refined product definition, a lifecycle, a capability contract, a consent
ladder, a scheduled-job contract, a dashboard architecture, a competitive
comparison, seven tensions, and a seven-phase order. It arrived without
access to this repository.

The whole of it was checked against the corpus before anything was accepted.
That check is the useful part of this note, and it went in both directions.

## What the check found

Of the seven tensions the brief raised, four were already settled here and
three were real.

Settled: #47's north-star sentence already says *"through visible, reversible
changes"*, not merely "continuously improve". #24 already says *"Not every
unknown - no endless interviews"* and defines what decision-relevant means.
Permanent setup and work modes were rejected in ADR-0008, whose title is
"no modes, tiered application". The dashboard already sits downstream of
evidence, in ADR-0002 and `architecture.md` §4.

Real: #27's end-of-session retrospective hook is shadow-only but is neither
opt-in, host-detected, nor budgeted. #23 asks for domain research "A-to-Z for
any profession", which collides with #57. And `direction.md` tells a newcomer
the product *"quietly sets everything in place… and then gets out of your
way"*, which is the opposite of what the approval transaction does.

That third one was first reported as stale and not present in the corpus.
It was present; the search had not reached `docs/meta/`. Recording the
correction here because the pattern is worth keeping: a claim of absence is
only as good as the search behind it, and this repository's own anti-churn
test — check what the corpus actually does before agreeing something is
broken — applies to the reviewer as readily as to the reviewed.

## What was decided

ADR-0016 carries the decision itself: the product starts from the
environment rather than from a folder, is summoned rather than ambient,
promises something falsifiable rather than "best possible", remembers what it
has built across workspaces, and permits recurring work only where a person
declared it and the environment was first shown to allow it.

Four things were found genuinely unowned, all four asked for by name:
a capability record, a build log across workspaces, a research ledger, and a
job contract. Each is small, and all four are now tracked as work items.

Four work items narrowed rather than changed: #23, #27, #28, #85.

The brief's seven-phase order was not adopted as structure. It maps onto
Phase 0–6 and v0 Personal Preview closely enough that a second scheme would
only give each work item two possible homes. Twenty-three work items that had
no milestone were assigned to the existing ones instead.

## What was declined, and why

*A heavy formal model of how things relate.* The instinct was right and is
kept — being explicit beats inferring from surface plausibility. The size was
not. The measured picture is that small vocabularies carry almost all the
value: in the largest natural experiment available — published usage analysis
of schema.org — roughly a dozen types and about thirty predicates account for
nearly all real-world use, while most of the vocabulary's several thousand
terms appear on fewer than a thousand domains each; corpus study of published
models (PARSE, EMNLP 2025) finds validation rules present in a fraction of a
percent of them, against structure in a majority; and published comparisons
of graph-structured retrieval show it measurably *losing* to plain reranked
retrieval on simple lookups, at a large token premium, while winning on
multi-hop questions. So: a small typed vocabulary that grows only when a named
case demands it, and no formal axioms until something has failed for want of
one.

Those three figures are named here but not yet sourced to a line. The debt is
real and this note is not the place to pay it — the sourced version belongs in
a findings note under `sources/`, which does not exist yet.

*The word for that model.* Accurate, and alienating on any surface a person
reads. The kernel's plain-language rule decides it.

*One citation.* The brief's central organising metaphor — a fixed spine with
adaptive edges — was attributed to a source that could not be verified, and
two of the risks credited to it appear in no version of it. The shape is
sound and does not need that source: it is Parnas on information hiding and
Simon on near-decomposability, both already credited in `foundations.md`.
The shape was kept and the citation dropped. Given how seriously this project
takes crediting borrowed ideas, crediting the wrong source is the worse
failure.

*A fifteen-field job manifest.* Not wrong in size, wrong in shape: it mixed
what a person declares with what a run accumulates. Those are two objects,
and a manifest the system edits after every run cannot be diffed or reviewed.

## What is still open

The `identity.boundary` line in `control-plane/constitution/policy.yaml`
still opens *"Given a folder of real project materials"*. It describes the
earlier product. The control plane is protected and that sentence is Amine's
to write; until it is rewritten, the constitution and the decisions disagree,
and anything compiling from the constitution follows the constitution.

Also open: whether #22 already owns the typed model or it sits beside it;
the name (#64); the measurement thresholds, which are constitution values;
and what a recurring run is called on the surface the person sees.

## For whoever picks this up next

Nothing about a session survives it. What survives is what lands in files —
which is what METHOD.md says and what ADR-0006 decided. This note, ADR-0016,
and the issue bodies are the whole of what carries forward. The issue bodies
are, as they have been from the start, where this project's working memory
actually lives.
