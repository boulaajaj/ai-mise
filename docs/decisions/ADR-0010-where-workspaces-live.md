# ADR-0010: Vendor the format, install the machinery

**Status:** Proposed · 2026-07-26 (merge = agreement)
**Trigger:** Amine, issue #69: "How is this going to live beside the user's environment and repository? Is this going to be part of the repository? Is it going to be completely independent? It is still foggy."

## Context

The fog was ours. [[deployment]] sketched three pieces and was honest about being a working doc; meanwhile #12 (adapter output location), #27 (v0 preview), #47 (install), #48 (isolation) and #22 (vault) each proceeded on a private assumption about the answer. Assumptions held privately by four issues are how a project acquires a decision it never made.

Three positions were weighed in #69, plus two later ones. The self-contained workspace (everything vendored) is the most literal reading of [[ADR-0006-formats-over-tools|ADR-0006]] and gives maximum portability, at the cost of N copies of code to upgrade. The installed tool with a thin workspace is how ordinary developer tools behave and upgrades in one place, but the folder is then not self-describing: hand it to someone else and it cannot be reconstructed. The template-plus-pull-requests model makes upgrades reviewable, which is attractive, but it requires the person to have a git remote before they have any value, and template drift is a well-documented failure once people edit generated files.

The split that resolves this is not between the three options; it runs *through* them. Some of what a workspace contains must outlive this project entirely. The rest is replaceable code.

## Decision

**Vendor the format. Install the machinery.** This is [[METHOD|the kernel-and-adapter discipline]] applied to deployment rather than to documents.

1. **A workspace is a local git repository**, initialized quietly at creation. Git is how "restore any prior state exactly" (#11) is actually delivered, and per [[ADR-0008-no-modes-tiered-application|ADR-0008]] the person never sees it. **No remote is created and none is required** — a remote means an account and an upload, which are the person's decisions, not preconditions for first value (#47).

2. **The workspace carries everything that means something and nothing that executes.** It holds its own constitution (`policy.yaml`, user-owned), the schemas that describe its own files, claims, sources, memory, views, receipts, and a version marker naming the Builder version that wrote it. Validators, hooks, adapters and the mutation gateway are installed once per machine and are referenced, never copied. Meaning must survive us; code is replaceable, and N copies of code is N upgrade problems.

3. **Improvements never arrive silently.** Upgrading the machinery is one action in one place and changes no workspace. A vendored format change reaches a given workspace only through Setup Mode, as a proposed transaction with a plain-language purpose, an approval and a rollback — the same path as any other change ([[ADR-0003-shadow-mode-self-improvement|ADR-0003]]). **A workspace may therefore be older than the Builder, and that is legal**: the version marker makes the gap visible and the Builder reads older formats.

4. **What travels is the folder.** Copy it to another machine or hand it to another person; install the Builder there; it works. Reading never requires the Builder at all, because the files are markdown. Two constraints follow and are binding: **no absolute paths are ever written into workspace files**, and **no credentials are ever stored in a workspace**.

5. **Beside a new project, inside an existing one.** With nothing to preserve, the workspace *is* the project folder, visibly named by the person. Where a project folder already exists, everything lands in a single `.ai-mise/` directory inside it — one thing to inspect, one thing to delete, zero residue (#48). Nothing outside that directory is written without an approved transaction that shows the person exactly what would change.

6. **Committing is the person's choice, asked once, at the moment it matters** — never as setup configuration. The default is not committed. When they choose to commit, the **governed** material goes in (constitution, schemas, claims, sources index, views) and the **personal** layer stays out by ignore rule (memory, preferences, their own approval receipts). A team can share a governed workspace without sharing one person's memory of themselves.

## The three workflows

**Starting from nothing.** Install once. Have a conversation. The Builder asks only what it cannot infer and what would change its recommendation (#24), proposes a workspace in plain language, and on approval creates the folder, initializes git quietly, writes the vendored format and records the receipt. No account, no remote, no configuration before first value.

**Starting from something that already exists.** First contact is read-only — the inspector reads and never writes. The Builder reports what it found (an existing `CLAUDE.md` or `AGENTS.md`, skills, conventions, prior structure) and proposes bringing it under governance **one piece at a time**, each as its own approved transaction. Existing files are never overwritten in place: an existing instruction file is **adopted as a source** first, and a compiled one is written only when the person approves the replacement, with the original preserved and restorable. When the person says "just work with what I already have," the correct outcome is a workspace that references their existing configuration and adds only what is missing.

**Living with the Builder.** Setup Mode is a conversation, not a settings screen ([[ADR-0005-builder-vs-workspace|ADR-0005]]). Changes arrive as proposals; approval is per transaction; every change leaves a receipt and a way back. Uninstalling removes the plugin and the machinery and leaves every workspace readable forever, because they were only ever markdown.

## Consequences

- [[deployment]] is promoted from working doc to decision and now points here; its target order (Claude Code now, Codex later, OpenHarness later) is unaffected.
- **New binding constraints on generated content:** no absolute paths, no credentials, and a version marker in every workspace. These need a validator (#9) — a workspace that cannot move is a bug, not a preference.
- The Builder must read formats older than itself. This is a real cost and it is the price of never changing someone's workspace without asking.
- #12, #27, #47, #48 and #22 now share one written answer instead of four private ones.
- One plain-language companion ships with this decision: [[where-your-work-lives]].

## Alternatives not taken

**Template plus pull requests** — rejected for now: it requires a git remote before the person has received any value, and template drift once generated files are edited is a well-known and painful failure. The reviewable-upgrade instinct behind it is preserved by decision 3, which makes every upgrade an approved transaction with a diff.

**Scoped configurations as git branches** (Adaptive Auto-Harness, arXiv 2606.01770 — its harness tree, per-branch tool registries and solve-time router) — not taken now. Long-lived divergent branches are git's sharpest edge for a non-technical person, and scoping is adequately served by directories plus policy without a router. Revisit if #24's scope taxonomy proves that directories cannot express it. *[prior art]*

**The workspace behind a local service** — deferred, not rejected. Files remain the authority either way, so a service is an access layer over this decision rather than an alternative to it. It becomes the right question when a host that cannot read files (today, ChatGPT) becomes a target; #69 keeps the analysis.
