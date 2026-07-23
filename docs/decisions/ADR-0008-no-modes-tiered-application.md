# ADR-0008: No modes — changes carry the label, tiered by risk

**Status:** Proposed · 2026-07-21 (merge = agreement)
**Refines:** [[ADR-0005-builder-vs-workspace|ADR-0005]] (identities stay; the separate-session default is dropped). **Supersedes** issue #36's persistent Setup/Work indicator design (issue retitled accordingly).
**Trigger:** Amine: "anything that gets in the way of the user is forbidden" — but users must still know when their infrastructure changes.

## Decision

All items below are [default] — chosen product behavior, adjustable via policy, not derived from research.

1. **One conversation. No mode switching.** The user never travels to a setup mode; the *change* is labeled, not the user. #36's indicator becomes a per-change badge, not a state.
2. **Naming settled:** user-facing badge word is **"Setup"** ("Setup change — undoable anytime"). The user-named assistant is the single user-facing identity; "the Builder" and "Work Mode / Setup Mode" are retired from user-facing vocabulary.
3. **Tiered application:**
   - **Routine + low-risk structural** (save a skill, schedule a task, record a preference): applied immediately, versioned with a restore point, acknowledged in one line. Reviewed in batch later; trivially reversible.
   - **Fail closed:** if the restore point, rollback identifier, before/after hashes, or validation results cannot be produced, immediate application is refused and the change falls back to a queued proposal. No undo guarantee, no instant apply.
   - **Governance + safety tier:** still pause for explicit approval — but **never mid-task**. They queue and are raised at a natural break. Danger is the only exception.
4. **Queryable, silent bookkeeping.** Commits, versions, receipts happen invisibly; "what changed this week?" answers from the change log in plain language.

## Consequences

- Approval stays meaningful by becoming rarer: only the tiers where a wrong change truly hurts.
- The undo guarantee is what makes instant application safe — Phase 2's hash-exact restore (issue #11) is a hard prerequisite for this UX, and the fail-closed rule above holds until it ships.
- Threat scenario 30 in [[scenarios]] unchanged: shadow-mode self-improvement still never self-applies; this ADR covers *user-requested* help only. Loyal dissent per [[ADR-0007-challenge-before-compliance|ADR-0007]] applies before any tier is entered.
- policy.yaml risk-tier table gains an `apply` column (proposal for Amine to apply by hand).
