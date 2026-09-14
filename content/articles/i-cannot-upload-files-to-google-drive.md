---
title: "I cannot upload files to Google Drive"
cat: cloud
icon: "☁️"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Jul 23, 2026"
mins: "3"
excerpt: "You drag a file into Drive, the upload starts — and fails, freezes, or sits at 0% forever."
---

You drag a file into Drive, the upload starts — and fails, freezes, or sits at 0% forever. Uploads fail from the obvious (no internet, full storage) to the sneaky (file names with strange characters, browser extensions interfering, an unstable connection dropping long uploads at the last second).

## The checks, obvious to sneaky

1. **Storage first: one.google.com/storage.** A full quota silently refuses uploads — the error appears late or not at all. Free space or upgrade; everything else in this list assumes you have room.
2. **The file itself:** check its size against your quota (a 20 GB upload to 5 GB free fails by math, not by bug), and simplify the name — odd characters and very long names occasionally break the upload flow. A file open and locked in another program can also refuse to upload; close it first.
3. **The connection:** uploads are more fragile than downloads — Wi-Fi that "works" for browsing can drop a long upload at 90%. Prefer a wired or stable connection for big files, and resume rather than restart: Drive keeps partial progress per file.
4. **The browser:** try incognito (no extensions) and another browser. Ad blockers, download managers and privacy extensions are the most common invisible saboteurs. Clearing cache for drive.google.com fixes stubborn cases.
5. **The alternative route that usually works:** install Google Drive for desktop and drop the file into the synced folder — the desktop app uploads more reliably than any browser tab, and retries automatically.

## The 0%-forever case

An upload stuck at exactly 0% for minutes usually means the browser tab is throttled in the background — keep the tab visible during big uploads, or use the desktop app.

((ad))
