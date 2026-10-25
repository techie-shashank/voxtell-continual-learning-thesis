"""List every \\todo{...} in the thesis chapters and write them into thesis_tracker.md.

The list replaces the block between <!-- TODOS:BEGIN --> and <!-- TODOS:END --> in
thesis_tracker.md (section D), grouped by type (defense, cite, ref, check, other).

Usage (from the repository root):
    python scripts/list_todos.py
"""
import re
from collections import defaultdict

from _common import REPO

THESIS = REPO / "thesis"
TRACKER = REPO / "thesis_tracker.md"
BEGIN, END = "<!-- TODOS:BEGIN -->", "<!-- TODOS:END -->"
TODO = re.compile(r"\\todo(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}")


def main():
    groups = defaultdict(list)
    for tex in sorted(THESIS.glob("*.tex")):
        for n, line in enumerate(tex.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("%"):
                continue
            for m in TODO.finditer(line):
                text = " ".join(m.group(1).split())
                kind = text.split(":", 1)[0].strip().lower() if ":" in text else "other"
                if kind not in {"defense", "cite", "ref", "check"}:
                    kind = "other"
                groups[kind].append(f"- `{tex.name}:{n}` {text}")
    lines = []
    for kind in ["defense", "check", "cite", "ref", "other"]:
        if groups[kind]:
            lines.append(f"**{kind}** ({len(groups[kind])})")
            lines.extend(groups[kind])
            lines.append("")
    total = sum(len(v) for v in groups.values())
    block = "\n".join([BEGIN, f"Total: {total}", ""] + lines + [END])
    text = TRACKER.read_text(encoding="utf-8")
    start, end = text.index(BEGIN), text.index(END) + len(END)
    TRACKER.write_text(text[:start] + block + text[end:], encoding="utf-8")
    print(f"{total} todos written to {TRACKER.name}")


if __name__ == "__main__":
    main()
