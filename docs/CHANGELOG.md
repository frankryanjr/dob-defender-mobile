## Alpha2.74 — 23 October 2026 — approved Sound Test 5

- **Approved candidate:** `Dob_Defender_Alpha2.73_Sound_Test_5.html`; user explicitly requested production.
- **Added:** Three self-contained edited WAV sound effects: laser firing, comet destruction, ground impact.
- **Removed:** Meteor destruction and asteroid destruction sound effects (visual/gameplay effects retained).
- **Preserved:** Alpha2.73 gameplay, approved telescope/start-screen artwork, controls, scoring, aircraft warnings, leaderboard and night progression.
- **Archive:** `releases/Dob_Defender_Alpha2.74.html` (exact approved candidate, blob `e008527ad54663e5b0e063b19653e93450e5f297`).
- **Production:** `main:index.html` (commit `585712ed4981752f68dd88cab4f2997389647654`, blob `e59a59f3a30881d8466a71f0e336eb4a6a459654`). Only version/title labels changed to `Alpha2.74`.
- **Validation:** User approved candidate; independent assistant Android and live Pages checks pending.

## Alpha2.73 — 19 October 2026 — approved Test 6

- **User production approval:** “Push to prod” for Alpha2.73 Test 6 after Android screenshot feedback and the final full-width CONTINUE button change. Android visual testing of the prior warning layout was demonstrated; independent device confirmation of Test 6 and live production remains pending.
- **Immutable exact tested archive:** `releases/Dob_Defender_Alpha2.73.html`, Git blob `fadb44348f49a26bd0a38574e866a32f6487c044`. **Production source:** `main:index.html`, release commit `9bb678fce01fba069b2746f578eff09b2b6e306e`, blob `5dc1679fa33bcc66326215385e0d49c2f0ff4d15`.
- **Difficulty:** Increased scheduled threat counts in early/mid nights (Night 1 unchanged), increased multi-object grouping earlier and modestly raised early object speeds, while maintaining later progression. Night 8 target is 36 scheduled threats. These are the approved Test 1 changes.
- **Power-ups:** Guaranteed opportunity on Night 3; 70% opportunity chance on each subsequent night, versus the prior 1/3 chance from Night 3. Power-up still requires player action to collect.
- **Laser energy:** Shots cost 2% Nights 1–5, 1.65% Nights 6–10 (about 60 full-energy shots), 1.85% Nights 11–12, 2% Night 13 onward. Rebalances the increased threats without relying on an ISS recharge.
- **End-of-night tally:** Shortened per-category score animation and score flight; cumulative total begins counting immediately when points arrive; red cumulative number while deducting negative score, reverting to white when finished.
- **Aircraft warning:** Replaced small OK button with full-width, rounded, bold green CONTINUE button matching the tally Continue control.
- **Preserved:** Alpha2.72 Game Over final score layout, unified version source, telescope artwork, Start Screen v1, mobile controls, leaderboard and other approved gameplay.
- **Version-label-only production differences from exact archive:** `<title>Dob Defender Alpha2.73 Test 6</title>` → `<title>Dob Defender Alpha2.73</title>`; `const DD_GAME_VERSION='Alpha2.73 Test 6';` → `const DD_GAME_VERSION='Alpha2.73';`. No other intentional code changes.
- **Testing:** Test 6 JavaScript syntax checked; independent live Pages retrieval, GitHub Actions completion and user production Android confirmation to be recorded separately.
- **Production play link:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.73

## Alpha2.72 — 19 October 2026 — approved Test 3

- Approved by user request “Ok. Push it” after Alpha2.72 Test 3 was delivered; independent Android test of Test 3 was not separately confirmed.
- Immutable exact approved test archive: `releases/Dob_Defender_Alpha2.72.html` (Git blob `d062d45e236fa0852fe27a889c9a62fc07851026`). Production source: `main:index.html` (commit `71b55a85f6e8eaaafba55927245b3800358c7fda`, blob `8c19ad692d03cc0d1992a083da796d67968828c1`).
- Redesigned final Game Over results: FINAL SCORE heading styled like GAME OVER with numeric final score beneath; COWS RESCUED styled like prior COWS label with rescued count beneath. Removed the previous three-column final-results presentation and observatory-destroyed subtitle from that panel; leaderboard and Play Again retained.
- Unified game version: `DD_GAME_VERSION` is the single source for visible start/game-over version labels, browser title and submitted leaderboard score version. Fixed stale hardcoded Alpha2.69 footer in prior production.
- Production differs from exact Test 3 archive **only** in two label substitutions: `<title>Dob Defender Alpha2.72 Test 3</title>` → `<title>Dob Defender Alpha2.72</title>`; `const DD_GAME_VERSION='Alpha2.72 Test 3';` → `const DD_GAME_VERSION='Alpha2.72';`. No gameplay/artwork changes beyond the approved end-screen presentation.
- Preserved Alpha2.71 leaderboard pagination, Android viewport restart fix, DEV leaderboard button and DEV automatic pause, telescope, artwork and other gameplay. Syntax passed for Test 3; live Pages and Android verification tracked separately.
- Production link: https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.72

## Alpha2.71 — 19 October 2026 — approved Test 6

- Approved candidate: Dob_Defender_Alpha2.71_Test6.html (user requested production after testing Test 5 successfully and receiving Test 6). Exact immutable archive: releases/Dob_Defender_Alpha2.71.html (Git blob 84163c26f7e917309f772382f31252fd0214d602).
- Production root index.html derived from approved Test 6 with exactly two label-only substitutions: HTML title and start-screen visible version changed to Alpha2.71. Production HTML commit: 5d91d203deb2e555711d16378a74f366b385d2b8, blob fdfde6c7090d697b6cd7c49ade5657f7169cf269.
- Corrected submitted leaderboard score version to Alpha2.71; corrected Android bottom-control clipping after View Leaderboard → Play Again (user confirmed Test 3); leaderboard shows 10 ranked scores per page with Previous/Next and page counter; removed Your position message; added View Leaderboard in DEV controls (user confirmed Test 5).
- DEV controls opening pauses an active game; closing DEV leaves game paused until manually resumed; restart/jump starts normally. Test 6 JavaScript syntax was reported passed; independent Android testing of Test 6 not confirmed before production request.
- Preserved approved telescope, start artwork and unaffected gameplay. Production Pages deployment and user production Android verification must be tracked separately.

**19 October 2026 — Alpha2.70 production label correction:** After user reported `Alpha2.70 TEST 8` on the live start screen, production `main:index.html` was corrected to display `Alpha2.70`, and the HTML title was corrected from `Dob Defender Alpha2.70 Test 6` to `Dob Defender Alpha2.70`. Exactly two label substitutions; no gameplay/artwork changes. Original approved archive `releases/Dob_Defender_Alpha2.70.html` remains unchanged (blob `b464c01399c78370c2ecaccba7862cc439069bed`). Production label correction commit `b487dde6d43a0f6b16af3b7fb6640680ae84aa52`, resulting blob `ed078df52a98604992d55d1742df373163334591`. Workflow now mandates clean production labels (commit `88666c695ac529dbc9f87370be7fdadc797916f5`). Live Pages deployment of this correction still requires confirmation.

## Alpha2.70 — 19 October 2026 (approved Test 8)

- Fixed floating hit-score popups freezing at dawn by allowing fade progression through night-end and clearing remaining popups at tally.
- Removed the gameplay HUD leaderboard button; final-results leaderboard access remains.
- Removed the moon from the sky.
- Changed rendering order so cows appear in front of the dome walls.
- Corrected zero-integrity dome animation: stationary outline is erased from apex down curved sides and then vertical walls to ground, with no whole-dome translation, rotation or shrinking. Iterated Tests 4–7; user confirmed Test 8 succeeded on Android.
- Archived exact approved Test 8 HTML at `releases/Dob_Defender_Alpha2.70.html`; root `index.html` has identical Git blob SHA `b464c01399c78370c2ecaccba7862cc439069bed`.
- Production HTML commit `7421e3f23ae138cde4a9cb585b5adc3d2f5ad634`; independent Android test by assistant not performed. Deployment verification recorded separately.
- Approved file intentionally retains Test 8 visible label and an older HTML title "Test 6"; no untested label changes applied.

# Alpha2.69 — Night-end flow, final scores and space junk (18 October 2026)

**Approved candidate:** Alpha2.69 Test 18. **Permanent approved HTML:** `releases/Dob_Defender_Alpha2.69.html`. **Production:** `main:index.html`; production differs from the approved archive only by version-label text. Previous approved version Alpha2.68 remains archived.

### Added
- Night-end animated tally of remaining laser energy, dome integrity, cows saved (+25 each) and cows lost (-25 each); scores roll into one overall total.
- Final Game Over tally before the final score screen.
- Persistent Game Over screen with separate VIEW LEADERBOARD and PLAY AGAIN buttons.
- DEV option to guarantee at least one power-up junk item per night.
- Additional tumbling space-junk types from night 3: rocket stage, Sputnik, damaged ISS and Apollo capsule, cycling and decreasing in size.
- Atmospheric burn-up effect with leading-edge glow, translucency, fragmentation and fading trail.

### Changed and fixed
- Registered scores submit in the background without automatically opening the leaderboard.
- Leaderboard offers PLAY AGAIN; player rank shown when available from returned standings.
- Removed redundant old Night Defended overlay during the new tally flow.
- Removed the extra survival/performance bonus tally row and redundant score explanations.
- Energy HUD low-power warning is intended to respond to genuinely low energy rather than every shot.
- Dome destruction outline retracts from the top towards ground; ground impact shake separated from dawn.
- Preserve dawn cow waking, standing and walking, and approved laser-sight timing, colour and expiry behaviour.

### Validation and limitations
- Exact approved HTML transferred to GitHub and checked against local length/checksum.
- JavaScript and gameplay behaviour still require end-to-end Android confirmation; online leaderboard requires connectivity.
- Release deployment and subsequent Android confirmation are separate checks, not implied by committing HTML.

# Alpha2.68 — Integrated damage and night scoring (18 October 2026)

- Production game: root `index.html`; archived release: `releases/Dob_Defender_Alpha2.68.html`.
- Embedded approved Start Screen v1 JPEG as a data URI for standalone Android HTML use; retained approved telescope and thumb controls.
- Laser Sight rocket-junk pickup, 20-second guide, expiry fade/flicker/retraction, energy-coloured guide and shots.
- Direct dome damage: meteor 20%, asteroid 35%, comet 30%, asteroid partial 15%, split fragment 20%; ground structural damage: 5%, 9%, 8%, 4%, 5% respectively. Dome-only shake and colour-linked outline; no cracks; 1.2-second outline retraction at zero integrity.
- Independent HUD resource warning pulses (25%/10%/0%) and gain/loss flashes. Resource percentages are not score points during play.
- Comet +5, meteor +10, asteroid staged +15/25, split meteor fragments +20 total; compact numeric hit popups.
- Night Complete animated energy/dome/cow/bonus tally and Continue control. Saved cow +25 and lost cow -25 in tally; existing +50 rescue reward remains.
- **Testing:** JavaScript syntax compiled; embedded JPEG decoded (1023 × 1536); full browser execution was blocked by environment, Android/device testing outstanding. GitHub Pages deployment not yet independently verified.
- **Known limitations:** online leaderboard and sky-data functions require connectivity; local HTML gameplay itself uses embedded Start Screen art. Full scoring, collision and animation device tests are pending.

# Alpha2.67 — 15 October 2026

- Global leaderboard now ranks individual game submissions rather than only each player's personal best.
- Same player may appear multiple times, with score, night and game version shown for each result.
- Existing history retained; Supabase Edge Function upgraded to version 3.
- Full game HTML JavaScript syntax compilation checked. Browser end-to-end testing remains pending.

# Alpha2.65 — 15 October 2026

- Fixed incomplete Alpha2.64 HTML upload: restored final game event listener, initialization and closing script tags.
- This repairs inert DEFEND and LEADERBOARD controls caused by JavaScript not executing.
- Full JavaScript syntax compilation verified; Android runtime and Supabase end-to-end behaviour still require device testing.
- Gameplay, artwork and controls otherwise unchanged.

## Alpha2.64 — 15 October 2026

- Added nickname-only registration, remembered on the browser.
- Added global top-50 high-score table with best score per player and night reached.
- Added nickname changes that preserve the player ID and best score.
- Added Supabase database and server-side score submission, rate limiting and nickname uniqueness.
- Browser-side scores cannot be fully verified against tampering. Android gameplay testing pending.

# Changelog

## Alpha2.63 — 14 October 2026

- Updated title screen copy: “Protect your observatory from the Meteorites, Asteroids & Comets”, “Save the cows!”, “Don't shoot the planes”.
- Changed start button to “DEFEND!”.
- Centred version text at the bottom of the start screen.
- Intended as a presentation-only change from Alpha2.62; existing gameplay retained.

## Alpha2.62

- Latest pre-title-screen milestone supplied for this repository.
- Includes DEV tools, mobile aiming controls, astronomical sky data and multi-night gameplay.
- For exact earlier changes see the historical project handover.

## Earlier alpha milestones

- Alpha2.17 is the first retained build and repository baseline. Earlier prototypes are not required.
- Historical builds and detailed change history are maintained in the handover where available.

## Repository initialization — 15 October 2026

- Established versioned source layout, README, documentation and preserved Alpha2.63.
- Repository setup is not a gameplay release.
