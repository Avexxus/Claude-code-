#!/usr/bin/env python3
"""Count repeated words and phrases in a story draft (story text only, stops at <!-- NOTES --> or <!-- LEDGER -->).
Usage: python3 scripts/wordcheck.py FILE [FILE...]
Prints: words, top content words, tic words and phrases with counts per 1,000 words, and repeated 3–5-word phrases."""
import re, sys, collections
STOP=set("""a an the and or but if of to in on at by for with from as is was were be been being it its it's he she they them his her their him i you we us our me my your this that these those there here then than so not no do did does done had has have having would could should will can just up out down off over into onto about what which who whom when where why how all any some one two three like said""".split())
TICS=["didn't","nobody","nothing","a long time","a long while","for a while","the way you'd","the way","as if","something","somewhere","very slightly","slightly","a little","almost","never once","the oval with nothing in it","he didn't look","didn't look","for a moment","then","just","only","still"]
def story(path):
    t=open(path,encoding="utf-8").read()
    for m in ("<!-- NOTES -->","<!-- LEDGER -->"):
        if m in t: t=t.split(m)[0]
    return t
for path in sys.argv[1:]:
    t=story(path); low=t.lower()
    words=re.findall(r"[a-z']+",low); n=len(words) or 1
    print(f"== {path}: {n} words")
    c=collections.Counter(w for w in words if w not in STOP and len(w)>3)
    print("top content words:", ", ".join(f"{w} {k}" for w,k in c.most_common(25)))
    print("tics (count, per 1k):")
    for tic in TICS:
        k=len(re.findall(r"\b"+re.escape(tic)+r"\b",low))
        if k: print(f"  {tic!r}: {k} ({k*1000/n:.1f})")
    for size in (5,4,3):
        grams=collections.Counter(" ".join(words[i:i+size]) for i in range(n-size+1))
        rep=[(g,k) for g,k in grams.items() if k>=3 and not all(x in STOP for x in g.split())]
        rep.sort(key=lambda x:-x[1])
        if rep: print(f"repeated {size}-word phrases:", "; ".join(f"{g} ×{k}" for g,k in rep[:15]))
    starts=collections.Counter(" ".join(s.split()[:2]).lower() for s in re.split(r"(?<=[.!?])\s+",t) if s.split())
    print("most common sentence openings:", ", ".join(f"{g!r} {k}" for g,k in starts.most_common(10)))
