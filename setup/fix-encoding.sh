#!/usr/bin/env bash
# One-time repair: milestone titles / issue bodies / committed script picked up
# double-encoded em-dashes (UTF-8 read as CP1252, re-encoded). Pure-ASCII file.
set -euo pipefail
FULL="boulaajaj/harnessmith"
BAD=$'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d'   # mojibake of em-dash
EM=$'\xe2\x80\x94'                        # proper em-dash

for n in 1 2 3 4 5 6 7; do
  t=$(gh api "repos/$FULL/milestones/$n" -q .title)
  f=${t//$BAD/$EM}
  if [ "$t" != "$f" ]; then
    gh api -X PATCH "repos/$FULL/milestones/$n" -f title="$f" >/dev/null
    echo "fixed milestone $n: $f"
  fi
done

for n in $(seq 1 19); do
  b=$(gh issue view "$n" -R "$FULL" --json body -q .body)
  f=${b//$BAD/$EM}
  if [ "$b" != "$f" ]; then
    gh issue edit "$n" -R "$FULL" --body "$f" >/dev/null
    echo "fixed issue $n body"
  fi
done

# repair the committed setup script itself
c=$(cat setup/setup-github.sh)
printf '%s' "${c//$BAD/$EM}" > setup/setup-github.sh

# sanity: confirm directly-written UTF-8 files were never affected
if git grep -q "$BAD" -- ':!setup/fix-encoding.sh'; then
  echo "WARNING: mojibake remains in tracked files:"; git grep -l "$BAD" -- ':!setup/fix-encoding.sh'
else
  echo "tracked files clean"
fi
echo "done"
