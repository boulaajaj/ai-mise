# ADR-0017: First contact introduces the capability, and the name is the trigger

**Status:** Proposed · 2026-08-27
**Trigger:** Amine's correction after the first real install, 27 August 2026: *"Install once, then ask it what it can do for me. That's it. No commands… The first thing that is absolutely required is to present its capabilities in a very intuitive manner."* Recorded as #146. The install itself worked; what followed it did not, and the session ended with a correct trigger and no idea what to do next.

## Context

The install succeeded in two commands, first try, twice **[verified]** — the friction log records the terminal output. What failed was everything after it, and each of those failures is observed rather than inferred:

- The documented command did not exist **[verified]** — four invocations were tried and their output captured (#140).
- The account sync failed three times and left an empty marketplace **[verified]** — the error and the network trace are both in the log (#141).
- The working invocation opened onto nothing a person could act on **[verified]** — the session ended there, and the report of it is what triggered this record.

That third failure is the one this record is about, because it is the only one that would have survived fixing the other two. `SKILL.md` §2 said the first thing to say should be short, should promise that nothing changes without approval, and should "leave an easy thing to say next". Nowhere did it say what AI-Mise can do, how else to reach it, or what to ask. The material that would have answered all three exists — the README's "Things to ask it" — and it is in a file the person is not reading. They have just installed a skill; they are talking to the skill.

There is a second, quieter defect in the same place. Every install document leads with a typed command, which taught two lessons at once: that AI-Mise is a command, and that the way to learn it is to read about it. [[ADR-0016-environment-not-folder|ADR-0016]] decision 2 already says the opposite — *"The person calls it by name"* **[verified]**. The documents drifted from the decision; the decision was right.

## Decision

Both decisions are *[default]* — chosen product behaviour, not derived from research.

**1. The name is the trigger, and the typed form is a shortcut.** Saying the name — the given one, or the one the person chose instead — starts AI-Mise, with or without a request attached. Saying only the name is itself a request: it means *introduce yourself*. The skill's own description carries this, so the dispatch happens on every host that routes by what a skill says it is for, rather than through machinery each host would have to provide separately. Where a host also offers a typed form, it is named once, as a convenience for people who prefer typing. No surface presents it as the way in.

**2. First contact presents the capability.** Before understanding anything about the person, and after orienting to the host, the opening says four things: what AI-Mise can do for them in their terms, how to reach it *on this host*, that it can be renamed and that the choice is theirs, and two or three questions that would each start real work. Someone who has read nothing finishes that exchange able to start. The ordering matters: orientation comes first, because "how to reach it here" and "what you already have and are not using" are only truthful once the host has actually been looked at.

## What this changes about a recorded rule

`SKILL.md` §2 said *"Do not ask for a name before they have a reason to want one, and never require one."* The first half is superseded; the second half stands, and is load-bearing.

The reasoning behind the first half was sound and its conclusion was wrong. Deferring the name avoided opening with a demand — but the fix for a demand is to stop demanding, not to stop mentioning. A person cannot want something they have not been told exists, so "wait until they have a reason" resolved, in practice, to never. Naming is now **offered** at first contact and never required, never waited on, and never asked twice; ignoring the offer is a complete answer to it.

`SKILL.md` §2 also said *"offer no list to choose from"*, and that rule survives unchanged. It is about not asking a person to classify themselves before anything has been done for them. A list of what AI-Mise offers is a different object from a list the person must place themselves in — the first is an introduction, the second is a form.

The instruction to keep the first impression *short* also survives, and is the real constraint on this decision. Presenting everything AI-Mise can do would replace one wall of text with another and lose the point. The resolution is **structured, not longer**: one screen, scannable, no preamble. A first contact that needs scrolling has failed on the same axis the README failed on.

## Consequences

- The skill's frontmatter `description` becomes load-bearing for invocation rather than merely descriptive. This repository now treats it as an interface: wherever a host decides relevance from what a skill declares about itself, that field is what decides whether AI-Mise is reached at all, so changes to it are reviewed as interface changes rather than as wording. How each host actually dispatches is its own business and moves month to month, so the rule recorded here is about the care taken *[default]*, not a claim about what every host does.
- Every install document has to invert: name first, typed form second. #142, #143 and #144 all touch these files and should carry the inversion rather than adding it separately.
- README and INSTALL currently promise that the account sync "turns up on the phone as well". That is false until #141 is confirmed fixed, and a promise about reach is exactly the kind this record makes prominent. It goes or it gets qualified.
- The first-contact presentation is now the product's most-read output, and nothing tests it. That belongs with the behavioural regression work in #129 rather than being invented here — but it should be said plainly that this decision ships untested behaviour on the most exposed surface there is.
- Whether that presentation renders or prints is not decided here. #76 owns it, and #136's one-page framing already governs the shape.

## Alternatives not taken

All *[default]*.

**Leave first contact short and let the README carry the introduction** — rejected: this is the status quo, and the install session is the evidence against it. The person is in the assistant, not in the repository, and telling them to go and read is the failure being fixed.

**Ship a `commands/` directory so `/ai-mise` resolves** — rejected as a fix for the wrong problem. It would make the bare command work and leave the product command-shaped, which is the thing being moved away from. #140 makes the documented command *true*; that is a different and smaller claim than making it the front door.

**Ask for a name up front, as a required first step** — rejected: it opens by demanding something before anything has been done for the person, which is the defect the original rule existed to prevent. Offering costs one line and keeps the objection answered.

**Detect the host and branch the introduction in the skill** — rejected: section 1 already establishes what the host offers, and the introduction should read from that rather than carry its own copy of the same knowledge. A second place that knows what hosts can do is a second place that goes stale.
