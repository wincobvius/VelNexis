---
title: "My printer is not printing anything at all"
cat: printer
icon: "🖨️"
image: "assets/uploads/topics/printer-man.jpg"
date: "Jul 20, 2026"
mins: "3"
excerpt: "You send a print job and the printer does absolutely nothing — no sound, no movement, no page."
---

You send a print job and the printer does absolutely nothing — no sound, no movement, no page. Printing is a chain: computer → connection → printer → paper → ink. When nothing happens, one link in that chain is broken, and the fastest way to find it is testing the printer by itself, without the computer.

## Step 1 — Test the printer alone

1. **Print the printer's own test page** — from its buttons/screen menu, "Print Test Page" or "Print Quality Report" (every printer has this). The page prints → the printer, paper and ink are all fine; the problem is the computer or the connection. Nothing prints → printer-side: check it shows no error (paper/ink lights), and see our pickup and paper-jam guides.

## Step 2 — The connection

2. **USB:** reseat both ends, try another port and another cable. Check the printer's screen lights up/plays its connect sound when you replug — silence means the cable or the port.
3. **WiFi:** is the printer still on the network? Print its network config page. The computer and printer must be on the same network name (see our "cannot find printer" guide for the 2.4/5GHz trap).

## Step 3 — The computer side

4. **The queue is the usual suspect:** Settings → Printers & scanners → your printer → Open print queue. Stuck jobs block everything behind them — cancel all documents, then send a fresh job.
5. **"Use Printer Offline" ticked?** In the same queue window: Printer menu → untick "Use Printer Offline" if ticked. Windows sets it silently when the printer vanishes for a moment, then never unticks it — a classic silent killer.
6. **Wrong printer selected:** the document went to "Microsoft Print to PDF" or an old printer entry from a USB past. Check the print dialog's selected printer — the default printer may have changed (Windows' "let Windows manage my default printer" switches defaults to whatever you used last).
7. **Restart the print spooler:** Windows Search "Services" → Print Spooler → Restart. The spooler is the postal service of printing; restarting it clears jammed queues at the system level.

## Step 4 — The reset

Nothing above working: uninstall the printer from Printers & scanners, restart, re-add it (Windows re-installs the driver). That full rebuild ends most software-chain failures.

((ad))
