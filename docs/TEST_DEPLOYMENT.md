# Development branch and isolated test site

Status (31 October 2026): **`dev` branch created. Test deployment not yet configured or verified.**

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

## First unverified setup task
Inspect existing GitHub Pages source and Actions workflow definitions; implement and verify an isolated `tests/` deployment without changing `main:index.html`. Then recover and upload the verified boss test for Android gameplay. Do not represent a branch or placeholder as a playable boss build.
