# ADR-0013: History is local by default; the remote is the person's choice

**Status:** Proposed · 2026-07-27 (merge = agreement)
**Trigger:** Amine's directive, 2026-07-27, settling how source control and cloud storage should work: "Local history is automatic; external storage is optional; uploading is never automatic."

## Context

[[ADR-0010-where-workspaces-live|ADR-0010]] already made the workspace a local git repository with no remote required. What it did not settle is whether the person has to *know* that, or how a remote gets chosen when someone wants one.

The repository answered both by accident. `setup/setup-github.sh` is 168 lines — the largest executable file here — and it creates a GitHub repository. Whatever the documents said, GitHub was the default path by construction.

The README already promises that the person never sees git. Storage is the half of that promise that had not been kept: a person keeping notes about a house renovation does not have a GitHub account, and asking them to make one is the moment they stop.

## Decision

All decisions below are *[default]* — chosen product behavior, not derived from research.

1. **Version history happens quietly and requires no account.** From the first save the workspace keeps its own history, locally. The person is not asked to create anything, sign in anywhere, or learn what a commit is. They see *Save Version · What Changed? · Restore*, as the README already says.

2. **A remote is optional, named by the person, and never assumed.** GitHub, GitLab, OneDrive, Google Drive, an external disk, a folder that something else already syncs — all equally valid. The product prefers none of them and recommends none of them unasked.

3. **Nothing is uploaded automatically, ever.** Upload happens when the person asks, to the place they named, with what they chose. Silence is not consent, and neither is having connected an account once for something else.

4. **The GitHub setup script leaves the default path.** It remains available for people who want it. It stops being what "setting up AI-Mise" means.

## Consequences

- Install must be able to complete with no account of any kind. #47 gains that as a constraint.
- `HANDOFF.md` states that the setup script "creates the private repo." That was already wrong — this repository is public — and decision 4 makes it wrong twice. Tracked separately.
- [[ADR-0010-where-workspaces-live|ADR-0010]] decision 4 said what travels is the folder, with no absolute paths and no credentials. This is its complement: what does not travel is anything the person did not send.
- Personal-data handling (#87) gains a hard edge it needs. An obligation about deletion only means something if nothing left the machine unasked in the first place.
- The vendor-death test in [[ADR-0006-formats-over-tools|ADR-0006]] decision 4 now applies to storage. No remote may become a dependency by habit.

## Alternatives not taken

**Require a remote so history is durable** — rejected: durability that costs an account costs it from the people least able to absorb the friction, and a local repository plus whatever backup the person already runs is how every other file they own is protected.

**Bless one remote and support it properly** — rejected: a blessed remote becomes a dependency by habit even when the documents call it optional, which is precisely how GitHub became the default here without anyone deciding it.

**Ask at first run where history should live** — rejected: it is a question whose answer does not change what happens next, which the voice section of [[METHOD]] rules out. Local history works immediately; the person can name a remote the day they want one.
