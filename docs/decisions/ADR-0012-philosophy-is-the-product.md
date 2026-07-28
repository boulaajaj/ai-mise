# ADR-0012: The philosophy is the product; code earns its place by guaranteeing

**Status:** Proposed · 2026-07-27 (merge = agreement)
**Trigger:** Amine's directive, 2026-07-27: "I want it to be just a philosophy instruction that resides on the user's environment, and from there things happen. I don't want any code or anything, really."

## Context

The repository was measured before this decision was written: 1,853 lines of Markdown against 613 lines of executable code — and of that 613, only 83 lines are product. The rest is the repository's own CI guarding and one developer tool. AI-Mise was already almost entirely instruction. What was missing was the decision that it stays that way.

Code accumulates by default. Each addition arrives with a reason, and no single one is wrong. Nobody ever decides that the product has become software; it becomes software one justified addition at a time, and the philosophy ends up as documentation *about* a system rather than as the system itself.

The directive also settles a question the skills had answered by accident. `skills/inspector` and `skills/blank-slate` differ by whether a folder exists — a split by circumstance rather than by kind, which forces the model to choose before it has looked.

## Decision

All decisions below are *[default]* — chosen product behavior, not derived from research.

1. **The intelligence is instruction; the code is guarantee.** AI-Mise's capability comes from philosophy that a capable model reads and applies. Code exists only where reasoning is the wrong tool — where something must be true every time rather than judged well most times. Today that is: hashing, local version history, rollback, validation, file I/O, and platform integration.

2. **New code passes the guarantee test or it is not written.** The question is never "would a careful model get this right most of the time?" It is "does this need to be identical every time, without depending on the model?" If yes, code. If no, instruction. Most things are instruction.

3. **Infrastructure stays out of the conceptual architecture.** Someone learning what AI-Mise *is* meets the philosophy. The machinery that provides the guarantees is real and documented, and it lives below the line — it never becomes how the product is explained, and it never shapes how the product is designed.

4. **One core skill.** Not split by whether a folder exists, not split by phase. The same skill understands the person's situation, inspects available materials when there are any, asks only decision-changing questions, and proposes what to do next. Supporting skills appear when a real need appears — never in anticipation of one.

5. **Instruction names capabilities, never products.** The skill says *if this host can enforce something without asking the model, that is where enforcement belongs — find out whether it can, and ask the person to set it up.* It never names a vendor's feature. When something ships next month the instruction is already correct, and only the answer to "what does this host expose?" changes. This generalizes [[ADR-0011-exit-tests-name-capabilities|ADR-0011]] from exit tests to all instruction.

6. **The mind map leaves product scope.** `tools/generate_mindmap.py` may remain as optional developer tooling. It is not part of the runtime and it does not shape the architecture. **This supersedes [[ADR-0006-formats-over-tools|ADR-0006]] decision 3.** A general visual knowledge map returns only if a real user need justifies it.

## Consequences

- `skills/inspector` and `skills/blank-slate` merge into one core skill, with the folder-exists branch moving inside it. Tracked as an issue; not done here.
- `skills/inspector/scripts/inventory.py` survives — hashing is a guarantee, and a guarantee that depends on a model remembering to produce it is not one. What changes is its standing: supporting infrastructure the skill calls, never part of what the skill *is*.
- The four validators keep their place for the same reason. They guarantee.
- `docs/mindmap.md` stops being a required artifact. Issue #22 is unaffected — [[ADR-0006-formats-over-tools|ADR-0006]] decision 2 already made it a wikilink-linked markdown graph, and that stands.
- The README's product boundary loses its presumption that a folder exists.
- The decision router in #24 becomes the core skill's spine. It already names kinds rather than vendors, which is decision 5 in miniature.
- `docs/architecture.md` and `HANDOFF.md` describe an architecture in which the machinery is more prominent than decision 3 allows. Correcting them is tracked separately rather than bundled here.

## Alternatives not taken

**No executable code at all** — rejected: hashing, rollback and validation are guarantees, and a guarantee a model might forget to honour is a hope. The instinct behind it — that the product must not quietly become software — is what decisions 2 and 3 are for.

**Keep the folder-exists split** — rejected: two skills whose descriptions differ only by circumstance ask the model to choose at the one moment it cannot yet know. Inside a single skill the same branch is a question it answers after looking.

**One skill per phase** — rejected: six descriptions compete at startup and the model has to pick correctly every time. Progressive disclosure inside one skill gives the same separation without the competition.
