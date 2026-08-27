# Installing AI-Mise

One command, or one sentence. Find the line for the thing you are using.

**Whichever route you take, you start it by saying its name.** "AI-Mise, have
a look at my setup" works everywhere. The typed shortcuts below differ from
tool to tool, and from route to route within the same tool — which is worth
knowing, and is why each one is spelled out. None of them is required.

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

```bash
claude plugin marketplace add boulaajaj/ai-mise
claude plugin install ai-mise@ai-mise --scope user
```

Inside a session already running, the same two steps are `/plugin marketplace
add boulaajaj/ai-mise` and then `/plugin install ai-mise@ai-mise`. The scope
picker appears there instead of the flag.

Then say `ai-mise`. If you would rather type, the shortcut on this route is
`/ai-mise:ai-mise` — Claude Code namespaces a plugin's skills as
`plugin:skill`, so the plugin name on its own is not a registered command
here and answers `Unknown command`.

**About `--scope`.** `--scope user` installs it for you everywhere, which is
almost always what you want. `--scope project` installs it only for the
directory you are standing in, so Claude Code loads it when started from
there and nowhere else — which looks exactly like a failed install if you
then go and check from somewhere else.

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
repository, and paste `https://github.com/boulaajaj/ai-mise`. This route goes
through your account rather than through one machine, which is what would
carry it to the phone and to Cowork. Say the name to start it.

> **Known issue.** This sync was failing as of 27 August 2026: the
> marketplace is created and arrives empty. The cause and the fix are
> [#141](https://github.com/boulaajaj/ai-mise/issues/141). Until it is
> confirmed working, the terminal routes above are the ones that install
> reliably. This note goes when the sync is verified, not before.

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

The plugin installers above use the marketplace's plugin name, so on Claude
Code you get `/ai-mise:ai-mise`. To call it something of your own, clone the
repository and run `install.sh` or `install.ps1` instead. It asks for a name,
installs under that name, and then that word is the trigger: `/celine` in
Claude Code, `$celine` in Codex. A bare word this time, with nothing before
the colon, because this route places the skill folder directly rather than
inside a plugin.

### What each route leaves you with

Saying the name works in every row. The differences are in what you can type
and where it is available, and they are the reason "is it even installed?"
was a hard question to answer.

<!-- trigger-ok-start: the gh skill route places the skill folder directly rather than inside a plugin, so the bare folder name really is its trigger -->

| Route | Typed shortcut | Available where |
| --- | --- | --- |
| `claude plugin install … --scope user` | `/ai-mise:ai-mise` | everywhere you use Claude Code |
| `claude plugin install … --scope project` | `/ai-mise:ai-mise` | only when started from that one directory |
| `gh skill install … --agent claude-code` | `/ai-mise` | everywhere, at user scope |
| `install.sh` / `install.ps1` | the name you chose, e.g. `/celine` | everywhere, at user scope |
| claude.ai marketplace | — none | every surface on your account — see the known issue above |

<!-- trigger-ok-end -->

## What is placed

The skill folder, `ai-mise`, holding `SKILL.md` and the scripts beside it.

The installers put it in two places, `~/.claude/skills/` and
`~/.agents/skills/`, because different tools look in different ones, and
that is what lets a single command cover all of them. They also write a zip
next to you, which exists only for the claude.ai upload that carries the
skill to a phone. Delete it once you have used it. Every path written is
printed as it happens.

Whatever is already on the machine stays exactly as it is. No existing
`CLAUDE.md`, `AGENTS.md` or skill is edited, and no folder someone else made
is overwritten. Where something already sits under that name, the install
stops and says what it found rather than deciding for you.

Nothing here needs a runtime you do not already have. Where a step wants one
the machine lacks, the same result is reached another way, and which way is
said out loud.

## Check it worked

There are five states between running the installer and having something
useful, and only two of them are ours. Knowing which one you are in is the
difference between a two-minute fix and an afternoon.

| State | How you can tell | If you are stuck here |
| --- | --- | --- |
| **Installed** | the installer printed the paths it wrote | re-run it and read what it printed; it stops rather than overwriting |
| **Loaded** | the tool lists it — `/plugin` in Claude Code, `/skills` in Codex | wrong scope is the usual cause: a project-scope install only loads from its own directory |
| **Trusted** | no "this workspace has not been trusted" warning | accept the trust prompt. Until you do, the tool ignores the permissions in the folder's settings and says so |
| **Authenticated** | you are signed in to the tool itself | run `/login`. Headless runs (`claude -p`) fail here with `Not logged in` |
| **Invokable** | you say the name and it answers | if the first four hold and it still does nothing, that one is ours — please open an issue |

The middle three are the tool's gates, not AI-Mise's. They are listed here
because they all land between "installed" and "working", which is exactly
where it is easy to conclude the thing is broken when it is not.

Then check that it actually does something. Say its name and ask it to look
at the setup you are already in, changing nothing. What comes back should
name things you recognise — what is switched on here, what is sitting unused
— and should end with something you can do next. If it describes a generic AI
setup rather than yours, it did not orient, and that is worth knowing before
you rely on it.

## Removing it

Delete the folders the installer named when it ran, and nothing else. Where
you linked to a clone rather than copying, remove the link and do not follow
it — following it deletes the clone it points at. The clone, if there is one,
is yours and stays.

Your own configuration should be byte-for-byte what it was before.
