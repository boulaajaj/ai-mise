# Installing AI-Mise

One command, or one sentence. Find the line for the thing you are using.

## If you have a terminal

The single command that covers the most tools:

```bash
gh skill install boulaajaj/ai-mise ai-mise --scope user
```

That installs it for GitHub Copilot by default. Add `--agent claude-code`,
`--agent codex`, `--agent gemini` or `--agent cursor` to put it where one of
those looks instead.

If you would rather use the tool's own installer:

**Claude Code**

```
/plugin marketplace add boulaajaj/ai-mise
/plugin install ai-mise@ai-mise
```

**Codex**

```bash
codex plugin marketplace add boulaajaj/ai-mise
codex plugin add
```

**Grok Build**

```bash
grok plugin marketplace add boulaajaj/ai-mise
grok plugin install ai-mise
```

**Gemini CLI**

```bash
gemini extensions install https://github.com/boulaajaj/ai-mise --auto-update
```

**Cursor** — Dashboard, Plugins, Team Marketplaces, Add Marketplace, Import
from Repo, then this repository.

## If you do not have a terminal

**Claude, on the web, on the desktop, or on your phone.** Customize in the
sidebar, then Plugins, then the plus button, Add marketplace, Add from a
repository, and paste `https://github.com/boulaajaj/ai-mise`. It syncs
through your account, so it turns up on the phone as well.

## If your assistant cannot install anything

Then there is nothing to install, and one sentence does it. Paste this:

```
Read https://raw.githubusercontent.com/boulaajaj/ai-mise/main/skills/ai-mise/SKILL.md and follow it. Remember it for future conversations.
```

That works in ChatGPT, in Grok, and in Claude with web search switched on.
The second sentence is the part that makes it stick: each of those can save
it themselves when asked, and so can Microsoft Copilot.

It does not work in the Gemini app, which searches the web rather than
opening a link you hand it, or in Copilot's consumer chat, which reads Bing's
index rather than the page itself. For those, and for Grok without a
terminal:

**Gemini** — Gems, New Gem, and paste the file in as the instructions. A Gem
can then be shared by link, and whoever has that link can use it without
signing in at all.

**Grok** — grok.com/skills, and upload the file. Grok keeps a skill across
every conversation.

**Meta AI** — nothing reliable. There is no instructions field, and AI Studio
stopped accepting new assistants in August 2026. You can tell it single
things to remember in a one-to-one chat, in the US and Canada, and that is
the whole of it.

## Calling it something else

Every installer above uses the folder name as the word you type, so you get
`/ai-mise`. To call it something of your own, clone the repository and run
`install.sh` or `install.ps1` instead. It asks for a name, installs under
that name, and then that word is the trigger: `/celine` in Claude Code,
`$celine` in Codex.

## What is placed

One folder, `ai-mise`, holding `SKILL.md` and the scripts beside it. Nothing
else, nowhere else.

Whatever is already on the machine stays exactly as it is. No existing
`CLAUDE.md`, `AGENTS.md` or skill is edited, and no folder someone else made
is overwritten. Where something already sits under that name, the install
stops and says what it found rather than deciding for you.

Nothing here needs a runtime you do not already have. Where a step wants one
the machine lacks, the same result is reached another way, and which way is
said out loud.

## Check it worked

Two checks.

The first is that it loads, so you can start it by name.

The second is that it does something. Ask it to look at the setup you are
already in, and to change nothing. What comes back should name things you
recognise — what is switched on here, what is sitting there unused. If it
describes a generic AI setup rather than yours, it did not orient, and that
is worth knowing before you rely on it.

## Removing it

Delete the folder that was created, and nothing else. Where you linked to a
clone rather than copying, remove the link and do not follow it — following
it deletes the clone it points at. The clone, if there is one, is yours and
stays.

Your own configuration should be byte-for-byte what it was before.
