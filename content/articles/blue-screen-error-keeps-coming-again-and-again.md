---
title: "Blue screen error keeps coming again and again"
cat: windows
icon: "🪟"
image: "assets/uploads/topics/broken-phone.jpg"
date: "Jul 22, 2026"
mins: 2
excerpt: "Suddenly the whole screen turns blue with white text and the PC restarts. This is the famous 'Blue Screen of Death' (BSOD)."
---
Suddenly the whole screen turns blue with white text and the PC restarts. This is the famous "Blue Screen of Death" (BSOD). It means Windows hit a serious error it could not survive — usually a bad driver, faulty RAM, a dying hard drive, or overheating. One blue screen is a warning; repeated blue screens mean something hardware-related is failing and needs attention.

## How to fix it

1. Note the error name on the blue screen (like MEMORY_MANAGEMENT).
2. Search that name on Google to find the cause.
3. Update Windows and your drivers, especially the graphics driver.
4. Check the hard drive health: open Command Prompt as admin, type chkdsk /f /r and press Enter.
5. Remove any new RAM or hardware you added recently — it may be faulty.

((ad))

## Work the problem properly
- Write down the stop code (like CRITICAL_PROCESS_DIED) and any file name shown on the blue screen. That name is the biggest clue.
- Did it start after a new program, driver or update? Undo that change first - most repeat blue screens start with something recent.
- Update graphics, audio and storage drivers from the makers' websites.
- Run the Windows Memory Diagnostic (search 'memory diagnostic'). Bad RAM is a classic repeat-blue-screen cause.
- Boot into Safe Mode. If the PC is stable there, the problem is software, not hardware - remove recent things one by one.
- Run a disk check on C: (right-click the drive > Properties > Tools > Check) to rule out drive errors.

Keep a small log of when blue screens happen - the app open, the time, what was plugged in. After three or four entries, a pattern almost always appears, and the pattern points at the guilty component faster than any diagnostic tool.

The stop code on the blue screen names the failing part of the system. Match yours to the row below and fix that component only.

## Read the stop code first

| Stop code on screen | Usual culprit | Typical fix |
| MEMORY_MANAGEMENT | Faulty RAM or a bad driver | Run Windows Memory Diagnostic overnight |
| DPC_WATCHDOG_VIOLATION | Storage driver conflict | Update SSD firmware and chipset drivers |
| KERNEL_POWER | Power supply or overheating | Clean the dust, check the PSU, monitor temps |
| DRIVER_IRQL_NOT_LESS_OR_EQUAL | A specific driver, often network or audio | Note the .sys file name, update that driver |
