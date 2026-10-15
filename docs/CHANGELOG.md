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
