# Dob Defender — Start Screen Artwork v1

Status: **Approved and locked**, 16 October 2026.

- Artwork: `Dob_Defender_Start_Artwork_v1.jpg` (exact image data embedded in approved working HTML; do not regenerate, recolour, crop or stretch).
- Playable implementation: `Dob_Defender_Start_v1_Playable.html`.
- START text: separate HTML overlay with subtle 8% pulsing animation, 1.6-second cycle.
- Version text: `Alpha2.67` as separate HTML overlay.
- Game baseline: Alpha2.67, `frankryanjr/dob-defender-mobile`, `main/index.html`.
- Original test wrapper fetched production at runtime; deployed production uses the local versioned image asset.
- Production integration: approved Start Screen v1 with unchanged Alpha2.67 gameplay.
- Image SHA-256: `f6556a7a82ac0411ce6cb59c839c19d0cf80c46b114412758760851b1e091731`.

## Changelog

- Start screen artwork v1 approved; preserved original art and proportions.
- Locked START button placement and subtle text pulse.
- Saved reproducible HTML and image asset together.

## Release links and cache management (project rule)

For each approved production release:

1. Publish the complete game to the GitHub Pages production source without changing the approved gameplay or artwork unless requested.
2. Verify the GitHub Pages deployment workflow completed successfully for the intended commit. Where possible, verify the live page itself as well; distinguish deployment confirmation from device/browser testing.
3. Share the GitHub Pages link with a unique release query parameter, for example `https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.68`. Use a new parameter value for each release; never reuse the previous release value.
4. Treat the query parameter as a cache-busting aid for the HTML document, **not** a guaranteed refresh of every cached asset or a forced reload on each visit.
5. Keep the canonical URL `https://frankryanjr.github.io/dob-defender-mobile/` unchanged. If users still see an older release, test with a private/incognito window and investigate browser caches, service workers, deployment source and asset caching.
6. Provide the verified versioned play URL, release commit, and relevant deployment result in the release handover. Never label a release fully tested without actual browser/device testing.

Current share URL: `https://frankryanjr.github.io/dob-defender-mobile/?v=startscreen-v1-20261016`.

