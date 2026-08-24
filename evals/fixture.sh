#!/usr/bin/env sh
# Builds the synthetic evaluation fixture. Deterministic: the same tree every
# time, so a result from one machine can be compared with one from another.
#
# The fixture is a small volunteer-run site whose AI configuration has five
# defects planted in it. None are labelled; a run has to find them.
#
#   1. a postgres-reporting MCP server, unused, under a key Claude Code does
#      not read from settings.json
#   2. CLAUDE.md at 229 lines, 220 of which list files that do not exist
#   3. .cursorrules contradicting CLAUDE.md on voice, and never loaded
#   4. a changelog-writer skill needing git history in a folder with no repo
#   5. Bash(npm run build) permitted with no package.json
#
# Usage: sh fixture.sh <destination-directory>

set -e
DEST="${1:?usage: fixture.sh <destination-directory>}"

# Strip trailing slashes before any test. `[ -L dir/ ]` is false even when
# dir is a link, because the slash forces the kernel to resolve it, so a
# single stray character would have walked straight through the guard below.
while [ "${DEST%/}" != "$DEST" ]; do
  DEST="${DEST%/}"
done
if [ -z "$DEST" ]; then
  echo "fixture.sh: refusing to build at the filesystem root" >&2
  exit 2
fi

# The fixture is only comparable across machines if the tree is only the
# fixture, so refuse a destination that would leave other files mixed in,
# or that would write through a link to somewhere else. This also stops the
# obvious accident: run with `.` in a working tree, it overwrites that
# project's own CLAUDE.md with the 229-line one planted below.
if [ -L "$DEST" ]; then
  echo "fixture.sh: destination is a symlink, refusing: $DEST" >&2
  exit 2
fi
if [ -e "$DEST" ]; then
  # An unreadable directory makes `ls -A` fail and print nothing, which read
  # as "empty" and let the fixture land on top of whatever was in it.
  if ! CONTENTS=$(ls -A "$DEST" 2>/dev/null); then
    echo "fixture.sh: cannot list destination, refusing: $DEST" >&2
    exit 2
  fi
  if [ -n "$CONTENTS" ]; then
    echo "fixture.sh: destination is not empty, refusing: $DEST" >&2
    echo "fixture.sh: give a new directory, or remove that one first" >&2
    exit 2
  fi
fi

mkdir -p "$DEST/.claude/skills/changelog-writer" "$DEST/src" "$DEST/content"
cd "$DEST"

cat > .claude/settings.json <<'EOF'
{
  "permissions": { "allow": ["Read", "Grep", "Glob", "Bash(npm run build)"] },
  "enabledPlugins": {},
  "mcpServers": {
    "postgres-reporting": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/eastside"]
    }
  }
}
EOF

cat > .claude/skills/changelog-writer/SKILL.md <<'EOF'
---
name: changelog-writer
description: Turns merged pull requests into a plain-language changelog entry for the public site.
---
Read the merged PRs since the last release tag. Write one short paragraph per
user-visible change, in plain language, no jargon. Skip internal refactors.
EOF

# The counter is written out rather than using `seq`, which is not POSIX. A
# missing seq failed silently inside the `for` list and produced a 9-line
# CLAUDE.md, quietly removing the second planted defect.
{
  echo "# Eastside Neighbourhood Site"
  echo
  echo "## Voice"
  echo
  echo "Write warmly and at length. Residents like detail, so err on the side of"
  echo "more explanation rather than less. Use a friendly, chatty register."
  echo
  echo "## Repository layout"
  echo
  for d in src content public scripts config tests docs assets vendor legacy; do
    for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22; do
      echo "- \`$d/module_$i.ts\` - part of the $d area"
    done
  done
} > CLAUDE.md

cat > .cursorrules <<'EOF'
Keep all resident-facing copy short. Maximum three sentences per section.
Neutral, factual register - avoid chatty or conversational phrasing.
EOF

cat > README.md <<'EOF'
# Eastside Neighbourhood Site

A volunteer-run site for the Eastside neighbourhood association: meeting
notes, an events calendar, and a directory of local services. Two volunteers
maintain it. Content is written by whoever is free that week, which is why
the tone drifts.
EOF

echo "Board meeting, 4 March. Traffic calming on Vine St discussed." > content/2026-03-04-meeting.md
echo "Board meeting, 1 April. Budget approved for the spring cleanup." > content/2026-04-01-meeting.md
echo "export function renderCalendar(events: Event[]) { /* ... */ }" > src/calendar.ts
echo "export function renderDirectory(orgs: Org[]) { /* ... */ }" > src/directory.ts

# The header above claims 229 lines and five planted defects. Check the claim
# rather than trusting it: a fixture that quietly lost a defect would show up
# as the skill failing to find something that was never there.
LINES=$(wc -l < CLAUDE.md | tr -d ' ')
if [ "$LINES" -ne 229 ]; then
  echo "fixture.sh: CLAUDE.md is $LINES lines, expected 229 - fixture is wrong" >&2
  exit 1
fi
