---
title: "My computer cannot find my printer"
cat: printer
icon: "🖨️"
image: "assets/uploads/topics/printer-man.jpg"
date: "Aug 19, 2026"
mins: "3"
excerpt: "You try to add your printer to the computer and the search comes back empty — the printer exists, is on, maybe even prints from other devices, but thi."
---

You try to add your printer to the computer and the search comes back empty — the printer exists, is on, maybe even prints from other devices, but this computer cannot see it. Discovery failures come from network separation (different WiFi bands act like different networks), USB cable issues, or Windows' discovery service napping on the job.

## Network printer (WiFi)

1. **Same network check — including the band:** the printer and the computer must be on the same network NAME. Printers connect to 2.4GHz; if your router splits it into "MyWiFi" and "MyWiFi_5G", a computer on the 5G name is on a different network as far as discovery cares. Reconnect the computer to the same name the printer uses, or enable "band steering" on the router so both share one name.
2. **Printer's own connection:** print its network configuration page (printer menu) — it must show your network name and "Connected". A printer that dropped off WiFi is invisible to everything; rerun its WiFi wizard.
3. **Restart both, router included** — the classic triangle (printer off/on, computer off/on, router unplug 30s) fixes discovery more often than any setting.
4. **Windows discovery:** Settings → Printers & scanners → Add device → "Add manually" → "My printer is a little older. Help me find it." — the old-style search catches printers the modern dialogue misses. Also run the Printer Troubleshooter (Settings → System → Troubleshoot) which restarts the print spooler and discovery services.
5. **IP address as the last resort:** the printer's config page shows its IP address (e.g., 192.168.1.50). Add printer manually → "Add a printer using TCP/IP address" → type it. Bypasses discovery entirely — a printer reachable by IP is always addable.

## USB printer

6. Try another USB port and another cable (charge-only cables strike again), and check Device Manager — an unknown USB device under "Other devices" with a warning icon means Windows sees hardware but lacks the driver: install the maker's driver.

## The phone test

Print from a phone on the same WiFi first — phone prints but computer cannot = computer-side; phone also blind = printer/network-side. One test halves the suspects.

((ad))
