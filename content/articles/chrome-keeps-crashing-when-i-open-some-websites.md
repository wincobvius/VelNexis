---
title: "Chrome keeps crashing when I open some websites"
cat: browser
icon: "🧭"
image: "assets/uploads/topics/laptop-error.jpg"
date: "Aug 11, 2026"
mins: 2
excerpt: "Chrome dies on certain sites only — 'Aw, Snap!' again and again. That pattern points to graphics settings, an extension, or an old driver."
---

Some websites crash Chrome completely — the tab shows "Aw, Snap!" or the whole browser closes — while other sites work fine. That pattern is the clue: those sites run heavy graphics or scripts, and something in your setup chokes on exactly that. Graphics settings, an extension, or an old driver — in that order of likelihood.

## Work down this list

1. **Update Chrome first** (Settings → About Chrome). Crash fixes ship constantly; testing an old build wastes time.
2. **Turn off hardware acceleration:** Settings → System → "Use graphics acceleration when available" → off → relaunch. This makes Chrome render sites in software instead of handing them to the graphics driver — and it settles the majority of these crashes.
3. **Test the site in an incognito window.** Incognito disables extensions. If the site works there, an extension is the problem — re-enable them one by one to find which.
4. **Update the graphics driver** from your PC maker's site (laptop) or graphics-card maker's site (desktop), not just Windows Update.
5. **Clear that site's data only:** padlock icon → Site settings → Delete data. This signs you out of that one site but keeps everything else intact.

## Still crashing?

Create a new Chrome profile (profile icon → Add) and test the site there. If it works, your old profile is corrupted — bookmarks and passwords can be exported over, then the old profile reset.

((ad))

## Quick recap
- Test a new browser profile - if crashes stop, your profile or extensions are the cause.
- Disable hardware acceleration in Settings > System and retest.
- One specific site crashing only there means the site, not Chrome.
- Run a Defender scan - adware causes a large share of random browser crashes.
