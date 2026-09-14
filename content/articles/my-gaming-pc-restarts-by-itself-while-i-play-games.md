---
title: "My gaming PC restarts by itself while I play games"
cat: gaming
icon: "🎮"
image: "assets/uploads/topics/broken-phone.jpg"
date: "Aug 28, 2026"
mins: 2
excerpt: "Everything runs fine — until you launch a demanding game, and minutes later the PC restarts instantly, no warning, no blue screen."
---
Everything runs fine — until you launch a demanding game, and minutes later the PC restarts instantly, no warning, no blue screen. Games push the whole system to maximum: power supply, CPU, GPU. A component at its limit is usually the guilty party — most often the power supply (PSU) that cannot deliver the punch, or heat reaching shutdown levels.

## How to fix it

1. Games push the power supply hard — a weak or old PSU is the number one cause.
2. Check temperatures with HWMonitor — overheating CPU/GPU forces shutdown.
3. Clean dust from the PC and fans.
4. Update GPU drivers.
5. Check Windows Event Viewer for the shutdown reason, and test with the side panel open + a fan blowing to see if heat is the cause.

((ad))

## Find the real cause
- Sudden restarts during games are usually heat or power. Install HWMonitor and watch CPU and GPU temperature while playing - anything near 90 degrees is too hot.
- Clean the dust out with a blower, focusing on fans and heatsinks. Dust is the most common cause of gaming overheats.
- Check your power supply wattage against your graphics card's needs. A weak power unit restarts the PC exactly when a game loads the GPU.
- Open Event Viewer > Windows Logs > System and look for 'Kernel-Power 41' errors - their timing tells you if the cause is power or heat.
- Update graphics drivers with a clean install (tick 'perform a clean installation' in the installer).
- If the RAM or CPU was overclocked, set everything back to stock speeds and test again.

Borrow a power supply for one evening if you can - it is the fastest way to isolate the cause. Power supplies degrade quietly, and a PSU that ran your build for years can become the restart trigger after a graphics card upgrade.
