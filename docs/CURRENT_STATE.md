## Checkpoint — boss test published (31 October 2026)

- Published: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html`, git blob `a35d1897ecb9713aeca9e7a0702ec7fdcbc6c65e`, 3,792,550 bytes. Same blob on `origin/dev` and `origin/main`.
- Production `main:index.html` unchanged, blob `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`.
- Actions: JavaScript syntax check and pages build succeeded for both commits.
- User-reported confirmation (31 October 2026): live public test URL loads and runs; boss test works on Android. Not independently re-checked by the assistant.
- Still open: balance and feedback for Test 2 (shield node hits, reactor orbit, orb pressure). Test scores go to the live worldwide leaderboard.
- Next action: collect balance feedback for Test 2 on `dev`. Do not promote to production.

# Dob Defender — Current State
Updated: 31 October 2026. **Status is a committed documentation checkpoint, not a new game release.**

## Authority and startup
- GitHub repository: https://github.com/frankryanjr/dob-defender-mobile
- **Read the root README and the entire [WORKFLOW.md](WORKFLOW.md) first.** Complete all mandatory WORKFLOW onboarding, including inspection of handover, specs/history and production/archive verification. This summary does not replace those requirements.
- For blockers, follow WORKFLOW §2A and consult proven recovery procedures **before** declaring failure or asking the user to transfer files.
- This file is a short restart pointer. Current verified repository evidence takes precedence over this snapshot.

## Approved production
- Latest documented approved production: **Alpha2.80**.
- `main:index.html`: Git blob SHA `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`, 3,784,184 bytes; production commit `9df9a4085e18872de3d6721af8299d54644f51e7`.
- Approved immutable release: `releases/Dob_Defender_Alpha2.80.html`, Git blob SHA `1a4c399c361466c384f23767bedc11719cd37895`.
- GitHub Actions Pages/syntax workflows reported success on 26 October. On 31 October user confirmed Android production playback, Pages version and itch.io update; independent fresh live HTTP and exact itch.io upload SHA were not established in that confirmation.
- **No new production release is approved.** Do not edit production or release artifacts without explicit approval and WORKFLOW release gates.

## Active development — Night 3 Mothership Boss Test 1
- Source: [top of HANDOVER.md](HANDOVER.md) (31 October 2026).
- Candidate: `Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html`, **local/hosted-preview only**, not in GitHub; 3,792,550 bytes; Git blob SHA `a35d1897ecb9713aeca9e7a0702ec7fdcbc6c65e`. A private claude.ai artifact preview is not byte-identical to standalone HTML and mocks leaderboard requests.
- Night 3 boss appears after scheduled threats. Two 5-hit shield nodes, then moving/orbiting front-arc reactor (6 hits); shootable plasma orbs. Balance values are placeholders, **not approved**. All unrelated approved artwork and controls are preserved.
- Verified in Claude environment: direct anonymous `git clone` retrieved exact Alpha2.80 production/archive and `git hash-object` matched; modular split/check passed (9 blocks, 46 assets); four JS scripts passed syntax; headless Chrome 390×844 with mocked backend exercised boss defeat→dawn and orb damage→game over, with no page errors.
- **Not verified:** Android device boss gameplay/balance, live leaderboard, other-night regressions and audio cues. README says Android preview works, but HANDOVER explicitly has no completed Android gameplay test report. Treat player assessment as pending.
- Direct `git clone` is proven **in Claude's container only**. Any new environment must separately verify its access and Git blob SHA. The documented lossless alternative remains available.

## Development branch / test deployment checkpoint (31 October 2026)
- Created branch `dev` from `main`; no boss test has been uploaded.
- The locked WORKFLOW now provides standing authorisation for isolated test-only publishing, not production publishing. `dev:docs/TEST_DEPLOYMENT.md` contains safe deployment requirements.
- **Publishing blocker:** actual GitHub Pages source and existing Actions workflow configuration have not been inspected; a direct dev-branch Pages switch could replace production. Test landing page now committed at `main:tests/index.html` (commit `e58e875cb4e0f20e982351da02b8b50fe89e7117`), but live Pages serving and automated deployment are unverified. Exact boss Test 1 is not in GitHub.
- **First unverified next action:** independently verify Pages serves `/tests/` and inspect Actions/Pages setup before enabling automation. Then recover exact boss Test 1 or generate a new SHA-verified test candidate and publish as a standalone HTML.

## Prior gameplay feedback task (after setup)
**Get user Android gameplay feedback on the Night 3 boss Test 1** (dev panel → Night 3): boss size, node/reactor hit difficulty, orb pressure and any clipping. The private preview does not submit scores. Then plan a scoped Test 2 and deliver a complete standalone downloadable HTML. If the exact candidate is unavailable in a new environment, recover it by an authorised route or rebuild from newly SHA-verified GitHub Alpha2.80, clearly marking it a new unverified candidate. Do **not** imply the uncommitted Test 1 is in GitHub. Do not publish any test or production game without the separate approvals required by WORKFLOW.

## Handover discipline
- At each meaningful development milestone, update this compact state and the detailed [HANDOVER.md](HANDOVER.md) on GitHub with observed evidence, open checks, identifiers and **one** next step; keep the README pointer accurate.
- The full [GAMEPLAY.md](GAMEPLAY.md), [CHANGELOG.md](CHANGELOG.md), [DEVELOPMENT.md](DEVELOPMENT.md), [PROJECT_HISTORY.md](PROJECT_HISTORY.md), [EFFICIENCY_HANDOVER.md](EFFICIENCY_HANDOVER.md) and [MODULAR_WORKSPACE.md](MODULAR_WORKSPACE.md) remain intact and authoritative for their respective scope.
- Avoid placing large HTML, embedded media or complete historical documentation in conversation output. Do not interpret reduced context use as proof that the conversation-length issue is fixed.

## Checkpoint: Mothership Boss Test 5 published under tests/ (31 October 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_5.html`, git blob `cc53d099c7f944e5eb84b2aa774a904a6f58cd0c`, 3,800,501 bytes.
- Source committed to `dev` (`82c4f9b`); test copy published to `main:tests/` (`6c29770`) with the landing-page card on top. Test 4 tagged PREVIOUS TEST.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.
- Headless Chrome checks: shooting run (900 points, no errors); out-of-laser run (scouts take cows, leave, bomb, `destroyed`); ISS radio-wave arcs visible during the ISS pass.
- Not yet verified: independent live fetch of the GitHub Pages URL (sandbox blocks github.io); Android playtest.
- Remaining player tests: Android feedback on Test 5 (saucer shape, glow-line shield pulse, generator hits, radio wave, scout exit and bomb).
- Design notes to confirm: laser passes through the shield line (generators stay hittable); a hit only pulses the line; a dome destroyed earlier stays down at boss arrival.

## Checkpoint: Mothership Boss Test 6 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_6.html`, git blob `5c9205ee5ac81b96fc307b0a2d153c46f196e835`, 3,795,964 bytes.
- Source committed to `dev`; test copy published to `main:tests/` with the landing-page card on top. Test 5 tagged PREVIOUS TEST.
- Changes: no mothership shield or generators; health bar (24 hits, placeholder); laser full for the whole fight (ISS recharge); four scouts take cows with randomised, non-overlapping lifts; mega bomb removed.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.
- Headless Chrome checks: shooting run (boss destroyed, 1,080 points, no errors); no-shoot run (three cows lifted, max one beam at a time, energy full, no errors); health bar visible.
- Not yet verified: live Pages fetch (sandbox blocks github.io); Android playtest.
- Open design questions for the player: what ends the fight if the scouts take all cows (current: the fight continues until the mothership is shot down); whether the mothership should keep dropping plasma orbs.

## Checkpoint: Mothership Boss Test 7 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_7.html`, git blob `96984408c1c6956e1a0aee60783bdb59338b118f`, 3796839 bytes.
- Source committed to `dev`; test copy published to `main:tests/` with the landing-page card on top. Test 6 tagged PREVIOUS TEST.
- Changes: orb hit on the dome sets laser to zero; orbs stop while laser is empty; shot-down scouts are replaced while unclaimed cows outnumber scouts in play; the mothership leaves once all cows are taken (no destruction bonus); no infinite laser.
- Headless checks: no-fire run (orb drains laser, four cows lifted one at a time, mothership leaves, no errors); scouts-only run (scouts replaced after kills, four cows lifted, no errors); shooting run (mothership destroyed, bonus awarded).
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.
- Not yet verified: live Pages fetch (sandbox blocks github.io); Android playtest.
- Open placeholder values: 24 mothership hits; 20 points per hit; 500 kill bonus; laser drain of 100% per orb hit (interpreted as "one orb hit depletes the laser to zero").

## Checkpoint: Mothership Boss Test 8 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_8.html`, git blob `2de4f3dbb941b10fadf5d1e08c7b6fcdfe46a281`, 3797107 bytes.
- Playtest feedback on Test 7: spamming the laser killed the mothership and the scouts in seconds. The laser has no fire-rate limit.
- Changes: mothership health 24 to 40 hits; heals 2 HP per second after 4 seconds without a hit. Scouts unchanged.
- Headless spam check: mothership destroyed in about 4 seconds with the laser ending at zero. Spam still wins, but it costs most of the laser bar.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.
- Open options for the next round: ISS passes again to refill the laser; scouts need two hits; a fire-rate limit on the laser.

## Checkpoint: Mothership Boss Test 9 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_9.html`, git blob `1f96be460a2edc69a0167d7128b464285965868b`, 3798008 bytes.
- Playtest feedback on Test 8: scouts should never be still except while abducting; the mothership should fire more and drop lower occasionally.
- Changes: scouts wander while waiting and tilt with sideways motion; orbs every 3.2 s (up to 14); mothership drops about 0.6 hull every 9 to 13 s, capped above the dome.
- Headless checks: no-fire run (lifts spaced, mothership leaves, no errors); probe (scouts tilt and move, mothership descends); shooting run (no errors).
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 10 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_10.html`, git blob `9b6cd3d9d5461ae18db277b081c79e7212561fcb`, 3798865 bytes.
- Playtest feedback on Test 9: UFOs too slow; laser ran out too quickly; threats bunched; mothership too steady.
- Changes: scouts have random speed changes and roam targets away from each other; orbs have random speed and interval; mothership sway speed changes at random; an orb hit drains 30 laser (was all of it).
- Headless checks: no-fire run (no errors, lifts spaced); probe (scouts spread and move, mothership sway varies).
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 11 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_11.html`, git blob `9b0122078ce0bf703b3c131d9cb681eaf10f1e01`, 3798662 bytes.
- Playtest feedback on Test 10: the mothership should not replenish shield health; there was not enough laser to destroy the mothership and threats with a margin.
- Changes: no mothership healing; 30 hits to destroy; laser costs 1.5 per shot in the boss fight (was 2); an orb hit drains 20 laser (was 30).
- Headless check: spam run kills the mothership with 33 laser left, no errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 12 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_12.html`, git blob `fa508e03ff0202711b7cbb0d4fcd425d277235ab`, 3798854 bytes.
- Playtest feedback on Test 11: spam fire still destroys the mothership easily; the first shots after the 3-2-1 countdown do nothing to the mothership.
- Changes: 220 ms gap between laser shots during the boss fight; laser hits register while the mothership is still entering.
- Headless check: spam run takes about 12 s to destroy the mothership with 33 laser left, no errors. The early-hit fix is not exercised by the harness.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 13 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_13.html`, git blob `a69b5c7b25bdf3abdeba437be7f57fe926e919e4`, 3798921 bytes.
- Playtest feedback on Test 12: laser runs out halfway through the mothership fight; the last scout freezes after the fourth cow is taken and the mothership leaves.
- Changes: laser costs 1.0 per shot in the boss fight (was 1.5); an orb hit drains 12 laser (was 20); scouts keep updating during the leave state, and the mothership is removed only after no scouts remain.
- Headless checks: spam run ends with 45 laser left, no errors; probe shows the last scout exiting before the mothership is removed.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 14 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_14.html`, git blob `5adffba60200d8ebf8a384398461311a04b0e0cf`, 3799952 bytes.
- Playtest feedback on Test 13: playable, but still too easy; asked for scouts to dodge some laser fire and for the mothership to get more aggressive under half health.
- Changes: half of laser shots on scouts are dodged; at 50% health the mothership enters an enraged state and dives fast, zips left and right, then climbs back, every 5 to 7 seconds.
- Headless check: shooting run reaches 50% health, dies with 1 laser left, no errors. The dive and zip are not separately checked.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 15 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_15.html`, git blob `92b98fc844eac157257ae3f00149c55b23af0862`, 3799427 bytes.
- Playtest feedback on Test 14: the enraged dive-and-zip does not work and is removed; a scout occasionally shakes or vibrates when about to abduct a cow.
- Changes: enraged dive removed; scout hover over a cow is now steady (the scout no longer alternates between pulling in and hovering out each frame). Scout dodge kept.
- Headless checks: scouts-only run completes with no errors; no-fire run ends with the dome destroyed, as expected when nothing shoots the orbs. The steady hover is confirmed by code only, not by visual check.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 16 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_16.html`, git blob `9f30cbf123f2bfa5ee56df411be6880c19804af9`, 3799668 bytes.
- Playtest request: at 10% mothership health, the mothership should dodge half of the laser fire.
- Changes: at 10% health or below (3 of 30 hits), half of laser shots that reach the mothership are dodged, with a "DODGE" label. Scout dodge kept.
- Headless check: shooting run destroys the mothership with 28 laser left, no errors. The dodge is not separately exercised by the harness.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 17 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_17.html`, git blob `9a617cb953e3aca6c65dfa858c9acf3344b0b0e9`, 3799581 bytes.
- Playtest request: do not show the word dodge in the game.
- Changes: removed the on-screen "DODGE" label for both scout and mothership deflections. Mechanics unchanged.
- Headless check: shooting run finishes with 23 laser left, no errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 18 published under tests/ (1 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_18.html`, git blob `3ca92c4c5df1b72ea52d583074c32aa60e56300a`, 3799347 bytes.
- Playtest feedback on Test 17: some UFOs took several hits to die; each scout should die from one hit.
- Changes: removed the scout deflection, so one hit kills a scout. Mothership 10% deflection kept.
- Headless checks: scouts-only run completes with no errors; the scout deflection path is removed from the code.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 19 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_19.html`, git blob `8ff43206c5fad30e499303dfad0dfce9a2c56559`, 3799423 bytes.
- Playtest feedback on Test 18: when an orb hits the telescope, laser should empty fully and stop firing, and the UFOs should be free to take cows.
- Changes: during the mothership fight, an orb that reaches the telescope sets laser to zero and the game continues. Previously the telescope hit called destroyScope, which ended the game.
- Headless check: nofire run continues with no errors after the dome is drained. The telescope-hit path is confirmed by code only.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 20 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_20.html`, git blob `5b31812f90aeefbca0db5325295454f02d0f6b82`, 3799565 bytes.
- Playtest request: once the laser drains, the UFOs should go straight to abducting with no waiting.
- Changes: with laser at zero, scouts skip waits, choose cows immediately, dive faster, and lift after a shorter gap (2.3 to 2.8 s, still no overlapping lifts).
- Headless check: laser forced to zero at fight start; lifts begin about 3.5 s later, all four cows taken by about 28 s, one lift at a time, no errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 21 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_21.html`, git blob `f6b801d27ee4e86cd66d706225018e16f6908578`, 3800058 bytes.
- Playtest request: a second ISS pass during the boss fight, once laser falls to about 10%; the player shoots the ISS to refill some laser.
- Changes: when laser is 10% or below during the fight, one ISS pass starts with a transmission. Refill uses the existing ISS hit (+40), not an automatic refill.
- Observation from playtest: after the dome shield is destroyed, orbs that reach the telescope empty the laser, so the mothership stops firing orbs (by the laser-zero rule). Not changed in this test.
- Headless checks: ISS pass spawns at low laser; the harness did not record a clean ISS hit, so the refill is confirmed by code only. No errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 22 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_22.html`, git blob `0fae55d7c2b1e1abb84a168a179f22f006638b9d`, 3799988 bytes.
- Playtest clarification: the second ISS pass (at about 10% laser) gives no free energy; the player shoots the ISS as on a normal night.
- Changes: a brief "SHOOT ISS FOR LASER ENERGY" label replaces the transmission box on the second pass.
- Headless check: ISS test run completes with no errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 23 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_23.html`, git blob `a1c27cd1a963720ad85180f282000b22582234f6`, 3800143 bytes.
- Playtest request: when the mothership reaches 10% health, ramp up the orbs.
- Changes: at 10% health or below, orbs come at about 1.4 s gaps (was 3.2 s), and the orb cap rises by 10.
- Note: the ramp was in the working copy but not in the published Test 22; Test 23 is the first published build with it.
- Headless check: shooting run shows the orb count rising about one per second once health is at 3 or below. No errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 24 published under tests/ (2 November 2026)

- Candidate: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_24.html`, git blob `a25aa10791c52cd399306a64e2743f3916b4b1c6`, 3800212 bytes.
- Playtest request: remove the title screen from production. Tested first as a candidate, not promoted.
- Changes: the start splash (`#ddApprovedStartV1`) is hidden. New players go straight to the callsign prompt; returning players go straight into the night. The Worldwide Nights button on the splash is no longer shown.
- Headless check: harness run (shoot mode) reaches the boss, the boss dies, the dawn tally shows, no page errors.
- Not yet checked: returning-player start on a device with a saved callsign; Android playtest.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.

## Checkpoint: Mothership Boss Test 24 revised (2 November 2026)

- Playtest: the old start overlay ("DOB DEFENDER / DEFEND!") flashed for a moment before the game started. It is in production too.
- Change: the play overlay is hidden from the first paint, so it no longer flashes. Test 24 file replaced, git blob `c3e126309db855e15149117d0b370ee6797a6ba5`, 3800261 bytes.
- Headless check: overlay hidden from first paint, callsign prompt shows for new players, shooting run reaches the boss kill with no errors.
- Production `main:index.html` (`3a0b8ce5…`) and `releases/Dob_Defender_Alpha2.80.html` (`1a4c399c…`) unchanged.
