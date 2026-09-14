# 📋 Editor Manifest — Master Prompt Rewrite Pass
**Checkpoint file (public content se bahar)** · Date: Sep 2026

## Inventory (mutually exclusive, reconcile = 330)

| Category | Count | Slugs |
|---|---:|---|
| 1. Full editorial rewrite (21 priority + 2 claim fixes) | 23 | `editor-manifest-data.json` → "rewrite" |
| 2. Steps-repaired only (PDF line-wrap se recover) | 164 | → "repair_only" |
| 3. Warning re-fit only | 8 | → "warn_only" |
| 4. Repair + warning dono | 10 | → "repair_and_warn" |
| 5. Untouched (automated checks pass; full manual pass pending) | 125 | → "untouched" |
| **Total** | **330** | ✓ reconcile |

## Status definitions
- **rewrite** = poori article naye sire se likhi gayi (structure type ke mutabiq: troubleshooting / privacy explainer / scam-response / buying guide / career advice). Excerpt + reading time update. Date/slug/URL preserve.
- **repair** = sirf truncated steps PDF ke asal text se restore hue (language unchanged). Parser bug tha (`steps.append` + rebinding) — ab fixed.
- **warning re-fit** = generic "back up everything" box hata kar action-specific warnings (13 destructive / 8 moderate / 2 custom / 22 removed as misfit).
- **untouched** = automated checks pass (koi artifact/truncation/placeholder nahi) lekin **full manual language pass abhi nahi hui** — yeh agla kaam hai.

## Verification flags (alag from editorial status)
Yeh claims online/current-source verify karne hain (browse access available tha kuch ke liye, baqi owner ya live check):
1. WhatsApp/Meta AI — current privacy policy wording (articles mein "check current policy" hedging laga di gayi hai)
2. OpenAI data controls — exact retention timeline (hedged in article)
3. Google One — PKR/local pricing (article mein "check current price" note)
4. Gmail storage-bar update timing (~1 din) — owner account se confirm

## Owner materials (rule 6 — sirf owner de sakta hai)
- Real screenshots (settings screens, error messages)
- "Tested on [device]" notes
- Current local prices

## Checkpoint / Next action
- **Remaining full language pass:** 307 articles (categories 2-5)
- **Next batch (15):** warn_only (8) + repair_and_warn (10) + sab se zyada-traffic PDF topics
- Resume yahin se: `editor-manifest-data.json` → categories 2-5 ki list
- Script: `audit.py` (read-only) — naye articles ke liye chalayen

## Files changed (is pass mein)
- `content/articles/*.md` — 205 articles touched (23+164+8+10)
- `build.py` — ordered-list + link fixes (pehle se)
- Build regenerate: 330 article HTML pages

## Scanner limitations (jaan-boojh kar — §11 ke mutabiq)
1. `audit.py` ka "guaranteed" flag (2 hits) = **attributed scam quotes** hain jo debunk ho rahi hain (courses + trading bots) — remove nahi karna (master prompt rule).
2. `audit.py` ka "risky_no_warning" top-level-box heuristic hai — 7 high-risk articles mein warning **step-level inline** hai ("back up data and factory reset"), jo better hai. Sab 7 verify kiye gaye.
3. "Thin" threshold 100 words sirf signal hai — publish-quality threshold nahi (master prompt rule).

## Before/After samples (report ke liye)
- **factory-reset-tv:** "One of these five routes always works." → "The available reset method depends on your TV's brand and model."
- **ai-job-rumor:** "A study saying '40% of work tasks can be automated'…" → "a claim like '40% of work tasks could be automated' sounds like '40% of people will lose their jobs' by the time it reaches a headline. Those are completely different statements." (clearly hypothetical)
- **chatgpt-data:** "Deleted chats are removed from training after you turn the setting off." → "Do not assume it reaches back and removes earlier data from an already-trained model — that is not how model training works."

---
## CONTINUATION LOG — Batch 3 (Sep 2026)

### Naya bug pakra aur fix hua: Duplicated Frontmatter (41 files)
Pehli audit ke P1 autofix mein `partition("---\n")` bug tha — 41 files mein frontmatter body mein duplicate ho gaya tha aur **article text ke upar "title: ... cat: ..." leak ho raha tha** (HTML mein visible). Sab 41 files dedupe kar ke rebuild — ab HTML leak **0**. Yeh master prompt §11 ka wahi point tha jo pehli report mein miss hua tha — honest correction.

### Batch 3 complete: 18 articles (warn/repair queue)
- **14 full rewrites** (USB ×3, TV ×2, camera ×2, browser ×2, password, boot-loop, Wi-Fi, apps-crash, pendrive)
- **4 already-good** (hand-written: app-keeps-crashing, play-store-not-downloading, wifi-disconnects, when-to-upgrade-phone) — dedup + warning fit only
- Galat warnings replace: USB articles pe "factory reset" nonsense hata kar action-specific (format erases drive / chkdsk / diskpart select-disk caution)
- Baqi bacha: **289 articles** (164 repair-pending + 125 untouched)

### Updated categories (reconcile = 330 ✓)
| Category | Count |
|---|---:|
| Full rewrite done | **41** |
| Steps-repaired, language pass pending | 164 |
| Untouched, checks pass | 125 |

---
## GROUP PLAN (user-approved: 4 groups, thora thora karke)
`editor-groups.json` — Group 1: security/payments/earning/cloud/recovery (84) · Group 2: PC (65) · Group 3: mobile/comms (85) · Group 4: entertainment/rest (55) = 289 remaining

### G1 Sub-batch 1 DONE: 16 security articles (full rewrites)
- Intro-less articles (6) ko intros mil gaye; sab structure-type-C (protective action pehle)
- Sensitive topics careful: blackmail article (non-judgmental, StopNCII.org, FIA 1991), OTP scam, prize calls, ransomware (No More Ransom)
- hackers-accounts: already good — skipped intentionally
- **G1 progress: 16/84** (next: payments 18, phir earning 18, cloud 18, recovery 13)
- audit.py detector false-positive fix (trailing ** / ) endings)

---
## FINAL LOG — CONTINUOUS MODE COMPLETE (Sep 2026)

User instruction: ek hi baar mein, continuous, tamam groups. Protocol: 5-article batches, good-passages preserved, no padding.

### Triage result (pehle): 273 remaining → 140 clean + 133 flagged
### Is run mein: 126 full rewrites (Group 1 payments 18 + security ke baad sab groups ke flagged)
### 7 flagged lekin already-good (punchy short intros, reviewed-accepted): battery-drain, overnight-charging, router-mistakes, wifi-slow-night, hackers-accounts, ai-job-rumor (+incognito-truth earlier)

### FINAL STATE (reconcile = 330 ✓)
| Editorial status | Count |
|---|---:|
| Full editorial rewrite/repair complete | **184** |
| Reviewed — good as-is, no change needed | **146** |
| Remaining / blocked | **0** |

### Checks (sab sach mein chale): build ✓ · broken links 0 ✓ · dup-FM leak 0 ✓ · truncated steps 0 ✓ · PDF artifacts 0 ✓ · JS syntax ✓ · render samples ✓ · 35-word intro threshold ki 21 "fails" manually review ki — sab ke sab achhe punchy intros hain (master prompt: "a few direct sentences are enough") — accepted.

### Factual checks jo owner/live-stage par karne hain (honest list)
1. Facebook monetization numbers (5k followers / 60k minutes) — Dashboard live values check karein (article mein "check Dashboard" hedging hai)
2. PayPal/Payoneer/Wise availability + fees — Pakistan context, publish se pehle ek baar current rates
3. Meta AI / OpenAI data policies — live hone ke baad official pages se wording confirm
4. StopNCII participating platforms list
