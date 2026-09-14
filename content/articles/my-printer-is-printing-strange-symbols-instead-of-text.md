---
title: "My printer is printing strange symbols instead of text"
cat: printer
icon: "🖨️"
image: "assets/uploads/topics/printer-man.jpg"
date: "Sep 6, 2026"
mins: "3"
excerpt: "Your printouts are gibberish — random symbols, garbage characters, endless lines of nonsense instead of your document."
---

Your printouts are gibberish — random symbols, garbage characters, endless lines of nonsense instead of your document. The document is fine; the translation between computer and printer broke. This is almost always a driver problem: wrong driver, corrupted driver, or the job sent to the wrong printer in the list.

## The three fixes, in order

1. **Wrong printer target — check first:** open the print dialog and look at WHICH printer is selected. A document sent to a different printer model (an old entry, a PDF printer, a different model in the office) prints as garbage because the translation is for the wrong machine. Select the right one and reprint — sometimes the whole fix.
2. **Cancel the garbage properly:** the queue may still hold corrupted jobs that keep printing nonsense page after page. Cancel all documents in the print queue (Printers & scanners → your printer → Open queue), and if they refuse to die: restart the print spooler (Search "Services" → Print Spooler → Restart), then power-cycle the printer to flush its own memory.
3. **Reinstall the driver — the real fix:** Settings → Printers & scanners → remove the printer → restart → re-add it. If Windows pulls the same broken driver again, download the FULL driver package from the maker's official site (exact model!) and install it fresh. A corrupted driver translation produces exactly this symptom on every page.

## The less common causes

4. **A bad cable or connection** corrupts the data stream itself — gibberish from a USB printer on a flaky long cable is a real thing: swap the cable. On WiFi, a printer at the edge of signal range receives corrupted jobs — move it closer to the router.
5. **The wrong "print language":** some printers offer PCL/PostScript modes, and a job sent in the wrong language prints as symbols. In the printer's driver settings, try switching the language/emulation to the maker's default.

## One expectation

Ink-level, cartridge and paper problems never cause gibberish — those change QUALITY, not characters. Gibberish is translation: target, driver, or connection. Always.

((ad))
