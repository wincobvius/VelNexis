---
title: "'Too many redirects' error is showing on a website"
cat: browser
icon: "🧭"
image: "assets/uploads/topics/laptop-error.jpg"
date: "Aug 30, 2026"
mins: "3"
excerpt: "A website bounces you in a circle: page A sends you to B, B sends you to A, until the browser gives up with 'ERR_TOO_MANY_REDIRECTS'."
---

A website bounces you in a circle: page A sends you to B, B sends you back to A, until the browser gives up with "ERR_TOO_MANY_REDIRECTS". Redirect loops come from leftover cookies confusing the site, VPN interference, or the website's own broken configuration. Your side is fixable; the site's side is their problem.

## Your-side fixes, in order

1. **Clear that site's cookies only:** click the padlock (or the tune icon) → Cookies and site data → Delete. This is the classic fix — a stale cookie (usually an old login or region setting) tells the site you are somewhere you are not, and the site bounces you trying to fix it. Deleting cookies for the one site avoids logging you out of everything else.
2. **Test in incognito:** incognito has clean cookies. If the site loads there, cookie corruption is confirmed — the step above is your permanent fix.
3. **VPN or proxy interference:** a VPN exit node in another country can clash with the site's region redirects. Toggle the VPN off and retry; if that fixes it, use a different server location for that site.
4. **Check the site without your browser:** a different device or mobile data gives a clean verdict. Loads everywhere but your machine → your browser data is the problem. Broken everywhere → the site's configuration is broken, and no amount of cookie-clearing on your side will fix their server.

## When it is their side

If the loop happens for the whole world (check via down-detection sites or a friend on another network), all you can do is wait — site teams usually fix redirect loops within hours, and their error-monitoring pages often admit the outage honestly.

## One caution

"Delete cookies for all sites" (the big hammer) also signs you out of everything. It works, but do the per-site deletion first — same fix, none of the re-login marathon.

((ad))
