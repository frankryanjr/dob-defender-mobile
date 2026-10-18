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

Alpha2.17 is the first retained build and repository baseline. Alpha2.x identifies numbered milestones. Alpha2.63 is the current supplied build. Earlier prototype versions are not required.

## Local play

Download `index.html` and open it in Chrome or another modern browser. Some external catalogue downloads may require network access and may behave differently on local `file:` origins.

## Deployment

To host with GitHub Pages, configure repository **Settings → Pages**, deploy from branch `main`, root `/`. Once enabled, the root `index.html` is the entry point. Do not claim a live Pages URL before checking deployment.

## Validation status

GitHub upload confirms file persistence, **not** Android runtime testing. No browser gameplay test was performed during repository initialization.
