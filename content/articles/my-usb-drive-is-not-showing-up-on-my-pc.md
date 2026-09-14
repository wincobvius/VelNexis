---
title: "My USB drive is not showing up on my PC"
cat: windows
icon: "🪟"
image: "assets/uploads/topics/cloud-sync.jpg"
date: "Aug 3, 2026"
mins: 2
excerpt: "You plug a USB drive or external hard disk and nothing appears in 'This PC' — as if you plugged nothing."
---
You plug a USB drive or external hard disk and nothing appears in "This PC" — as if you plugged nothing. Sometimes you hear the connection sound, but no drive shows. Causes: a damaged port, a broken cable, the drive having no drive letter assigned, a driver problem, or (worst case) the drive itself failing. The order of checks goes from easiest to hardest.

## How to fix it

1. Try a different USB port.
2. Try the drive on another computer. If it works there, your port has a problem.
3. Check Disk Management: right click Start → Disk Management. If the drive shows without a letter, right click it → Change letter → Add.
4. If it shows as "not initialized", do not format if you need data — use recovery software first.
5. Update USB drivers in Device Manager.

((ad))

## Bring the USB drive back
- Try another port, then another PC - rule out the port before anything else.
- Right-click Start > Disk Management. If the drive appears there, right-click it > Change Drive Letter > Add. It appears in Explorer instantly.
- If it shows as RAW or Unallocated, do NOT format it when files matter - run a recovery tool first.
- Device Manager > USB controllers: uninstall the device, unplug, replug.
- Drives with a cable: try another cable - charging cables look the same but carry no data.
- A drive that clicks or gets warm: stop plugging it in - that is professional recovery territory.
- Mac-formatted drives are invisible on Windows by design - plug them into a Mac or use a Mac-drive tool.

Try the port on the back of a desktop PC - front-panel USB ports are connected through cheaper controllers and fail first. It is the fastest way to rule the port in or out.

Each test below eliminates one suspect completely. Work down the rows and the fault reveals itself without any tools.

## What each test rules out

| Test result | What it rules out | What to try next |
| A different port works | The first port is failing | Use rear ports; note the dead one |
| A different computer works | The drive itself is healthy | Reinstall your PC's USB drivers |
| A different cable works | The cable was the fault | Replace it - cables fail silently |
| Nothing works anywhere | The drive or its enclosure | Try a new enclosure before giving up |
