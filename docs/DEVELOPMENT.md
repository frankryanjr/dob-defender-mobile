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
