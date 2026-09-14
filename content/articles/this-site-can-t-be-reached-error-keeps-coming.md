---
title: "'This site can't be reached' error keeps coming"
cat: browser
icon: "🧭"
image: "assets/uploads/topics/laptop-error.jpg"
date: "Jul 29, 2026"
mins: "3"
excerpt: "Chrome shows 'This site can't be reached' — the page refuses to load while other sites work fine, or all sites fail together."
---

Chrome shows "This site can't be reached" — the page refuses to load while other sites work fine, or all sites fail together. This error is the browser saying "I knocked on the website's door and nobody answered." The knock can fail because of your internet, your DNS settings, or because the website itself is down for the whole world.

## First question: all sites, or just one?

1. **All sites failing → it is your connection.** Check Wi-Fi/cable, restart the router (unplug 30 seconds), and check whether other devices on the same network are also down. Device-specific failure points to the device's network settings (airplane mode, DNS, proxy — keep reading).
2. **One site failing while others load → the site may simply be down.** Check it on your phone's mobile data (different network entirely) or a site like downforeveryoneorjustme.com — if it is down for everyone, close the tab and come back later; no restart on your side will revive their server.

## Your-side fixes

3. **The classic 30-second cure:** Ctrl+F5 (hard reload skipping cache), then restart the browser completely.
4. **DNS flush — the most common software fix.** Command Prompt → `ipconfig /flushdns`. Then try changing your DNS to a public one (Settings → Network → adapter properties → DNS: 8.8.8.8 and 8.8.4.4): if your provider's DNS is flaky, this single change makes "can't be reached" errors rare for good.
5. **Proxy and VPN check:** leftover proxy settings (Settings → Network → Proxy) or a VPN that silently died block sites while the internet "works". Turn the proxy off, toggle the VPN.
6. **Firewall/antivirus overreach:** temporarily pausing a security suite (if you consciously can) reveals whether it started eating your traffic. If pausing fixes it, adjust the suite rather than living with it off.

## The error code tells the tale

`ERR_CONNECTION_RESET` points to network interference; `DNS_PROBE_FINISHED_NXDOMAIN` is DNS; `ERR_CONNECTION_TIMED_OUT` is often the site or an overstrict firewall. Google your exact code with one of these fixes in mind and you are halfway there.

((ad))
