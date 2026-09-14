---
title: "OneDrive keeps asking me to sign in again and again"
cat: cloud
icon: "☁️"
image: "assets/uploads/topics/login-password.jpg"
date: "Aug 13, 2026"
mins: "3"
excerpt: "Every time you open a file or start the PC, OneDrive demands your password again — you sign in, it works, and tomorrow it asks again."
---

Every time you open a file or start the PC, OneDrive demands your password again — you sign in, it works, and tomorrow it asks again. This login loop comes from broken saved credentials, an out-of-date OneDrive app, or Windows and OneDrive being signed into different accounts. A reset of the sync connection usually ends the loop.

## End the loop

1. **Check the accounts match.** The Microsoft account signed into Windows (Settings → Accounts) and the account OneDrive uses (click the cloud icon → Settings → Account) must be the same. A Windows login with a personal email and a OneDrive signed into a work account is the classic loop-maker.
2. **Unlink and relink OneDrive:** cloud icon → Help & Settings → Settings → Account → **Unlink this PC**. Nothing is deleted — files stay both in the cloud and on the disk. Then sign in again, choose the same folder, and let it reconnect. This rebuilds the saved credentials and ends most loops.
3. **Clear the stale credential** if relinking did not: Windows Settings → Credential Manager → Windows Credentials → remove the entries mentioning OneDrive/MicrosoftOffice, then sign in fresh.
4. **Update or reset the app:** an old OneDrive client mis-handles modern authentication. Microsoft Store → Library → Update; or Settings → Apps → OneDrive → Reset (Windows keeps your files through both).

## The corporate variant

A work/school OneDrive looping after a password change is normal once — sign in with the NEW password everywhere (Windows mail apps included). If it loops forever, your organization's admin may need to re-register the device — that one is not fixable from your side, and one message to IT ends it.

((ad))
