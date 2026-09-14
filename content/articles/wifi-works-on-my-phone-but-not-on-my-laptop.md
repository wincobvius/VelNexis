---
title: "WiFi works on my phone but not on my laptop"
cat: internet
icon: "📶"
image: "assets/uploads/cats/internet.jpg"
date: "Aug 8, 2026"
mins: 2
excerpt: "Every phone in the house connects to the WiFi fine, but one laptop refuses — it cannot find the network, fails to connect, or connects with 'no intern."
---
Every phone in the house connects to the WiFi fine, but one laptop refuses — it cannot find the network, fails to connect, or connects with "no internet". This proves the router is fine and the problem is inside the laptop: usually its WiFi switch is off, the saved network details are wrong, or the WiFi driver is old or damaged. Laptop WiFi problems almost always stay laptop problems.

## How to fix it

1. Restart the laptop.
2. Turn laptop WiFi off and on (there is often a key like F2 with a WiFi symbol).
3. Forget the network on the laptop and connect again.
4. Update the WiFi driver: Device Manager → Network adapters → right click → Update driver.
5. Run Windows network troubleshooter: Settings → Network → Troubleshoot.

((ad))

## Fix the laptop side
- Forget the WiFi network on the laptop and join again with the password typed fresh.
- Update the WiFi driver from your laptop maker's website, not from Windows Update - this fixes most 'phone works, laptop does not' cases.
- Open Command Prompt as admin and run: netsh winsock reset then netsh int ip reset, and restart.
- Also run ipconfig /release and ipconfig /renew if the laptop shows a 169.x.x.x address - that means it never really connected.
- If the router has two network names, try the 2.4 GHz one - some laptop WiFi cards fail on 5 GHz.
- Check the router's MAC filter list. A blocked device shows full signal but never connects.

## Quick recap
- Driver from the laptop maker's site, not Windows Update.
- Forget and rejoin the network fresh.
- netsh winsock reset fixes the deep stack.
- Try the 2.4 GHz name - some laptop cards refuse 5 GHz.
