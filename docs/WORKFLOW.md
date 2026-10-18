# DOB DEFENDER — AUTHORITATIVE DEVELOPMENT & RELEASE WORKFLOW

**Status: LOCKED.** This document is the highest-priority project operating procedure. It governs all new development chats. Read it before any code changes or file delivery. Repository: https://github.com/frankryanjr/dob-defender-mobile

## 1. Mandatory new-chat startup

When told "Go to GitHub and read the instructions", immediately:
1. Fetch the **current** GitHub `README.md`, then this `docs/WORKFLOW.md`. Do not substitute memory, previous chats, local uploads, historical handovers or old HTML.
2. Read current `docs/HANDOVER.md`, `docs/GAMEPLAY.md`, `docs/CHANGELOG.md`, `docs/DEVELOPMENT.md`, `docs/Start_Screen_v1_Handover.md`.
3. Fetch **root `index.html` on branch `main`** and the latest *approved* archive under `releases/`. Compare version, implementation and release status. Production is **not** `main/index.html` (that is a mistaken historical path); `main` is the branch, `index.html` is the path. `game/index.html` is a historical mirror, never the default baseline.
4. State the current approved version, source file, locked designs, pending candidate changes, known issues and testing status. If sources conflict, identify the conflict before editing. If GitHub is inaccessible, disclose it and stop rather than silently using an old copy.
5. Follow this workflow as the primary authority. Historical handover sections are history, not current instructions.

## 2. Non-negotiable two-stage delivery

### STAGE A — DEVELOPMENT / USER TESTING (DEFAULT)

1. Start from the current **approved** production HTML, not a cached file, an old attachment, an earlier numbered release, or an unapproved test branch.
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
4. Update `README.md`, `docs/HANDOVER.md`, `docs/CHANGELOG.md`, and gameplay/development docs as relevant. Record changes, test results, remaining issues and release commit.
5. Commit to GitHub, verify the intended GitHub Pages deployment and where possible fetch the actual published HTML and confirm the intended version. Do not equate commit success with deployment.
6. Give the user the **playable production link**, `https://frankryanjr.github.io/dob-defender-mobile/?v=AlphaX.Y`, using a **new unique** version query value. This aids HTML cache-busting but does not guarantee asset refresh. Keep the canonical website URL unchanged.
7. User opens the production URL on Android and confirms. Record that confirmation as **user device testing**, not assistant testing.
8. Also supply the complete downloadable release HTML and updated Markdown handover.

## 2A. Approved HTML transfer to GitHub (fallback when direct transfer fails)

This procedure applies **only after explicit production approval**. A GitHub upload used for transfer is a staging artifact, **not** permission to publish an unapproved test build.

1. First attempt to transfer the **exact approved standalone HTML** using the available GitHub connection. Do not claim a transfer limitation until the available supported methods have been checked.
2. If the connection cannot read the complete local candidate or transfer its bytes, ask the user to upload the **exact approved HTML file** through GitHub's web interface to a clearly identified temporary staging path (for example, `staging/Dob_Defender_AlphaX.Y_Approved.html`). **Do not ask the user to replace `index.html` or alter production themselves.** This user-authorized staging upload is an exception to Stage A's default no-test-commits rule, solely for an already approved release.
3. Fetch the staged file through the GitHub connector. Verify its completeness, expected candidate/version and, whenever both copies are accessible, an exact byte-for-byte hash comparison with the locally approved candidate. If the transfer mechanism changes line endings or encoding, investigate and reconcile explicitly; never silently substitute a different build. If the original candidate cannot be accessed for comparison, disclose that limitation and obtain confirmation before proceeding.
4. Only after verifying the staged candidate, make the **minimal agreed release-label changes** (if any), run syntax checks, and archive it under `releases/`. Confirm the archived content matches the intended production content. Never reconstruct an approved candidate from memory, a prior test or the older production baseline.
5. Update `main:index.html` from the verified release content, update release documentation, and verify the actual GitHub Pages deployment as required by Stage B.
6. Keep the staging artifact clearly marked as non-production. Remove it only after production verification and with appropriate authorization, or document why it remains. Do not confuse the staging URL with the live game.
7. If any step fails, **stop and report the blocker**. Do not replace the working production version or announce success prematurely.

## 3. Version, cache and approval safeguards

- Approved production as of 18 October 2026: **Alpha2.68** in `main` branch root `index.html`; archived as `releases/Dob_Defender_Alpha2.68.html`.
- **Alpha2.69** is an **unapproved candidate** addressing four reported issues (energy bar flashes red when firing, dome retracts in wrong direction, developer power-up forcing missing, ground impact shake missing). Prior experimental GitHub files `tests/alpha2-69-four-fixes.html` and `alpha2-69-play.html` were prematurely committed; they are **not** approved production and must not be treated as release authority.
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
