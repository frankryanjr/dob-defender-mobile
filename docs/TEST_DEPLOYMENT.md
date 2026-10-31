# Development branch and isolated test site

Status (31 October 2026): **`dev` branch created. Production Pages `main:tests/index.html` landing page committed; live deployment not independently verified. Automated copy from `dev` is not configured.**

## Purpose
The `dev` branch holds unapproved gameplay candidates; `main` keeps approved production. Test builds should be playable through a stable GitHub Pages `tests/` landing page and immutable versioned test files. **Branch creation alone does not publish a separate GitHub Pages site.**

## Release safeguards
1. Read root README and the full locked WORKFLOW before work.
2. Verify current `main:index.html` and approved archive by Git blob hash. Keep the approved baseline intact.
3. Prepare a complete standalone HTML candidate and confirm its exact byte count, blob SHA and syntax/regression tests.
4. Commit only development candidate material to `dev`, never overwrite approved production on `main`.
5. Determine current Pages source and existing Actions before configuration. Do not switch the site's Pages branch to `dev`; doing so could replace the public game.
6. Publish test-only files into the isolated `tests/` URL namespace using a deployment method that preserves production root byte-for-byte. Retain a unique versioned test artifact and update the test landing page. Confirm the served file independently before giving a play link.
7. Production still requires user approval and archive/label-diff/deployment checks per WORKFLOW.

## Known active candidate
Night 3 Mothership Boss Test 1: `Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html`, expected Git blob `a35d1897ecb9713aeca9e7a0702ec7fdcbc6c65e` (3,792,550 bytes), currently **not in GitHub**. Do not reconstruct it from a modified Claude preview without verification. Recover the exact standalone test or rebuild a newly named candidate from SHA-verified production.

## Deployment architecture and checkpoint
- Development candidate source is stored on `dev` after complete standalone verification.
- The existing production Pages source retains `main:index.html`. The test landing page is committed separately at `main:tests/index.html` (commit `e58e875cb4e0f20e982351da02b8b50fe89e7117`). This should become `/dob-defender-mobile/tests/` when Pages serves main; the URL could not be independently fetched in this environment.
- Publishing a playable candidate requires copying the exact SHA-verified standalone HTML to a unique `main:tests/<versioned-filename>.html` path and updating `tests/index.html` with its link. This is test-only publishing under standing authorisation, not a production promotion. The `main:index.html` bytes must remain unchanged.
- An automated `dev` -> `main:tests/` workflow has **not** been installed because the actual Pages/Actions settings could not be inspected. Do not call the setup automated until that inspection and a verified test deployment are complete.

## First unverified setup task
Independently verify the test landing page is served and check Pages/Actions source configuration; if appropriate, add a constrained automated candidate-copy workflow after inspection. Then have Claude commit exact boss Test 1 to `dev` and copy the verified test file into `main:tests/` with its own versioned name and landing-page link. Do not represent a branch or placeholder as a playable boss build.
