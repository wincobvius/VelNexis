---
title: "My hard drive is not showing up on my computer"
cat: recovery
icon: "🗄️"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Jul 25, 2026"
mins: 2
excerpt: "You connect an internal or external hard drive and the computer ignores it — nothing in 'This PC', maybe a connection sound but no drive."
---
You connect an internal or external hard drive and the computer ignores it — nothing in "This PC", maybe a connection sound but no drive. Causes climb a ladder of severity: loose cables and missing drive letters (easy fixes), unallocated partitions (recoverable), or a physically dying drive (professional help). Disk Management is the window that shows which rung you are on.

## How to fix it

1. Try another USB port and another cable.
2. Listen — if the drive spins and clicks softly, it has power.
3. Open Disk Management (right click Start) — if the drive shows without a letter, right click → Change drive letter → Add.
4. If it shows "Unallocated", do NOT format if data matters — use recovery software first.
5. Try the drive on another computer to know if it is the drive or the PC.

((ad))

## Make Windows see the drive
- Right-click Start > Disk Management. A drive showing without a letter just needs one: right-click > Change Drive Letter.
- Brand new drives show as Unallocated - they must be initialized and formatted before use (that erases them, so only for new drives).
- A drive that worked before: try another cable, another port, another PC.
- Device Manager > Disk drives: a warning icon means driver trouble - update or roll back.
- External drives with a power adapter: a half-dead adapter spins the disk while the PC sees nothing.
- Clicking sounds mean stop and go to a professional - software makes it worse.
- Drives over 2 TB sometimes need GPT conversion, visible right in Disk Management.

Listen as you plug it in - a healthy drive spins with a soft whir, a dying one clicks in rhythm. That sound check, done once, tells you whether to try software fixes or go straight to a recovery shop.

Each symptom below points to a different layer of failure. Find your row before opening the case or ordering anything.

## Quick diagnosis by symptom

| Symptom | Likely meaning | Next step |
| Not in File Explorer, visible in Disk Management | No drive letter assigned | Assign a letter in Disk Management |
| Clicking sound | Mechanical failure starting | Stop using it, go to a recovery shop |
| Visible but asks to format | Corrupted partition table | Recovery software first, never format |
| Not detected anywhere | Cable, enclosure or port dead | Swap the cable, try a second enclosure |
