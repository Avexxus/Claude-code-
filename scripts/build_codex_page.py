#!/usr/bin/env python3
"""Rebuild the Codex v5 artifact page from the markdown files in codex_v5/.

Usage:  python3 scripts/build_codex_page.py [output.html]
Default output: build/codex_v5.html

The repo copy of the codex is the master. After any change to codex_v5/,
run this and republish the output to the Codex v5 artifact
(https://claude.ai/artifact/DejDv6wZUCqZGEpZDonS4W) so the page Patrick
reads on claude.ai matches the repo.

File order, labels and groups come from scripts/codex_manifest.json.
A new codex file that isn't in the manifest is added at the end of its
group (guessed from the filename) and reported, so the manifest can be
updated by hand.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CODEX = ROOT / "codex_v5"
TEMPLATE = ROOT / "scripts" / "codex_page_template.html"
MANIFEST = ROOT / "scripts" / "codex_manifest.json"


def words(text):
    return len(re.findall(r"\S+", text))


def main():
    out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "build" / "codex_v5.html"
    manifest = json.loads(MANIFEST.read_text())
    known = {m["name"] for m in manifest}
    entries = []
    # Pending rulings go first: they override the codex files until a pass writes them in.
    bank = ROOT / "decisions" / "BANK.md"
    if bank.exists():
        text = ("> **READ THIS FIRST.** These are Patrick's rulings since 31 October 2026. "
                "They have NOT yet been written into the files below, and where they disagree, "
                "**these rulings win.** The codex files are older.\n\n" + bank.read_text())
        entries.append({"id": "pending-rulings", "name": "BANK.md",
                        "label": "⚠ Rulings since Oct 31 (override)",
                        "group": "Read first", "words": words(text), "text": text})
    for m in manifest:
        path = CODEX / m["name"]
        if not path.exists():
            print(f"missing from codex_v5/, skipped: {m['name']}")
            continue
        text = path.read_text()
        entries.append({**m, "words": words(text), "text": text})
    for path in sorted(CODEX.glob("*.md")):
        if path.name in known:
            continue
        group = "Trackers (open, not settled)" if path.name.isupper() else "Codex v5"
        text = path.read_text()
        stem = path.stem
        entries.append({"id": stem.lower().replace("_", "-"), "name": path.name,
                        "label": stem.replace("_", " ").title(), "group": group,
                        "words": words(text), "text": text})
        print(f"new file added (update the manifest): {path.name}")
    data = json.dumps(entries, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text().replace("__ARCHIVE_JSON__", data, 1)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    total = sum(e["words"] for e in entries)
    print(f"wrote {out} — {len(entries)} files, {total:,} words, {len(html):,} bytes")


if __name__ == "__main__":
    main()
