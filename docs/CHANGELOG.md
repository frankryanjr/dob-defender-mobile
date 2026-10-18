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
