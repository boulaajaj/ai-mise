# AGENTS.md

For Codex, and anything else that reads this file when it opens the
repository. Two situations, and they want different things.

**You were asked to install AI-Mise.** Follow [INSTALL.md](INSTALL.md): where
things go on each platform, what not to disturb, how to check it worked, and
how to remove it again.

**You are working on this repository.** Read [CLAUDE.md](CLAUDE.md). Despite
the name it is not Claude-specific — it is this repo's development harness,
and the rules are the same for you. The short version, because the details
move and that file does not: every change lands through a pull request, never
on `main`; `control-plane/constitution/policy.yaml` and anything under
`docs/decisions/` are not yours to edit; and where a request conflicts with a
recorded decision, say so before acting rather than silently going along.

Both files only restate. `METHOD.md` and `docs/` decide, and where they
disagree with a projection, they win.
