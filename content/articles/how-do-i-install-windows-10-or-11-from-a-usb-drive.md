---
title: "How do I install Windows 10 or 11 from a USB drive"
cat: windows
icon: "🪟"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Aug 13, 2026"
mins: 2
excerpt: "You need a fresh Windows — because of viruses, a dead system, or a new drive — and the proper way is installing from a bootable USB."
---

You need a fresh Windows — because of viruses, a dead system, or a new drive — and the proper way is installing from a bootable USB. This sounds like a technician's job, but Microsoft gives a free official tool that prepares the USB for you. The only things you need: another working PC, an 8 GB USB drive, and one hour of time.

## How to fix it

1. On another PC, download the "Media Creation Tool" from Microsoft's website.
2. Insert an 8 GB USB drive. The tool will make it a bootable Windows USB (this erases the USB).
3. Plug the USB into your PC. Turn it on and press the boot menu key (F12, F9, Esc or F2 depending on brand).
4. Choose the USB from the boot menu.
5. Follow the setup: choose "Custom install" for a clean Windows. Select the C drive partition carefully — installing erases that drive.

((ad))

## The USB install, done right
- You need an 8GB-plus USB stick (it gets erased), Microsoft's Media Creation Tool, and your files backed up first.
- Run the tool and choose 'Create installation media' - it builds the bootable stick itself.
- Boot from it: restart, press your brand's boot key (F12, F2 or Del), pick the USB.
- Watch the drive list during setup - installing onto the wrong drive erases it. Unplug other drives if unsure.
- Custom install shows partitions; deleting them wipes those drives. Choose carefully.
- After install: WiFi driver first if missing, then Windows Update until quiet, then your programs.
- If the PC ignores the USB, enable USB boot or disable Secure Boot in the BIOS.
- BitLocker drives must be decrypted from inside Windows first, or the data locks forever.
