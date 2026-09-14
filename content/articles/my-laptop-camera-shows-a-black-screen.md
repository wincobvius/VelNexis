---
title: "My laptop camera shows a black screen"
cat: camera
icon: "📷"
image: "assets/uploads/topics/broken-phone.jpg"
date: "Aug 24, 2026"
mins: "3"
excerpt: "Your laptop's built-in camera shows a black screen in every app."
---

Your laptop's built-in camera shows a black screen in every app. Before assuming the camera died, know that laptops hide camera controls in surprising places: physical privacy shutters, keyboard function keys, and Windows privacy settings that silently block everything. Most "dead" laptop cameras are just switched off somewhere.

## The switch hunt

1. **Physical shutter first:** many modern laptops have a sliding cover over the lens or a camera kill switch on the side. A shuttered lens shows black, not error — the single most common "dead camera" cause.
2. **The function key:** look for a camera-slash icon on the F-key row (F8/F10, varies by brand) — one tap mutes the camera at firmware level, and it survives reboots. Toggle it and watch the camera LED.
3. **Windows privacy settings:** Settings → Privacy & security → Camera — the MASTER toggle "Camera access" and "Let apps access your camera" both on, and your specific app enabled in the list. A Windows update occasionally flips these off silently, producing black screens everywhere.

## The software checks

4. **Test the camera in another app:** the Camera app built into Windows, Zoom, a browser test site — if the camera works anywhere, the driver is fine and the failing app's own settings are the problem (Zoom/Meet have their own camera-selection dropdowns where the wrong device is often selected).
5. **Device Manager:** look under Cameras — is it listed without a warning icon? Disable → re-enable the device; roll back or update the driver if one was recently updated.
6. **Antivirus camera protection:** suites like Kaspersky and Norton include camera guards that block apps by default. Check its "camera protection" module before anything more drastic.

## If nothing wakes it

An external USB webcam is the cheap, honest workaround — and a laptop opened for repair recently points at a disconnected camera ribbon inside: re-attachable in minutes at a shop.

((ad))
