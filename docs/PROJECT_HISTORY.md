## Alpha2.75 — 24 October 2026 — approved Test 5

- **Approval:** User confirmed “All working. Push to prod” for Alpha2.75 Test 5, including Chrome Incognito playback and music.
- **Immutable approved archive:** `releases/Dob_Defender_Alpha2.75.html` (blob `51a1a99c514b932270a4afd76d13c5192bd24ed8`), identical to tested `tests/Dob_Defender_Alpha2.75_Test_5.html`.
- **Production:** `main:index.html`, release commit `de1fd741b9096dffef6fa59448df96aa9ccf749c`, blob `c101c9609bef5b606dc2c61957a3aca587c96e78`. Differences from approved archive are **only** the HTML document title and `DD_GAME_VERSION`, removing “Test 5”.
- **Changes:** New-player callsign gate with generated callsign or 3–18-character custom entry, DEFEND! starts Night 1; returning players with saved identity bypass registration. One looping background track `DobDefGame2.mp3`, 20% volume, first-interaction fallback for autoplay restrictions, pause/resume integration. Existing approved telescope, title artwork, gameplay, controls, scoring, sounds and leaderboard preserved.
- **Testing:** JavaScript syntax checked for candidate; user confirmed Test 5 working in Chrome Incognito. Independent Android end-to-end and production live-page verification pending.
- **Production URL:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.75

## 23 October 2026 — Alpha2.74 production approval and sound release

- User explicitly approved Sound Test 5 for production. Immutable archive: `releases/Dob_Defender_Alpha2.74.html` (blob `e008527ad54663e5b0e063b19653e93450e5f297`).
- Production `index.html` committed as `585712ed4981752f68dd88cab4f2997389647654` (blob `e59a59f3a30881d8466a71f0e336eb4a6a459654`). Only title and `DD_GAME_VERSION` labels changed versus approved archive.
- Laser, comet destruction and ground impact audio embedded. Meteor and asteroid destruction audio removed. Other gameplay/artwork preserved. User Android production verification pending.

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

## 19 October 2026 — Alpha2.70 approved production

- User tested and approved **Alpha2.70 Test 8**, resolving dome destruction after multiple failed animation candidates.
- Fixed frozen floating score popups at dawn; removed gameplay leaderboard button and moon; placed cows in front of dome walls; erased fixed dome outline from apex down to ground on destruction.
- Approved test archived unchanged as `releases/Dob_Defender_Alpha2.70.html`; production `index.html` exact match (blob `b464c01399c78370c2ecaccba7862cc439069bed`).
- Production HTML commit: `7421e3f23ae138cde4a9cb585b5adc3d2f5ad634`. Deployment and live-device confirmation for production URL require separate records.

# Dob Defender — Project History and Production Tracker

**Updated:** 19 October 2026  
**Current approved production:** **Alpha2.69**, released 18 October 2026.  
**Production game:** [Play Alpha2.69](https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.69)  
**Approved test archive:** [Alpha2.69 Test 18](../releases/Dob_Defender_Alpha2.69.html)  
**Live production source:** [index.html](../index.html)

> **Purpose:** A readable overview of how Dob Defender evolved, what reached production, and how to trace changes. This is a historical index, **not** a replacement for the authoritative [WORKFLOW](WORKFLOW.md), [CHANGELOG](CHANGELOG.md), [HANDOVER](HANDOVER.md), [GAMEPLAY](GAMEPLAY.md), or approved HTML. Earlier handover sections may describe superseded baselines or plans. Only a documented approval and production release establish production status.

## Development timeline

| Period / milestone | Development and design changes | Evidence / status |
|---|---|---|
| Initial concept and chat previews (before Alpha1) | Mobile astronomy arcade game: aim an Obsession-style Dobsonian and fire a side-mounted green laser at meteors, asteroids, comets and other targets. Early chat previews `v9`–`v28` iterated on artwork, size, slider and firing controls. | Historical narrative, not individually tagged production releases; [HANDOVER §7](HANDOVER.md) |
| **Alpha1 — 12 Oct 2026** | Approved small brown truss Dobsonian: short UTA and mirror box, four silver trusses with inward diagonals (not an X), attached silver altitude bearing, narrow fixed U-shaped wooden cradle, side-mounted green pointer. Original gameplay used three hearts, score-based levels and hold-to-fire. | Preserved Alpha1-era uploaded baseline `Dob_Defender_Alpha1-2.html`; historical handover also mentions emailed `Dob_Defender_Alpha1.html`. These filenames are not proof of a GitHub production deployment. |
| **Initial Alpha2 — 12 Oct 2026** | Replaced hearts/random continuous spawning with scheduled **NIGHT** waves, dusk/dawn, laser-energy and dome-health systems, single shots, impact rules, cumulative score, cows and UFO abductions, ISS recharge, aircraft warnings and Starlink passes. Preserved telescope artwork. | Playable `Dob_Defender_Alpha2-1.html`; initial prototype with limited browser smoke testing, not established as a GitHub production release. |
| **Alpha2.3 — 12 Oct 2026** | User playtest led to faster early nights, sky tap-to-fire, improved tracking, cows remaining visible, UFO targeting and abduction-motion refinements. Starlink intercepting shots was deliberately retained. | Historical playtest/candidate entries in [HANDOVER](HANDOVER.md). |
| **Alpha2.5–Alpha2.20 — Oct 2026** | Iterative refinements to relative thumb steering, cow survival during UFO lifts, comet tails, collision handling, destruction sequences, ground impacts and artwork/animation. | Individual milestone notes in [HANDOVER](HANDOVER.md); do not treat every candidate number as a published release. |
| **Alpha2.17** | First retained build in the GitHub repository history according to the changelog. | [CHANGELOG](CHANGELOG.md); earlier builds documented through historical handover. |
| **Alpha2.62** | Pre-title-screen milestone with DEV tools, mobile controls, astronomical sky data and multi-night gameplay. | [CHANGELOG](CHANGELOG.md). |
| **Alpha2.63 — 14 Oct 2026** | Title-screen text, **DEFEND!** button and centred version label; presentation changes rather than gameplay redesign. | [CHANGELOG](CHANGELOG.md). |
| **Repository initialized — 15 Oct 2026** | Established GitHub versioned source, README, docs and retained release files. | Repository event, **not** a gameplay release. |
| **Alpha2.64 — 15 Oct 2026** | Nickname registration and global top-50 leaderboard backed by Supabase, player identity and server-side submission. | [CHANGELOG](CHANGELOG.md). |
| **Alpha2.65 — 15 Oct 2026** | Repaired incomplete Alpha2.64 HTML upload that left DEFEND and LEADERBOARD controls inert; restored script closure and initialization. | Syntax verified; device tests not independently established. |
| **Alpha2.67 — 15 Oct 2026** | Leaderboard changed from personal-best-only rankings to individual game submissions; repeat entries from one player supported; Supabase Edge Function upgraded. | [CHANGELOG](CHANGELOG.md). |
| **Start Screen v1 — 16 Oct 2026** | Approved title artwork preserved as an asset and later embedded in standalone HTML. | [Start Screen handover](Start_Screen_v1_Handover.md). |
| **Alpha2.68 — 18 Oct 2026** | Integrated Laser Sight power-up, refined dome and ground damage, resource HUD feedback, object scores, night scoring and offline embedded title artwork. | [Archived release](../releases/Dob_Defender_Alpha2.68.html); syntax checks recorded, not equivalent to Android testing. |
| **Alpha2.69 — 18 Oct 2026** | Animated night-end and Game Over score tally; saved/lost cow adjustments; persistent final score and replay/leaderboard choice; background leaderboard submission; new tumbling space-junk variants and atmospheric burn-up; HUD/dome feedback fixes. | **Approved production**, from **Test 18**; archived and deployed. User subsequently confirmed the production game worked on their device. |

## Production and release evidence

| Version | Approved source / deployment | Verification and limitations |
|---|---|---|
| Alpha2.68 | [Archive](../releases/Dob_Defender_Alpha2.68.html) | Recorded as prior approved production; retained for rollback. Syntax and embedded image validation documented; Android end-to-end testing was not independently performed by assistant. |
| **Alpha2.69** | [Exact approved Test 18 archive](../releases/Dob_Defender_Alpha2.69.html) → root [index.html](../index.html) → [live game](https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.69) | Approved test source transferred with text-length/checksum verification. Archive commit `d7b69f3`; production commit `400427309`. Production differs from archive only in test-version labels. GitHub Pages deployment succeeded; user confirmed Android playability. |

**Release record notes:** Alpha2.69 source transfer checked 343,607 decoded text characters and FNV-1a `d4d94208` for the approved Test 18. This is a text integrity check, **not** a cryptographic or byte-level hash. A deployment check, browser playtest and Android user confirmation are different evidence types.

## Evolution by area

- **Telescope art:** Generic early illustrations evolved into the small approved wooden truss Dobsonian. The fixed cradle and moving mirror box/bearing relationship was repeatedly corrected; preserve the approved geometry unless a new change is explicitly requested.
- **Controls:** Early FIRE-button and held-fire approach evolved into mobile relative-swipe steering and tap-to-fire. Historical controls are not necessarily current controls.
- **Core game:** Alpha1 hearts and random spawning became Alpha2 scheduled nights, energy, dome damage, night transitions and richer hazard behaviour.
- **Characters and events:** Cows gained grazing, sleeping, abduction and rescue outcomes; ISS recharge, aircraft penalties, Starlink interference and later space junk broadened encounters.
- **Scoring and leaderboard:** Local scores and bonuses evolved into registered online standings, individual game submissions and Alpha2.69's background submission plus explicit leaderboard navigation.
- **Presentation:** Approved title artwork, feedback effects, dome impact cues, laser-sight visuals, night-end tally and Game Over flow matured through Alpha2.68–2.69.

## Gaps and interpretation

- The handover's early version labels include **playtest candidates** and historical chat iterations, not a complete sequence of independently approved GitHub production releases.
- Exact intermediate release dates, approvals, Android results and archives are **not established for every Alpha2.x number**. Do not infer them from numbering.
- Some older README/handover/gameplay sections still describe superseded “current” versions; use the newest verified production release and [WORKFLOW](WORKFLOW.md).
- Proposed features and historical “known limitations” (for example early notes saying no cloud leaderboard) must not be mistaken for current product state.
- This tracker should be updated **after each approved production release** with milestone, test identifier, archive, deployment, validation and user-confirmation status. New experiments can be recorded as candidates but must not be labelled production.

## Primary sources

- [CHANGELOG.md](CHANGELOG.md) — release-level feature changes
- [HANDOVER.md](HANDOVER.md) — detailed early design decisions, iterations and technical history
- [DEVELOPMENT.md](DEVELOPMENT.md) — implementation, commits and validation records
- [GAMEPLAY.md](GAMEPLAY.md) — current mechanics reference with historical sections
- [WORKFLOW.md](WORKFLOW.md) — mandatory development and release procedure
- [GitHub commit history](https://github.com/frankryanjr/dob-defender-mobile/commits/main/) — repository-level change audit
- [Archived releases](../releases/) — retained numbered game files
