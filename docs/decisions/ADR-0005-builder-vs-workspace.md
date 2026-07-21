# ADR-0005: The Builder and the Workspace are two distinct conversational identities

**Status:** Accepted · 2026-07-20
**Trigger:** Amine's observation: "the user needs to know when they are talking to the harness builder versus when they're talking to their own harness."

## Context

The product creates a second thing the user talks to. After bootstrap there are two conversational surfaces: the **Builder** (the compiler — interviews, proposes, constructs, refactors, runs retrospectives) and the **Workspace assistant** (the compiled harness — helps with the user's actual profession every day). If these blur, two failure modes follow: the user asks their assistant to change its own rules and can't tell whether governance applied; and worse, the assistant *appears* to change itself, destroying the trust the whole product depends on. The architecture already forbids self-modification structurally (ADR-0001: the gateway is the only mutation path) — this ADR gives that boundary a *face*.

## Decision

1. **Two named identities.** The Builder and the user's assistant (which takes the workspace's own name, chosen at bootstrap) are distinct personas with distinct greeting lines, injected by the adapter into each generated projection. Every session opens by stating who is present: "You're working with your assistant" / "You're with the Builder — we change how your workspace works here."
2. **Mode is structural, not stylistic.** Builder sessions run with the bootstrapper plugin active and gateway tools available. Workspace sessions run from the generated projection, where structural writes are blocked by hooks and deny-rules. The identity announcement simply *reveals* which enforcement regime is active — it can't lie, because the tools differ.
3. **The handoff is the UX of the block.** When a workspace session receives a structural request ("stop formatting reports that way", "you should always check X first"), the assistant does not refuse and does not comply. It hands off: "That's a change to how I work — let me bring in the Builder." What happens mechanically: the request is recorded as a correction (retrospective input), and the user is offered a Builder session where it becomes a proposal. The denied-write hook message is rewritten to this friendly handoff, so even a drifting agent hitting the block produces the right experience.
4. **Asymmetric memory.** Builder sessions read everything and write only through the gateway (proposals, receipts, decision records). Workspace sessions write work products and corrections, never structure. A correction spoken to the assistant surfaces in the Builder's next retrospective — the user never repeats themselves, which is what makes the handoff feel like one system, not two products.
5. **Plain-language naming.** Non-technical users hear "your assistant" and "the Builder." The words "harness," "control plane," and "gateway" never appear in either surface.

## Consequences

- The adapter (Phase 3) must generate the identity lines, the handoff-styled hook messages, and a `builder` entry point (e.g., a slash command or separate launcher) — added to the Phase 3 issue.
- New threat scenario 35: a workspace session accepts a structural instruction and attempts to act on it directly instead of handing off — the test asserts the block fires *and* the correction is recorded.
- The retrospective pipeline (Phase 5) gains a new input class: handoff-originated corrections, pre-tagged with the user's verbatim request.
- Open question, deliberately deferred: whether the Builder and assistant may ever share one session with visible mode-switching, or must always be separate sessions. Separate sessions are the safe default; revisit after the Arduino pilot shows how often handoffs actually occur.
