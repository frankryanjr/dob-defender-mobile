## Checkpoint — boss test published (31 October 2026)

- Published: `tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html`, git blob `a35d1897ecb9713aeca9e7a0702ec7fdcbc6c65e`, 3,792,550 bytes. Same blob on `origin/dev` and `origin/main`.
- Production `main:index.html` unchanged, blob `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`.
- Actions: JavaScript syntax check and pages build succeeded for both commits.
- NOT verified: live served content at `https://frankryanjr.github.io/dob-defender-mobile/tests/Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html` (not reachable from the build environment). Android: user reports the playtest works (earlier build). Test scores go to the live worldwide leaderboard.
- Next action: user confirms the public test URL loads on Android; then collect balance feedback for Test 2 on `dev`.

# Dob Defender — Current State
Updated: 31 October 2026. **Status is a committed documentation checkpoint, not a new game release.**

## Authority and startup
- GitHub repository: https://github.com/frankryanjr/dob-defender-mobile
- **Read the root README and the entire [WORKFLOW.md](WORKFLOW.md) first.** Complete all mandatory WORKFLOW onboarding, including inspection of handover, specs/history and production/archive verification. This summary does not replace those requirements.
- For blockers, follow WORKFLOW §2A and consult proven recovery procedures **before** declaring failure or asking the user to transfer files.
- This file is a short restart pointer. Current verified repository evidence takes precedence over this snapshot.

## Approved production
- Latest documented approved production: **Alpha2.80**.
- `main:index.html`: Git blob SHA `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`, 3,784,184 bytes; production commit `9df9a4085e18872de3d6721af8299d54644f51e7`.
- Approved immutable release: `releases/Dob_Defender_Alpha2.80.html`, Git blob SHA `1a4c399c361466c384f23767bedc11719cd37895`.
- GitHub Actions Pages/syntax workflows reported success on 26 October. On 31 October user confirmed Android production playback, Pages version and itch.io update; independent fresh live HTTP and exact itch.io upload SHA were not established in that confirmation.
- **No new production release is approved.** Do not edit production or release artifacts without explicit approval and WORKFLOW release gates.

## Active development — Night 3 Mothership Boss Test 1
- Source: [top of HANDOVER.md](HANDOVER.md) (31 October 2026).
- Candidate: `Dob_Defender_Alpha2.80_Mothership_Boss_Test_1.html`, **local/hosted-preview only**, not in GitHub; 3,792,550 bytes; Git blob SHA `a35d1897ecb9713aeca9e7a0702ec7fdcbc6c65e`. A private claude.ai artifact preview is not byte-identical to standalone HTML and mocks leaderboard requests.
- Night 3 boss appears after scheduled threats. Two 5-hit shield nodes, then moving/orbiting front-arc reactor (6 hits); shootable plasma orbs. Balance values are placeholders, **not approved**. All unrelated approved artwork and controls are preserved.
- Verified in Claude environment: direct anonymous `git clone` retrieved exact Alpha2.80 production/archive and `git hash-object` matched; modular split/check passed (9 blocks, 46 assets); four JS scripts passed syntax; headless Chrome 390×844 with mocked backend exercised boss defeat→dawn and orb damage→game over, with no page errors.
- **Not verified:** Android device boss gameplay/balance, live leaderboard, other-night regressions and audio cues. README says Android preview works, but HANDOVER explicitly has no completed Android gameplay test report. Treat player assessment as pending.
- Direct `git clone` is proven **in Claude's container only**. Any new environment must separately verify its access and Git blob SHA. The documented lossless alternative remains available.

## Development branch / test deployment checkpoint (31 October 2026)
- Created branch `dev` from `main`; no boss test has been uploaded.
- The locked WORKFLOW now provides standing authorisation for isolated test-only publishing, not production publishing. `dev:docs/TEST_DEPLOYMENT.md` contains safe deployment requirements.
- **Publishing blocker:** actual GitHub Pages source and existing Actions workflow configuration have not been inspected; a direct dev-branch Pages switch could replace production. Test landing page now committed at `main:tests/index.html` (commit `e58e875cb4e0f20e982351da02b8b50fe89e7117`), but live Pages serving and automated deployment are unverified. Exact boss Test 1 is not in GitHub.
- **First unverified next action:** independently verify Pages serves `/tests/` and inspect Actions/Pages setup before enabling automation. Then recover exact boss Test 1 or generate a new SHA-verified test candidate and publish as a standalone HTML.

## Prior gameplay feedback task (after setup)
**Get user Android gameplay feedback on the Night 3 boss Test 1** (dev panel → Night 3): boss size, node/reactor hit difficulty, orb pressure and any clipping. The private preview does not submit scores. Then plan a scoped Test 2 and deliver a complete standalone downloadable HTML. If the exact candidate is unavailable in a new environment, recover it by an authorised route or rebuild from newly SHA-verified GitHub Alpha2.80, clearly marking it a new unverified candidate. Do **not** imply the uncommitted Test 1 is in GitHub. Do not publish any test or production game without the separate approvals required by WORKFLOW.

## Handover discipline
- At each meaningful development milestone, update this compact state and the detailed [HANDOVER.md](HANDOVER.md) on GitHub with observed evidence, open checks, identifiers and **one** next step; keep the README pointer accurate.
- The full [GAMEPLAY.md](GAMEPLAY.md), [CHANGELOG.md](CHANGELOG.md), [DEVELOPMENT.md](DEVELOPMENT.md), [PROJECT_HISTORY.md](PROJECT_HISTORY.md), [EFFICIENCY_HANDOVER.md](EFFICIENCY_HANDOVER.md) and [MODULAR_WORKSPACE.md](MODULAR_WORKSPACE.md) remain intact and authoritative for their respective scope.
- Avoid placing large HTML, embedded media or complete historical documentation in conversation output. Do not interpret reduced context use as proof that the conversation-length issue is fixed.
