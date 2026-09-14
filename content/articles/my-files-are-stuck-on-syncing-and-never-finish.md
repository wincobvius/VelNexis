---
title: "My files are stuck on 'syncing' and never finish"
cat: cloud
icon: "☁️"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Aug 26, 2026"
mins: "3"
excerpt: "The sync status shows 'Syncing…' or a spinning circle for hours — the file never finishes uploading, and other files queue behind it."
---

The sync status shows "Syncing…" or a spinning circle for hours — the file never finishes uploading, and other files queue behind it. Stuck syncs have classic causes: the file is open in another program, its name contains forbidden characters, storage ran out mid-upload, or the sync app itself froze.

## Unstick it, in order

1. **Restart the sync app** — the cloud icon in your system tray/menu bar → Quit → reopen. Half of all stuck syncs are a frozen app, and this costs nothing.
2. **Find the actual stuck file.** Click the sync icon — Drive/OneDrive/Dropbox all show which file is processing. The fix targets THAT file, not the whole queue.
3. **Open files block sync:** a document still open in Word/Excel locks its file and stalls the queue. Close the program (not just the window), and watch the queue move.
4. **Rename problem files.** Characters that upset sync apps even today: `? * : " < > |` and names ending in spaces or dots. Rename the stuck file to plain letters and numbers.
5. **Check quota mid-upload** — a file larger than remaining cloud storage fails at the end and retries forever, looking exactly like a hang. Free space or remove the file from the sync folder.

## The deeper fixes

- **Huge single files** (video projects, disk images) legitimately take hours — check the app's upload progress rather than the generic "syncing" icon before declaring it stuck.
- **Selective sync / choosing which folders sync** can exclude a problematic folder to let the rest flow, then attack the problem folder alone.
- Still stuck after all this? Unlink and relink the app (sign out of the sync app, sign back in) — the nuclear-ish reset that rebuilds the sync database.

((ad))
