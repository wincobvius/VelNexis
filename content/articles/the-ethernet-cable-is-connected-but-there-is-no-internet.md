---
title: "The Ethernet cable is connected but there is no internet"
cat: internet
icon: "📶"
image: "assets/uploads/cats/internet.jpg"
date: "Aug 14, 2026"
mins: 2
excerpt: "You plugged the network cable (LAN cable) straight into your computer, but there is still no internet, and the computer may show a small globe or cros."
---
You plugged the network cable (LAN cable) straight into your computer, but there is still no internet, and the computer may show a small globe or cross icon. This happens with loose cables, a disabled network adapter, wrong network settings, or the router not giving the computer an address. Cable problems are easier to fix than WiFi because there are fewer things to check.

## How to fix it

1. Check both ends of the cable are pushed in fully. You should hear a click.
2. Look at the port lights. If no light at all, the cable or port is dead — try another cable.
3. Restart the computer and the router.
4. Windows: Settings → Network → Change adapter options → right click Ethernet → Disable, then Enable.
5. Set network to get IP address automatically (DHCP) in adapter properties.

((ad))

## Fix the cable connection
- Push both ends in until they click - the clip breaks and cables slide out halfway. Try another cable first; they fail more than ports do.
- No lights on the port at all means cable, port or adapter trouble.
- Restart the router and the PC together.
- Run the built-in network troubleshooter: Settings > Network > Ethernet.
- Device Manager > Network adapters > your Ethernet adapter > Uninstall, then restart.
- In Command Prompt as admin, run ipconfig /release, then ipconfig /renew, then ipconfig /flushdns.
- Check the router: the cable must go into a LAN port, and the router light for that port should be on.
- USB Ethernet adapters fail often - try another one or another USB port.

Swap the cable before believing anything else - cables fail more than routers, ports and settings combined, and they fail silently. The second cable test costs nothing and ends the guessing.
