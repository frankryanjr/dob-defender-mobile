## FOUNDING RULE — ASSISTANT HANDLES DEVELOPMENT; USER ONLY ACTS WHEN NEEDED

**Mandatory for every new chat:** Read the complete [authoritative workflow](docs/WORKFLOW.md), especially **“FOUNDING PRINCIPLE — MINIMUM USER INVOLVEMENT.”** The user should only download/open/test something when they personally need it. The assistant must handle modular source, scripts, transfer files, ZIPs, internal build artifacts, release mechanics and troubleshooting without making the user a file courier. Before offering a download or link, ask whether the user actually needs the artifact. If not, keep it internal and proceed. Never waste time fixing delivery of an internal-only artifact. Actual gameplay testing still requires a complete standalone playable HTML, and production still requires explicit user approval.

## Proven large-file GitHub-to-local transfer — 24 October 2026

**Use this procedure when GitHub `fetch_file` returns empty or truncated content for a large standalone game HTML.** This was successfully used to recover the complete approved Alpha2.75 production baseline for the Alpha2.76 Sound Test 1. It supplements the mandatory rules in [docs/WORKFLOW.md](docs/WORKFLOW.md); that file remains authoritative.

1. Complete GitHub onboarding. Fetch `main:index.html` metadata/SHA and the approved release record. If `fetch_file` gives no complete HTML, use the GitHub connector's `fetch_blob` with the exact production blob SHA. Alpha2.75's `fetch_blob` returned complete source where `fetch_file` did not.
2. Convert the **entire** returned UTF-8 source to bytes, then Base64 in the connector-capable execution environment. Do not encode JavaScript UTF-16 code units as bytes or omit non-ASCII characters.
3. Transfer the Base64 in **ordered, numbered segments** to temporary Google Docs using `batch_update_document` / `insertText`. Approximately 12,000 Base64 characters per insertion worked in this session. Multiple insertions may be grouped where supported, but large batches can fail. When a document reaches its practical size limit, create a second document and continue at the exact next offset; do not restart, skip or overlap segments.
4. Export each temporary Google Doc as **plain text** through the Google Drive connector, making the exports available in the local/container runtime. Concatenate exported Base64 payloads in original order, removing only exporter-added document formatting/newlines, **not** payload characters. Check the expected Base64 length and segment boundaries before decoding.
5. Base64-decode into a local `.html` file under `/mnt/data`. Require a complete HTML ending, then run `git hash-object <local-file>` and compare the resulting **Git blob SHA exactly** with the production source blob SHA. **Stop if it differs.** Preserve this verified source unchanged and develop in a separately named working copy.
6. Deliver a complete standalone downloadable HTML test, run applicable syntax checks and follow the workflow's approval gate. **A documentation-only update does not authorize publishing a game test or changing production.** Clean up temporary transfer documents where possible.

**Verified example (historical, not future expected values):** Alpha2.75 production `main:index.html` Git blob `c101c9609bef5b606dc2c61957a3aca587c96e78`; UTF-8 source **1,178,955 bytes**; Base64 **1,571,940 characters**; two temporary Google Docs; reconstructed local file's Git blob SHA matched **exactly**. The approved archive and production HTML are not interchangeable: always use the verified current `main:index.html` as the next development baseline.

**Failure handling:** A successful connector response or matching length alone is not proof. If any document insert fails, identify the last confirmed successful offset and resume without duplication; if export introduces unexpected characters or SHA mismatches, rebuild/retransfer and verify rather than editing an untrusted file. Never fall back to an old uploaded game file.

---

### Alpha2.75 process lessons — preserve accumulated guidance

This README incorporates lessons from multiple earlier releases; **do not replace, shorten or discard historical instructions** when adding a new lesson. `docs/WORKFLOW.md` remains the authoritative, locked development and release procedure.

- For Android testing, provide the complete standalone HTML as required by the workflow. If the user explicitly authorizes GitHub-hosted tests, also provide a versioned `tests/` Pages URL for Chrome/Incognito testing; a Pages link does not replace the downloadable HTML.
- Large HTML transfers must be verified against the approved source's **Git blob SHA**. A successful write or plausible file length is insufficient.
- Before touching production `main:index.html`, fetch the permanent release archive back from GitHub and verify its blob SHA exactly matches the approved test. On any mismatch, **stop, correct, and re-verify**.
- Verify deployment separately from GitHub commit success; record user Android confirmation separately from automated checks.
- Alpha2.75's first archive transfer was incomplete and was corrected before production. See `docs/PROJECT_HISTORY.md` and `docs/WORKFLOW.md` for the recovery procedure.

## Alpha2.75 — 24 October 2026 — approved Test 5

- **Approval:** User confirmed “All working. Push to prod” for Alpha2.75 Test 5, including Chrome Incognito playback and music.
- **Immutable approved archive:** `releases/Dob_Defender_Alpha2.75.html` (blob `51a1a99c514b932270a4afd76d13c5192bd24ed8`), identical to tested `tests/Dob_Defender_Alpha2.75_Test_5.html`.
- **Production:** `main:index.html`, release commit `de1fd741b9096dffef6fa59448df96aa9ccf749c`, blob `c101c9609bef5b606dc2c61957a3aca587c96e78`. Differences from approved archive are **only** the HTML document title and `DD_GAME_VERSION`, removing “Test 5”.
- **Changes:** New-player callsign gate with generated callsign or 3–18-character custom entry, DEFEND! starts Night 1; returning players with saved identity bypass registration. One looping background track `DobDefGame2.mp3`, 20% volume, first-interaction fallback for autoplay restrictions, pause/resume integration. Existing approved telescope, title artwork, gameplay, controls, scoring, sounds and leaderboard preserved.
- **Testing:** JavaScript syntax checked for candidate; user confirmed Test 5 working in Chrome Incognito. Independent Android end-to-end and production live-page verification pending.
- **Production URL:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.75

## Alpha2.74 — 23 October 2026 — approved Sound Test 5

- **User approval:** “Ok push to prod as it is now” for complete standalone `Dob_Defender_Alpha2.73_Sound_Test_5.html`.
- **Exact approved archive:** `releases/Dob_Defender_Alpha2.74.html`, Git blob `e008527ad54663e5b0e063b19653e93450e5f297`. Production: `main:index.html`, initial release commit `585712ed4981752f68dd88cab4f2997389647654`, blob `e59a59f3a30881d8466a71f0e336eb4a6a459654`.
- **Sound:** Embedded edited Freesound recordings for laser firing, comet destruction and ground impact. Meteor-destroyed and asteroid-destroyed sounds are removed; corresponding gameplay and visual effects remain unchanged.
- **Preserved:** Approved Alpha2.73 gameplay, artwork, controls, scoring and leaderboard.
- **Production-label-only differences:** document title and `DD_GAME_VERSION` changed from `Alpha2.73 Sound Test 5` to `Alpha2.74`. Archived tested candidate remains unchanged.
- **Testing:** User approved Sound Test 5; assistant did not independently perform Android device testing. GitHub Pages and CI deployment verification recorded separately.
- **Production link:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.74

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

## Current production — Alpha2.70 (19 October 2026)

- Approved source: [releases/Dob_Defender_Alpha2.70.html](releases/Dob_Defender_Alpha2.70.html), exact user-tested **Alpha2.70 Test 8**.
- Production: [index.html](index.html), byte-identical to approved archive (Git blob SHA `b464c01399c78370c2ecaccba7862cc439069bed`).
- Changes: floating hit-score popups fade correctly across dawn; gameplay top-right leaderboard button removed (end-game leaderboard retained); moon removed; cows rendered in front of dome walls; dome destruction erases stationary arch from apex down curved sides and vertical walls to ground without movement.
- Android: user explicitly confirmed Test 8 success, specifically corrected dome destruction. Other changes retained from earlier tests; independent assistant Android testing not performed.
- Release commit for production HTML: `7421e3f23ae138cde4a9cb585b5adc3d2f5ad634`. Deployment verification is recorded separately.
- Production URL: https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.70
- Note: approved file retains internal Test 8 label and historical HTML document title "Test 6"; no gameplay or label changes were made to the approved artifact.


**Required GitHub-to-local procedure:** See **VERIFIED GITHUB-TO-LOCAL TEST BUILD PROCEDURE** in `docs/WORKFLOW.md`. Retrieve and hash-check current `main:index.html`, use the container-backed Python environment to create a complete `/mnt/data/` HTML test, and give the user a direct download link. Do **not** ask the user to download the GitHub HTML and re-upload it. A prior failed raw-HTTP download is not proof that the workflow is impossible. Never publish a test before approval.

## Current production — Alpha2.69 (18 October 2026)

- Approved source: [releases/Dob_Defender_Alpha2.69.html](releases/Dob_Defender_Alpha2.69.html), an exact archive of the user-approved Alpha2.69 Test 18.
- Production: [index.html](index.html), copied from the approved archive with only TEST 18 / internal test-version labels replaced by Alpha2.69.
- Features: night-end scoring tally for laser energy, dome integrity, cows saved and cows lost; final Game Over tally; persistent final score screen with VIEW LEADERBOARD and PLAY AGAIN; background score submission without automatic leaderboard redirect; space-junk variants and atmospheric burn-up; HUD, dome and impact feedback improvements.
- Source transfer: complete approved HTML reconstructed from conversation file reads and verified by length and checksum before archival; no user download/reupload required.
- Syntax/device status: Test 18 generated and statically inspected; no independent Android device test was performed by the assistant. GitHub Pages verification must be recorded separately.
- Previous approved release: Alpha2.68, retained in `releases/`.

# START HERE — MANDATORY FOR EVERY NEW CHAT

**Development session shorthand:** Requests like “Let's make some developments” mean begin development mode for any part of the game (sound, gameplay, leaderboards, artwork, controls, animations, bugs or new features). Complete GitHub onboarding, then ask which change to work on. Create complete downloadable HTML tests; do not publish without separate explicit approval. See §1A of [docs/WORKFLOW.md](docs/WORKFLOW.md).

**FIRST ACTION:** Read [docs/WORKFLOW.md](docs/WORKFLOW.md) in full. This is the **single authoritative, locked development/test/approval/production procedure**. Follow it before modifying game code, creating test artifacts, publishing to GitHub or sharing links. A new chat may contain only "Go to GitHub and read the instructions"; that instruction means **read this README, then WORKFLOW.md, then all required project sources**. Do not rely on previous-chat memory or old uploaded files.

**Non-negotiable:** Development builds are complete downloadable standalone HTML attachments for the user to test locally. **Only after explicit approval** may an approved release be committed to production and linked via GitHub Pages. Never send a GitHub source-file link or unverified Pages test link as the test deliverable.

**Current approved production:** Alpha2.69 at branch `main`, root `index.html`. The approved Alpha2.69 Test 18 is permanently archived under `releases/`. Historical candidate files are not production authority.

---

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

# Dob Defender

Mobile-browser astronomy arcade game. Defend the observatory against meteorites, asteroids and comets, save cows, avoid shooting aircraft.

**Current production gameplay:** Alpha2.69. **Approved title artwork:** Start Screen v1 (16 October 2026). **Production entry point:** [index.html](index.html). **Production game:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.69 (deployment must be verified before making new release claims)

## REQUIRED: New-chat onboarding (read before any development)

This repository is the durable source of truth across ChatGPT Project chats. At the start of **every new Dob Defender development chat**, the assistant must:

1. Fetch this README from GitHub (do not rely on an old pasted copy or chat memory), then **read [docs/WORKFLOW.md](docs/WORKFLOW.md) in full as the highest-priority process authority**.
2. Read [docs/PROJECT_HISTORY.md](docs/PROJECT_HISTORY.md), [docs/HANDOVER.md](docs/HANDOVER.md), [docs/GAMEPLAY.md](docs/GAMEPLAY.md), [docs/CHANGELOG.md](docs/CHANGELOG.md), [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md), and [docs/Start_Screen_v1_Handover.md](docs/Start_Screen_v1_Handover.md).
3. Inspect [index.html](index.html) and the latest numbered release in [releases/](releases/) before editing. Determine the actual newest working baseline; **some historical documentation still mentions Alpha2.63 or earlier and is outdated**. Prefer the deployed implementation and newest verified changelog entry, and flag discrepancies instead of silently assuming.
4. Briefly report: current version, approved locked features, current task, known unresolved issues, and testing status. Ask for clarification only when needed to protect approved designs.
5. Make minimal changes to the latest working game, never an unnecessary rebuild.

**If GitHub access is unavailable:** disclose it and request the current README/HTML/handover rather than inventing a project state.

## Locked designs and mechanics

- Preserve approved Dobsonian telescope artwork: brown UTA and mirror box, four silver trusses, silver circular altitude bearing in fixed narrow brown U-shaped cradle, side-mounted green pointer.
- Preserve Android thumb-friendly controls, relative-swipe aiming slider, tap-to-fire, laser geometry, collisions, scoring, dome/lives, pause/restart, cows/UFOs, aircraft and leaderboard unless explicitly instructed otherwise.
- Approved Start Screen v1 artwork is stored at [assets/Dob_Defender_Start_Artwork_v1.jpg](assets/Dob_Defender_Start_Artwork_v1.jpg). Do not redraw, recolour, crop or stretch without approval. START pulse is a separate HTML animation.

## Release and handover contract

After **each approved saved milestone**:
1. Preserve older numbered HTML releases; publish a complete playable game, not a patch or replacement function. Supply downloadable complete HTML and Markdown handover to the user.
2. Update README current version and status, [docs/HANDOVER.md](docs/HANDOVER.md), [docs/CHANGELOG.md](docs/CHANGELOG.md), and any affected gameplay/development docs. Record changes, design decisions, known issues, next work and actual test results.
3. Run available syntax checks; inspect aiming maths, laser position, collisions, scoring, lives/dome, restarting and Android layout. Never confuse syntax validation with real browser/device playtesting.
4. Confirm GitHub Pages deployment for the intended commit. Share a **new versioned Pages URL** (e.g. `https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.69`) for every new release, retaining the canonical URL. Query strings help with document caching but do not guarantee all assets refresh.
5. State the production commit and what was verified; never claim deployment or testing that was not confirmed.

## Repository map

- [docs/WORKFLOW.md](docs/WORKFLOW.md) — **authoritative locked process; read first**

- [index.html](index.html) — current production game (Alpha2.69)
- [game/index.html](game/index.html) — historical mirror; **check whether synchronized** before using
- [releases/](releases/) — archived numbered builds; check most recent
- [docs/PROJECT_HISTORY.md](docs/PROJECT_HISTORY.md) — consolidated chronological development and production tracker
- [docs/HANDOVER.md](docs/HANDOVER.md) — accumulated detailed project history, some older headings
- [docs/GAMEPLAY.md](docs/GAMEPLAY.md) — gameplay mechanics
- [docs/CHANGELOG.md](docs/CHANGELOG.md) — milestone changes
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) — validation and release workflow
- [docs/Start_Screen_v1_Handover.md](docs/Start_Screen_v1_Handover.md) — approved title screen and caching rule
- [assets/](assets/) — approved image assets

## Known housekeeping issues

- README and development docs previously still identified Alpha2.63; this README is updated for Alpha2.68 plus Start Screen v1. Other docs may retain historical/stale version statements.
- Alpha2.69 production deployment succeeded and the user confirmed the game worked on their device; independent assistant-run Android end-to-end testing has not been performed.
- A prior Android screenshot showed an older title screen at the canonical Pages URL while a commit-pinned CDN link worked; a versioned URL is the recommended share link. Do not assume the caching issue is fully diagnosed.
- Confirm whether `game/index.html` and archived release files match production before treating them as current.

## Recommended model effort

GPT-6 Instant: copy, labels, colours and docs. GPT-6 Medium: ordinary gameplay and controls. GPT-6 High: telescope geometry, bearings, difficult bugs or refactors. Extra High only for exceptional complexity. Model selection is controlled by the user.

Copyright © 2026 Frank Ryan Jr. All rights reserved. See [LICENSING.md](LICENSING.md).

## Alpha2.76 production release — 25 October 2026

Current approved production: **Alpha2.76**, approved from **Alpha2.76 Sound Test 25**. Production source: `main:index.html`; exact approved test archive: `releases/Dob_Defender_Alpha2.76.html` (Git blob `52352378f7fe288c52351d73b0fd4c74abc3b1aa`). Production is the archive with version-label-only changes (Git blob `68da879b0120364df1128848e115200deec636b6`). Adds and refines standalone embedded sound effects for meteors, comets, asteroids, aircraft, UFOs, warnings, 3-2-1-GO countdown and three-note morning chime; adds the compact amber-red SAFETY WARNING popup and clears transient lasers/debris at dawn. Gameplay and approved artwork preserved. Production commit: `521e842f65284b4663cbb7430ce80b3fd9dc229b`. Deployment and Android verification are tracked separately.
