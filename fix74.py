import io, sys

path = '.github/instructions/docs.instructions.md'
with io.open(path, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

OLD = ("- Verify claim labels ([verified] / [prior art] / [default]) on factual assertions\r\n"
       "  about platform behavior, research findings, or third-party projects (ADR-0004).\r\n"
       "  The plain-language exemption in `.github/copilot-instructions.md` §2 applies here in\r\n"
       "  full. It is defined there once and deliberately not restated here, because a rule\r\n"
       "  written in two places is a rule that will eventually disagree with itself.")

NEW = ("- Verify claim labels on factual assertions about platform behavior, research\r\n"
       "  findings, or third-party projects (ADR-0004). Two things this file deliberately\r\n"
       "  does not reproduce, because both apply here in full and a rule written in two\r\n"
       "  places is a rule that will eventually disagree with itself: the label vocabulary\r\n"
       "  and its exact written form, defined in `docs/architecture.md` §1, and the\r\n"
       "  plain-language exemption, defined in `.github/copilot-instructions.md` §2.")

if s.count(OLD) != 1:
    print('FAIL: %d matches' % s.count(OLD))
    sys.exit(1)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(s.replace(OLD, NEW))
print('ok %s' % path)
