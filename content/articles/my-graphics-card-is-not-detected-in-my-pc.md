---
title: "My graphics card is not detected in my PC"
cat: gaming
icon: "🎮"
image: "assets/uploads/topics/money-transfer.jpg"
date: "Aug 31, 2026"
mins: 2
excerpt: "Your games run on weak built-in graphics, and the system ignores the powerful graphics card entirely — Device Manager shows nothing, or it appears wit."
---

Your games run on weak built-in graphics, and the system ignores the powerful graphics card entirely — Device Manager shows nothing, or it appears with an error. Detection failures come from physical seating (the card slightly out of its slot), missing power cables, BIOS settings, or driver conflicts. A reseat fixes a remarkable number of "dead" cards.

## How to fix it

1. Turn off the PC, remove the card, put it back firmly and connect the power cables.
2. Check the monitor cable is in the GPU port.
3. Boot into BIOS and check the GPU is detected and primary display is set to PCIe.
4. In Windows, open Device Manager → scan for hardware changes.
5. Test the card in another PC — if it is not found there either, the card is faulty.

((ad))

## Make the PC see the card
- Reseat the card: power off, take it out, push it back into the top PCIe slot until the lock clicks.
- Check the power cables from the power supply are fully plugged into the card - many cards light up without full power and then stay invisible.
- Connect your monitor to the graphics card itself, not the motherboard port. This is the most common 'not detected' of all.
- In Device Manager under Display adapters, a warning icon means driver trouble - right-click and update or roll back.
- Install drivers from NVIDIA, AMD or Intel directly - Windows Update drivers are often too old for new cards.
- Compare your power supply wattage with the card's requirement - weak supply runs fans but not the card.
- Testing in another PCIe slot or another PC tells you whether the card or the motherboard is at fault.
