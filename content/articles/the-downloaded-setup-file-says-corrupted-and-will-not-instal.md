---
title: "The downloaded setup file says corrupted and will not install"
cat: software
icon: "🧩"
image: "assets/uploads/topics/downloading-apps.jpg"
date: "Aug 10, 2026"
mins: "3"
excerpt: "You downloaded a program and the installer says 'file is corrupted', 'installer integrity check failed', or it errors at a random percent."
---

You downloaded a program and the installer says "file is corrupted", "installer integrity check failed", or it errors at a random percent. The file got damaged during download — internet hiccups, antivirus interference, or an unstable connection. The fix is a clean re-download, done the right way so it does not break again.

## The clean re-download

1. **Delete the broken file entirely** — do not re-run it hoping; integrity failures do not heal. Empty the Downloads of the old copy so the new one cannot be confused with it.
2. **Re-download from the maker's official site** (not the same mirror that failed — the official download itself). Prefer a stable connection; a download that "finished" after hanging at 99% for minutes is exactly the file that declares itself corrupted later.
3. **Let the download finish completely before opening** — browsers that pause/resume mid-click produce half-files. Check the file size against the site's listed size (when shown) before running.
4. **Try a different browser or a download manager** for large files: browser download stacks break on flaky connections, and a download manager resumes properly instead of corrupting.

## The other corruption sources

5. **Antivirus stripping the installer:** some suites quarantine parts of installers mid-download (they contain compressed executables — exactly what AV watches). Check the antivirus quarantine log: if the file landed there, restore it and add an exception for the maker's installer, or pause protection only for this trusted download.
6. **The disk itself:** files corrupting repeatedly across DIFFERENT downloads point at the drive or RAM — run a disk check (this PC → drive → Properties → Tools → Check) and Windows Memory Diagnostic. Random corruption across files is a hardware tell, not a download problem.
7. **The false alarm:** a few security suites slap "corrupted/dangerous" on perfectly valid installers (repacked installers from official sources occasionally trip heuristics). Verify the file's checksum when the maker publishes one — a matching checksum proves the download is intact, and the "corruption" message is the antivirus misbehaving.

((ad))
