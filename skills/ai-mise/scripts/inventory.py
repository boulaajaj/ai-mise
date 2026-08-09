#!/usr/bin/env python3
"""Deterministic source inventory for AI-Mise (Acquire step).

Walks a source folder, hashes every regular file (SHA-256), and emits a
manifest JSON plus a human-readable summary. Read-only by construction:
opens files only for reading and writes only to the --out path.

Three properties the manifest is meant to have:

Reproducible. Two runs over an unchanged tree produce the same
`content_digest`; everything that depends on when the run happened lives
in `run`, outside the digest. `mtime_utc` is recorded but left out of the
digest, because a file whose bytes are identical is the same material
whenever it was last touched.

Path-clean. Nothing records where the folder sits on this disk, only what
it is called. Provenance has to say where material came from; it does not
have to say who the person is or how their disk is laid out. Error text
is reduced to the reason, since the OS puts full paths in its messages.

Read-consistent. Each file is opened once and hashed and stated through
that one descriptor, so `sha256`, `bytes` and `mtime_utc` describe one
state of one file rather than three glimpses of a path. Where the file
moves under the read it is re-read, and where it keeps moving it is
skipped rather than recorded wrongly. On platforms with O_NOFOLLOW the
final component is never followed; elsewhere a swap between walking and
opening is still possible, so what is recorded is what was opened.

Usage:
    inventory.py --sources <folder> --out <manifest.json>
"""
import argparse
import hashlib
import json
import os
import stat as statmod
import sys
from datetime import datetime, timezone
from pathlib import Path

CHUNK = 1 << 20
REREAD_LIMIT = 3
MANIFEST_VERSION = 2


class Rejected(Exception):
    """Recorded in `skipped` with this reason. Never carries a path."""


def open_no_follow(path: Path):
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    return os.fdopen(os.open(path, flags), "rb")


def volatile(st) -> tuple:
    return (st.st_size, st.st_mtime_ns)


def hash_handle(f):
    """Hash and stat one descriptor. Raises Rejected if it moves mid-read."""
    before = os.fstat(f.fileno())
    if not statmod.S_ISREG(before.st_mode):
        raise Rejected("not a regular file when opened")
    h = hashlib.sha256()
    while True:
        b = f.read(CHUNK)
        if not b:
            break
        h.update(b)
    after = os.fstat(f.fileno())
    if volatile(before) != volatile(after):
        raise Rejected("changed while being read")
    return h.hexdigest(), after


def entry_for(path: Path, rel: str) -> dict:
    last = None
    for _ in range(REREAD_LIMIT):
        try:
            with open_no_follow(path) as f:
                digest, st = hash_handle(f)
        except Rejected as e:
            last = e
            continue
        return {
            "path": rel,
            "sha256": digest,
            "bytes": st.st_size,
            "mtime_utc": datetime.fromtimestamp(
                st.st_mtime, tz=timezone.utc).isoformat(timespec="seconds"),
        }
    raise last


def digest_body(entries: list, skipped: list, label: str) -> dict:
    """Exactly what content_digest is taken over. Note: no mtime, no run."""
    return {
        "manifest_version": MANIFEST_VERSION,
        "source_label": label,
        "file_count": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "files": [{k: e[k] for k in ("path", "sha256", "bytes")} for e in entries],
        "skipped": skipped,
    }


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
        print("refusing to write manifest inside the source folder "
              "(read-only mandate)", file=sys.stderr)
        return 2

    entries, skipped = [], []
    for p in root.rglob("*"):
        rel = p.relative_to(root).as_posix()
        if p.is_symlink():
            skipped.append({"path": rel, "reason": "symlink"})
            continue
        if not p.is_file():
            continue
        try:
            entries.append(entry_for(p, rel))
        except Rejected as e:
            skipped.append({"path": rel, "reason": str(e)})
        except OSError as e:
            skipped.append({"path": rel, "reason": e.strerror or "unreadable"})
    entries.sort(key=lambda e: e["path"])
    skipped.sort(key=lambda e: e["path"])

    body = digest_body(entries, skipped, root.name or "root")
    digest = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False).encode("utf-8")).hexdigest()

    manifest = dict(body)
    manifest["files"] = entries
    manifest["content_digest"] = f"sha256:{digest}"
    manifest["run"] = {
        "generated_at": datetime.now(tz=timezone.utc).isoformat(
            timespec="seconds"),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"inventoried {len(entries)} files "
          f"({manifest['total_bytes']:,} bytes), skipped {len(skipped)} "
          f"-> {args.out}")
    print(f"content digest {manifest['content_digest']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
