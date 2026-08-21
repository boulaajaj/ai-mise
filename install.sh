#!/usr/bin/env sh
# Installs AI-Mise under a name you choose, so that name is what you type.
# Needs nothing but a shell. Touches only your own skills folders.

set -e
HERE="$(pwd)"
SRC="$(cd "$(dirname "$0")" && pwd)/skills/ai-mise"
[ -f "$SRC/SKILL.md" ] || { echo "Run this from the repository root."; exit 1; }

printf 'What would you like to call it? [ai-mise] '
read -r RAW
[ -z "$RAW" ] && RAW="ai-mise"

NAME=$(printf '%s' "$RAW" | tr '[:upper:]' '[:lower:]' \
  | sed 's/[^a-z0-9]\{1,\}/-/g; s/^-*//; s/-*$//' | cut -c1-64)
[ -n "$NAME" ] || { echo "That leaves nothing usable. Letters and numbers work best."; exit 1; }
[ "$NAME" = "$RAW" ] || echo "Using \"$NAME\" - the format allows lowercase letters, numbers and hyphens."

ROOTS="$HOME/.claude/skills $HOME/.agents/skills"

for ROOT in $ROOTS; do
  if [ -e "$ROOT/$NAME" ]; then
    echo "$ROOT/$NAME already exists. Nothing was touched."
    echo "Choose another name, or move that folder aside first."
    exit 1
  fi
done

for ROOT in $ROOTS; do
  mkdir -p "$ROOT/$NAME"
  cp -R "$SRC/." "$ROOT/$NAME/"
  sed "s/^name: .*/name: $NAME/" "$SRC/SKILL.md" > "$ROOT/$NAME/SKILL.md"
  echo "installed  $ROOT/$NAME"
done

echo
echo "Type /$NAME in Claude Code, \$$NAME in Codex, /$NAME in Grok Build."
if command -v zip >/dev/null 2>&1; then
  ( cd "$HOME/.claude/skills" && zip -qr "$HERE/$NAME.zip" "$NAME" )
  echo "wrote      $HERE/$NAME.zip"
  echo "For Claude on your phone: upload that at claude.ai, Customize, Skills."
else
  echo "For Claude on your phone: zip $HOME/.claude/skills/$NAME and upload it"
  echo "at claude.ai, Customize, Skills."
fi
echo "To remove it, delete the folders named above. Nothing else was changed."
