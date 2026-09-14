---
title: "After the Windows update my software stopped working"
cat: software
icon: "🧩"
image: "assets/uploads/topics/laptop-error.jpg"
date: "Aug 2, 2026"
mins: "3"
excerpt: "Windows updated itself last night, and this morning a program you use daily is broken — will not open, crashes, or acts strange."
---

Windows updated itself last night, and this morning a program you use daily is broken — will not open, crashes, or acts strange. This happens because big Windows updates change system parts that older programs depend on. Microsoft provides compatibility tools for this exact collision, and the program's maker usually ships a fix within days.

## The recovery ladder

1. **Update the program first:** open the program's own "Check for updates" (Help/About menu), or download the newest version from the maker's site. Makers patch update-breakage fast — a version from this week often already contains the fix.
2. **Compatibility mode:** right-click the program's shortcut → Properties → Compatibility tab → "Run this program in compatibility mode for" → the Windows version the program was happy on. Also tick "Run as administrator" if it previously needed it. This one dialog rescues a large share of broken-after-update programs.
3. **The one-click rollback, if the program matters more than the update:** Settings → Windows Update → Update history → Uninstall updates → the most recent quality update. This rolls back the Windows patch (not your files) — the decisive fix when the timing is proven and nothing else works. Windows will try to re-install it later; use "pause updates" for a week while waiting for the program's fix.
4. **Repair install:** many programs ship a "Repair" option — Settings → Apps → the program → Modify → Repair. Rebuilds the program's files without touching your settings or data.

## The pattern to notice

- **One program broken** → this ladder, in order.
- **Several older programs broken** → same ladder, starting with compatibility mode for each.
- **The WHOLE PC sluggish after update** → that is a different problem (see our Windows-slow-after-update guide) — post-update background housekeeping, not breakage.

## The prevention that works

Before major Windows version updates (the once-a-year "feature updates"), check business-critical software makers' sites for "works with version X" notes. Home users rarely need this discipline; a business running specialist software absolutely does.

((ad))
