---
title: "My pendrive is write protected, I cannot copy anything"
cat: recovery
icon: "🗄️"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Aug 7, 2026"
mins: 2
excerpt: "'The disk is write protected' has three real causes: a lock switch, a Windows flag, or a failing chip protecting itself. Check them in this order."
---

Your USB drive refuses every write — "The disk is write protected" — no copying to it, no deleting from it, sometimes no formatting either. Three things cause this: a physical lock switch, a Windows write-protection flag, or — the serious one — the drive's memory failing into permanent read-only mode as its last act of self-protection.

> **Note:** In the diskpart steps below, double-check you have selected the USB drive, not your computer's own disk. And if the drive has become unreliable, copy your files off it before anything else.

## Check in this order

1. **Look for a physical lock switch.** Some drives (and SD-card adapters) have a tiny slider on the side. It is easy to bump, and it explains everything when engaged.
2. **Try another computer and port.** Rules out a confused USB controller on the PC side.
3. **Clear Windows' write-protection flag.** Command Prompt as administrator:
   - `diskpart` → `list disk` → `select disk X` (X = your USB, check the size column!)
   - `attributes disk clear readonly`
4. **Check the registry flag** (advanced): regedit → HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies → set **WriteProtect** to 0 → replug the drive.
5. **Still read-only everywhere?** The controller chip has locked itself to prevent data loss. Copy everything off the drive while you still can, then replace it — this state is not repairable, and the drive's next stage is failure.

((ad))

## Quick recap
- Some pendrives have a tiny physical lock switch on the side - check it first.
- Command Prompt: diskpart > list disk > select disk 1 > attributes disk clear readonly.
- The registry fix (StorageDevicePolicies WriteProtect value to 0) handles stubborn cases.
- A pendrive that stays read-only across every PC is failing - copy its data off now.
