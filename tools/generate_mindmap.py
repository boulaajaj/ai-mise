#!/usr/bin/env python3
"""Generate the repo mind map as committed Mermaid (ADR-0006).

Scans all tracked .md files, extracts [[wikilinks]], relative markdown links,
and backtick path references (`docs/architecture.md`) between them, and emits
docs/mindmap.md containing a Mermaid graph. The output is GENERATED — never
hand-edit; regenerate with:

    python tools/generate_mindmap.py

Deterministic output (sorted nodes/edges) so regeneration diffs cleanly.
Stdlib only. Vendor-death note: Mermaid is only the renderer; the graph's
source of truth is the links inside the markdown files themselves.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "mindmap.md"
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
MDLINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
BACKTICK = re.compile(r"`([A-Za-z0-9_.\\/-]+\.md)`")


def node_id(rel: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", rel)


def label(rel: str) -> str:
    p = Path(rel)
    return p.stem if p.stem.lower() != "readme" else (p.parent.name or "repo") + "/README"


def main() -> int:
    md_files = {}
    for p in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel == OUT.relative_to(ROOT).as_posix():
            continue
        md_files[rel] = p

    by_stem = {}
    for rel in md_files:
        by_stem.setdefault(Path(rel).stem.lower(), rel)

    edges = set()
    for rel, p in md_files.items():
        text = p.read_text(encoding="utf-8", errors="replace")
        targets = set()
        for m in WIKILINK.finditer(text):
            t = by_stem.get(m.group(1).strip().lower())
            if t:
                targets.add(t)
        for m in BACKTICK.finditer(text):
            cand = m.group(1).replace("\\", "/")
            if cand in md_files:
                targets.add(cand)
            else:
                t2 = by_stem.get(Path(cand).stem.lower())
                if t2:
                    targets.add(t2)
        for m in MDLINK.finditer(text):
            cand = (p.parent / m.group(1)).resolve()
            try:
                t = cand.relative_to(ROOT).as_posix()
            except ValueError:
                continue
            if t in md_files:
                targets.add(t)
        for t in sorted(targets):
            if t != rel:
                edges.add((rel, t))

    groups = {}
    for rel in md_files:
        top = rel.split("/")[0] if "/" in rel else "root"
        groups.setdefault(top, []).append(rel)

    lines = [
        "# Repository mind map (generated)",
        "",
        "<!-- GENERATED FILE - do not edit. Regenerate: python tools/generate_mindmap.py (ADR-0006) -->",
        "",
        f"Nodes: {len(md_files)} markdown files · Edges: {len(edges)} links · The link graph inside the files is the source of truth; this is only a rendered view.",
        "",
        "```mermaid",
        "graph LR",
    ]
    for top in sorted(groups):
        if top == "root":
            for rel in sorted(groups[top]):
                lines.append(f'  {node_id(rel)}["{label(rel)}"]')
        else:
            lines.append(f"  subgraph {node_id(top)}_g[{top}]")
            for rel in sorted(groups[top]):
                lines.append(f'    {node_id(rel)}["{label(rel)}"]')
            lines.append("  end")
    for a, b in sorted(edges):
        lines.append(f"  {node_id(a)} --> {node_id(b)}")
    lines += ["```", ""]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"mindmap: {len(md_files)} nodes, {len(edges)} edges -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
