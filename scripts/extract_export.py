#!/usr/bin/env python3
"""Extract Patrick's own lines from a claude.ai data export.

Usage: python3 -I scripts/extract_export.py sources/account_export/conversations.json [outdir]
Writes one markdown file per conversation (only the human's turns, plus the
assistant turn just before each one in a collapsed, clearly-labelled AI block for
context), and an INDEX.md sorted by date. AI text is marked "AI, NOT PATRICK".
"""
import json, sys, os, re

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "sources/account_export/patrick_lines"
os.makedirs(out, exist_ok=True)
data = json.load(open(src, encoding="utf-8"))

def text_of(m):
    t = m.get("text") or ""
    if not t and isinstance(m.get("content"), list):
        t = "\n".join(c.get("text", "") for c in m["content"] if isinstance(c, dict))
    return t.strip()

index = []
for conv in data:
    name = conv.get("name") or "untitled"
    date = (conv.get("created_at") or "")[:10]
    msgs = conv.get("chat_messages") or []
    human = [m for m in msgs if m.get("sender") == "human" and text_of(m)]
    if not human:
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60] or "untitled"
    fn = f"{date}_{slug}_{conv.get('uuid','')[:8]}.md"
    words = 0
    with open(os.path.join(out, fn), "w", encoding="utf-8") as f:
        f.write(f"# {name}\n{date} · {len(human)} Patrick turns\n\n")
        prev_ai = ""
        n = 0
        for m in msgs:
            t = text_of(m)
            if m.get("sender") == "human" and t:
                n += 1
                if prev_ai:
                    f.write(f"<details><summary>AI, NOT PATRICK (context)</summary>\n\n{prev_ai[:600]}…\n</details>\n\n")
                f.write(f"**P{n}** ({(m.get('created_at') or '')[:16]}):\n{t}\n\n")
                words += len(t.split())
            elif t:
                prev_ai = t
    index.append((date, name, fn, len(human), words))

index.sort()
with open(os.path.join(out, "INDEX.md"), "w", encoding="utf-8") as f:
    f.write(f"# Patrick's lines from the claude.ai export: {len(index)} chats, {sum(i[4] for i in index)} words\n\n")
    f.write("| date | chat | turns | words |\n|---|---|---|---|\n")
    for d, n, fn, t, w in index:
        f.write(f"| {d} | [{n}]({fn}) | {t} | {w} |\n")
print(f"{len(index)} chats, {sum(i[4] for i in index)} Patrick words -> {out}")
