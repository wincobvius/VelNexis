---
title: "My printer shows offline but it is connected"
cat: printer
icon: "🖨️"
image: "assets/uploads/topics/printer-man.jpg"
date: "Jul 26, 2026"
mins: 2
excerpt: "Your printer is on, connected, working for other tasks — but Windows insists it is 'offline' and refuses every print job."
---
Your printer is on, connected, working for other tasks — but Windows insists it is "offline" and refuses every print job. This status mismatch is one of the most common office problems in the world. The cause is usually a stale status flag in Windows (a checkbox nobody knows exists) or a sleeping print service.

## How to fix it

1. Turn the printer off and on.
2. On the computer: Control Panel → Devices and Printers → right click the printer → "See what's printing" → Printer menu → untick "Use Printer Offline".
3. Restart the Print Spooler: Windows search "services.msc" → Print Spooler → Restart.
4. For WiFi printers, check printer and computer are on the same network.
5. Remove the printer from the computer and add it again.

((ad))

## Bring it back online
- In Windows Settings > Printers, turn off 'Let Windows manage my default printer' and set this printer as default yourself.
- Restart the Print Spooler: press Win+R, type services.msc, find 'Print Spooler', right-click Restart.
- If it is a WiFi printer, give it a fixed IP in the router. When the IP changes, Windows keeps looking for the old address and shows 'offline'.
- Open printer Properties > Ports and uncheck 'Enable SNMP status' - this setting makes many healthy printers show as offline.
- Remove the printer and add it again. It takes two minutes and rewrites the broken connection settings.
- Reboot the router and the printer together. Many 'offline' printers are just WiFi reconnection problems in disguise.

## Quick recap
- Restart the Print Spooler service.
- Give a WiFi printer a fixed IP.
- Uncheck SNMP status in the port settings.
- Remove and re-add the printer when all else fails.
