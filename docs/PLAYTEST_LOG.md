# Dob Defender — Playtest log

Every player report that led to a change, the decision taken, and the result. Newest first. Record each report here before building the next candidate. Results marked "tested" come from the user's own play, on the device stated. Anything else is untested.

## 10 November 2026: Test 41 (unapproved, awaiting playtest)
- **Report:** the tether should swing a bit while the claw is lowered, as the same physics applies. Between claw drops the ship should dodge laser fire, moving left and right, and smoothly up and down, fluidly, but avoid going too low where it is easy to hit.
  - **Decision (cable):** the cable bow is now also driven by the ship's sideways acceleration, plus a small living sway while lowering. It is drawing only; the claw is still the only hit area.
  - **Decision (dodging):** in the pause between drops the ship moves by smooth velocity steering. It wanders on two blended sine paths. It predicts where each upward shot will cross its height and pushes away from it, and rises when a shot is close. Its height range is 26 px below normal to at most 48 px above, so it never dives. It heads back to its normal height over the last 0.6 s before a drop. It keeps its sideways speed into the drop instead of stopping, so there is no jump.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome, shots aimed at the ship's current position every 5th frame during the pause: Test 40 was hit by 16 of 31 shots (52%); Test 41 by 2 of 33 (6%). Ship never went more than 5 px below normal height. While lowering the cable bow reached 6.7 px. No page errors. A real player aims and leads shots, so the real hit rate will be higher. Not looked at on a phone screen.
  - **Known:** one frame at the hand-off into the pause has a small vertical speed change (about 2 px).
  - **Result:** awaiting playtest.

## 9 November 2026: Test 40 (unapproved, awaiting playtest)
- **Report:** make the tether grey lines for a metal rod or cable feel; make the circle part of the grabber grey; the cable swings rigidly, so there should be a little extra curve at the top of the swing.
  - **Decision:** the cable is drawn as light grey with diagonal dark-grey strand lines and a thin centre line. The hub is solid metal grey with a small darker centre. The cable bows by a spring that is driven by how fast the swing turns round, so the bow is biggest at the top of each swing, goes outward, and settles back. The bow is capped at 7% of the cable length or 16 px. It is drawing only: the cable is not shot, and the hit area is still the claw.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome run: no page errors, bow up to 13 px in play, canvas crops show the strand lines, grey hub and the bow. Not looked at on a phone screen.
  - **Result:** awaiting playtest.

## 9 November 2026: Test 39 (unapproved, awaiting playtest)
- **Report:** the mothership in the claw fight should keep attempting to abduct until dawn comes or the ship is destroyed. (The last words of the message were garbled; this is my reading.)
  - **Decision:** removed the 4-grab limit and the one-attempt-per-cow rule. After each grab (cow taken, claw destroyed, or cow dropped) the ship goes back to swaying and picks the next cow, preferring the one grabbed fewest times, then the nearest. Saved cows can be targeted again. The banner reads GRAB n. The ship leaves only when no live cow remains (ALL COWS TAKEN) or after 12 s if cows exist but none can be grabbed.
  - **Open point:** there is no dawn timer during a boss fight. Dawn starts only once the boss is gone, so in practice the fight now ends when the ship is destroyed or all cows are taken. A fight time limit is possible if wanted.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome, claw shot every grab: 7 grabs, tries per cow 1,2,2,2, ship still attempting, then destroyed and dawn began. No shooting: 4 grabs, all four cows taken, ship left, dawn began. No page errors. Not looked at on a phone screen.
  - **Result:** awaiting playtest.

## 9 November 2026: Test 38 (unapproved, awaiting playtest)
- **Report:** when the mothership is destroyed, a few of its destruction particles freeze on screen and stay there through the dawn animation. They should fade away even while dawn is happening.
  - **Cause:** the night ends the moment the mothership is gone, so dawn starts while the explosion is still going. The explosion spawns its later bursts from the draw loop (on a wall-clock timer), so they appear after dawn has begun. Dawn mode never updated the particle list, so every one of them stayed where it was spawned. In the reproduction on Test 37, 182 particles stayed frozen through all of dawn and into the tally screen.
  - **Decision:** fading particles are now updated in every mode except night and the observatory-destroyed screen (which has its own update), so dawn, the tally and dusk move and expire them. The end-of-night clear no longer wipes the sparks. They fade out, and only the debris fragments (which never expire) are still dropped there.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome reproduced the freeze on Test 37 (182 particles, none moving). On Test 38 the count falls 195, 122, 57, 8, 3 and reaches zero 2.45 s into dawn, stays at zero through the tally, with no still particles at any sample and no page errors. Not looked at on a phone screen.
  - **Also affects production:** the same bug exists in Alpha2.82 (index.html) on the Night 3 mothership. It is not fixed there. This needs your explicit approval before any production change.
  - **Result:** awaiting playtest.

## 9 November 2026: Test 37 (unapproved, awaiting playtest)
- **Request:** a slight natural swing while the claw is being lowered.
  - **Decision:** the ship's sideways glide over the cow now pushes the cable, plus a small natural sway. The swing is capped at about 6 degrees (0.1 rad) while lowering, fades out in the last 120 px, and the claw only grabs once it is lined up and settled. Measured in the test: 18 to 28 px of sideways swing while lowering, claw within 2 px of the cow at the grab.
- **Report:** when the laser hit the claw the beam kept travelling. It should be absorbed.
  - **Cause:** a claw hit counted the hit but left the shot alive, so it carried on.
  - **Decision:** a laser shot that hits the claw is removed on the spot (the same way the alien beam absorbs shots). It no longer carries on to the ship or elsewhere.
  - **Checks:** `node --check` passed on all 4 inline scripts. A shot fired up at the claw was removed and counted one hit (0 shots left). Headless Chrome at 390×844 played the full Night 9 fight, three claw hits destroyed the claw, the cow landed on screen, no page errors. Android feel is untested.
  - **Result:** awaiting playtest. Please say whether the lowering swing is the right amount.

## 9 November 2026: Test 36 (unapproved, awaiting playtest)
- **Request:** use random pulls for all cows. Smooth sway and the mixed mode are dropped from the DEV panel (one start button again).
  - **Decision:** the ship uses random pulls on every grab. The smooth-sway code is left in the file but is not used.
- **Request:** the player should hit the claw, not the cable. Three hits on the claw destroy it. (The report said "theater"; read as "cable".)
  - **Decision:** the hit area is a circle (radius 26 px) around the claw and the cow it holds. A shot across the cable no longer counts. Each hit shows 1/3, 2/3, then CLAW DESTROYED, and the claw arms get thinner (2.8, 2.1, 1.4 px). The cable stays a steady 3 px. The third hit destroys the claw: the broken claw falls away, the cow keeps part of the sideways motion and lands on screen.
  - **Checks:** `node --check` passed on all 4 inline scripts. Headless Chrome at 390×844 played the full Night 9 fight: a shot straight across the cable did not register, three shots on the claw destroyed it, the cow landed on screen (at the 24 px safe margin when released near the left edge), peak swing 0.5 rad, no page errors. Android feel is untested.
  - **Result:** awaiting playtest. Please say whether the claw is easy enough to hit while it swings, and whether three hits feels right.

## 9 November 2026: Test 35 (unapproved, awaiting playtest)
- **Design discussion (user):** the cable and cow should swing like a pendulum hung from the mothership. Moving the ship left and right makes the claw swing, which is harder to shoot and more realistic. A long cable gives a broad, slow swing. As it is reeled in the swing gets shorter and faster. When the cable is cut the cow keeps some of the motion and lands on screen. It must not drop straight down or be flung off screen.
  - **Decision:** build both ship movement styles and play them side by side.
  - **Physics:** cable length L, swing angle, ship sideways acceleration as the pivot push, reel-in speed in the equation. Gravity 1500 px/s², light damping, widest swing capped at 0.5 rad (about 29 degrees), the claw is kept on screen.
  - **Swing modes (DEV panel buttons):** SMOOTH SWAY (steady side to side, timed near the pendulum's natural period), RANDOM PULLS (irregular left-right pulls), SMOOTH THEN PULLS (smooth on cows 1 and 2, pulls on cows 3 and 4).
- **Request:** hitting the cable should make it thinner and thinner until it snaps.
  - **Decision:** cable width is 3 px, then 2.2 px after hit 1, 1.4 px after hit 2. Hit 3 snaps it ("SNAP!"), the claw falls away and the cable whips back up.
- **Request:** the cow's legs should move while it dangles and while it falls. Done. The cow also tilts with the cable.
- **Release:** the cow keeps about half of the claw's sideways speed (capped), slows with air drag, and is pulled into the safe landing zone so it always lands on screen and clear of the dome gap.
  - **Checks:** `node --check` passed on all 4 inline scripts. A standalone physics test matches the pendulum period 2π√(L/g) within 0.1% at 600, 300 and 100 px. A sideways push on the ship swings the claw the opposite way. Reeling in speeds the swing. The angle cap keeps the claw on screen. Headless Chrome at 390×844 played the full Night 9 fight in both modes: peak swing 0.5 rad, three cable hits thinned and snapped it, the saved cow landed on screen, no page errors. Android feel is untested.
  - **Result:** awaiting playtest. Please say which mode feels best, how hard the swing is to shoot, and whether the swing size is right.

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
