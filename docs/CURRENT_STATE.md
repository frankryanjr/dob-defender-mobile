# Dob Defender — Current State

**Updated:** 11 November 2026 (Alpha2.83 released). This is the restart pointer for any new chat or AI. The full checkpoint history from October and early November is preserved in `docs/archive/CURRENT_STATE_2026-11-07.md`.

## Read these first, in this order
1. `README.md`: project entry point and the mandatory blocker-recovery rule.
2. `docs/WORKFLOW.md`: the authoritative development, testing, approval and release process. Section 4 is the approval rule.
3. This file: where things stand now.
4. `docs/PLAYTEST_LOG.md`: what the player reported and what changed because of it.
5. `docs/GAMEPLAY.md` and `docs/BOSS_MOTHERSHIP.md`: the game design and the boss-fight design.
5a. `docs/MODULAR_BUILD_HANDOFF.md`: how to split the game HTML into editable pieces and rebuild it. Read this before any code change.
6. `docs/CHANGELOG.md`: what each production release contains.

## Production (live)
- **Version:** Alpha2.83, released 11 November 2026.
- **Production file:** `main:index.html`, Git blob `e66a8aa9102294e0f9e26a64a31fda141b90eb60`.
- **Production archive:** `releases/Dob_Defender_Alpha2.83.html`. Previous production: `releases/Dob_Defender_Alpha2.82.html`.
- **Approved test archive it was derived from:** `releases/Dob_Defender_Alpha2.82_Claw_Boss_Test_46.html`, Git blob `1d103f7ee7f9bdb1e25a68fa265dc71853cb4b83`.
- **Live web play link:** https://frankryanjr.github.io/dob-defender-mobile/
- **itch.io:** https://stargazerman.itch.io/dob-defender. Updated to Alpha2.82 on 7 November 2026 at the user's explicit request. Public embedded game loaded and displayed Alpha2.82. Independently retrieved served HTML matches the approved 3,817,622-byte production file (blob `b7bf1fd3d0a0e5e42df039ffab1468763018a06f`) plus only itch.io's standard 87-byte hosting script. Alpha2.80 and Alpha2.81 remain separate downloads. Android gameplay of the updated itch.io build awaits confirmation.
- **Player status:** the user tested Alpha2.81 and reported it as good. Test 27 (late-stage orb reduction) was approved and released as Alpha2.82 on 7 November. He said he was happy with the Night 9 fight (Test 46) and approved release as Alpha2.83 on 11 November.

## What production contains
- **Night 9:** claw boss (released in Alpha2.83). See the section below for how it works.
- **Night 3:** mothership boss with UFO scouts and plasma orbs (in production since 5 November).
- **Night 6:** alien boss. Aliens lift cows on tractor beams that a single laser hit can break. Lifted cows are easier to hit, and a laser kill in the air shows a red burst. Defeating the mothership triggers an explosion.
- **Other:** callsign entry for new players, spacebar fires on PC, touch tap fires on phones, typewriter sound on ISS messages.
- Boss nights follow the schedule in `BOSS_MOTHERSHIP.md`: every third night from Night 3. Night 9 (claw) is built (Alpha2.83); Night 12 is not.

## How development works (summary; WORKFLOW.md is authoritative)
1. **Request.** The user describes a change or reports a playtest result. Record the feedback in `docs/PLAYTEST_LOG.md`.
2. **Build a candidate.** Make the change as one complete standalone HTML file with a unique test name. Check that every inline script passes `node --check`, and run a smoke test in headless Chrome at 390×844 with no page errors.
3. **Publish a test (unapproved).** Commit the exact tested file to `tests/` on `main` and `dev`, label it **UNAPPROVED / TEST BUILD**, and give the user a link with a new `?v=` number. Never publish to `index.html` at this stage.
4. **Playtest.** The user plays on Android and PC and reports back. Repeat steps 1–4 until the user is happy.
5. **Production, only on explicit approval.** The user must say so in plain words, such as "push to prod". Then:
   - Archive the exact tested file as `releases/Dob_Defender_AlphaX.Y_...html`, keeping its test labels.
   - Derive production from that archive, changing only the version label and removing test labels. Check the diff: it must contain only those label lines.
   - Verify the production blob SHA, update `index.html`, and push to `main`.
   - Update `CHANGELOG.md`, `README.md`, and this file.
   - Confirm the GitHub Actions "pages build and deployment" run succeeded. Then check the live page. Do not claim success before both checks pass.
6. **Ask for Android confirmation** after release. Syntax checks and headless tests are not device tests.

## Night 9 claw boss (released in Alpha2.83)
- **Released from:** Test 46 (`tests/Dob_Defender_Alpha2.82_Claw_Boss_Test_46.html`, archived under `releases/`). Tests 33 to 46 are listed in `tests/index.html` and described in `docs/PLAYTEST_LOG.md`. Tests 42 and 43 (dodging in every phase) were rejected as too erratic; Test 44 reverted to Test 41's behaviour.
- **What it does:** a claw on a swinging cable grabs cows. Hit the claw 3 times to destroy it. The ship dodges laser fire between drops, keeps trying until it is destroyed or no cow is left, fires 1, 2, 3 then 4 orbs on grabs 1 to 4 (and 4 after) while lowering and grabbing, and calls an ISS when the laser is low (Test 46 fix).
- **Player status (11 November 2026):** the user said he is happy with the Night 9 boss fight (Test 46 build). This is not production approval.
- **Released:** the user said "Push to prod" on 11 November 2026 and Alpha2.83 was derived from Test 46 with label-only changes.
- **Playtest results never reported:** Tests 28, 29, 31 and 32, and detailed results for 33 to 46.
- **Dawn particle bug:** frozen explosion particles in the dawn after a boss is destroyed were fixed in Test 38 and are in Alpha2.83 for all boss nights. The user has not yet confirmed Nights 3 and 6 on device.
- **Not decided:** a time limit for the claw fight (nothing ends it except destroying the ship or losing all cows); what grabs 5 and later fire (currently 4 orbs).
- **Build source:** the modular workspace and test scripts are in the assistant's session environment, not in this repo (see Open items).

## Open items
- **Source is not in GitHub.** The game's build sources and test scripts are in the assistant's working environment, not in this repo. A new AI can edit the standalone HTML directly, but cannot regenerate it from source. **Decision needed:** should the source blocks and build script be committed to a `source/` folder on `dev`?
- **itch.io:** still Alpha2.82; Alpha2.83 is not uploaded (separate step, only on request). Alpha2.82 browser upload and public version verified on 7 November. Android gameplay still awaits user confirmation; older uploads remain separate downloads.
- **Docs not yet updated for November work:** `PROJECT_HISTORY.md`, `DEVELOPMENT.md` and `HANDOVER.md` still stop in late October.
- **Difficulty progression across nights** is not specified or verified. The user wants bosses to get harder as the game goes on.
- **Android device testing** of the grumble timing and the explosion volume is still pending from the user.
