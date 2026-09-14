---
title: "My browser stopped saving my passwords"
cat: browser
icon: "🧭"
image: "assets/uploads/topics/login-password.jpg"
date: "Aug 26, 2026"
mins: "3"
excerpt: "You log into a site, and next visit the browser asks for the password again — it stopped offering to save, or saved passwords vanished."
---

You log into a site, and next visit the browser asks for the password again — it stopped offering to save, or saved passwords vanished. Causes: the save setting got switched off, the site landed on a "never save" list, incognito mode was used, or a sync problem wiped the vault. All are fixable in settings.

## The settings, in order of likelihood

1. **The master switch:** Chrome Settings → Autofill and passwords → Google Password Manager (or autofill) → confirm **"Offer to save passwords" is ON**. Updates and account switches occasionally flip it off silently.
2. **The "Never save" list:** in the same settings, review "Never save" / blocked sites — one accidental "Never" click and that site never asks again. Remove the site from the list.
3. **Incognito was the culprit:** incognito windows never save passwords or history, by design. If "it stopped saving" after a session of private browsing, nothing is broken — use a normal window.
4. **Autofill declines:** if it saves but does not FILL, check "Auto sign-in" and that the site is not blocking autofill in its own code (banks do this deliberately for "security"). Their right, their loss of convenience.

## The missing-vault cases

5. **Signed out of sync:** if Chrome's passwords vanished across ALL sites at once, check the profile (top right) — a signed-out or switched profile shows an empty vault. Sign back into the same Google account with sync on; passwords return with it.
6. **"View and manage" at passwords.google.com** — the web vault shows what is truly saved, independent of any one device's confusion.

## When a site refuses to let the browser save

Some bank and payment sites suppress password saving. The honest options: let the site's own "remember this device" do the job, or keep that one password in a full password manager app, which can force-save where the browser is shy.

((ad))
