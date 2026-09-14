---
title: "My app is not updating on my computer"
cat: software
icon: "🧩"
image: "assets/uploads/topics/downloading-apps.jpg"
date: "Jul 30, 2026"
mins: "3"
excerpt: "A program offers an update, you accept, and the update fails — or the app's 'check for updates' spins forever."
---

A program offers an update, you accept, and the update fails — or the app's "check for updates" spins forever. App updates fail when the app is running while updating, when permissions block the updater, or when the updater's downloaded files are broken. The reliable backup plan is always the same: install the new version on top.

## The ladder

1. **Close the app completely before updating** — including from the system tray (the little icons near the clock: right-click → Exit). An updater cannot replace files the running app is holding; "update failed" after a silent background instance of the app is the classic case. Task Manager (Ctrl+Shift+Esc) shows the truth: end every process of that app.
2. **Run the updater as administrator:** right-click the app (or its updater) → Run as administrator. Updaters write into Program Files, which needs elevation — a failed permissions write reads as "update error" with no further explanation.
3. **Antivirus quarantine:** some security suites block updaters by default (downloading an .exe is exactly what they watch for). Check the antivirus's blocked/quarantine list, allow the app's updater, retry.
4. **The fallback that always works — install fresh on top:** download the newest full installer from the maker's official site and run it WITHOUT uninstalling. Installers are built to upgrade in place: your settings, accounts and data survive, and the result is the same as a successful update. This is the fix when the in-app updater is permanently broken.
5. **"Spinning forever" specifically:** the app checks for updates through the network — a VPN, proxy or firewall blocking the update server produces the eternal spinner. Toggle the VPN off for the check.

## When to give up on the built-in updater

If the in-app updater fails on every release for months, stop respecting it: bookmark the maker's download page, use route #4 each time, and tick "notify me" if the site offers update emails. An app whose updater is broken but whose installer works is an annoyance, not a dead end.

((ad))
