---
title: "The iOS update keeps failing on my iPhone"
cat: iphone
icon: "🍎"
image: "assets/uploads/topics/downloading-apps.jpg"
date: "Jul 31, 2026"
mins: "3"
excerpt: "Every time you try to update iOS, it fails — stuck on 'Update Requested', an error mid-install, or 'Unable to Install Update'."
---

Every time you try to update iOS, it fails — stuck on "Update Requested", an error mid-install, or "Unable to Install Update". Updates fail for boring reasons most of the time: not enough free space, weak WiFi, low battery. When the phone's own update method keeps failing, the computer method almost always succeeds.

## The pre-flight checks (the boring three)

1. **Free space:** Settings → General → iPhone Storage — updates need several GB free, more than the download size itself. Freeing space fixes a surprising share of "update failed" cases outright.
2. **Wi-Fi:** updates refuse mobile data by design, and weak Wi-Fi produces the endless "Update Requested". Test the Wi-Fi with a video; move closer to the router for the update attempt.
3. **Battery/plug:** below 50% or off-charger, iOS postpones or refuses. Plug in, then retry: Settings → General → Software Update.

## The fixes in sequence

4. **Delete the downloaded update and re-download:** Settings → General → iPhone Storage → find the iOS update in the list → Delete Update. A corrupted partial download retries forever; removing it forces a fresh one.
5. **Force restart, then retry** — volume up, volume down, hold side button. Clears stuck update states.
6. **Update from a computer — the reliable path.** Connect to a PC/Mac with iTunes (or Finder on newer Macs) → click the phone → "Check for Update" → Download and Update. The computer route bypasses the phone's over-the-air machinery entirely and succeeds where the phone method loops. This is THE fix for repeatedly failing updates.

## One caution

If the phone is stuck mid-install (Apple logo for over an hour), do not keep restarting blindly — connect it to the computer and let recovery mode offer "Update" (keeps data) before any "Restore" (erases). Update first, restore only as the last resort.

((ad))
