---
title: "Windows update fails every time, what should I do"
cat: windows
icon: "🪟"
image: "assets/uploads/topics/compare-phones.jpg"
date: "Jul 27, 2026"
mins: 2
excerpt: "Every time you try to update Windows, it downloads, installs to some percent, says 'failure, undoing changes', and rolls back."
---
Every time you try to update Windows, it downloads, installs to some percent, says "failure, undoing changes", and rolls back. This cycle can repeat for weeks. Causes: not enough free space on C drive, damaged update files stuck in the update folder, a conflicting program, or a patch that does not agree with your hardware. Windows has a repair path for each cause.

## How to fix it

1. Restart the PC and try the update again once.
2. Free up space. Updates need at least 20 GB free on C drive.
3. Run the Windows Update Troubleshooter: Settings → System → Troubleshoot → Other troubleshooters → Windows Update.
4. Reset update files: search "cmd", run as admin, type these one by one: net stop wuauserv, net stop bits, then open C:\Windows\SoftwareDistribution and delete its contents, then type net start wuauserv and net start bits.
5. Restart and update again. If it still fails, use the "Windows Update Assistant" from Microsoft's site.

((ad))

## Fix the failing update
- Restart and run it again - one retry fixes most.
- Settings > Troubleshoot > Windows Update - the official repair for corrupt update queues.
- The classic deep fix: stop the update services, rename the SoftwareDistribution folder, restart - Windows rebuilds its download cleanly.
- Free space: under 10GB on C: breaks updates.
- Unplug USB devices during the install - their drivers hang it.
- Note the error code: it points at the exact fix, and Microsoft's site lists each one.
- DISM then sfc /scannow repair the broken system files that break updates.
- Still stuck? Download that specific update from Microsoft's Update Catalog by its KB number and install it by hand.

Write down the error code - it looks like 0x80070002. That exact code maps to a specific fix on Microsoft's own support pages, and searching it beats guessing through ten generic solutions.
