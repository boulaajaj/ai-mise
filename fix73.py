import io, sys

path = 'docs/where-your-work-lives.md'
with io.open(path, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

OLD = ("*This page is written for anyone, with no technical background assumed. "
       "It describes how this is meant to work. It is still being built — today "
       "only the reading part of it exists — and it is written down first so that "
       "what gets built has something to be held to. The reasoning behind it is in "
       "[[ADR-0010-where-workspaces-live|ADR-0010]].*")

NEW = ("*This page is written for anyone, with no technical background assumed.*\r\n"
       "\r\n"
       "> **Not built yet.** What follows describes how this is meant to work. "
       "Today only the reading part of it exists. It is written down first so that "
       "what gets built has something to be held to — the reasoning is in "
       "[[ADR-0010-where-workspaces-live|ADR-0010]].")

if s.count(OLD) != 1:
    print('FAIL: %d matches' % s.count(OLD))
    sys.exit(1)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(s.replace(OLD, NEW))
print('ok %s' % path)
