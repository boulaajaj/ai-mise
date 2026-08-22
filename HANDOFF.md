# Handoff — continuing AI-Mise

This file tells the next session — yours, or another agent's — what AI-Mise
is now, what is built, and what to do next. Read it before
`docs/architecture.md`, which still describes the earlier design.

## What AI-Mise is

A concierge for the AI setup someone already has. It is invoked by name and
is not ambient. It orients to the host first — which assistant this is, what
it offers, what is switched on and what is going unused — then works out what
the person is actually trying to do, audits what is already there before
adding anything, and recommends the lightest thing that would help: a native
capability first, an established tool second, something built for them last.

It recommends, and it shows. It changes nothing without approval.

It is **not** a workspace compiler and it does not build a workspace. That
was the earlier design. ADR-0016 records the change; #124 and #125 shipped
it. Any document still describing a builder is stale, not authoritative.

## Ground rules for every session

- `control-plane/constitution/policy.yaml` is user-owned. No agent edits it.
  Propose changes in conversation; Amine applies them by hand.
- Never commit directly to `main`. Every change is a pull request.
- Never edit a **merged** ADR under `docs/decisions/` — supersede it with a
  new one. A **proposed** ADR may be revised inside its own pull request
  (#113).
- Claim hygiene (ADR-0004): label design assertions [verified], [prior art]
  or [default]. Numbers that are product choices belong in policy.yaml
  rather than in prose.
- The plain-language surface is a first-class exit criterion. If a
  non-technical person could not understand the output, it is not done.
- `docs/meta/retro-log.md` is append-only. End a working session by adding
  to it.

## Where it stands

| Piece | State |
|---|---|
| The skill | `skills/ai-mise/SKILL.md` — orient, understand, anchor, audit, recommend, show |
| Install | One repository, six manifests, each tool's own command. Verified live against the remote (#125) |
| Naming | `install.sh` / `install.ps1` install under a chosen name, making that word the trigger |
| Reach | Claude Code, Claude web/desktop/mobile, Codex, Grok Build, Gemini CLI, GitHub Copilot, Cursor; ChatGPT, Grok and Claude in a browser via one pasted URL |
| Inventory | `skills/ai-mise/scripts/inventory.py` — hashing, symlink-refusing, reproducible |
| First validator | `protected_path_validator.py` — working, self-tested |
| Dev harness | `CLAUDE.md`, `docs/meta/dev-harness.md`, `docs/meta/retro-log.md` |
| Evaluation | Not built. It is the open question this project owns — see below |

## What to do next

1. **Run it cold on a real project** (#18, #58). This is the only work in the
   backlog that can return a negative result, and little downstream is worth
   doing until it has. Run it against a code project and against a non-code
   personal case, and do not reconcile the two: the gap between them says
   which product this actually is.
2. **Orientation and the understanding gate** (#85, #88). #85 owns learning
   what the environment already knows before asking the person to repeat
   themselves. #88 owns whether enough is understood to recommend anything —
   including the layered analysis that makes a large project tractable, and
   the difference between having looked at something and understanding it.
3. **Evaluation.** A portable record of what a test run actually did, and a
   behavioural regression suite for the skill across hosts. This is quality
   assurance for an instruction, not automatic self-improvement — that was
   deliberately descoped.

## The open question this project owns

Every harness system surveyed in the August 2026 build-versus-adopt review
needs a benchmark, or a stream of labelled tasks, to close its loop. A person
has neither. *How do you know a personal harness got better?* is unanswered
anywhere in the field, and answering it is what separates AI-Mise from a
configuration generator. The evaluation work above is the first honest
attempt at it.

## Known open questions

- Interview stopping quality remains the least-grounded area of the design.
- Platform capabilities move monthly, so anything freshness-sensitive is
  checked live at runtime rather than answered from memory.
- What is remembered between runs, and across hosts, is unsettled (#23).
