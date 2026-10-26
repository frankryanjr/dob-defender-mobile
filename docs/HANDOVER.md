## Alpha2.80 resumed verification — 26 October 2026 (this session)

- Mandatory README, locked full WORKFLOW and relevant specifications/history/efficiency/modular docs inspected. Read earlier Alpha2.80 entries including existing local Bugfix Test 1 checkpoint.
- Reverified *current* GitHub default-branch production `index.html` Git blob `84f89682b3459577746c7678912a9b9dbcdcf4eb` and Alpha2.79 approved archive `131654b11232190f6470032f01180994bd969b1b`. GitHub HEAD observed `b134452c541d92b856b6d76518e0a834fe29994e` before this documentation write.
- Tested `mcp__GitHub__fetch_blob` with exact production SHA: success, returned 3,782,426 JS characters with valid HTML beginning/end, and confirmed score/cow routines in-source. Direct container GitHub DNS fetch failed; the prior /mnt/data Alpha2.80 Test 1 file from another session is **not mounted in this environment**. Source has not been reconstituted to a locally SHA-verified standalone file in this session.
- Verified defect in production: escape marks cow `dead=true` but `drawCow` has no `dead` guard. Score POST only on `ddFinishGameOver`; catch discards unsuccessful submissions. Live network rejection / itch.io CORS or origin remains unverified. Existing historical local Alpha2.80 Test 1 was previously syntax and startup tested, but local artifact is not available in this session; **do not offer an unverified local link**.
- No gameplay/release files changed or published. **First unverified next task:** recover or reconstruct the exact local Alpha2.80 Test 1 using documented lossless blob-to-local transfer, check complete file SHA against baseline and candidate evidence, then deliver the locally verified downloadable HTML; follow with Android and real endpoint testing. Do not deploy without explicit user approval.

## Alpha2.80 investigation — conversation-limit handover (26 October 2026)

**Current objective:** Fix two user-reported Alpha2.79 issues in a **complete downloadable standalone Alpha2.80 Test 1 HTML** (no production deployment without separate approval):
1. User played several games on itch.io but scores did not upload/update on leaderboard. Trace submission, errors/CORS/origin, server response, leaderboard refresh and account/callsign identity.
2. A cow already abducted returns visually and floats above the ground. Trace abducted/lost state, reuse/spawn, positioning, rendering and rescue/lift/escape transitions. Lost cows must not reappear that night; rescued cows must land properly.

**Verified repository context:** GitHub `main:index.html` Alpha2.79 blob SHA `84f89682b3459577746c7678912a9b9dbcdcf4eb`; exact approved archive `releases/Dob_Defender_Alpha2.79.html` blob `131654b11232190f6470032f01180994bd969b1b`. User confirmed GitHub live/Android playback, and itch.io game playable. Production on GitHub and itch.io must remain unchanged while testing.

**Mandatory onboarding next chat:** Read README, entire locked docs/WORKFLOW.md, docs/HANDOVER.md, GAMEPLAY, CHANGELOG, DEVELOPMENT, PROJECT_HISTORY, EFFICIENCY_HANDOVER, MODULAR_WORKSPACE; follow source verification and archived lossless transfer guidance. The user explicitly mandated **blocker recovery**: search README/workflow/archived procedures/history for previous solved blockers and try proven workarounds BEFORE declaring a blockage or asking user to act as courier. Rule recorded in README and WORKFLOW §2A (commits `1877f7d`, `7c74b8b`).

**What failed:** Connector `mcp__GitHub__fetch_file` for whole production `index.html` and bounded lines 1–30, 100–120, 1000–1020 returned SHA but zero content. Connector `mcp__GitHub__fetch` raw.githubusercontent URL returned HTTP 400 file too large/unsupported. Container direct GitHub network earlier failed DNS. Previously tried historical mounted files were older and must NOT substitute for exact main baseline. Archived WORKFLOW describes a lossless GitHub→Base64→Google Doc→local route, but requires source to retrieve.

**Crucial newly discovered untried method at interruption:** GitHub connector action **`mcp__GitHub__fetch_blob`** accepting `{repository_full_name:"frankryanjr/dob-defender-mobile",blob_sha:"84f89682b3459577746c7678912a9b9dbcdcf4eb"}`. This tool surfaced immediately before conversation ended; **not yet invoked**. Try it FIRST with bounded output (report length, not full blob), then apply documented lossless transfer, and verify exact Git blob SHA locally before editing. Also check alternate connector APIs/transfer records in archived WORKFLOW. Do not repeat identical failed fetch_file attempts without a reason.

**Current status:** No root cause confirmed, no Alpha2.80 game file created, no gameplay code changed. Documentation only. First unverified next step: invoke GitHub `fetch_blob` for exact production SHA, assess source availability, transfer losslessly into /mnt/data and verify byte count/sha; then isolate, fix and test both issues, deliver complete Alpha2.80 Test 1 HTML for user Android/itch-oriented testing without publishing.

## Alpha2.80 Bugfix Test 1 — 26 October 2026, LOCAL TEST ONLY

- **Baseline recovered successfully using mandatory blocker-recovery rule:** GitHub `fetch_blob` on current `main:index.html` blob SHA `84f89682b3459577746c7678912a9b9dbcdcf4eb` returned complete content (where `fetch_file` did not). Lossless transfer used four smaller temporary Google Docs Base64 chunks (Google Docs failed precondition above ~1.5M characters). Local reconstruction is **3,782,476 bytes**, `git hash-object` exactly `84f89682b3459577746c7678912a9b9dbcdcf4eb`.
- **Confirmed cow bug:** UFO successful escape sets `cow.dead=true` but normal night render loops all `cows`, leaving a dead, still-`lift` cow visibly floating. Minimal fix skips `dead` cows while preserving objects for once-per-cow night census/tally.
- **Leaderboard findings:** score submission runs on final game-over transition (`ddFinishGameOver`), not each night; failed POST submissions were discarded, no persistence/retry; scoreboard refresh can overwrite failure messages. **Actual user-reported failure's backend/network cause remains unverified.** Candidate retains pending score locally until acknowledged, retries on leaderboard opening and online event, and displays submission status. Server best-score semantics and auth unchanged.
- Complete standalone test candidate: `/mnt/data/Dob_Defender_Alpha2.80_Bugfix_Test_1.html` (3,783,944 source characters, Git blob SHA `f9d4c96ba19484dda7248dcf4f32398332e06b66`). Four inline JavaScript blocks pass Node syntax checks. Headless Chromium `page.set_content` smoke-test loaded canvas/title with no page JS exceptions. Network score submission, game-over flow and Android visual/gameplay remain **untested**. No game code published to GitHub or itch.io.
- **First unverified next task:** user tests complete local test HTML on Android and reports floating-cow state and score-submission result; separately test leaderboard API response and whether score is better than the registered player best. Fix any real failures in a new candidate. Do not release without explicit approval.

## Alpha2.80 investigation — recovered GitHub blob source (26 October 2026)

- Recovery success: `mcp__GitHub__fetch_blob` with exact current production SHA `84f89682b3459577746c7678912a9b9dbcdcf4eb` returned complete Alpha2.79 HTML (3,782,426 JS string characters, `</html>` present). GitHub `fetch_file` still returned SHA metadata but empty content; the blob interface is the established solution for inspecting source.
- **Important:** Source bytes have not yet been reconstructed into a hash-verified local HTML. The blob response has 3,782,426 characters and includes non-ASCII, so string length is not file byte count. A multi-part Base64 → Google Docs transfer was attempted: one temporary Doc stopped accepting text around 1.5 million characters with HTTP 400 FAILED_PRECONDITION. Smaller segment Docs were created, but full transfer was not completed. A later attempt met connector/tool safety or tool-call limit. Do not claim a complete standalone test candidate or SHA-verified local source yet.
- Source inspection finding: `ddSubmitScore` is called in `ddFinishGameOver` when `ddPlayer` exists. It POSTs `action:'score'`, stored player ID/secret, score, night, and `DD_GAME_VERSION` to Supabase `dob-leaderboard`; failures are caught and displayed using `ddSetMessage`. No submission at every night-end was found in the inspected path. Actual itch.io browser POST and backend acceptance remain unverified.
- Cow inspection: `updateUfo` transitions `level → lift → escape`; sets `cow.dead=true` and `nightOutcome='lost'` after carrier exits screen. `wakeCowsForDawn` resets a cow in `lift` to `stand` without checking whether a carrier remains in escape/lift, so a possible interaction exists. `cowScreenY` calculates lifting/escape positions based on carrier. Diagnose reproduction and preserve falling/rescue mechanics before editing.
- No game modifications, no test release or production publication. **First unverified next step:** reconstruct current main HTML bytes losslessly from blob response into local file and verify Git blob SHA; use multiple bounded Docs/transfer parts or another supported connector transfer. Then instrument the two paths, fix only verified defects, run static/browser tests and deliver standalone Alpha2.80 Test 1 for user testing.

## Alpha2.79 bugs — source retrieval blocked (26 October 2026)

User authorised investigation and construction of standalone Alpha2.80 Test 1 for two issues: (1) itch.io sessions don't submit/update leaderboard scores; (2) an abducted cow returns floating above ground. No fixes are claimed.

- Mandatory README, full WORKFLOW and supporting docs reviewed; consulted archived WORKFLOW proven lossless transfer recipe. Current GitHub `main:index.html` blob SHA `84f89682b3459577746c7678912a9b9dbcdcf4eb` matches Alpha2.79 production release record.
- Tried GitHub connector `fetch_file` for whole file and lines 1–30, 100–120, 1000–1020: connector returned valid metadata SHA but zero content each time. Tried connector `fetch` at raw.githubusercontent.com URL: HTTP 400 'file may be too large or unsupported'. Container Git network attempt failed DNS resolution of github.com. Inspected mounted `/mnt/data`: only historical game versions (Alpha1 and Alpha2.20) present, no exact Alpha2.79 source. The documented Drive/Base64 transfer cannot start because GitHub connector supplies no content to encode.
- Hence exact production HTML bytes and Git hash verification gate could not be satisfied. No source changes, candidate HTML, browser tests or production deployment made. Do **not** use older attached HTML or approved archive in place of main.
- **First unverified next task:** obtain current main's complete 3.8MB source losslessly via a supported connector file transfer or GitHub transfer mechanism; verify Git blob SHA and length, then trace score-submit and cow state transitions. Only then build and syntax-test a complete standalone Alpha2.80 Test 1 for Android, without publishing.

## Alpha2.79 player verification confirmation — 25 October 2026

- User explicitly confirms that Alpha2.79 is live-deployed and has been verified on Android.
- This is a user-reported deployment/device verification, not a fresh independent assistant HTTP, GitHub Actions, or device check. No new code or release artifacts changed.
- Production stays Alpha2.79, `main:index.html` blob `84f89682b3459577746c7678912a9b9dbcdcf4eb`, commit `0925ddac00764ce6fa71ff061d40954e96c41f25`.
- First unverified next task: when development resumes, retrieve and hash-check exact current production baseline per WORKFLOW before making edits; then choose the next scoped change and test it.

## Alpha2.79 production release — 25 October 2026

- **User approval:** “Push it all to prod” for complete Alpha2.79 Leaderboard Button Test 7 (not independently Android-verified after scope fix).
- **Exact immutable approved test archive:** `releases/Dob_Defender_Alpha2.79.html` Git blob `131654b11232190f6470032f01180994bd969b1b` (3,782,528 bytes), release archive commit `949e06e9e164c5410dad57f81bd144d436e77eb6`; re-fetched SHA matches local approved Test 7 exactly.
- **Production:** `main:index.html` Git blob `84f89682b3459577746c7678912a9b9dbcdcf4eb`, production commit `0925ddac00764ce6fa71ff061d40954e96c41f25`. Produced from exact GitHub archive with precisely two label substitutions: HTML `<title>` and `DD_GAME_VERSION` remove “Leaderboard Button Test 7”; no gameplay edits in promotion. Re-fetched production Git blob matches connector response.
- **Changes since Alpha2.78:** start-screen clickable NIGHTS DEFENDED WORLDWIDE badge opens leaderboard, four starting cows, revised once-per-cow dawn saved/lost census, scheduled early UFO abductions, up to two separate-target simultaneous abductors from Night 6, cow splat fade expiry fix, 9% music during tally with 20% normal return, counter label fit; existing +50 rescue and +10 dome reward retained.
- **Known limitation:** worldwide badge sums final-night values from public leaderboard response, not authoritative all-time aggregate; capped records can imply a lower bound.
- **Validation:** four inline JS blocks syntax-checked on Test 7; release archive/local SHA and production label-only changes verified. GitHub Actions status, live Pages HTTP content and Android production gameplay **not independently verified**; environment live HTTP fetch returned inaccessible/cache miss. User to confirm on device. Do not imply completed deployment from successful GitHub write.
- **First unverified next step:** verify latest GitHub Actions Pages deploy/syntax checks and independently fetch served Pages Alpha2.79 HTML; user tests on Android counter → leaderboard → back → START, four-cow abductions/scoring, Night 6 dual UFO, red splats, tally audio. Investigate discrepancies before further code changes.

## Alpha2.79 Test 7 production request — BLOCKED, not released (25 October 2026)

- User explicitly requested "Push it all to prod" for current Alpha2.79 Leaderboard Button Test 7, without separate Android confirmation of the repaired button. Approval request recorded, **but no release performed**.
- Local complete Test 7 exists at `/mnt/data/Dob_Defender_Alpha2.79_Leaderboard_Button_Test_7.html`; `git hash-object` independently verified `131654b11232190f6470032f01180994bd969b1b` against prior checkpoint.
- Blocker: GitHub connector create/update requires complete source string in its runtime; local/container file bytes cannot currently be supplied to that connector through the available interface. Local network access to GitHub fails DNS; Google Drive connector upload requires a connector file URI, not a local path. No archive write, root index update, or Pages deployment attempted. Do **not** treat production as Alpha2.79 or supply a production link for it.
- **First unverified next task:** establish supported lossless local-to-GitHub source transfer (read relevant archived workflow transfer section), write immutable `releases/Dob_Defender_Alpha2.79.html`, verify Git blob matches exact approved Test 7 SHA before any production change, derive label-only production and verify diff, update root, check Actions and served live version. Production Alpha2.78 remains authoritative until independently proven otherwise.

## Alpha2.79 Leaderboard Button Test 7 — fixed JS scope, unapproved (25 October 2026)

- User reports worldwide counter in Test 6 did not open leaderboard. Confirmed root cause in exact Test 6 source: start screen's independent IIFE attempted direct access to `ddOpen` / `ddFinalLeaderboard`, both lexically scoped inside main-game IIFE, so `typeof ddOpen` was `undefined` and click did nothing.
- Generated complete standalone local `/mnt/data/Dob_Defender_Alpha2.79_Leaderboard_Button_Test_7.html` (3,782,528 bytes; Git blob `131654b11232190f6470032f01180994bd969b1b`) from exact local Test 6. Minimal fix exports `window.ddOpenFromStartScreen` from game closure, resets final leaderboard flag and invokes existing `ddOpen(false)`; start-screen listener calls this bridge. Label version advanced to Test 7. No other gameplay changes; production remains Alpha2.78.
- Four inline JS scripts passed `node --check`, full HTML closing tag and Git hash verified. **First unverified next step:** user tests Android counter tap → leaderboard loads → BACK TO GAME returns to splash → START still starts game. No production approval.

## Alpha2.79 Leaderboard Button Test 6 — local unapproved checkpoint (25 October 2026)

- User requested the NIGHTS DEFENDED WORLDWIDE start-screen counter open the existing leaderboard. Local complete HTML `/mnt/data/Dob_Defender_Alpha2.79_Leaderboard_Button_Test_6.html`, 3,782,432 bytes, Git blob `bf5813cc58e4e8390f2ea716c5b693dc4d7402fe`, derived directly from local Counter & Audio Test 5. No production code changed; production Alpha2.78 remains `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`.
- Counter changed from status-only element to keyboard-accessible button semantics and clickable tap target. Click/Enter/Space calls existing `ddOpen(false)` with `ddFinalLeaderboard=false`. Existing leaderboard panel moved above title splash by fixed positioning/z-index 10001; CLOSE retains splash, START remains independent and centered. Worldwide total and gameplay/audio unchanged.
- Four inline JS blocks passed `node --check`, complete HTML closing element and local Git SHA verified. No browser/Android UI testing yet. **First unverified step:** Android user tests counter → leaderboard → CLOSE → START and checks viewport, registration and leaderboard scrolling; fix any behaviour before release. No production approval given.

## Alpha2.79 Counter & Audio Test 5 — local unapproved checkpoint (25 October 2026)

- Built local standalone `/mnt/data/Dob_Defender_Alpha2.79_Counter_Audio_Test_5.html` from local Cow Splat Test 4, Git blob SHA `1df2949cfc0a9c0f6e22f29e881c86a764086856`, 3,781,988 bytes. **No production changes**; production remains Alpha2.78 `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`.
- User requested louder music during night tally and correction of start-screen worldwide counter label overflow. Scoped changes: tally music volume .06 -> .09 (normal .20 on Continue unchanged); smaller label font, remove letter spacing, constrain width/overflow inside badge. START centered and version footer preserved. Four cow, dual UFO, cow splat and score logic from Test 4 preserved.
- Four inline JavaScript blocks passed Node syntax; HTML closing tag and file Git blob SHA checked. Visual layout and Android/music listening not yet tested.
- **First unverified step:** user tests Test 5 on Android for label fit at actual device width and tally music level; verify no night-end tally, four cow, dual-UFO or cow splat regressions. Adjust test candidate if needed. Explicit approval required before production release.

## Alpha2.79 Cow Splat Test 4 — local unapproved checkpoint (25 October 2026)

- User Android screenshot of Test 3 on Night 7 showed persistent red ovals at cow death positions. Exact Test 3 source `drawCow` uses `Math.min(1,c.timer/.45)` and continues drawing after the timer falls below zero. Invalid negative canvas alpha is ignored, leaving prior draw alpha and an indefinitely rendered mark. Cow state remains splat to preserve tally census; no code removal is needed.
- Complete standalone `/mnt/data/Dob_Defender_Alpha2.79_Worldwide_Nights_Cow_Splat_Test_4.html`, 3,781,873 bytes, Git blob SHA `0a911c2bade99a7f0b60b61c94f432a233d1db36`, based on local unapproved Dual UFO Test 3. Minimal `drawCow` fix: return if `c.timer<=0`; clamp alpha to [0,1]. Retains cow census, four cows, dual UFO abductions from Night 6 and worldwide badge. Four inline JavaScript blocks pass `node --check`; closing HTML verified. No browser/Android test of new candidate yet.
- **First unverified step:** Android play Test 4, confirm red ovals fade/disappear following cow deaths (including Night 7) and the end-of-night saved/lost tally remains correct. Production Alpha2.78 unchanged; explicit approval required for release.

## Alpha2.79 Worldwide Nights Dual UFO Test 3 — local unapproved checkpoint (25 October 2026)

- Local candidate `/mnt/data/Dob_Defender_Alpha2.79_Worldwide_Nights_Dual_UFO_Test_3.html` (3,781,758 bytes), Git blob SHA `d21de160b6d8ffd64d21065012e60ddc0490b95a`; derived from Cow Tally Test 2, **not** published. Production still Alpha2.78 `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`.
- From Night 6 onward at most two active abduction UFOs; independently reserved cows via `selected`, staggered paired event schedule, carrier-specific position, kill/rescue/escape handling and end-of-night active-UFO gate. Nights 1–5 retain one abductor. Additional later-night opportunities retained. Four cows, cow outcome tally, worldwide counter retained.
- Four inline JavaScript blocks passed Node syntax; complete HTML closing element and SHA checked. Browser/Android gameplay **not verified**. User must check dual concurrent arrivals/beam lifting, different target cows, shooting one while another continues, escaped cows lost once, and tally transition. No production release approved.
- **First unverified step:** Android gameplay test this exact Test 3 candidate; diagnose/fix any overlap, collision, abduction and tally symptoms with a new standalone build. Do not publish game code without explicit approval.

## Alpha2.79 Cow Tally Test 2 local checkpoint — 25 October 2026\n\n- Production remains Alpha2.78 (`main:index.html` Git blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`); no game code published. This checkpoint records the **new local** candidate, not approval.\n- Complete standalone local candidate `/mnt/data/Dob_Defender_Alpha2.79_Worldwide_Nights_Cow_Tally_Test_2.html`, 3.78MB Git blob `bf81ac694cb9a26b3441dd7ebf31132118923eba`. Based on previous local worldwide counter Test 1 which came from exact verified production. Four unique cows per night; no replacement spawns; guaranteed scheduled abduction event night 1 and 2; later increased UFO opportunities. Night-end tally enumerates surviving/lost cow states once: +25 alive; -25 dead, killed, abducted. Immediate +50 rescue and +10 dome recovery preserved.\n- **Known limitation**: only one active abductor can run at once; two simultaneous different-target abductions not yet implemented. The worldwide counter uses returned leaderboard best-night values, not a verified all-time server aggregate.\n- All four inline JavaScript blocks passed Node syntax; no browser simulation or user Android test completed.\n- **First unverified step**: user test standalone Test 2 on Android for four cows, night 1 abduction, rescue/loss tally, continued nights, worldwide counter fit and tally transition. Investigate failures and produce revised complete candidate; do not promote to production without explicit approval.\n\n## Alpha2.79 Worldwide Nights Counter Test 1 — local candidate (25 October 2026)

- Fresh development from exact approved production Alpha2.78 `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`, verified local 3,778,502-byte reconstruction with matching `git hash-object`; **no abandoned Alpha2.79 cow/UFO candidates used**.
- Standalone `Dob_Defender_Alpha2.79_Worldwide_Nights_Test_1.html`, 3,780,511 bytes, Git blob `6873508b50e977b6a2f408f884fe06873d0017ad`. Delivered locally for Android testing; NOT pushed to GitHub or production. Four inline JavaScript blocks passed `node --check`. No browser/Android rendering or functionality testing performed.
- Counter sits left of centered START (poster-relative left 5.5%, width 23%, top 86%, height 6%); dark translucent fill, clipped fully rounded cyan/blue outline, two-line label, cyan total, no globe; bottom version footer preserved. Reads existing public `dob-leaderboard` endpoint and sums returned `best_night` rows; failures show dash. Existing response is capped at 50 rows, so counter uses a '+' marker at that limit. **Important scope caveat:** this is a sum of ranked players' highest-night values, NOT all game sessions or necessarily a truly exhaustive historical worldwide nights count. A separate aggregate backend would be needed for that stronger definition.
- **First unverified step:** user opens standalone Test 1 on Android, checks counter placement/scale and live number and verifies START and footer. Clarify whether best-night leaderboard aggregate is acceptable or true all-session worldwide counter is required; if latter, plan and test a read-only aggregate backend without changing production until approved. User approval remains required for release.

## Fresh Alpha2.79 Worldwide Counter Test 1 — 25 October 2026 (NOT RELEASED)

- User explicitly abandoned earlier Alpha2.79 cow/UFO and worldwide Test 4 candidates. Restarted from **exact current production Alpha2.78** main:index.html Git blob SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`, 3,778,502 bytes, reconstructed using 13 bounded Base64 Google Docs segments, repaired and verified with local `git hash-object` before editing.
- Created complete local Android-test HTML `Dob_Defender_Alpha2.79_Worldwide_Counter_Test_1.html`, 3,780,528 bytes, Git blob SHA `5099a6ccebf03713f9dd09eeb5a0fa7b8018ba70`. **Not published to GitHub or production.** Preserves centered START, adds no-globe left counter of equal height with blue rounded clipped border, dark fill, stacked label and cyan number; existing bottom version preserved. Four inline JS blocks pass Node syntax checks. Browser rendering and Android testing NOT performed.
- Counter reads public leaderboard GET `scores`, sums `best_night` for returned player-best records, appending `+` at 50-record cap; offline shows dash. **Limitation:** this is not a verified all-time global sum of every completed night or submission. Backend authoritative aggregate will be required for a guaranteed true worldwide all-time figure. Production and backend unchanged.
- **First unverified next task:** user Android tests Test 1 appearance/START/version and loading behaviour, then design/read-only verify an authoritative backend total across all actual defended nights before representing the number as an exact all-time worldwide total. Obtain approval before any production release.

## Alpha2.79 Cow/UFO — Worldwide Nights Defended Test 4 checkpoint (25 October 2026)

- Exact starting production remains Alpha2.78 `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`; the local production source was previously reconstructed and Git-blob verified byte-for-byte. Test 4 carries forward the Alpha2.79 cow/UFO test changes and updates the start-screen badge.
- Complete standalone candidate `Dob_Defender_Alpha2.79_Cow_UFO_Nights_Defended_Test_4.html`: 3,780,736 bytes, Git blob SHA `1adeb31800f6a3d5f2ecb1e333821981f0da686c`. Badge reads “NIGHTS DEFENDED” with a globe, left of START, and sums the returned records’ final-night values. Current database has 27 accepted submissions totaling 157 nights. The current public endpoint returns at most 50 records; once capped, the badge appends “+” to show the sum is a lower bound until a server-side aggregate endpoint is added. Test submissions are rejected by the production version-format rule and do not affect the total.
- All three inline JavaScript blocks pass `node --check`; complete HTML closing tag verified. Browser rendering and Android visual/gameplay testing remain unverified. No production game code or backend function changed.
- **First unverified next task:** user tests Test 4 on Android, checking the badge fits left of START and the number shows total defended nights; also recheck cow/UFO mechanics. If approved, prepare the separate production release and any required aggregate-endpoint change under the release workflow. No release is authorized yet.

## Alpha2.79 Cow/UFO Test 1 — reconstructed candidate checkpoint (25 October 2026)

- Verified production `main:index.html` Alpha2.78 Git blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`; losslessly reconstructed 3,778,502 bytes with matching `git hash-object` from 13 temporary Drive transport parts. Root production was **not modified**.
- The historical Test 1 candidate (`6b9a7f91b47521b54bef783438dd5a0d440360e2`, 3,779,420 bytes) was not found in attached/container/Library files. Rebuilt from exact production instead: locally created complete `Dob_Defender_Alpha2.79_Cow_UFO_Test_1_Rebuilt.html`, 3,779,351 bytes, Git blob `09000256f99a480c89b764ffc48cd4348a6fef40`. **Different SHA from historical candidate: not an exact recovery.**
- Rebuild intent: four cows per night from Night 1, +25 surviving/-25 lost once per cow, retain immediate +50 rescue and +10 dome; guarantee a Night 1 abduction; later concurrent two-UFO different-cow targeting from Night 6. Preserved existing artwork and unrelated source. All 3 inline JavaScript scripts passed `node --check`. Chromium local file navigation blocked `ERR_BLOCKED_BY_ADMINISTRATOR`; no browser game simulation or user Android validation passed.
- **First unverified next task:** deliver and test rebuilt standalone HTML on Android; confirm four visible cows, Night 1 abduction, later separate-target dual UFOs, lost cow tally and score, rescue/dome bonus, end screen and regression. Fix based on feedback and repeat checks. Never publish test or production without relevant explicit permission and release gates.

## NEW-CHAT RESTART — Alpha2.79 cow/UFO test (25 October 2026)

- **Current production:** Alpha2.78, `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`; approved archive `releases/Dob_Defender_Alpha2.78.html` blob `168c505247fa450a64824d6a9c706b3d82aef3ef`. User confirmed production live. No Alpha2.79 deployment authorised.
- **User-approved test scope:** exactly four unique cows per night starting Night 1; +25 per survivor, -25 per cow killed/escaped abducted, with each cow counted only once. Keep immediate +50 rescue and dome +10. Guarantee one Night 1 cow-abduction attempt, scale UFO frequency later; two simultaneous abductors at later stages must choose separate cows. Preserve artwork, gameplay outside scope and tally audio.
- **Latest recorded development checkpoint:** `docs/OPEN_FIXES.md` records a standalone `Dob_Defender_Alpha2.79_Cow_UFO_Test_1.html`, 3,779,420 bytes, Git blob `6b9a7f91b47521b54bef783438dd5a0d440360e2`, built from SHA-verified production. Three inline JS scripts passed syntax tests; actual browser/Android behavior **not verified** (local browser access was blocked). This candidate has **not** been approved or uploaded to the repo.
- **Availability caveat:** At this new-handoff checkpoint the above candidate **was not present** under `/mnt/data` in the active container. Its SHA is a documented historical checkpoint, **not** evidence that the file is presently retrievable. A local `prod_check.html` exists but earlier SHA differed from production; **never use as baseline** without exact SHA verification.
- **First unverified next step:** check whether the exact Test 1 candidate is accessible in new-chat attachments/Files/working filesystem and verify its Git blob `6b9a7f91b47521b54bef783438dd5a0d440360e2`. If absent, retrieve/reconstruct current production from GitHub by the WORKFLOW-proven lossless method, validate SHA, then recreate and validate the candidate from documented scope. Deliver **complete standalone test HTML** for Android. Do not publish to production until Android test and explicit user approval followed by archive/SHA/deployment gates.
- **Startup:** Read README and full `docs/WORKFLOW.md`, then current HANDOVER, GAMEPLAY, CHANGELOG, DEVELOPMENT, PROJECT_HISTORY, OPEN_FIXES and task-specific efficiency handovers from GitHub. GitHub remains authoritative; follow workflow rather than treating this note or older uploads as a verified source.

## Alpha2.79 cow/UFO test — started, not yet built (25 October 2026)

User authorised development of four cows per night, night-survival saved/lost tally, one guaranteed Night 1 abduction, increasing later UFO pressure with two concurrent different-target UFOs. Production remains Alpha2.78 SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`. Current README/WORKFLOW/HANDOVER/GAMEPLAY/CHANGELOG/DEVELOPMENT/PROJECT_HISTORY/OPEN_FIXES/EFFICIENCY_HANDOVER/MODULAR_WORKSPACE reviewed. GitHub `fetch_blob` returned complete content length 3,778,456 characters but no verified local transfer yet. Local `/mnt/data/prod_check.html` exists but SHA `4dc6ee1db20f74a91738f08dcbb5159899b7be38` does **not** match production; do not use it as baseline. **First unverified step:** transfer exact current GitHub blob to local by documented bounded Base64/Drive procedure, verify `git hash-object` matches `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`, then inspect cow spawn/UFO scheduler/cow death and tally paths, implement scoped test candidate, run syntax/behavior checks and deliver complete HTML for Android. No game code changed or deployed; no user test available yet.

## Current release: Alpha2.78 — 25 October 2026

User tested and approved Tally Audio Test 2 ("Perfect push to prod"). Exact archive `releases/Dob_Defender_Alpha2.78.html`, SHA `168c505247fa450a64824d6a9c706b3d82aef3ef` (3,778,569 bytes) matches approved file. Production is `main:index.html` SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`, commit `7db1c86f8c0df0850cf88e367876585f8342e0d2`, derived with release-label/comment-only edits. Effects: bar rise tones, rapid score clicks, saved cow ping, lost cow dud, deduction depletion; louder tally mix and music duck from 20% to 6% during tally, restoring after Continue. Scoring mechanics unchanged; user cow-related requests remain open in `docs/OPEN_FIXES.md`. Independent Pages live HTML/device verification outstanding until separately confirmed.

## Current release: Alpha2.77 — 25 October 2026

User approved Audio Mix Test 3 and explicitly directed production push. Exact approved test archive `releases/Dob_Defender_Alpha2.77.html` Git blob `0d4fcefdaf6d9ac3208c6236c90931b40b7e95d9`, 3,776,589 bytes. Promoted by four label/comment-only replacements: HTML title, DD_GAME_VERSION and two comments, yielding production `main:index.html` blob `ae484817ab23bb3895dca9806f957c2688827b1e`, commit `6d732ec905915f0e997c442317a335c7f6759f1c`. All three inline JS scripts Node syntax checked. 31 active sound audition levels approved with meteor hit 0.60 and slew 0.32; 46 embedded clips retained, candidate removal list of 15 remains unacted on. No changes to approved game artwork/scoring/leaderboard. Confirm GitHub Actions and live Pages independently; obtain user production Android confirmation after deployment. Full details in CHANGELOG.

## Alpha2.75 — 24 October 2026 — approved Test 5

- **Approval:** User confirmed “All working. Push to prod” for Alpha2.75 Test 5, including Chrome Incognito playback and music.
- **Immutable approved archive:** `releases/Dob_Defender_Alpha2.75.html` (blob `51a1a99c514b932270a4afd76d13c5192bd24ed8`), identical to tested `tests/Dob_Defender_Alpha2.75_Test_5.html`.
- **Production:** `main:index.html`, release commit `de1fd741b9096dffef6fa59448df96aa9ccf749c`, blob `c101c9609bef5b606dc2c61957a3aca587c96e78`. Differences from approved archive are **only** the HTML document title and `DD_GAME_VERSION`, removing “Test 5”.
- **Changes:** New-player callsign gate with generated callsign or 3–18-character custom entry, DEFEND! starts Night 1; returning players with saved identity bypass registration. One looping background track `DobDefGame2.mp3`, 20% volume, first-interaction fallback for autoplay restrictions, pause/resume integration. Existing approved telescope, title artwork, gameplay, controls, scoring, sounds and leaderboard preserved.
- **Testing:** JavaScript syntax checked for candidate; user confirmed Test 5 working in Chrome Incognito. Independent Android end-to-end and production live-page verification pending.
- **Production URL:** https://frankryanjr.github.io/dob-defender-mobile/?v=Alpha2.75

## Alpha2.74 — 23 October 2026 — sound release handover

- **Approved test:** `Dob_Defender_Alpha2.73_Sound_Test_5.html`, explicitly approved by user for production.
- **Immutable archive:** `releases/Dob_Defender_Alpha2.74.html`, SHA `e008527ad54663e5b0e063b19653e93450e5f297`.
- **Production:** `main:index.html`, commit `585712ed4981752f68dd88cab4f2997389647654`, blob `e59a59f3a30881d8466a71f0e336eb4a6a459654`.
- **Audio:** Embedded edited recordings: laser fire, comet destroyed, ground impact. No meteor-destroyed or asteroid-destroyed audio. Preserve approved Alpha2.73 gameplay, telescope, controls, art, leaderboard, scoring and collisions.
- **Only differences from exact tested archive:** title and `DD_GAME_VERSION` set to clean `Alpha2.74`.
- **Testing:** User approved test candidate; independent assistant Android test not performed. Live deployment and production Android verification to be recorded separately.

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

## Alpha2.70 — 19 October 2026 — approved Test 8

- Source of truth: branch `main` root `index.html`. Immutable approved archive: `releases/Dob_Defender_Alpha2.70.html`. Both verified identical Git blob `b464c01399c78370c2ecaccba7862cc439069bed`.
- User approved Test 8 after confirming the stationary dome erasure animation works on Android. Earlier Tests 4–6 wrongly moved or shrank the dome; Test 7 lacked vertical walls; Test 8 restores the walls and erases the fixed arch from apex to ground.
- Other retained changes: hit score popups no longer freeze at dawn; moon removed; top-right in-play leaderboard button removed; cows drawn over dome walls.
- Production HTML commit `7421e3f23ae138cde4a9cb585b5adc3d2f5ad634`. Test 8 archive intentionally retains its original internal labels, including an older HTML title.
- Preserve approved telescope, title art, controls, collisions, leaderboard access on final results and all unaffected mechanics.
- User Android testing: Test 8 dome animation passed. No assistant-run Android end-to-end test. Check GitHub Pages deployment and ask user to verify the new production URL.

# Alpha2.69 production handover — 18 October 2026

**User verification (18 October 2026):** User confirmed Alpha2.69 production game worked on their device after successful GitHub Pages deployment. This is user-reported Android/device validation, not an assistant-run device test.

**Approved source:** `releases/Dob_Defender_Alpha2.69.html` is the exact user-approved Alpha2.69 Test 18 file, preserved permanently. **Production source:** `main:index.html`, copied from that archive with only visible/internal version identifiers changed from TEST 18 to Alpha2.69. **Prior production:** Alpha2.68, retained for rollback.

**Approved changes:** animated night-end and final Game Over tallies; saved/lost cow adjustments; persistent final Game Over with VIEW LEADERBOARD and PLAY AGAIN; background leaderboard submission without redirect; obsolete night overlay removal; dev power-up guarantee; HUD and dome feedback fixes; ground-impact shake; varied shrinking space junk and atmospheric burn-up.

**Locked and preserved:** Start Screen v1 artwork, approved Dobsonian telescope drawing and mobile thumb controls; underlying shooting, collisions, cows, aircraft and leaderboard mechanics except changes explicitly documented for Alpha2.69.

**Release process learning:** local generated HTML can be transferred through the Files reader to GitHub file-write operations. Reconstruct full content, compare exact length/checksum to local approved file, archive permanently first, then use the archive as the production source. No user download/reupload is required.

**Testing:** file integrity verified; code-level validation does not establish Android gameplay testing. Verify GitHub Pages separately and request user Android confirmation. Continue to track any issues observed on device.

> **CURRENT PROCESS AUTHORITY:** [WORKFLOW.md](WORKFLOW.md) governs all new-chat onboarding, standalone HTML testing, explicit user approval, and production publishing. Historical instructions and version labels below are reference only when they conflict with WORKFLOW.md. Approved production: Alpha2.68 at branch `main`, root `index.html`. Alpha2.69 is unapproved. Do not commit or publish tests by default.

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

# Alpha2.7: Cow survival during tractor-beam lift (12 October 2026)

- UFO destroyed before lift begins: cow is saved as before.
- UFO destroyed during the slow tractor-beam lift: cow drops with animated kicking legs, lands safely, resumes standing, awards COW SAVED (+50) and repairs dome by 10%.
- UFO destroyed during its rapid upward escape: cow drops with kicking legs and dies in the existing red, fading SPLAT! effect. No rescue reward.
- Direct laser hit on the cow remains fatal.
- Gameplay and the locked telescope/relative steering are otherwise unchanged.
- JavaScript syntax checked; Android gameplay still needs testing.

---

# Alpha2.6 Handover Update

Latest playable candidate: `Dob_Defender_Alpha2-6.html`

Alpha2.6 changes: enforce a central telescope exclusion zone for cows; accelerate early-night pacing; vary comet nucleus/tail size (small, medium, large) and soften the curved tails; introduce occasional three-hit large asteroids with distinct large, medium and smallest stages. The 35-shot mandatory budget includes extra large-asteroid hits.

**Testing:** JavaScript parsed successfully with `node --check`. Android touch gameplay, complete wave simulations, and rendering remain to be tested.

**Preserved:** Approved telescope artwork, tap sky to fire, compact relative-swipe steering, UFO/cow interactions, ISS, aircraft warning, Starlink interference and prior releases.

---

> **Current playtest build:** Alpha2.3 (`Dob_Defender_Alpha2-1.html`), derived from Alpha2. Original Alpha1 and Alpha2 files are preserved.
> **Verification:** JavaScript syntax passed; browser runtime test blocked by environment restrictions. Awaiting Android feedback.

# Dob Defender: Project Handover and Development Log

**Project:** Dob Defender  
**Latest playable build:** Alpha2  
**Latest HTML:** `Dob_Defender_Alpha2-1.html`  
**Previous preserved baseline:** `Dob_Defender_Alpha1-2.html` (uploaded Alpha1 iteration)  
**Companion gameplay specification:** `Dob_Defender_Alpha2_Gameplay_Spec.md`  
**Last updated:** 12 October 2026  
**Status:** First playable Alpha2 prototype, browser smoke-tested, awaiting full mobile gameplay balancing

## 1. Instructions for the next developer or AI chat

Read the newest numbered HTML, this handover and the Alpha2 Gameplay Specification before editing. The latest HTML is the implementation baseline, while this handover and the specification record approved intent. Preserve prior HTML files instead of overwriting them. Never replace just a function as the final user deliverable: provide a full playable game and a downloadable standalone HTML, alongside an updated handover whenever a milestone is saved.

**Locked design:** The Obsession-style truss Dobsonian is approved artwork. Do not redesign the UTA, laser, bearing, mirror box, cradle, trusses or small scale. Preserve the aiming slider and compact translucent FIRE button. No third-party assets or runtime network dependencies. Focus on Android/mobile usability. Do not include em dashes in game-visible text.

**Important source note:** The provided Alpha1 iteration is named `Dob_Defender_Alpha1-2.html` in this project. The older historical handover referred to an emailed file `Dob_Defender_Alpha1.html`. Both references designate Alpha1-era development, but only the actual uploaded baseline was edited to create Alpha2. Do not assume the older emailed file exists in this workspace.

## 2. Current playable Alpha2 game

The player operates a small, side-on, brown truss Dobsonian telescope under a starry sky, adjusting aim with a thumb slider and shooting a green laser from its side-mounted pointer. Each level is a **NIGHT**. A four-second dusk precedes a scheduled wave of hazards. All required threats must be resolved before a five-second dawn with a four-second **SURVIVAL!** results panel. Each subsequent night starts with 100 laser energy and 100 shield. Score is cumulative. After Night 10, play continues indefinitely with a 160% maximum baseline speed and four active mandatory hazards at once.

Alpha2 replaces the historical Alpha1 lives system with a faint observatory dome. Meteors cost 20% shield, full asteroids 35%, their fragments 15%, and comets 30%. A destroyed dome makes the observatory vulnerable to one more hostile impact. Rescuing a cow restores 10 shield, including rebuilding from zero. An intact-dome bonus is only for nights with zero impacts.

FIRE is **one laser shot per tap**, costing 2 of the 100 starting energy. No auto-fire when held. Zero energy disables the laser without ending the night. Mandatory threats require no more than 35 perfect shots. Asteroids require two hits; the first halves their diameter, creates dust and increases fragment speed by 20%. Comets are slower than meteors and asteroids, with occasional harmless flybys.

UFOs: one harmless pass on Night 1, another on Night 2, then a guaranteed cow abduction attempt on Night 3. Random abduction encounters follow: at most one on Nights 4-5, two on Nights 6-8, three from Night 9. Up to three cows may independently enter, graze, kneel, sleep with Zzz, and depart. A three-second rescue window ends when the cow lifts off. Early UFO hit saves cow for +50 points and +10 shield; late hit yields comic SPLAT; an escaped abduction costs 10 energy.

An ISS pass may appear at most once a night. At 1-25 energy its selected probability is 45%, with lower odds at higher power; one successful hit restores +40 energy, capped at 100. The first ISS pass pauses for an instruction and user-tapped OK; later alerts flash twice without pausing. Friendly aircraft blink red and green. Their first appearance shows the embedded cartoon pilot warning; a hit carries a -10 extra-energy penalty. Starlink trains have 12 equally spaced lights in a straight line; destroyed satellites leave gaps, and a 35% chance second pass can return the survivors in reverse direction.

The scoring and full timing tables are in `Dob_Defender_Alpha2_Gameplay_Spec.md`. The results screen shows cows saved and accuracy at dawn; Game Over shows score, nights survived, cows saved and accuracy, with PLAY AGAIN.

## 3. Historical Alpha1 mechanics (superseded where noted)

Alpha1 started with 3 hearts, score-based levels (1 + floor(score/400)), random continuous spawning and repeated fire when held. Its old object scores were satellite 5, meteor 15, asteroid 20, comet 30 and UFO 50. Alpha2 deliberately replaced these rules with scheduled nights, shield/energy economy, single-shot taps and the approved Alpha2 point table. Use the Alpha1 code only as the preserved reference for telescope geometry, side laser origin, visual language and input-slider mathematics.

## 4. Approved telescope art — preserve unless instructed otherwise

**The telescope artwork was refined through many user screenshots and red annotations. The latest approved geometry is in the Alpha1 HTML. Do not reintroduce superseded designs.**

### Appearance

- Telescope is a **side-on stylised vector illustration** of a large wooden Obsession-type truss Dobsonian, not a conventional solid-tube telescope.
- **No astronomer/person.**
- **UTA:** short rectangular/cylindrical-looking upper cage represented in brown timber, with light brown top and bottom rings. Simple round dark focuser on its front. No black bar across the top and **no laser beam from the middle of the UTA**.
- **Green laser:** small green device vertically fixed on the UTA's right edge; green shots fire in the direction in which the whole telescope is aimed. The green tip should remain aligned to the actual firing origin.
- **Trusses:** four silver/grey poles. Two outer mostly parallel poles, plus two inward-angled poles. They form two V-like diagonal lines, **NOT an X**. Avoid crossing the middle pair.
- **Mirror box:** short wooden brown rectangular top with circular/rounded lower profile. In the final design it is intentionally compact, not a tall square box; the long truss poles connect directly to its upper edge. The large upper rectangle drawn in early versions was removed after the user marked it with an X.
- **Altitude bearing/quadrant:** a bright silver curved strip attached to the outside/front side of the moving brown mirror box, running around its rounded bottom. It must not look like a disconnected ring floating in the stationary wooden base.
- **Fixed cradle:** a narrow brown wooden box with short, minimally raised ends and an accurately circular inward U-shaped seat. It sits flat on the ground, without extra pivots, separate side rectangles or other invented hardware. The moving mirror box and its silver bearing sit **inside and behind** the fixed base's front face.
- Preserve the relative look and colors established in Alpha1. This is a deliberately simplified game vector, not a photorealistic render.

### Important mechanical model

The real Dobsonian uses two motions: altitude pivots of the optical assembly against the rocker, and azimuth rotation of the rocker on a ground board. **This game is a side-on 2D approximation of the altitude pivot only.** The user repeatedly clarified that the **wooden base/cradle remains fixed**, and the mirror box, bearing, trusses, UTA and laser must **all tilt together**.

The bearing and the wooden seat have **concentric circular geometry** so rotation cannot make the bearing drift or float away from the cradle. The center of these circles is the telescope's rotation pivot. The moving elements render first and the fixed front cradle renders last to create the proper depth and occlusion.

### Actual Alpha1 geometry (verify against accompanying HTML)

The current `.html` declares:

```js
const BR = 40;           // moving circular mirror-box/bearing radius, logical units
const CR = 43;           // fixed cradle cutout radius
const BASE_BOTTOM = 57;  // cradle floor, logical units below pivot
const BASE_TOP = 13;     // height of abbreviated upper ends
const BASE_HALF = 49;    // fixed cradle half-width
const floor = () => H - 86;
const scale = () => Math.min(.43, Math.max(.19,
  Math.min(H * .125 / 272, W * .34 / 102)));
const origin = () => ({x: W / 2, y: floor() - BASE_BOTTOM * scale()});
```

The **Alpha1 small scale is intentional** and was the latest explicit request. In the reference screenshot the user labelled A as the scope's then-current full height and B as the desired much shorter full height. The telescope was reduced to roughly 25% of the earlier on-screen height while the full-size background and controls stayed in place. Maintain that small scale unless a newer user request changes it.

The telescope function rotates all moving parts by `angle + π/2` using `canvasContext.rotate`, so straight-up (`-π/2`) corresponds to rotation zero. The mirror-box lower edge uses a circular arc based on `BR`, and the fixed base uses a circular cutout based on `CR`. Exact drawing positions, stroke widths, and order are in the HTML.

**Artwork caveat:** The compact illustration is an approved stylised representation, not mechanically rigorous CAD. If new tweaks are requested, keep the shape familiar, the silver bearing visibly attached to the mirror box, and the fixed cradle in front of the lower moving unit. Do not 'fix' the result by adding extra blocks, pivots or an oversized upper mirror box.

## 5. Alpha2 implementation and visual style

Alpha2 remains one standalone HTML canvas application with inlined CSS, JavaScript and an embedded compressed WebP of the aircraft safety popup. Canvas uses devicePixelRatio scaling, adaptive viewport dimensions and Pointer Events. The approved original `telescope()` implementation is preserved verbatim. The game has explicit title, dusk, night, tutorial, dawn and game-over states. Night objects use a capped group scheduler and segment-based laser collision test. The Moon, twinkling stars, hills, green ground and small telescope artwork remain in the original style, with the addition of a dome, cows, aircraft and ISS.

**Smoke testing:** Chromium with 390 x 844 mobile viewport and other portrait sizes, JavaScript syntax verification, pointer firing checks, tutorial OK interaction, energy and score checks, simulated wave-to-wave advancement, game-over and no-energy behaviours have been performed. See the Alpha2 specification's test section for scope. Android hardware gameplay and campaign-wide balancing have NOT yet been completed. Do not claim they have.

## 6. Known limitations and follow-up work

- Full thumb-control balancing of Nights 1-10 and endless mode is not yet validated on actual Android hardware.
- Optional event timing, small satellite hitboxes, cow rescue hitboxes and partial-dome shielding may require tuning through playtesting.
- There is no sound design, cloud high-score service, pause/settings screen, or PWA install flow.
- Current game is a first playable Alpha2 version, not a final release.
- All source changes should be assessed for regression of the exact telescope rendering, side laser origin, impact rules, accurate shot counting, pause/resume behaviour, dawn transitions and restart.

## 7. Historical design and change log

The versions below reflect the **development conversation**, not a rigorously tagged source-control history. `v9`–`v28` were iterative chat/game previews, and the only formally packaged emailed baseline is **Alpha1**.

| Stage | Summary / design decision |
|---|---|
| Initial concept | Astronomer aims Obsession-style Dobsonian; shoot meteors, comets, asteroids, UFOs and satellites with attached green laser. |
| Early gameplay | Make mobile game: thumb-angle control and tap to fire. |
| Control refinements | Switch to lower-sensitivity horizontal slider (line and ball), smaller transparent fire button, full-size screen. |
| Artwork simplification | Remove the man; shrink the telescope; use realistic Dobsonian proportions. |
| Telescope identity | Replace generic tower/tube with short brown UTA, open silver trusses, lower mirror box and rocker/base. |
| Truss corrections | Middle poles must angle inward rather than forming a large crossing X. |
| Laser correction | Laser must fire from small pointer on **side** of UTA; remove centre beam and black bar atop UTA. |
| Base corrections | Narrow, compact fixed wooden base with concave circular U-shaped seat. Remove extra rectangular pivot blocks and unnecessary wood pieces. |
| Layering corrections | Brown mirror box, bearing, trusses and UTA rotate together; stationary wooden cradle is drawn in front of lower moving components. |
| Bearing corrections | Silver curved metal altitude bearing belongs on the **front/side of the moving mirror box**, not painted into the fixed cradle or below it. |
| Mathematical correction | Establish shared centre and circular arcs for moving bearing vs fixed circular seat. |
| Mirror box refinement | Remove tall upper part of box, leave a short brown mirror box and longer poles. |
| Base height adjustment | Temporarily deepen fixed base, then trim surplus width/side heights/bottom per red annotations. |
| Approved art | User asked to **save the telescope design**; this became the reference artwork. |
| Scale corrections | User clarified A = telescope's then-current full height; B = **desired new full height**, much smaller. Final Alpha1 uses this compact size. |
| **Alpha1 — 2026-10-12** | Packaged as `Dob_Defender_Alpha1.html`, standalone playable mobile browser game; title **Dob Defender**. Alpha1 was emailed to `frankryanjr@gmail.com` with the HTML attached. |

## 8. Release tracking

| Version | Date | File | Status |
|---|---|---|---|
| Alpha1 | 2026-10-12 | `Dob_Defender_Alpha1-2.html` (uploaded baseline) | Preserved Alpha1-era file; historic Alpha1 was reported emailed under `Dob_Defender_Alpha1.html` |
| **Alpha2** | **2026-10-12** | **`Dob_Defender_Alpha2-1.html`** | Playable initial feature build, syntax and browser smoke-tested; awaiting hands-on Android balancing |

## 9. Alpha2 milestone changelog (12 October 2026)

- Added dusk and dawn cycle, fixed-sized night wave schedules, NIGHT level HUD and SURVIVAL results overlay.
- Added 100-point laser capacity with 2 points per shot and single-shot FIRE; maximum 35 mandatory accurate shots.
- Replaced Alpha1's three-heart system with 100-point protective dome, object-specific impact damage, cracks, red warnings and vulnerable final hit.
- Added full laser and dome restoration at the start of every night.
- Changed meteor, asteroid and comet speeds and scoring; introduced small 20%-faster asteroid second fragments and dust.
- Added random independent grazing, wandering and sleeping cows, plus UFO flybys and timed abduction/rescue/SPLAT outcomes.
- Added first guaranteed cow abduction on Night 3 and increasing later UFO encounter caps.
- Added ISS passes with low-energy weighted chance, +40 recharge and first-time OK tutorial, plus twice-flashing later alerts.
- Added occasional aircraft with red/green wing lights, -10 energy extra penalty and embedded illustrated first-time safety popup.
- Changed 12 detailed satellite sprites to evenly spaced Starlink-style points with a possible 35%-chance survivor-only return pass.
- Added per-target scoring, night survival/intact-dome/accuracy bonuses, complete Game Over statistics and replay.
- Kept approved Alpha1 telescope drawing function verbatim and preserved the compact mobile slider and circular FIRE control styling.
- Added game test observations, known limitations and Alpha2 specification file.

## 10. Starting prompt for a new chat

> Continue **Dob Defender** from `Dob_Defender_Alpha2-1.html`, with `Dob_Defender_Project_Handover.md` and `Dob_Defender_Alpha2_Gameplay_Spec.md`. Read all of these before development. Alpha2 is the newest playable first-build version; do not overwrite Alpha1. Preserve the exact small Dobsonian telescope, side-mounted green laser, fixed cradle, thin thumb slider and compact FIRE button. Follow the gameplay specification and changelog, avoid em dashes in all game-visible copy, check mobile pointer control, collisions, resource budgets, score, pause/tutorial behaviour, dusk/dawn and game-over/restart. After each change, provide a complete updated playable game and updated downloadable documentation.

---

**End of Alpha2 handover.**


## Alpha2.3 changes, 12 October 2026

User playtest of Alpha2 found that cows left after sleeping, early nights were too slow, the FIRE button was less convenient than tapping the sky, and aiming felt sluggish. Starlink satellites unintentionally intercepted hostile-target shots, which the user explicitly wants to keep.

Changes: sleeping cows persist until abduction or dawn; early wave density and speed increased starting from Night 1; the FIRE button was removed in favour of one tap per playfield shot; telescope tracking smoothing increased; Starlink interception preserved. Mandatory threat shot budget remains capped at 35.

Files: `Dob_Defender_Alpha2-1.html` and `Dob_Defender_Alpha2-1_Gameplay_Spec.md`. The previous Alpha2 HTML and documentation remain available. This is a playtest build rather than a fully accepted milestone. Runtime Chrome automation was blocked; JavaScript syntax was checked successfully.


## Alpha2.3 UFO movement and cow targeting update (12 October 2026)

- UFO abduction targets must be fully inside the visible playfield, with at least 23 logical pixels of clearance from the left and right edges. A cow partly entering the field is ineligible until fully visible.
- Abduction UFOs enter rapidly from above, descend vertically, visibly bank before a right-angle horizontal dash toward a cow, level out and gently bob while hovering.
- The three-second rescue window is preserved (two-second hover plus one-second beam preparation).
- If the cow is abducted, the UFO and captured cow depart rapidly straight upwards.
- Existing harmless UFO flybys, cow sleeping, scoring, dome restoration and tap-to-fire controls remain unchanged.
- Verification: JavaScript syntax checked with Node. Android gameplay and full end-to-end runtime interactions have not been verified in this update.


## Alpha2.3 adjustments (12 October 2026)

- Cows spawn entirely inside the playfield, are clamped within the full visible margin while walking, and remain visible until dawn, rescue consequences or abduction.
- ISS now crosses at a fixed high altitude (y=42 in the logical canvas), with smaller artwork and collision radius.
- Meteors have subtle random size variation and a low-intensity animated inner flame tail, retaining their original trajectories.
- Nights 1 and 2 retain an introductory UFO flyby and may additionally schedule an early cow-abduction attempt when an eligible cow is present. Night 3 guaranteed abduction is preserved.
- No changes to approved telescope geometry or tap-to-fire and aiming control design.
- Validation still required on physical Android hardware.


## Alpha2.5 relative thumb steering (12 October 2026)

- Control is 52% of screen width, left aligned 5% from the edge, up to 245px.
- Swipes steer relative to the previous target angle; thumb can lift and resume anywhere inside the control.
- Indicator tracks target bearing without jumping to the pointer position.
- 225px cumulative swipe covers the allowed telescope range.
- Sky taps still fire once; gestures on steering track do not fire.
- Previous telescope artwork and gameplay are unchanged.
- Node syntax checked; physical Android sensitivity remains to be tested.


## Alpha2.5: Cow entry and abduction collision update (2026-10-12)
- Based on Alpha2.4. Cows enter from off-screen and walk into their grazing location, never suddenly appearing at a visible edge. Cows are ineligible for abduction until fully inside the field.
- On reaching a cow the UFO proceeds immediately to lifting; the former hover and beam-delay stages have been bypassed.
- Player laser shots can strike cows. A cow hit is lost and creates a short red `SPLAT!` impact.
- Shooting a UFO after lifting has started causes the abducted cow to fall under gravity with kicking legs and then splat on the ground in a fading red impact. Before lift-off, shooting the UFO still saves the cow and restores shield.
- Existing relative swipe aiming, playfield tap-to-fire, telescope artwork, and all other systems preserved.
- JavaScript syntax checked with Node; browser and Android playtesting remain outstanding.


## Alpha2.9

- Refined comet rendering so tails are softer, fuzzier and fade more gently from the nucleus.


## Alpha2.10 (startup fix and comet tails)

- Fixed missing cow-death counter declarations that prevented the game from starting.
- Comet tails now remain straight with soft transparent falloff; curved tail geometry removed.
- Startup tested in Chromium at mobile viewport. Full Android playtesting pending.


## Alpha2.11

- Refined comet visuals to better match the supplied reference image.
- Straightened the tail and gave it a softer tapered fade from the bright nucleus.


## Alpha2.12 comet silhouette refinement

- Narrowed the straight comet tail to follow the red outline in the supplied screenshot. Removed the broad outer glow and wide mid-tail plume. The tail remains softly translucent and tapers to a fine tip, with a bright rounded nucleus. No collision or gameplay changes.


## Alpha2.13

- Refined comet rendering again to better match astrophotography references.
- Oval comet head with the brightest point toward the front.
- Tail now sprays outward and fades away.


## Alpha2.14

- Refined comet tails again so they spread more at the end and fade away more strongly.


## Alpha2.15

- Reduced comet head size.


## Alpha2.16

- Implemented telescope breakup animation on direct scope hits after dome failure.
- Added explosive outward fragments for the telescope artwork.
- Cows now panic and run out of frame when the telescope is destroyed.


## Alpha2.17: Destruction sequence timing

- Telescope fragments have gravity, remain visible, and stop at the ground.
- Surviving cows wake and run out of the playfield, including sleeping cows.
- The Game Over results appear after fragments have landed and surviving cows have escaped.
- A ten-second failsafe prevents a stalled animation from trapping the player.


## Alpha2.18

- Fixed cow panic state: all surviving cows run outward when the telescope explodes, irrespective of their previous grazing, walking, sleeping, or standing state.
- Airborne cows land and flee without incorrectly granting cow-rescue points.
- Unshielded falling enemy impacts and flying telescope debris land at the visible near horizon/ridge line rather than the bottom of the screen.
- Game Over waits for fragments to land and cows to leave, with the existing fallback timer.


## Alpha2.19 ground and cow collisions

- Fixed collision level to the flat foreground ground line, not the distant jagged mountain range.
- Telescope debris also lands on this ground level.
- Widened cow collision check at ground approach so falling threats that strike cows trigger the red splat and cow-death counter.


## Alpha2.20

- Updated cow artwork to black-and-white marked cows with ears.
- Added visible leg animation for fleeing cows.


## Alpha2.63 (14 October 2026)

- Base: uploaded Dob_Defender_Alpha2-62.html, verified internally as Alpha2.62.
- Updated start screen instructions to the three requested messages about threats, cows and aircraft.
- Changed start button from PLAY to DEFEND!.
- Added Alpha2.63 version label centred at bottom of start overlay.
- No gameplay, telescope, input, collision or scoring logic intentionally modified.
- Previous Alpha2.62 HTML retained.
- Testing: static HTML and JavaScript syntax checks; mobile browser gameplay not tested.
- Known issue: Yale BSC5 online catalogue may require connectivity or manual DEV import on some Android local-file origins.
## Current release handover — Alpha2.76 (25 October 2026)

Approved from user-tested **Alpha2.76 Sound Test 25**. Exact immutable archive `releases/Dob_Defender_Alpha2.76.html` SHA `52352378f7fe288c52351d73b0fd4c74abc3b1aa`; root production `main:index.html` SHA `68da879b0120364df1128848e115200deec636b6`, release commit `521e842f65284b4663cbb7430ce80b3fd9dc229b`. Production differs only by removal of three `Sound Test 25` labels and updating the release-status code comment. Approved game artwork and mechanics remain locked. Sound features: distinct impacts/alerts, plane engine, aircraft hit, cabin-style warning chime, 3-2-1-GO rising tones, gentle three-note dawn chime. Aircraft popup is compact and displays flashing-then-steady amber-red SAFETY WARNING. Dawn clears residual projectiles, effects and debris to prevent frozen artifacts. Sound files embedded; existing online music and leaderboard dependencies unchanged. JS syntax checked; browser deployment and Android release verification to be recorded separately. Begin next development from current verified root `main:index.html`, not a previous test.


## Alpha2.79 Cow Balance Test 1 — local candidate, NOT RELEASED (25 October 2026)

- Authoritative starting baseline **Alpha2.78 `main:index.html` SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`**, reconstructed from its exact approved Test 2 archive with documented label/comment-only production substitutions, and verified via local `git hash-object` against GitHub production blob.
- Local **complete playable** `Dob_Defender_Alpha2.79_Cow_Balance_Test_1.html` 3,780,030 bytes; blob SHA `3bc81d1d44b542e3163f7876683395eb5df9904f` (also prevents a cow killed while targeted from continuing UFO lift). Three inline scripts pass `node --check`. Gameplay/browser/Android tests **not yet run**.
- Candidate changes: four unique cow objects spawned per night, no replacement spawning; +25 tally per cow alive at dawn, -25 for lost/dead/abducted, with one per-cow outcome and no duplicate penalty; UFO rescues still grant +50 and 10 shield once, while failed UFO escapes count lost; impactor/direct laser fatalities count lost. Night 1 and 2 schedule 1 guaranteed attempt; Nights 3–5 schedule 1 guaranteed with optional second; Nights 6–8 schedule 2 near-simultaneous guaranteed with optional third; Night 9+ schedules 3 guaranteed with optional fourth. Target reservations are mutually exclusive. Preserve current art, tally audio and all other mechanics.
- **Open risk/first unverified next step:** test actual browser simulation and Android controls for four-cow spacing and two UFO concurrency, cow collisions, score tally exactly once, rescue animations and endgame. User approval of test required before release. Production Alpha2.78 remains untouched.
