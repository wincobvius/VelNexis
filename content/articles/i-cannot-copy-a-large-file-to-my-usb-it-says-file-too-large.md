---
title: "I cannot copy a large file to my USB, it says file too large"
cat: recovery
icon: "🗄️"
image: "assets/uploads/topics/hdd-backup.jpg"
date: "Aug 31, 2026"
mins: 2
excerpt: "20 GB free, but a 5 GB file refuses to copy? Free space is not the problem — the drive's FAT32 format has a hard 4 GB per-file limit."
---

Your USB drive has 20 GB free, but a 5 GB file refuses to copy: "The file is too large for the destination file system." The error is honest — free space is not the problem. The drive's file system is: FAT32, the default format on most USB drives for maximum compatibility, cannot hold any single file larger than 4 GB. It does not matter how much empty space sits next to it.

## Fix 1 — the real one: reformat as exFAT

> **Before you start:** Formatting erases everything on the drive. Copy its current contents to your computer first — the steps below assume you have already done that.

1. Copy everything on the USB drive to your computer.
2. Right-click the drive in File Explorer → **Format**.
3. Under File system, choose **exFAT** (not FAT32, not NTFS).
4. Leave "Quick Format" ticked and start. Afterwards, copy your files back — large ones included.

exFAT works on Windows, Mac and modern phones, and has no practical file-size limit.

## Fix 2 — when you cannot reformat

If the drive must stay FAT32 (some old TVs, car stereos and set-top boxes only read FAT32), split the file instead: right-click it in 7-Zip → "Add to archive" → set "Split to volumes" to 4000M. The file travels as parts you re-join on the other computer with the same tool.

((ad))

Q: Why not NTFS?
A: NTFS also handles big files, but Macs and many TVs read it poorly or not at all. For a drive that moves between devices, exFAT is the safer choice.

The 'file too large' error means the drive is FAT32 formatted, which caps single files at 4GB. Copy the data off, format the drive as exFAT, and copy back - exFAT handles huge files and works on Windows and Mac both.
