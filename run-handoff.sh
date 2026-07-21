#!/usr/bin/env bash
set -euo pipefail
cd /c/Users/ameen/repos/ai-mise
R="boulaajaj/ai-mise"

# Decision 1: fresh description (verified: old name was already absent; freshening anyway)
gh repo edit "$R" --description "AI-Mise - your AI mise en place. A governed workspace compiler: it interviews you, inspects your materials, and builds an auditable, versioned, agent-ready AI workspace. Formats over tools; approval over drift." >/dev/null
echo DESCRIPTION-SET

# Generate the mind map (Decision 2)
python tools/generate_mindmap.py

# Refactor issues 22 and 27 to format-first language (flagged change per handoff)
gh issue comment 22 -R "$R" -b "REFACTORED per ADR-0006 (formats over tools, from Amine's chat-session handoff): the deliverable is a wikilink-linked plain-markdown knowledge graph with the mind map as GENERATED Mermaid committed in-repo (tools/generate_mindmap.py already ships for the dev repo itself; the workspace compiler will emit the same for generated workspaces). Obsidian/Logseq/Foam are optional viewers, never dependencies. Original Obsidian-centric wording superseded." >/dev/null
gh issue comment 27 -R "$R" -b "Scope update per ADR-0006: v0 mind-map piece = generated Mermaid graph committed in-repo + wikilink canon (viewable on GitHub natively, and in Obsidian/Logseq if desired) - not an Obsidian-specific vault. Everything else unchanged." >/dev/null
echo ISSUES-REFACTORED

gh issue create -R "$R" --title "Wire mind-map regeneration into mini CI + adopt wikilinks in docs" --milestone "v0 Personal Preview" --body "Two follow-ups from ADR-0006: (1) regenerate docs/mindmap.md automatically on change (hook locally now; repo CI later) so the committed view never goes stale; (2) migrate internal doc cross-references toward [[wikilink]] canon where natural, keeping standard links working (generator already reads both). Acceptance: editing a doc's links and committing updates the mind map without a human remembering to run the generator." >/dev/null
echo ISSUE-CREATED

git add -A
git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Adopt ADR-0006 (formats over tools): generated Mermaid mind map, dependency vendor-death register, fresh description'
git push -q
echo PUSHED
rm -- "$0"
git add -A && git -c user.name='Amine Boulaajaj' -c user.email='ameen.b@gmail.com' commit -q -m 'Remove one-time script' && git push -q
echo DONE
