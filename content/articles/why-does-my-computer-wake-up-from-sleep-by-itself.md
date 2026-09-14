---
title: "Why does my computer wake up from sleep by itself"
cat: windows
icon: "🪟"
image: "assets/uploads/cats/windows.jpg"
date: "Jul 25, 2026"
mins: 2
excerpt: "You put the PC to sleep and leave, but later you find it awake — fans running, lights on — with nobody touching it."
---
You put the PC to sleep and leave, but later you find it awake — fans running, lights on — with nobody touching it. Some PCs even wake minutes after sleeping. The causes: the mouse or keyboard sending a signal, the network card waking it (Wake-on-LAN), scheduled updates and antivirus scans set for the night, or a USB device glitching. Windows can tell you exactly what woke it.

## How to fix it

1. Open Command Prompt as admin, type powercfg /lastwake and press Enter. It shows what woke the PC.
2. Device Manager → Network adapter → right click → Properties → Power Management → untick "Allow this device to wake the computer".
3. Check scheduled tasks in the night (updates, antivirus scans).
4. Move the mouse away from your hand's resting place — a moving mouse wakes it.
5. Turn off "Wake timers": Control Panel → Power Options → advanced settings → Sleep.

((ad))

## Find what wakes it
- Run powercfg /lastwake in Command Prompt - it names the last device that woke the PC.
- powercfg /devicequery wake_armed lists everything allowed to wake it. In Device Manager, open each one's Power Management tab and uncheck 'Allow this device to wake'.
- Mice are the usual offender - tiny vibrations wake sensitive mice. Uncheck the mouse first.
- Wake timers from Windows Update: Power Options > advanced > Sleep > Allow wake timers > Disable.
- Scheduled tasks like backups also wake PCs - check Task Scheduler for 'Wake the computer' boxes.
- Fast Startup confuses sleep on some PCs - toggle it off in Power Options.
- Waking at the same minute every night is always a scheduled task - the commands above say which.
