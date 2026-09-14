---
title: "My WiFi network name is not showing in the list"
cat: internet
icon: "📶"
image: "assets/uploads/cats/internet.jpg"
date: "Jul 26, 2026"
mins: "3"
excerpt: "You open the WiFi list on your phone and your home network's name is simply not there — but your neighbor's networks show."
---

You open the WiFi list on your phone and your home network's name is simply not there — but your neighbor's networks show. This means the phone cannot hear the router's signal, or the router stopped broadcasting its name. Causes: the router is off or crashed, you are too far away, the network is set to hidden, or a band/compatibility mismatch.

## The ladder

1. **Check the router is genuinely alive:** lights on, and other devices still connected. A router that crashed (all lights frozen or red) broadcasts nothing — power-cycle it (unplug 30 seconds). A surprising share of "network vanished" cases is just this.
2. **Check the network on ANOTHER device:** a laptop or second phone sees your network? Then the problem is the first device, not the router — toggle its WiFi off/on, restart it, and if it persists, "Forget" nothing — instead check it supports the band: very old devices cannot see 5GHz networks at all.
3. **Band mismatch:** if the router broadcasts 5GHz-only (or the 2.4GHz radio died), 2.4GHz-only devices see nothing. Log into the router (192.168.1.1) from a device that CAN connect → wireless settings → confirm both bands are enabled, or enable the 2.4GHz network.
4. **Hidden SSID check:** in the router's wireless settings, "Hide SSID" / "Broadcast network name" — if someone enabled hiding, the name disappears from every list by design (and adds no security worth having — see our hidden-SSID guide). Untick it.
5. **Channel mismatch (rare but real):** routers set to a fixed channel your device's regional firmware cannot see (common with imported devices) produce exactly this. Set the router's channel to Auto or a low channel (1-11) for 2.4GHz.

## The interim workaround

Add the network manually: phone WiFi settings → Add Network → type the exact name (SSID), security WPA2, password — devices connect to hidden/odd networks this way, which also tells you the router is broadcasting (reachable) even if not listing.

((ad))
