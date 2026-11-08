# Dob Defender — Playtest log

Every player report that led to a change, the decision taken, and the result. Newest first. Record each report here before building the next candidate. Results marked "tested" come from the user's own play, on the device stated. Anything else is untested.

## 8 November 2026: Test 34 (unapproved, awaiting playtest)
- **Report (on Test 33):** the cable and claw must not be yellow or flashing.
  - **Decision:** cable, ring, arms, hit pips and hit sparks are plain grey-white. The cable is a steady 3 px line.
- **Report:** at the start of the night the mothership seems to jump to the side.
  - **Cause:** the claw logic set the ship's x position directly, while the old sideways drift had been moving it during the entrance. The two disagreed when the fight began and again after every grab.
  - **Decision:** no drift during the entrance (the ship comes in at the centre), and the sideways sway between grabs is eased from a continuous phase, so it never snaps.
- **Report:** when the mothership leaves it extends the claw again.
  - **Cause:** the claw kept its last lowered position while the ship flew up, so the cable stretched.
  - **Decision:** nothing is drawn once the ship is leaving. After each grab the claw is also reeled back up under the ship before the next one.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome at 390×844 played the full Night 9 sequence with no page errors. Largest ship movement is a smooth glide of about 34 px per 0.1 s toward the next cow. A screenshot as the ship leaves shows no claw. Android feel is untested.
  - **Result:** awaiting playtest.

## 8 November 2026: Test 33 (unapproved, awaiting playtest)
- **Report:** Test 32 link returned a 404 for the user. The file is on main and the filename matches. Not confirmed as fixed. The user was asked to retry without `?v=`.
- **Request (design sketch):** the claw should grab around the cow. Single cable, slightly thicker than in Test 32. The cable is not doubled.
  - **Decision:** hub ring on the cable end with two curved arms. Open is a wide arch. Closed, the arms wrap round the cow's body and are drawn in front of it. Cable width is 3.4 px while winching and 2.8 px otherwise (was 2.2 and 1.6). The cable hit area grew from 9 to 11 px.
- **Request:** on the Night 9 boss the ship should try to abduct all 4 cows before it leaves.
  - **Decision:** the claw takes one cow at a time (nearest standing cow first) and each cow is tried once. A cow saved by three cable hits is not retried. After the fourth attempt, or when no untried cow is left, the ship leaves. A banner shows "COW n OF 4".
  - **Also changed:** the ship's x position is now owned by the claw logic during the fight, so the claw lines up over the cow before closing. The cow no longer swings out of the arms while it is winched. A cow held when the ship is destroyed is released.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome at 390×844 ran the full Night 9 sequence: 4 grabs, one cow saved by 3 cable hits, 3 taken, ship leaves, no page errors. Android feel is untested.
  - **Result:** awaiting playtest.
- **Not yet reported by the user:** results for Tests 28 (shield refill), 29 (cows walk in), 31 and 32 (claw difficulty and feel). Record them here when reported.

## 7 November 2026: Test 27 (released as Alpha2.82)
- **Report:** the first boss fight is a little too hard; reduce the orbs in the later stage.
  - **Decision:** below 25% health, orbs come every 2.1 s (was 1.4) with a cap of 18 in the air (was 24).
  - **Result:** "Yes it works please push to prod." Released as Alpha2.82.

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
