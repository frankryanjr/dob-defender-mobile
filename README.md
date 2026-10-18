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

**Current approved production:** Alpha2.68 at branch `main`, root `index.html`. **Alpha2.69 is unapproved**. Existing experimental Alpha2.69 GitHub test files are not production authority.

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
2. Read [docs/HANDOVER.md](docs/HANDOVER.md), [docs/GAMEPLAY.md](docs/GAMEPLAY.md), [docs/CHANGELOG.md](docs/CHANGELOG.md), [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md), and [docs/Start_Screen_v1_Handover.md](docs/Start_Screen_v1_Handover.md).
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

- [index.html](index.html) — current production game (Alpha2.68 gameplay with Start Screen v1)
- [game/index.html](game/index.html) — historical mirror; **check whether synchronized** before using
- [releases/](releases/) — archived numbered builds; check most recent
- [docs/HANDOVER.md](docs/HANDOVER.md) — accumulated project history, some older headings
- [docs/GAMEPLAY.md](docs/GAMEPLAY.md) — gameplay mechanics
- [docs/CHANGELOG.md](docs/CHANGELOG.md) — milestone changes
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) — validation and release workflow
- [docs/Start_Screen_v1_Handover.md](docs/Start_Screen_v1_Handover.md) — approved title screen and caching rule
- [assets/](assets/) — approved image assets

## Known housekeeping issues

- README and development docs previously still identified Alpha2.63; this README is updated for Alpha2.68 plus Start Screen v1. Other docs may retain historical/stale version statements.
- The current Start Screen v1 integration was syntax-checked and GitHub Pages deployment succeeded; full Android end-to-end testing has not been independently confirmed.
- A prior Android screenshot showed an older title screen at the canonical Pages URL while a commit-pinned CDN link worked; a versioned URL is the recommended share link. Do not assume the caching issue is fully diagnosed.
- Confirm whether `game/index.html` and archived release files match production before treating them as current.

## Recommended model effort

GPT-6 Instant: copy, labels, colours and docs. GPT-6 Medium: ordinary gameplay and controls. GPT-6 High: telescope geometry, bearings, difficult bugs or refactors. Extra High only for exceptional complexity. Model selection is controlled by the user.

Copyright © 2026 Frank Ryan Jr. All rights reserved. See [LICENSING.md](LICENSING.md).
