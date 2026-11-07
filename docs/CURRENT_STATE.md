# Dob Defender — Current State

**Updated:** 7 November 2026. This is the restart pointer for any new chat or AI. The full checkpoint history from October and early November is preserved in `docs/archive/CURRENT_STATE_2026-11-07.md`.

## Read these first, in this order
1. `README.md`: project entry point and the mandatory blocker-recovery rule.
2. `docs/WORKFLOW.md`: the authoritative development, testing, approval and release process. Section 4 is the approval rule.
3. This file: where things stand now.
4. `docs/PLAYTEST_LOG.md`: what the player reported and what changed because of it.
5. `docs/GAMEPLAY.md` and `docs/BOSS_MOTHERSHIP.md`: the game design and the boss-fight design.
6. `docs/CHANGELOG.md`: what each production release contains.

## Production (live)
- **Version:** Alpha2.81, released 7 November 2026.
- **Production file:** `main:index.html`, Git blob `09068f9fc7ede5118f5c74f1af94c6713446b268`.
- **Production archive:** `releases/Dob_Defender_Alpha2.81.html`.
- **Approved test archive it was derived from:** `releases/Dob_Defender_Alpha2.80_Mothership_Boss_Test_26.html`, Git blob `398334335c90e4062141445ff6eaf3ebfdd955bb`.
- **Live web play link:** https://frankryanjr.github.io/dob-defender-mobile/
- **itch.io:** https://stargazerman.itch.io/dob-defender. This is a separate manual upload. It has **not** been confirmed as updated to Alpha2.81.
- **Player status:** the user tested the Alpha2.81 release on 7 November and reported it as good.

## What production contains
- **Night 3:** mothership boss with UFO scouts and plasma orbs (in production since 5 November).
- **Night 6:** alien boss. Aliens lift cows on tractor beams that a single laser hit can break. Lifted cows are easier to hit, and a laser kill in the air shows a red burst. Defeating the mothership triggers an explosion.
- **Other:** callsign entry for new players, spacebar fires on PC, touch tap fires on phones, typewriter sound on ISS messages.
- Boss nights follow the schedule in `BOSS_MOTHERSHIP.md`: every third night from Night 3. Nights 9 and 12 are not built.

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

## Open items
- **Source is not in GitHub.** The game's build sources and test scripts are in the assistant's working environment, not in this repo. A new AI can edit the standalone HTML directly, but cannot regenerate it from source. **Decision needed:** should the source blocks and build script be committed to a `source/` folder on `dev`?
- **`tests/index.html` still lists Test 26 as UNAPPROVED.** Update it when the next test is published.
- **itch.io:** not confirmed as updated to Alpha2.81. Needs explicit approval before any upload.
- **Docs not yet updated for November work:** `PROJECT_HISTORY.md`, `DEVELOPMENT.md` and `HANDOVER.md` still stop in late October.
- **Difficulty progression across nights** is not specified or verified. The user wants bosses to get harder as the game goes on.
- **Android device testing** of the grumble timing and the explosion volume is still pending from the user.
