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

## Alpha2.70 production record — 19 October 2026

- Approved candidate: Alpha2.70 Test 8, user-confirmed successful Android visual test for dome destruction.
- Archived exact candidate at `releases/Dob_Defender_Alpha2.70.html`, Git blob SHA `b464c01399c78370c2ecaccba7862cc439069bed`.
- Updated production `main:index.html` from verified archive without modifying game content; production HTML commit `7421e3f23ae138cde4a9cb585b5adc3d2f5ad634`.
- Changes: score-popup fade at dawn, moon removal, in-play leaderboard removal, cows-over-dome layering, stationary apex-to-ground dome destruction erasure.
- Approved HTML retains original Test 8 visible label and stale document title Test 6 to preserve exact tested bytes.
- GitHub commit is not proof of Pages deployment; verify Actions and live URL separately. User has not yet confirmed production URL on Android.
- Historical instructions below that recommend starting from a numbered archive or automatically publishing are superseded by `docs/WORKFLOW.md`.

# Alpha2.69 release implementation and verification — 18 October 2026

**User verification (18 October 2026):** User confirmed Alpha2.69 production game worked on their device after successful GitHub Pages deployment. This is user-reported Android/device validation, not an assistant-run device test.

- Approved candidate: Alpha2.69 Test 18.
- Permanent exact approved archive: `releases/Dob_Defender_Alpha2.69.html`.
- Archive commit: `d7b69f3c8143c5e94fb5d6918caf9042393d4fea`.
- Production update commit: `40042730939fe76aea5465f04f916983cfa1d955`.
- Production `index.html` derived from archive, with only three test-version labels changed; no gameplay modifications.
- Transfer verification: 343,607 JavaScript string characters; FNV-1a checksum `d4d94208`, matching the local approved HTML. This checksum is a transfer-integrity check, not a security hash.
- Previous production Alpha2.68 remains archived.
- Testing status: static inspection and file-integrity validation performed. Android gameplay not independently tested by assistant; GitHub Pages live deployment verification pending independent fetch.
- Deployment URL to verify: `https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.69`.
- Mandatory process: read `docs/WORKFLOW.md`; approved archive is source of truth, document every release change, and verify deployment before claiming success.

> **CURRENT PROCESS AUTHORITY:** [WORKFLOW.md](WORKFLOW.md) governs all new-chat onboarding, standalone HTML testing, explicit user approval, and production publishing. Historical instructions and version labels below are reference only when they conflict with WORKFLOW.md. Approved production: Alpha2.68 at branch `main`, root `index.html`. Alpha2.69 is unapproved. Do not commit or publish tests by default.

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

# Development and release workflow

1. Start with the latest numbered working HTML. Never replace it with a rewrite unless specifically approved.
2. Preserve approved telescope artwork, cradle, trusses, laser geometry, relative-swipe slider and tap-to-fire behaviour.
3. Make the smallest change that fulfils the request.
4. Run JavaScript syntax checks. Review rotation maths, laser origin, hit detection, scoring, lives/dome damage, pause and restart.
5. Test on Android touch browser for layout, swipe and tap controls, orientation and performance. Record **not tested** if a real device test was not performed.
6. Publish the **complete standalone playable HTML** as `index.html`, `game/index.html`, and `releases/Dob_Defender_AlphaX-Y.html`.
7. Update gameplay reference, handover and changelog with each approved milestone.
8. Keep previous releases intact.

## Version naming

Alpha2.17 is the first retained build and repository baseline. Alpha2.x identifies numbered milestones. Alpha2.63 was the historical supplied build; current approved production is Alpha2.68. Earlier prototype versions are not required.

## Local play

Download `index.html` and open it in Chrome or another modern browser. Some external catalogue downloads may require network access and may behave differently on local `file:` origins.

## Deployment

To host with GitHub Pages, configure repository **Settings → Pages**, deploy from branch `main`, root `/`. Once enabled, the root `index.html` is the entry point. Do not claim a live Pages URL before checking deployment.

## Validation status

GitHub upload confirms file persistence, **not** Android runtime testing. No browser gameplay test was performed during repository initialization.
