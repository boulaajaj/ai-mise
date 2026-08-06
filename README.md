# AI-Mise

AI-Mise sets up the workspace an AI assistant works from. Not the assistant
itself — the things around it: what is true about your project, what has
already been decided, what good work looks like in your field, and which rules
the assistant is not allowed to touch. That setup is most of the difference
between an assistant that guesses and one that is useful. Building it well is
somebody's job, and it shouldn't have to be yours.

## Installing it

AI-Mise is an [Agent Skill](https://agentskills.io) in the open `SKILL.md`
format, so the same folder works in more than one tool. Installing it is the
few lines below and nothing else — there is no runtime to go and fetch first.
Keep `scripts/` next to `SKILL.md`: where there is a folder to read and a
`python3` to run the script with, the first pass uses it; where there isn't, it
reaches the same result another way. That first pass is all there is today, and
it runs in all three tools below. The deeper platform work, once there is a
workspace to project into a tool, starts with Claude Code —
[deployment](docs/deployment.md) has the order.

Or hand the job over: point your assistant at this repository and say
install. It follows [INSTALL.md](INSTALL.md), which does the same placements
on whichever tool you have, checks them, and tells you what it did.

**Claude Code**

```bash
git clone https://github.com/boulaajaj/ai-mise.git
cd ai-mise
mkdir -p ~/.claude/skills ~/ai-mise
ln -s "$PWD/skills/ai-mise" ~/.claude/skills/ai-mise
ln -s "$PWD/control-plane" ~/ai-mise/control-plane
```

Then, in any project, type `/ai-mise` — or just say it in your own words:
*"have a look at this folder and tell me how you'd set it up."* Because
they're symlinks, `git pull` updates them. On Windows without WSL, copy the
two folders instead.

**Codex**

```bash
git clone https://github.com/boulaajaj/ai-mise.git
cd ai-mise
mkdir -p ~/.agents/skills ~/ai-mise
cp -r skills/ai-mise ~/.agents/skills/
cp -r control-plane ~/ai-mise/
```

Start it with `$ai-mise`, or run `/skills` to see what's loaded. Codex also
reads `.agents/skills/` from your working directory up to the repository root,
so putting the folder there instead makes it available to everyone working on
that project.

**ChatGPT — web, desktop, or mobile**

Skills → Create → *Upload from your computer*, and upload
`skills/ai-mise/SKILL.md`. Then start it with `@ai-mise`. Two things to know:
personal skills are added separately on desktop and on web/mobile and don't
sync between them, and ChatGPT can't reach a folder on your disk — it works
from what you upload, so neither the inventory step nor the rules it reads
its own limits from are there.

## What it sets out to do

Understanding the situation comes first: what the work actually is, what you
are aiming at, what has already been decided, what counts as good here. Not
through a long questionnaire, though. It reads what is already there, asks only
the questions whose answers change what it does next, and otherwise stays out
of the way — a quiet observer rather than a form to fill in.

The building comes next, and that part isn't written yet — what follows is the
shape it is meant to take. The scaffolding, the starting structure, the
connections between things that were sitting in separate places, shaped for
that situation rather than to a template chosen in advance. And it isn't tied
to one kind of work. The first step of the method is always to find out how a
field works and what its practitioners hold themselves to, so what comes out
the other end can carry whatever expertise the situation calls for.

Part of that judgment is whether an assistant is wanted at all. Some work
doesn't need one, and saying so is a real answer. Where one would help, the
question is which one and what it should be good at — a careful reader of
research and a careful drafter are not the same thing, and neither is the same
as a second pair of eyes on a decision. Working that out, then setting up the
one that fits, is the part I most want to get right.

It also has to stay current. What people know about working well with AI keeps
moving, and tracking it is the sort of work I would rather do once than repeat
on every project. [Prior art](docs/prior-art.md) is where that reading gets
recorded, along with exactly what was taken from each source. Doing that by
hand doesn't scale past me, so the intent is for AI-Mise to watch on its own —
on whatever schedule the tool it is running in can offer, and only if you have
said yes to it. It would weigh work from places with a reputation to lose above
the rest, and bring you what it found rather than act on it.

The workspace is plain files. Markdown for anything you would read yourself,
plus whatever configuration a particular tool needs to pick it up. So it
travels, and it outlives the tool that made it. Its own evolution is logged, so
you can see how the setup arrived where it is. And you can go back to any
change it made, at any point in that history.

The closest comparison is a second brain — Tiago Forte's term, credited in
[foundations](docs/foundations.md) — except this one isn't for keeping notes.
It is for getting real projects done, with models that are already capable
enough.

## About guardrails

The rules you set live outside anything the assistant can write to, so it can't
quietly edit them. That is the whole of it, and I would rather not claim more.
Guardrails aren't containment — if something turns out smarter than all of us
put together, a file of my preferences is not what stops it. What this does is
duller: it keeps the rules out of reach, records what it changed, and lets you
undo that.

## Where it actually is today

Installing it gets you the first pass, and only that. AI-Mise reads the
materials you point it at, records what it understood, asks the few questions
whose answers would change the outcome, and hands back a plain-language
proposal for the workspace it would build — along with a list of everything it
assumed and what each assumption costs if it turns out wrong. All of that goes
to a folder you name, and nothing else on your disk is touched. Then it stops,
and the last thing it tells you is that no workspace has been created yet.

The building part isn't written. The rules are, and this repository already
runs on them: every change reviewed before it lands, every decision recorded,
every change reversible afterwards. So far the only thing AI-Mise has proved
is that the rules work on itself. [METHOD.md](METHOD.md) is the page the rest
is built on.

I haven't used it on a real project yet. I'll know much more when I have.

*(The name is from* mise en place *— everything prepped and in its place before
the work starts.)*

---

*Everything below this line is how it works inside.
The person using AI-Mise never needs any of it.* Internally, the machinery
that changes the setup is separate from the machinery that does the work
([[ADR-0005-builder-vs-workspace|ADR-0005]], [[ADR-0008-no-modes-tiered-application|ADR-0008]]) — separation the user benefits from
without ever seeing.

**The kernel:** [METHOD.md](METHOD.md) — one page that stays true regardless of platform, model, or decade. Everything else is an adapter.

## Product boundary (one sentence)

AI-Mise works out what you are doing — from your materials when you have them, from the conversation when you don't — asks a small number of justified questions, describes in plain language the workspace it would set up for your assistant, builds only what you approve, and can put anything back exactly as it was.

**Explicitly out of scope for the first release:** automatic self-improvement, SQLite, full wiki generation, multi-platform adapters, scheduled retrospectives, voice UX, marketplace distribution.

## One assistant — you name it

This is the promise being built (see Status below for what runs today):
the person using AI-Mise meets exactly one thing — an assistant they name at
the first hello. Small help is applied at once and can always be undone;
changes to how the assistant works are announced in plain words and wait for
a good moment. Nobody is asked to switch modes, and words like "builder" or
"compiler" never reach them.

## The two planes

| | Control plane (`control-plane/`) | Data plane (`workspace-template/` → a user's workspace) |
|---|---|---|
| Owns | Authority: policy, approval, mutation gateway, validators | Work: sources, knowledge, views, skills, decisions, generated artifacts |
| Written by | The user, manually and rarely | The agent — but **only through the mutation gateway** |
| Trust stance | Outside the agent's writable area; protected by OS + Claude Code permissions | Everything here is replaceable, restorable, and generated |

The workspace's `CLAUDE.md`, hooks, and skills are **generated platform projections** compiled from the control plane's policy — never the authoritative constitution itself. Swap the adapter, keep the workspace: that's the portability promise.

**Honesty note:** on a personal machine this boundary is protection against *accident and drift* — a confused or drifting agent — not against a determined adversary. A true security boundary requires OS-level sandboxing. The threat suite in `control-plane/threat-tests/` is scoped accordingly.

## The mutation gateway

Every persistent change follows one path:

```
Proposal → User approval of exact change set → Approval receipt
        → Stage in temporary worktree → Deterministic validators
        → Apply through gateway → Commit + restore tag + audit record
```

Approval covers a **transaction** (files, before/after hashes, plain-language purpose, risk category, validation results, rollback id, expiry) — not individual file operations. Fewer approvals, each one meaningful.

## Knowledge has three layers

```
sources/     immutable evidence — originals + hashed manifests, append-only
knowledge/   atomic claims with provenance (source span, authority, status,
             confidence, valid-from/until, contradicts/supersedes links)
views/       rebuildable synthesis — wiki pages, reports; never the source of truth
```

A view is never citable as evidence for a claim. This single rule prevents synthesis decay — AI summaries feeding AI summaries until nobody remembers the original fact.

## Non-technical surface (first-class requirement, every phase)

The person using an AI-Mise workspace never sees git, YAML, schemas, or hashes. They see: **Save Version · What Changed? · Safe Experiment · Keep It / Discard · Restore** — and proposals written in plain language. Any phase whose exit test can't be explained to a non-technical professional isn't done.

## Status

Phase 0 (contract + threat model) — **this repository is the Phase 0 deliverable**, plus the Phase 1 read-only first-contact skill. See `HANDOFF.md` for next actions, `docs/architecture.md` for the design, `docs/prior-art.md` for what we deliberately reuse from other projects, and `docs/decisions/` for why the architecture is shaped this way.

## The end-to-end scenario

One project runs end to end as the development fixture: every phase must improve the same run — inspect → constrain → ask → propose → build → perform a real task → absorb a correction → restore safely. The fixture is not the bar: what the product must clear is written without naming a profession ([[ADR-0011-exit-tests-name-capabilities|ADR-0011]]), and the generality test is a second pilot in a domain unlike the first.
