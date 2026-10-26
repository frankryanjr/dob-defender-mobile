## Alpha2.80 production release — 26 October 2026

- **Explicit user approval:** “Push fixes to prod” after confirming abducted-cow fix looks good and leaderboard seems fixed.
- **Immutable exact approved test archive:** `releases/Dob_Defender_Alpha2.80.html`, verified Git blob `1a4c399c361466c384f23767bedc11719cd37895`, commit `3ba750edbaf8371da3ef183e949a86d0e8d1be4e`. Original complete standalone Alpha2.80 Bugfix Test 1 is preserved unchanged, including historical test label and source comment.
- **Production:** `main:index.html` blob `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`, commit `9df9a4085e18872de3d6721af8299d54644f51e7`. Derived from exact verified archive with only two substitutions: HTML title `Dob Defender Alpha2.80 Test 1`→`Dob Defender Alpha2.80`, and `DD_GAME_VERSION='Alpha2.79'`→`DD_GAME_VERSION='Alpha2.80'`. The candidate had retained the Alpha2.79 version constant; production corrects that release label. No other gameplay changes.
- **Fixes:** dead abducted cows no longer render floating; game-over score submissions display acknowledged status / personal-best context and offer retry on network failure. Backend submission rejection on itch.io has not been independently established. Note: an unchanged leaderboard after a lower score is expected with personal-best ranking.
- **Validation:** local Test 1 four inline JS syntax checks passed; user reported cow fix looks good and leaderboard seems fixed. GitHub archive SHA gate passed; production update GitHub reported SHA above. GitHub Actions, independently served Pages version and production Android checks tracked separately.
- **Production only on GitHub:** itch.io upload remains separate and has not been changed by this release.
- **Next unverified task:** verify GitHub Actions and the live-served Alpha2.80 version; user tests released GitHub build and decides separately on itch.io update. Wording improvement “Your personal best score is shown on the worldwide leaderboard” is agreed for a future test revision, **not included in this exact approved Test 1 archive**.

## Alpha2.79 production release — 25 October 2026

- **User approval:** “Push it all to prod” for complete Alpha2.79 Leaderboard Button Test 7 (not independently Android-verified after scope fix).
- **Exact immutable approved test archive:** `releases/Dob_Defender_Alpha2.79.html` Git blob `131654b11232190f6470032f01180994bd969b1b` (3,782,528 bytes), release archive commit `949e06e9e164c5410dad57f81bd144d436e77eb6`; re-fetched SHA matches local approved Test 7 exactly.
- **Production:** `main:index.html` Git blob `84f89682b3459577746c7678912a9b9dbcdcf4eb`, production commit `0925ddac00764ce6fa71ff061d40954e96c41f25`. Produced from exact GitHub archive with precisely two label substitutions: HTML `<title>` and `DD_GAME_VERSION` remove “Leaderboard Button Test 7”; no gameplay edits in promotion. Re-fetched production Git blob matches connector response.
- **Changes since Alpha2.78:** start-screen clickable NIGHTS DEFENDED WORLDWIDE badge opens leaderboard, four starting cows, revised once-per-cow dawn saved/lost census, scheduled early UFO abductions, up to two separate-target simultaneous abductors from Night 6, cow splat fade expiry fix, 9% music during tally with 20% normal return, counter label fit; existing +50 rescue and +10 dome reward retained.
- **Known limitation:** worldwide badge sums final-night values from public leaderboard response, not authoritative all-time aggregate; capped records can imply a lower bound.
- **Validation:** four inline JS blocks syntax-checked on Test 7; release archive/local SHA and production label-only changes verified. GitHub Actions status, live Pages HTTP content and Android production gameplay **not independently verified**; environment live HTTP fetch returned inaccessible/cache miss. User to confirm on device. Do not imply completed deployment from successful GitHub write.
- **First unverified next step:** verify latest GitHub Actions Pages deploy/syntax checks and independently fetch served Pages Alpha2.79 HTML; user tests on Android counter → leaderboard → back → START, four-cow abductions/scoring, Night 6 dual UFO, red splats, tally audio. Investigate discrepancies before further code changes.

## Alpha2.78 production promotion — 25 October 2026

User confirmed full `Dob_Defender_Alpha2.78_Tally_Audio_Test_2.html` sounds perfect and explicitly authorised production release. Local approved test SHA `168c505247fa450a64824d6a9c706b3d82aef3ef` (3,778,569 bytes). Uploaded immutable `releases/Dob_Defender_Alpha2.78.html` SHA verified against approved test before production. Production title, `DD_GAME_VERSION` and comment-label substitutions only; resulting `main:index.html` SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3` (3,778,502 bytes) commit `7db1c86f8c0df0850cf88e367876585f8342e0d2`. Three inline JS syntax checks passed on Test 2. GitHub Actions/Pages live served version and Android production confirmation tracked separately. Open cow issues unaffected.

## Alpha2.77 release verification — 25 Oct 2026

Latest GitHub Actions on final documentation commit `e660845f3b048f5db4bad946dffc31c6967c9d3f`: `pages build and deployment` run `40184435539` **completed success**; `JavaScript syntax check` run `40184435367` **completed success**. Final committed production `index.html` Git blob `ae484817ab23bb3895dca9806f957c2688827b1e`, original release commit `6d732ec905915f0e997c442317a335c7f6759f1c`. Independent HTTP retrieval of live Pages URL failed in current browsing environment; do not state live HTML inspected. **First unverified task:** actual device open `https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.77` and confirm clean version/audio; if discrepancies inspect Pages cache and fetch externally.

## Alpha2.77 production promotion — 25 October 2026

Approval: user reported Audio Mix Test 3 sounds good and said `Push to prod`. Local exact candidate `Dob_Defender_Alpha2.76_Audio_Mix_Test_3.html` SHA `0d4fcefdaf6d9ac3208c6236c90931b40b7e95d9`; archived unmodified to `releases/Dob_Defender_Alpha2.77.html` and re-fetched GitHub blob SHA matched. Production from verified archive with title/version and two comment-label replacements only; `main:index.html` SHA `ae484817ab23bb3895dca9806f957c2688827b1e` verified after update, release commit `6d732ec905915f0e997c442317a335c7f6759f1c`. All three inline JavaScript blocks passed `node --check`; archive is 3,776,589 bytes, promoted file 3,776,590 bytes. Outstanding: Actions/deployment live verification and user Android production confirmation.

## Alpha2.75 — 24 October 2026 — approved Test 5

- **Approval:** User confirmed “All working. Push to prod” for Alpha2.75 Test 5, including Chrome Incognito playback and music.
- **Immutable approved archive:** `releases/Dob_Defender_Alpha2.75.html` (blob `51a1a99c514b932270a4afd76d13c5192bd24ed8`), identical to tested `tests/Dob_Defender_Alpha2.75_Test_5.html`.
- **Production:** `main:index.html`, release commit `de1fd741b9096dffef6fa59448df96aa9ccf749c`, blob `c101c9609bef5b606dc2c61957a3aca587c96e78`. Differences from approved archive are **only** the HTML document title and `DD_GAME_VERSION`, removing “Test 5”.
- **Changes:** New-player callsign gate with generated callsign or 3–18-character custom entry, DEFEND! starts Night 1; returning players with saved identity bypass registration. One looping background track `DobDefGame2.mp3`, 20% volume, first-interaction fallback for autoplay restrictions, pause/resume integration. Existing approved telescope, title artwork, gameplay, controls, scoring, sounds and leaderboard preserved.
- **Testing:** JavaScript syntax checked for candidate; user confirmed Test 5 working in Chrome Incognito. Independent Android end-to-end and production live-page verification pending.
- **Production URL:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.75

## Alpha2.74 release — 23 October 2026

- User approved `Dob_Defender_Alpha2.73_Sound_Test_5.html` for production.
- Verified exact approved candidate length 1,171,886 Unicode characters and FNV-1a text checksum `f5fb4b44` before archival. Git archive blob `e008527ad54663e5b0e063b19653e93450e5f297` matches local `git hash-object`.
- Published production from approved candidate with exactly two label changes (HTML title and `DD_GAME_VERSION`), commit `585712ed4981752f68dd88cab4f2997389647654`.
- Audio: laser fire, comet destroyed and ground impact present; meteor and asteroid destruction audio removed.
- GitHub Pages deployment verification and user Android production confirmation tracked separately; neither implied by a successful commit.

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

## Alpha2.76 release validation — 25 October 2026

User explicitly requested production publication of **Alpha2.76 Sound Test 25**. Local candidate Git blob `52352378f7fe288c52351d73b0fd4c74abc3b1aa`. Direct GitHub archive transfer initially mismatched because a line-range boundary newline was omitted; repaired transfer and re-fetched GitHub archive SHA matched exactly **before** updating production. Archive path `releases/Dob_Defender_Alpha2.76.html`. Production derived solely from verified archive by replacing three `Alpha2.76 Sound Test 25` labels with `Alpha2.76` and changing the release-status code comment. Local production blob SHA `68da879b0120364df1128848e115200deec636b6`, verified against GitHub update result; release commit `521e842f65284b4663cbb7430ce80b3fd9dc229b`. All three inline JavaScript blocks passed `node --check`. Browser/Pages deployment and user Android production confirmation are separate pending checks. No other gameplay changes made during promotion.
