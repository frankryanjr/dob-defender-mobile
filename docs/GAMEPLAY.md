## Alpha2.75 — Callsign and music

First-time players choose a generated or custom 3–18-character callsign; DEFEND! registers and starts Night 1. Returning players with saved identity use the normal start screen. The game uses one continuous looping background music track, `DobDefGame2.mp3`, at 20% volume; autoplay is attempted on load, with a first-tap fallback, and pause/resume follows the game. Gameplay and scoring otherwise remain Alpha2.74.

## Alpha2.74 audio behaviour — 23 October 2026

- Laser firing plays an embedded edited WAV effect.
- Comet destruction plays an embedded edited WAV effect.
- Ground impacts play an embedded edited WAV effect.
- Meteor destruction and asteroid destruction have **no destruction sound**. Existing destruction visuals, collisions, scoring and damage remain unchanged.
- Embedded audio works without separate sound downloads; optional online game features may still require connectivity.

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

## Alpha2.70 current gameplay amendments (19 October 2026)

- In-play leaderboard shortcut at top-right is removed. Leaderboard remains accessible from final results.
- Moon is no longer drawn in the night sky.
- Cows render in front of dome walls.
- Floating hit-score numbers fade during the transition to dawn and are cleared at the tally.
- At zero dome integrity, the stationary dome outline progressively vanishes from the central apex along both curved halves and then the vertical walls down to the ground. The arch does not translate, rotate or shrink.
- User confirmed the corrected dome behaviour in Alpha2.70 Test 8 on Android.

# Alpha2.69 — Current gameplay changes (18 October 2026)

Alpha2.69 preserves Alpha2.68 telescope artwork, thumb aiming, shooting, damage rules, aircraft, cow rescue, power-ups and approved Start Screen v1 except for the changes recorded below.

**Night scoring:** After each completed night, an animated tally awards points based on remaining laser energy and dome integrity and applies +25 for each cow saved and -25 for each cow lost. The existing +50 reward for saving a cow during play remains. The tally contributes to one running overall score; no separate survival/performance bonus row.

**Game Over:** A final tally runs before the final score screen. The Game Over screen remains visible until the player chooses VIEW LEADERBOARD or PLAY AGAIN. Registered players' scores submit in the background without navigating away. Leaderboard includes PLAY AGAIN and can show rank when the returned standings support it.

**Space junk:** From night 3, alternating tumbling rocket-stage, Sputnik, damaged ISS and Apollo capsule objects appear, scaling smaller across later nights. Mid-screen atmospheric burn-up uses glowing leading edges, fragmentation and fading trails.

**Feedback:** Laser energy low warning is intended only at low energy. Dome outline retracts downward when destroyed. Ground impacts produce a ground shake without the violent dawn shake. Developer mode includes an option to force at least one power-up per night.

**Preserved:** Dawn cows stand and resume movement; Laser Sight guide lasts approximately 20 seconds, matches energy colour and fades/retracts on expiry. Refer to Alpha2.68 history below for underlying mechanics.

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

# Dob Defender — gameplay reference

**Current release:** Alpha2.68. **First retained build:** Alpha2.17.

## Player profiles and leaderboard

Players register a unique nickname once per browser. A locally stored player identity supports nickname changes and automatic submission of the best score on Game Over. The global leaderboard shows up to 50 top scores and night reached. Clearing browser data loses the locally stored identity; internet access is required for registration and score submission.

## Objective

Defend your observatory from incoming meteorites, asteroids and comets. Save cows. Do not shoot aircraft. Survive each night until dawn.

## Touch controls

- Relative left/right swipe on centred aiming slider rotates telescope.
- Tap slider or sky to fire one shot.
- Pause button suspends gameplay.
- DEV panel offers testing tools, including jumping to a selected night, restarting and importing Yale BSC5 data.

## Systems to preserve

- Approved Dobsonian telescope silhouette and laser origin.
- Laser energy and recharge/cost; dome health; score; nights and restarts.
- Meteors/asteroids/comets, UFO cow abduction, aircraft warnings, ISS and Starlink encounters.
- Astronomical sky field and Yale Bright Star Catalogue support with local caching/import.
- Mobile-first responsive layout and thumb-operated controls.

## Scope

This is a concise reference, not a complete reverse-engineered mechanics specification. Consult the playable HTML and historical handover for precise constants, schedules, scoring and collision behaviour. When there is a discrepancy, the latest approved HTML is authoritative.
