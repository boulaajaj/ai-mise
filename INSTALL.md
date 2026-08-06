# Installing AI-Mise

Point your assistant at this repository and say install. What follows is the
protocol it reads. You are welcome to read along — nothing here is hidden
from you, and the last step is it telling you in plain words what it did.

## Two things get placed

The **skill** is the part that does the work: one folder, `skills/ai-mise/`,
holding `SKILL.md` and the scripts beside it.

The **control plane** is the part the skill is not allowed to rewrite:
`control-plane/`, holding the policy the skill reads its own limits from.
Keeping it outside the skill is the point — the rules stay out of reach of
the thing they govern ([ADR-0001](docs/decisions/ADR-0001-control-plane-separation.md)).

A workspace is not installed. It is built later, in the person's own project,
and only with their approval.

## Before placing anything

Whatever is already on this machine stays exactly as it is. Never edit an
existing `CLAUDE.md`, `AGENTS.md`, or skill. Never overwrite a folder you did
not create. Keep everything under a name of our own so that removing it later
is unambiguous. If something already sits at one of the paths below, stop and
say what you found rather than deciding for them.

Do not ask them to install a runtime. Use what the machine already has; where
you need something it does not have, reach the same result another way and
say which route you took.

## Where things go

You know which tool you are. Do not ask.

**Claude Code** — skill to `~/.claude/skills/ai-mise/`, control plane to
`~/ai-mise/control-plane/`.

**Codex** — skill to `~/.agents/skills/ai-mise/`, control plane to
`~/ai-mise/control-plane/`. Putting the skill in `.agents/skills/` inside a
project instead makes it available to everyone working on that project.

**ChatGPT** — there is no disk to install onto. Upload
`skills/ai-mise/SKILL.md` and say what that costs: the folder inventory does
not run there, and the skill cannot reach the control plane, so it works from
what is uploaded and nothing else ([deployment](docs/deployment.md)).

**Anything else** — if the tool loads instructions from files, the same two
placements apply; use its own skills directory in place of the ones above and
keep the `ai-mise` name. If it does not, say so rather than improvising.

Where you already have a clone and the tool follows links, link to the two
folders in place rather than copying, so `git pull` updates them. Where links
are awkward — Windows without WSL — copy, and tell them that updating means
copying again.

## Check it worked

Three checks. The skill loads, so they can start it by name. The inventory
step runs — either `python3 scripts/inventory.py --help` answers, or you have
confirmed some other hashing route the machine already has. And
`control-plane/constitution/policy.yaml` opens from where you put it, because
the skill reads its question limits there rather than from memory.

If any of the three fails the install is not finished. Say which one, and what
you would do about it.

## Then say what happened

In their words. What you placed and where, that nothing else was touched, and
what it can do today: read a folder you point it at, or talk it through when
there is no folder, and hand back a written proposal for the workspace it
would set up. Then say what it cannot do, because that matters more — it
builds nothing yet.

If they gave you a folder, offer to look at it now. If they did not, that is
an ordinary start too.

## Removing it

Delete the two folders you created, and nothing else. Their own configuration
should be byte-for-byte what it was before. If you changed anything outside
those two folders, saying so is better than leaving it.
