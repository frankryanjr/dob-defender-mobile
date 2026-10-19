# DOB DEFENDER — AUTHORITATIVE DEVELOPMENT & RELEASE WORKFLOW

**Status: LOCKED.** This document is the highest-priority project operating procedure. It governs all new development chats. Read it before any code changes or file delivery. Repository: https://github.com/frankryanjr/dob-defender-mobile

## 1. Mandatory new-chat startup

When told "Go to GitHub and read the instructions", immediately:
1. Fetch the **current** GitHub `README.md`, then this `docs/WORKFLOW.md`. Do not substitute memory, previous chats, local uploads, historical handovers or old HTML.
2. Read current `docs/PROJECT_HISTORY.md`, `docs/HANDOVER.md`, `docs/GAMEPLAY.md`, `docs/CHANGELOG.md`, `docs/DEVELOPMENT.md`, `docs/Start_Screen_v1_Handover.md`.
3. Fetch **root `index.html` on branch `main`** and the latest *approved* archive under `releases/`. Compare version, implementation and release status. Production is **not** `main/index.html` (that is a mistaken historical path); `main` is the branch, `index.html` is the path. `game/index.html` is a historical mirror, never the default baseline.
4. State the current approved version, source file, locked designs, pending candidate changes, known issues and testing status. If sources conflict, identify the conflict before editing. If GitHub is inaccessible, disclose it and stop rather than silently using an old copy.
5. Follow this workflow as the primary authority. Historical handover sections are history, not current instructions.

## 1A. Starting a development session — broad requests are intentional

Phrases such as **"Let's make some developments"**, **"Let's work on the game"**, **"Let's improve Dob Defender"**, or equivalent requests mean the user wants to enter **development mode**, not that a specific feature has already been selected.

Development can involve **any aspect of Dob Defender**: sound effects, music, gameplay mechanics, difficulty balancing, aiming and mobile controls, scoring, leaderboards and online integration, telescope or other artwork, animation, menus, user experience, bug fixes, performance, or entirely new features. Do not artificially limit the scope to the last feature discussed.

1. Complete the mandatory GitHub onboarding in §1 first, even when the user's first message is simply a broad development invitation. Establish the current approved production baseline and any pending work from the repository, not conversation memory.
2. Briefly state the approved baseline and ask **what the user wants to develop**, offering a few relevant directions only when useful. Do not invent a requested change or start editing without enough direction.
3. Discuss and plan the chosen change, implement it in the current approved game, and preserve **all unaffected approved** artwork and gameplay. Explicitly requested updates to previously locked elements may be explored in test builds, but do not silently alter other approved elements.
4. Deliver complete standalone downloadable HTML candidates, iterate through user testing, and distinguish test candidates from approved releases.
5. **Entering development mode is never production approval.** Publishing requires separate, explicit authorization for the exact tested candidate under Stage B. The user can switch between different development areas in the same chat without re-onboarding unless repository state must be refreshed.


## PROVEN LOSSLESS GITHUB → GOOGLE DRIVE → LOCAL TRANSFER (19 OCT 2026)

**Verified end-to-end without any user-uploaded production HTML.** Use this when GitHub connector can read the source but the local Python/container cannot download it directly.

1. Fetch the complete current `main:index.html` with GitHub `fetch_file`, capturing `result.content` and `result.sha`.
2. Within a single `functions.exec` call, encode the fetched UTF-8 text into **Base64** using JavaScript (a small pure-JS UTF-8/Base64 encoder works when `btoa` and `TextEncoder` are unavailable). Do not use plain Google Docs text insertion for raw HTML: Google Docs added 30 extra newlines to the 343,575-character Alpha2.69 source.
3. Create a temporary native Google Doc with `mcp__Google_Drive__create_file`. Insert Base64 text using `mcp__Google_Drive__batch_update_document` in manageable chunks (verified: 15,000 Base64 characters per `insertText` request, six requests per call, with `endOfSegmentLocation:{}`). Newlines introduced by Google Docs are harmless to Base64.
4. Export the temporary Doc with `mcp__Google_Drive__fetch({url:"https://docs.google.com/document/d/<id>/edit",download_raw_file:true,raw_export_mime_type:"text/plain",include_base64:false})`. This **automatically mounts the exported .txt file into `/mnt/data`**; the tool message supplies the exact mounted path.
5. In the local Python/container environment, read the exported text with `encoding="utf-8-sig"`, remove whitespace from the Base64, decode with `base64.b64decode(...,validate=True)`, and write the decoded bytes as `/mnt/data/Dob_Defender_<version>_GitHub_Verified.html`.
6. Run `git hash-object` on the resulting HTML and **require an exact match to the current GitHub `result.sha`**. Also check `</html>`. Do not use the file for development or link it if the hash differs. Then make the Stage A test changes and deliver the full HTML as usual.

**Successful reference:** Alpha2.69 source: 343,575 characters, 343,608 UTF-8 bytes, Base64 length 458,144, Git blob SHA `1a5e85ba0d1f9d74565249a657d40c39bd670f11`; exact SHA match after Drive transfer. These are **historical verification values only**, not expected values for later production. No user HTML upload was used in this successful transfer. Do not confuse a previously uploaded local file with this verified method.

## VERIFIED GITHUB-TO-LOCAL TEST BUILD PROCEDURE — MANDATORY

**This procedure exists because a previous assistant incorrectly claimed it could not turn GitHub source into a downloadable local HTML test. Do not repeat that claim without attempting the actual tools.**

1. Fetch `main:index.html` with the GitHub connector `fetch_file` and retrieve its **full** `result.content` as UTF-8 text, plus `result.sha`. Check that it is complete (including closing `</html>`), and verify the downloaded text against the Git blob SHA when possible. Read README, this workflow and release records first.
2. **Create the local HTML file directly using a container-backed Python execution tool** (for example `python_user_visible.exec` or `python.exec`, or the container tool). In the successful Alpha2.69 Test 19 session, `/mnt/data/index.html` was available in that runtime, its 343,575-character content was validated with `git hash-object` against the GitHub blob SHA `1a5e85ba0d1f9d74565249a657d40c39bd670f11`, and Python wrote `/mnt/data/Dob_Defender_Alpha2.69_Test19.html`. **These exact hashes and lengths are historical examples, not expected values for later versions.**
3. **Before declaring a transfer blocker**, inspect `/mnt/data` in the Python/container runtime for an already-mounted copy of the *current* fetched source, then check its Git blob SHA against the current GitHub `index.html`. If the source is not mounted, use available supported file-transfer/mount mechanisms to bring the fetched GitHub content into the Python/container environment. Do not use an old HTML attachment, archived release or mirror as a substitute. If transfer truly fails, report the specific attempted methods and errors; never say it is impossible merely because one HTTP raw-GitHub request fails.
4. Make minimal edits to that **verified production source**; write a uniquely named **complete standalone test HTML** to `/mnt/data`, run available JavaScript syntax checks, confirm the output file exists and provide the `sandbox:/mnt/data/...` download link. The user must not be asked to download production from GitHub and upload it back into ChatGPT.
5. This is **Stage A only**. Do not commit the test or change production until explicit user approval. After approval, use §2A direct transfer to the numbered release archive, verify the archive, then publish and document according to Stage B.

**Operational lesson:** A failed connector-to-container transfer attempt does not establish that the workflow is impossible. Check runtime-mounted files and verify hashes before asking the user to do manual transfers.

## 2. Non-negotiable two-stage delivery

### STAGE A — DEVELOPMENT / USER TESTING (DEFAULT)

1. **Every development change must start from the current approved production source: branch `main`, repository-root `index.html`.** This is the live production code, not the archived release HTML. Determine which version `index.html` represents from the current production declaration in `README.md`, then verify its approval and release history against the latest production entries in `docs/CHANGELOG.md` and `docs/PROJECT_HISTORY.md` (including the approved test identifier and archived release path). Inspect the actual `index.html` before editing and reconcile any mismatch; never guess the version from filenames or use a cached file, old attachment, earlier numbered archive, historical mirror or unapproved candidate as the development baseline.
2. Make the smallest requested changes. Preserve approved telescope artwork, Start Screen v1 artwork, thumb aiming, laser origin, collisions, scoring, cows, aircraft, leaderboard and all unaffected mechanics.
3. Produce a **complete self-contained playable HTML** with a unique candidate version/test identifier, plus a downloadable sandbox attachment **directly in ChatGPT**. Never provide only a patch, function, source-file URL, Google Doc or GitHub Pages test URL as the deliverable. Embedded artwork must work offline; explicitly disclose optional online services.
4. Perform available static/syntax checks and inspect affected gameplay. Report separately: syntax checked, code inspected, browser tested, Android device tested by user, and anything not tested. Do not claim testing not performed.
5. User downloads the HTML and tests it on Android. Iterate with new downloadable complete HTML builds and distinct identifiers until **explicit user approval**. User feedback or a request for fixes is not production approval.
6. **Do not publish or commit test HTML to GitHub by default**, including `tests/` or repository-root test URLs. Do not alter production `index.html` or archives in Stage A. Only use GitHub for tests if the user specifically authorizes that deviation.
7. Never substitute an unverified GitHub Pages URL for the downloadable test artifact. A commit does not equal a deployed, playable game.

### STAGE B — APPROVED PRODUCTION RELEASE (ONLY AFTER EXPLICIT APPROVAL)

1. Confirm the exact approved candidate is the one being released. If it differs from the latest approved production, do not silently rebuild from another version.
2. Continue Alpha2.x numbering; preserve Alpha1 and every prior numbered release. Archive the complete approved HTML as `releases/Dob_Defender_AlphaX.Y.html` without overwriting historical releases.
3. Update branch `main` root `index.html` to that **exact approved HTML**. Check whether any other maintained production mirrors need updating; never use an outdated mirror as source.
4. Update `README.md`, `docs/PROJECT_HISTORY.md`, `docs/HANDOVER.md`, `docs/CHANGELOG.md`, and gameplay/development docs as relevant. Record changes, test results, remaining issues and release commit.
5. **Mandatory production-label gate before commit:** inspect start-screen version text, HTML document title and other user-visible version labels; require clean `AlphaX.Y` with no `TEST N` or stale test number. Confirm a content diff against the immutable approved test archive contains only the documented label changes. Commit to GitHub, verify the intended GitHub Pages deployment and where possible fetch the actual published HTML and confirm the intended version. Do not equate commit success with deployment.
6. Give the user the **playable production link**, `https://frankryanjr.github.io/dob-defender-mobile/?v=AlphaX.Y`, using a **new unique** version query value. This aids HTML cache-busting but does not guarantee asset refresh. Keep the canonical website URL unchanged.
7. User opens the production URL on Android and confirms. Record that confirmation as **user device testing**, not assistant testing.
8. Also supply the complete downloadable release HTML and updated Markdown handover.

## 2A. Approved tested HTML as the permanent release source

This procedure applies **only after explicit production approval**. The exact user-tested, approved standalone HTML is the authoritative release candidate. **Prefer uploading it directly to its permanent numbered archive**, not to a temporary staging file.

1. **Use the successful Alpha2.69 direct-transfer method by default; do not require the user to download and re-upload the game.** Read the approved generated HTML from its local working file when available, or use `files.list` to locate the exact generated conversation attachment and `files.read` to retrieve its full text in consecutive line ranges. Reassemble all ranges in order, preserving original line separators. Compare the reconstructed file's full character length and checksum/hash with the original approved file before writing. The Alpha2.69 Test 18 transfer was verified at 343,607 characters with FNV-1a `d4d94208` (these values apply **only** to that exact build, not future versions). Use the GitHub `create_file` action to write the verified HTML **directly to** `releases/Dob_Defender_AlphaX.Y.html`, retaining the exact approved test file. If a supported direct local-file-to-GitHub transfer exists, it may be used instead with the same integrity checks. Ask the user for a manual upload only after these methods have actually failed, and explain the specific failure. Never ask the user to replace `index.html` themselves.
2. Fetch the archived HTML back through GitHub and verify its completeness, identity and candidate/version. Compare byte hashes when raw bytes are available, otherwise compare the full decoded text length and a documented text checksum, accounting for line endings and encoding. Do not mislabel a text checksum as a byte-for-byte hash. If comparison is impossible, disclose that limitation and request confirmation rather than claiming an exact match.
3. Preserve the **exact tested file** permanently as the approval record. Do not modify the archive simply to remove a TEST label. For every approved production release, **mandatory**: make only the production-label changes needed to remove test identifiers from the production copy (visible start-screen version must read exactly `AlphaX.Y`, with no `TEST N`; update HTML `<title>` and other user-visible test labels to the production version). Preserve the exact tested archive unchanged. Verify the intended substitutions by comparing archive and production content and confirm that the only differences are these version/label strings; record those differences in release documentation. If any other difference appears, stop and resolve it before publishing. The production gameplay must remain identical to the approved archive.
4. Use the verified archived HTML as the **sole source** for updating branch `main` root `index.html`. Do not rebuild from an old production file, earlier test or memory. Perform syntax checks, update release documentation and verify the live GitHub Pages deployment under Stage B.
5. Do not overwrite existing numbered archives. If the target archive exists with different content, stop and resolve the conflict before proceeding. Keep prior releases intact.
6. Temporary staging is a **last resort only** when the permanent archive cannot safely receive the approved file directly. If used, verify and transfer it to the permanent archive before changing production.
7. Confirm GitHub Actions syntax check and GitHub Pages deployment success for the final commit, and verify the *live* start-screen version label is clean and matches `AlphaX.Y`, and where possible independently retrieve the live page. Ask the user to confirm Android playability. Record GitHub deployment success separately from independent live-page validation and user device testing.
8. If verification or deployment fails, report the blocker and preserve the last working production version; never announce a release as successful prematurely.

## 2B. Mandatory version documentation and traceability

For **every approved production version**, record all verified changes and additions, not merely a version-number increment:

1. Maintain a dedicated version entry in `docs/CHANGELOG.md` with the release date, approved test-build identifier, added features, changed mechanics/UI, bug fixes, removals, scoring/leaderboard behaviour, and any known limitations. Distinguish observed/tested behaviour from intended behaviour.
2. Update `docs/GAMEPLAY.md` for the actual current gameplay rules, controls, scoring formulas, resource/damage behaviour, power-ups, night progression and end-of-game flow that changed.
3. Update `docs/HANDOVER.md` with the exact approved HTML archive path, production source, preserved locked designs, relevant implementation decisions, outstanding defects, test status and next steps.
4. Update `README.md` to identify the current production version and its archive; update `docs/DEVELOPMENT.md` with validation, release/deployment steps and results. Keep historical entries rather than overwriting the release history.
5. Record the production commit SHA, GitHub Pages verification result and any subsequent user Android confirmation. Never label syntax inspection as device testing.
6. Ensure documentation describes **the code actually released**. Compare the approved archive with production and document any permitted version-label-only differences. Do not invent undocumented changes from memory.
7. Publish documentation alongside the release, then verify the final GitHub state. If a required update fails, disclose the incomplete release documentation explicitly and finish it before declaring the release complete.

## 3. Version, cache and approval safeguards

- **Production source of truth:** `main:index.html`. The version must be discoverable in `README.md` and traceable through the corresponding approved release entry in `docs/CHANGELOG.md` and the production record in `docs/PROJECT_HISTORY.md`. Verify all three against the actual source before starting development; if they disagree, stop and resolve the discrepancy.
- **Current recorded production (18 October 2026): Alpha2.69**, approved from Test 18 and archived as `releases/Dob_Defender_Alpha2.69.html`. The preceding approved Alpha2.68 is retained for history/rollback, **not** as a development baseline. Earlier Alpha2.69 experimental test URLs were not production authority.
- For each new test build, generate a fresh standalone HTML from the correct baseline, with a distinct visible version/test identifier. Do not reuse a previously generated cached artifact. Confirm the actual output file exists before linking it.
- For production, verify the commit and Pages content/version. If the website shows an older version, diagnose deployment, HTML cache, service worker and asset cache. Never claim the query parameter guarantees freshness.
- Do not change the workflow, locked artwork, or release approval requirement without explicit user authorization.
- The user expects **a directly playable game** at every stage: a downloadable standalone HTML during testing, and a verified production Pages URL after approval.

## 4. Conflict-resolution order

1. This `docs/WORKFLOW.md` for **process**.
2. Current GitHub `README.md` for **current release entry point** and onboarding.
3. Approved `main:index.html` and latest approved archived release for **implemented gameplay**.
4. Current gameplay specification and latest changelog for intended mechanics and change history.
5. Current handover for decisions, known issues and continuity.
6. Historical documents, older release files and conversation memory only as supporting history.

Flag discrepancies; do not silently treat old Alpha2.63/Alpha2.67 labels or historical `main/index.html` references as current.

## 5. Validation and model effort

- Simple text, labels and docs: GPT-6 Instant.
- Regular gameplay and controls: GPT-6 Medium.
- Geometry, bearings, difficult bugs: GPT-6 High; exceptional architecture: Extra High if available.
- The assistant may recommend but cannot change the selected thinking effort.
- Inspect JS syntax, aiming rotation, laser position, collision handling, scoring, shield/energy, pause/restart, touch controls and responsive Android layout when relevant. Differentiate inspection from actual browser/device execution.

**Golden rule: READ GITHUB → BUILD COMPLETE DOWNLOADABLE TEST HTML → USER APPROVES → PUBLISH APPROVED PRODUCTION → VERIFY LIVE PLAY LINK. Never skip the approval boundary.**
