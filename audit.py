# -*- coding: utf-8 -*-
# AUDIT (read-only) — content ko modify NAHI karta, sirf report deta hai
# Chalane ka tareeqa: python3 audit.py
import re, glob, os

RISKY = re.compile(r"\b(factory\s?reset|hard\s?reset|wipe|erase all|diskpart|format(?:ting|ted)? (?:the|this|your)|network reset|clear data|uninstall)\b", re.I)
UNSUPPORTED = [r"\bstudies show\b", r"\bresearch (?:shows|proves)\b", r"\bguaranteed\b", r"\balways works\b", r"\b100% safe\b"]

issues = {"risky_no_warning": [], "unsupported": [], "thin": [], "truncated": [], "placeholders": []}
for fn in sorted(glob.glob("content/articles/*.md")):
    aid = fn.split("/")[-1][:-3]
    s = open(fn, encoding="utf-8").read()
    body = s.partition("---\n")[2]
    clean = "\n".join(l for l in body.splitlines() if not l.startswith("> **"))
    if RISKY.search(clean) and not re.search(r"^> \*\*", body, re.M):
        issues["risky_no_warning"].append(aid)
    for pat in UNSUPPORTED:
        if re.search(pat, clean, re.I):
            issues["unsupported"].append((aid, pat))
    if len(clean.split()) < 100:
        issues["thin"].append((aid, len(clean.split())))
    for ln in body.splitlines():
        st = ln.strip().rstrip("*").rstrip(")").rstrip("*")
        if re.match(r"^\d+\. ", st) and not st.rstrip().endswith((".", "!", "?", ":", '"')):
            issues["truncated"].append(aid); break
    if re.search(r"\[(?:add|insert|paste|TODO)", body, re.I):
        issues["placeholders"].append(aid)

print("=== READ-ONLY AUDIT ===")
for k, v in issues.items():
    print(f"{k}: {len(v)}", v[:6] if v else "")
if not any(issues.values()):
    print("SAB CLEAN ✓")
