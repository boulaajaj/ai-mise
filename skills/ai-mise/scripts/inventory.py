#!/usr/bin/env python3
"""Deterministic source inventory for AI-Mise (Acquire step).

Walks a source folder, hashes every regular file (SHA-256), and emits a
manifest JSON plus a human-readable summary. Read-only by construction:
opens files only for reading and writes only to the --out path.

Usage:
    inventory.py --sources <folder> --out <manifest.json>
"""
import argparse
import hashlib
import json
import mimetypes
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    root = args.sources.resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2
    if args.out.resolve().is_relative_to(root):
        print("refusing to write manifest inside the source folder (read-only mandate)", file=sys.stderr)
        return 2

    entries, skipped = [], []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if p.is_symlink():
            skipped.append({"path": rel, "reason": "symlink"})
            continue
        if not p.is_file():
            continue
        try:
            stat = p.stat()
            entries.append({
                "path": rel,
                "sha256": sha256_file(p),
                "bytes": stat.st_size,
                "mtime_utc": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(timespec="seconds"),
                "mimetype": mimetypes.guess_type(p.name)[0] or "application/octet-stream",
            })
        except OSError as e:
            skipped.append({"path": rel, "reason": str(e)})

    manifest = {
        "manifest_version": 1,
        "generated_at": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
        "source_root": str(root),
        "file_count": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "files": entries,
        "skipped": skipped,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"inventoried {len(entries)} files "
          f"({manifest['total_bytes']:,} bytes), skipped {len(skipped)} -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
