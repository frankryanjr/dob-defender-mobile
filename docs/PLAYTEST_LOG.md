# Dob Defender — Playtest log

Every player report that led to a change, the decision taken, and the result. Newest first. Record each report here before building the next candidate. Results marked "tested" come from the user's own play, on the device stated. Anything else is untested.

## 7 November 2026: Alpha2.81 production release
- **Report:** "I tested the latest release and it's good."
- **Result:** Alpha2.81 accepted by the user. Device not stated.

## 7 November 2026: Test 26 (released as Alpha2.81)
- **Report:** cows are too hard to hit, and a cow hit in the air splatted on the ground.
  - **Decision:** lifted cows get a wider hit area (18 px). Standing cows no longer block a beam that also crosses a lifted cow. A laser kill on a lifted cow now bursts red in the air.
  - **Result:** "Plays well now." (user, device not stated)
- **Report:** the grumble is too slow.
  - **Decision:** shortened to about 0.6 s, then about 0.4 s.
  - **Result:** user asked for faster again. Current timing is about 0.4 s.
- **Report:** a second, slightly faster grumble, alternating between aliens.
  - **Decision:** two alternating voices.
  - **Result:** built. Not yet confirmed on device.
- **Report:** dramatic explosion for the mothership.
  - **Decision:** flash, expanding rings, staggered bursts, sounds, and ground shake on defeat.
  - **Result:** built and checked in headless Chrome. Not yet confirmed on device.

## 6 November 2026: Test 25 and earlier
- **Report:** the ISS message needs a typewriter sound. The user could not hear it at first.
  - **Decision:** a computer-style keystroke sound.
  - **Result:** user-reported as working after later adjustment.
- **Report:** the grumble could not be heard.
  - **Decision:** rewritten as voiced pulses with a low-pass filter and mid boost, so phone speakers play it.
  - **Result:** user reported it audible in a later build.
- **Report:** the tally says "Mothership defeated" even when it escaped.
  - **Decision:** show "DEFEATED" only when destroyed, otherwise "DAMAGED".
  - **Result:** user-reported as working.
- **Report:** the shield came back to red after a cow was saved while it was down.
  - **Decision:** a downed dome stays down after a save.
  - **Result:** user-reported as working.

## Open reports
- **Tap to fire on phone** did not work for the user in an earlier test. The likely cause is that firing is blocked during dusk, but this is not confirmed.
- **Blink:** the user asked for random blinking, and reported in a test that they could not see it. Later builds added blinking. Not yet confirmed on device.
- **Shake timing:** the user asked for the shake to happen only when the cow lands. Which shake was meant (fist or grumble) was not confirmed.
- **Difficulty** across boss nights: the user wants bosses to get harder as the game goes on. Not yet specified.
