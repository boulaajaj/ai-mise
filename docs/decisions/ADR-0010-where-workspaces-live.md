# ADR-0010: Vendor the format, install the machinery

**Status:** Proposed · 2026-07-26 (merge = agreement)
**Trigger:** Amine, issue #69: "How is this going to live beside the user's environment and repository? Is this going to be part of the repository? Is it going to be completely independent? It is still foggy."

## Context

The fog was ours. [[deployment]] sketched three pieces and was honest about being a working doc; meanwhile #12 (adapter output location), #27 (v0 preview), #47 (install), #48 (isolation) and #22 (vault) each proceeded on a private assumption about the answer. Assumptions held privately by four issues are how a project acquires a decision it never made.

Three positions were weighed in #69, plus two later ones. The self-contained workspace (everything vendored) is the most literal reading of [[ADR-0006-formats-over-tools|ADR-0006]] and gives maximum portability, at the cost of N copies of code to upgrade. The installed tool with a thin workspace matches how developer tooling is usually distributed and upgrades in one place, but the folder is then not self-describing: hand it to someone else and it cannot be reconstructed. The template-plus-pull-requests model makes upgrades reviewable, which is attractive, but it requires the person to have a git remote before they have any value, and we expect drift once people edit generated files *[default]*.

The split that resolves this is not between the three options; it runs *through* them. Some of what a workspace contains must outlive this project entirely. The rest is replaceable code.

## Decision

**Vendor the format. Install the machinery.** This is [[METHOD|the kernel-and-adapter discipline]] applied to deployment rather than to documents.

1. **A workspace is a local git repository**, initialized quietly at creation. Git is how "restore any prior state exactly" (#11) is actually delivered, and per [[ADR-0008-no-modes-tiered-application|ADR-0008]] the person never sees it. **No remote is created and none is required** — a remote means an account and an upload, which are the person's decisions, not preconditions for first value (#47).

2. **The workspace carries everything that means something and nothing that executes.** It carries the constitution that governs it and the schemas its files are written against — **as projections, never as sources**: the authoritative policy and schemas stay in the control plane, outside the agent-writable tree, and changing them stays a deliberate act there ([[ADR-0001-control-plane-separation|ADR-0001]]). Alongside them it carries claims, sources, memory, views, receipts, and a version marker naming the Builder version that wrote it. Validators, hooks, adapters and the mutation gateway are installed once per machine and are referenced, never copied. **What travels is the record of what governed the work, not the authority to govern it**: a folder must be readable without us, and a workspace must never be able to rewrite its own rules. Meaning must survive us; code is replaceable, and N copies of code is N upgrade problems.

3. **Improvements never arrive silently.** Upgrading the machinery is one action in one place and changes no workspace. A vendored format change reaches a given workspace only through Setup Mode, as a proposed transaction with a plain-language purpose, an approval and a rollback — the same path as any other change ([[ADR-0003-shadow-mode-self-improvement|ADR-0003]]). **A workspace may therefore be older than the Builder, and that is legal**: the version marker makes the gap visible and the Builder reads older formats.

4. **What travels is the folder.** Copy it to another machine or hand it to another person; install the Builder there; it works. Reading never requires the Builder at all, because the files are markdown. Two constraints follow and are binding: **no absolute paths are ever written into workspace files**, and **no credentials are ever stored in a workspace**.

5. **Beside a new project, inside an existing one.** With nothing to preserve, the workspace *is* the project folder, visibly named by the person. Where a project folder already exists, everything lands in a single `.ai-mise/` directory inside it — one thing to inspect, one thing to delete, zero residue (#48). Nothing outside that directory is written without an approved transaction that shows the person exactly what would change.

6. **Committing is the person's choice, asked once, at the moment it matters** — never as setup configuration. The default is not committed. When they choose to commit, the **governed** material goes in (constitution, schemas, claims, sources index, views, receipts) and the **personal** layer stays out by ignore rule (memory and preferences). A receipt is what makes a change reversible and auditable, so it belongs with the work rather than with the person. A team can share a governed workspace without sharing one person's memory of themselves.

## The three workflows

**Starting from nothing.** Install once. Have a conversation. The Builder asks only what it cannot infer and what would change its recommendation (#24), proposes a workspace in plain language, and on approval creates the folder, initializes git quietly, writes the vendored format and records the receipt. No account, no remote, no configuration before first value.

**Starting from something that already exists.** First contact is read-only — the inspector reads and never writes. The Builder reports what it found (an existing `CLAUDE.md` or `AGENTS.md`, skills, conventions, prior structure) and proposes bringing it under governance **one piece at a time**, each as its own approved transaction. Existing files are never overwritten in place: an existing instruction file is **adopted as a source** first, and a compiled one is written only when the person approves the replacement, with the original preserved and restorable. When the person says "just work with what I already have," the correct outcome is a workspace that references their existing configuration and adds only what is missing.

**Living with the Builder.** Setup Mode is a conversation, not a settings screen ([[ADR-0005-builder-vs-workspace|ADR-0005]]). Changes arrive as proposals; approval is per transaction; every change leaves a receipt and a way back. Uninstalling removes the plugin and the machinery and leaves every workspace readable forever, because they were only ever markdown.

## Consequences

- [[ADR-0001-control-plane-separation|ADR-0001]] is refined, not superseded, and it is the reason decision 2 says *projections, never sources*: a workspace holding its own authority would be exactly the circular defense ADR-0001 exists to prevent.
- [[deployment]] remains a working doc and keeps what it is good at — the platform target order (Claude Code now, Codex later, OpenHarness later) and the v0 slice. The lifecycle questions it used to sketch are decided here, and it now points here for them.
- **New binding constraints on generated content:** no absolute paths, no credentials, and a version marker in every workspace. These need a validator (#9) — a workspace that cannot move is a bug, not a preference.
- The Builder must read formats older than itself. This is a real cost and it is the price of never changing someone's workspace without asking.
- #12, #27, #47, #48 and #22 now share one written answer instead of four private ones.
- One plain-language companion ships with this decision: [[where-your-work-lives]].

## Alternatives not taken

**Template plus pull requests** — rejected for now: it requires a git remote before the person has received any value, and it inherits the drift problem noted in the context above. The reviewable-upgrade instinct behind it is preserved by decision 3, which makes every upgrade an approved transaction with a diff.

**Scoped configurations as git branches** (Adaptive Auto-Harness, arXiv 2606.01770 — its harness tree, per-branch tool registries and solve-time router) — not taken now. Long-lived divergent branches are git's sharpest edge for a non-technical person, and scoping is adequately served by directories plus policy without a router. Revisit if #24's scope taxonomy proves that directories cannot express it. *[prior art]*

**The workspace behind a local service** — deferred, not rejected. Files remain the authority either way, so a service is an access layer over this decision rather than an alternative to it. It becomes the right question when a host that cannot read files becomes a target — [[deployment]] names today's example and gives the reasoning; #69 keeps the analysis.
