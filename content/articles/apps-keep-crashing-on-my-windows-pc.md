---
title: "Apps keep crashing on my Windows PC"
cat: windows
icon: "🪟"
image: "assets/uploads/topics/laptop-error.jpg"
date: "Aug 15, 2026"
mins: 3
excerpt: "Programs close by themselves with 'has stopped working' popups — one app, or many apps."
---

Programs close by themselves with "has stopped working" popups — one app, or many apps. Crashes happen when a program's files are damaged, Windows is missing updates, the graphics driver is old, or two programs fight over the same files. If crashes started after a specific event (an update, a new program), that event is the clue.

## The ladder, ordered by hit rate

1. **One app only?** Reinstall it cleanly: Settings → Apps → uninstall, restart, install the latest version from the maker's official site. Damaged program files are the #1 single-app cause, and a fresh install replaces them all.
2. **Many apps crashing?** Windows itself is the suspect — Settings → Windows Update → check and install everything pending (including optional driver updates). A Windows file-check follows: Command Prompt (admin) → `sfc /scannow` — it repairs corrupted system files that multiple programs depend on (see our DLL guide for the full routine).
3. **Graphics driver:** apps that crash during display-heavy moments (scrolling, video, games) point at the GPU driver — update from NVIDIA/AMD/Intel's site directly. A driver updated yesterday that started the crashes: roll back instead (Device Manager → display adapter → driver → roll back).
4. **The event clue:** crashes began right after installing something? That program (or its "optimizer"/cleaner companion) is the prime suspect — uninstall it and see. Antivirus suites are also known crashers of specific apps: temporarily pause real-time protection to test, consciously and briefly.
5. **Reinstall the crashing app's runtime pack:** Microsoft's Visual C++ redistributables power half the software on Windows — crashes across several different apps often fix with one VC++ reinstall.

## Reading the crash itself

The popup's "View details" names a faulting module — the .dll or .exe that failed. That name, searched together with the app's name, usually lands on the maker's own fix page. And Windows' Reliability Monitor (search "Reliability" in Start) charts every crash with its cause — a timeline that instantly shows which event started the pattern.

## When crashes are hardware

Random crashes across everything, worse when the machine is warm, that began after years of silence: overheating (dust — clean the fans) or failing RAM (Windows Memory Diagnostic) are the two classics. But software first — it is the cause far more often than hardware.

((ad))

## The five fixes that settle most crashes

- **Update the app, then the system.** Crashes that start right after a Windows update usually mean the app needs its own update. Check the maker's website, not just the Microsoft Store.
- **Run the app as administrator once.** Some apps crash on launch because a permissions change broke their folder access. Right-click the shortcut and choose Run as administrator. If that fixes it, set it permanently in the shortcut's Properties > Compatibility.
- **Rename the app's settings folder.** Apps that keep settings in AppData crash when those files corrupt. Press Win+R, type %appdata%, find the app's folder and rename it to .old — the app builds a fresh one on the next start.
- **Reinstall cleanly.** Uninstall, delete leftover folders in %appdata% and %localappdata%, then install the latest version. A clean reinstall fixes what repair buttons pretend to fix.
- **Test in a clean boot.** Run msconfig, hide Microsoft services, disable the rest, restart. No crashes in a clean boot means another program is interfering — antivirus overlays and RGB utilities are the usual pair.

## Keeping crashes away

Apps crash for reasons, and the reasons repeat. Keep Windows and drivers roughly current — a six-month backlog of updates is the most common crash factory on home PCs. Don't run two antivirus products at once; they fight over files and the app in the middle loses. And if one specific app crashes while everything else stays stable, the problem is that app's installation, not your PC — clean reinstall it and move on.
