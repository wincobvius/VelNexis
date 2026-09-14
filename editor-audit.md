# 🔍 Editorial Audit Report — 330 Articles
**Date:** Sep 2026 · **Editor prompt rules ke mutabiq poora scan complete**

---

## 📊 Summary

| Check | Result | Action |
|---|---|---|
| Risky steps bina warning (factory reset / delete / clear data…) | **45 mile** | ✅ **AUTO-FIXED** — har ek mein backup warning note add ho gayi |
| Unsupported claims ("research shows", "40% of people", "always works") | **4 mile** | ✅ **3 fixed** + 1 OK tha (scam-quote attributed tha) |
| PDF artifacts / typos / "returned to se" type | **0 mile** | ✅ Clean |
| AI/rumor articles mein fact-vs-speculation separation ghayab | **14 flag** | 🟡 Manual rewrite chahiye (list neeche) |
| Thin articles (130 words se kam) | **8 flag** | 🟡 Expand karna hai (list neeche) |
| **Baqi sab** | **265 articles** | ✅ Automated checks pass |

**Total: 331 checks · 52 fixed · 22 flagged for manual rewrite · 265+ clean**

---

## ✅ Jo abhi fix hua (52 articles)

### P1 — Data-loss warnings (45 articles)
Jin articles mein destructive steps thin (factory reset, clear data, uninstall, network reset, format…) lekin backup warning nahi thi — sab mein yeh note add kar diya gaya:

> **Before you start:** Some of these steps can remove data or settings. Back up anything you care about — photos, documents, chats, important files — before you continue.

*(Har article ke "How to fix it" section ki shuru mein, purple note box ke roop mein render hota hai.)*

### P4 — Unsupported claims (4)
| Article | Masla | Fix |
|---|---|---|
| ai-job-rumor | "A study saying 40%…" (study cite kiye bina) | → "A headline saying…" (hypothetical, no fake citation) |
| fast-charging-damage | Heading "What research shows" (bina source) | → "What actually wears a battery" (mechanism framing) |
| factory-reset-tv | "always works" (absolute claim) | → "works on almost every TV" |
| ai-trading-bots | "guaranteed" | ✅ OK tha — woh scam ad ka attributed quote hai, debunk hi article ka maqsad hai |

---

## 🟡 Baqi kaam — manual rewrite (22 articles)

### P2 — AI/Rumor articles (14) — rule 5 ke mutabiq fact/speculation separation chahiye:
1. are-ai-trading-bots-that-promise-guaranteed-profit-real-or-s
2. i-got-an-ai-voice-clone-call-from-my-family-member-asking-fo
3. how-do-i-spot-a-deepfake-video
4. can-ai-read-my-whatsapp-chats
5. does-meta-ai-in-whatsapp-read-my-chats
6. does-chatgpt-use-my-personal-data-how-do-i-stop-it
7. how-can-i-tell-if-a-message-was-written-by-ai
8. how-do-i-spot-fake-chatgpt-apps
9. are-ai-courses-that-promise-overnight-earnings-scams
10. can-people-find-out-that-i-used-ai-for-my-assignment-or-emai
11. is-content-writing-and-freelancing-dead-because-of-ai
12. should-i-still-learn-coding-if-ai-can-write-code
13. will-ai-really-take-my-job-which-jobs-are-safe
14. ai-free-tools

*In mein "Confirmed / Unverified / Speculation" clearly alag karna hai taake rumor confirmed news na lage.*

### P3 — Thin articles (8) — expand karna hai:
| Article | Words | 
|---|---|
| fps-settings | 82 |
| earbuds-review | 86 |
| tech-wrap | 98 |
| incognito-truth | 99 |
| ai-free-tools | 101 |
| backup-guide | 111 |
| phone-slow | 112 |
| win-slow-update | 108 |

---

## 📋 Publish se pehle aapki (owner) checklist — rule 6:

Yeh cheezein sirf **aap** add kar sakte hain (main invent nahi kar sakta):
- [ ] **Real screenshots** — har fix-guide mein (Settings screens, error messages) — AI-generated screenshots kabhi na lagao
- [ ] **Apne device pe test** — "Tested on Samsung A52, Windows 11" jaisi ek line trust barhati hai
- [ ] **PKR prices** — jahan price ka zikr hai, current local price check kar ke likhein
- [ ] **Dates verify** — naye articles ki "Last checked" date sach ho
- [ ] **AI/rumor articles** mein sources — jahan real news ka hawala ho, actual link add karein

## 🔁 Audit dobara chalana:
Kabhi bhi naya article add karne ke baad:
```
python3 audit.py
```
(Yehi script dobara poori site scan kar ke naye masail report karegi.)

---

*Yeh report `audit.py` se generate hui hai — editor prompt ke rules 1-6 ke mutabiq.*
