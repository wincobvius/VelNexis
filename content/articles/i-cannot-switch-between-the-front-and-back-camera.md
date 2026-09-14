---
title: "I cannot switch between the front and back camera"
cat: camera
icon: "📷"
image: "assets/uploads/topics/taking-photo.jpg"
date: "Sep 2, 2026"
mins: "3"
excerpt: "The camera switch button (selfie to main camera) does nothing — the view stays on one camera no matter how many times you tap."
---

The camera switch button (selfie to main camera) does nothing — the view stays on one camera no matter how many times you tap. This is almost always a software state problem: the camera app's memory is stuck, or one app is holding the other camera. Restarts and cache clears handle it.

## The unstick sequence

1. **Close the camera app completely** — from recent apps, swipe it away. Camera apps cache which lens is active; a crashed session leaves the switch dead. Reopen and test.
2. **Close EVERYTHING using a camera** — WhatsApp video call left running, Snapchat, a barcode scanner, the browser tab that asked for camera. Android and iOS allow only one owner of the camera at a time; a background holder blocks the switch even when the preview works.
3. **Restart the phone** — resets the camera service completely. This alone fixes the large majority of stuck-switch cases.
4. **Clear the camera app's data** (Android: Settings → Apps → Camera → Storage → Clear data) — resets saved camera states. On iPhone: offload/reinstall the Camera app is not possible (system app), so a settings reset (Settings → Camera → Preserve Settings on, toggle formats) or restarting is the equivalent.
5. **Test in another app that uses the switch** (Instagram stories, WhatsApp camera). Switch works there → the problem is your camera app alone: reinstall it or check its permissions (Settings → Apps → Camera → Permissions — camera permission granted?).

## The hardware hint

If the switch "works" but the view goes BLACK on one camera, that camera module has failed (or its connector loosened after a drop) — the switch is fine, the lens behind it is not. That is the repair-shop case, and our front-camera guide covers the diagnosis.

((ad))
