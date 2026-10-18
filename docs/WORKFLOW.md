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

## 2A. Approved tested HTML as the permanent release source

This procedure applies **only after explicit production approval**. The exact user-tested, approved standalone HTML is the authoritative release candidate. **Prefer uploading it directly to its permanent numbered archive**, not to a temporary staging file.

1. Check whether the available GitHub connection can transfer the complete approved HTML directly. If not, ask the user to upload that **exact approved file** using GitHub's web interface to `releases/Dob_Defender_AlphaX.Y.html`, provided that archive path does not already exist. Do not ask the user to replace production `index.html`.
2. Fetch the archived HTML through GitHub and verify its completeness, identity and candidate/version. Compare hashes byte-for-byte with the approved local test file whenever both are accessible. If comparison is impossible, disclose that limitation and request confirmation rather than claiming an exact match.
3. Preserve the **exact tested file** permanently as the approval record. Do not modify the archive simply to remove a TEST label. If a clean production version label is desired, make only the explicitly agreed label/identifier changes in the production copy; document the difference. The production gameplay must remain identical to the approved archive.
4. Use the verified archived HTML as the **sole source** for updating branch `main` root `index.html`. Do not rebuild from an old production file, earlier test or memory. Perform syntax checks, update release documentation and verify the live GitHub Pages deployment under Stage B.
5. Do not overwrite existing numbered archives. If the target archive exists with different content, stop and resolve the conflict before proceeding. Keep prior releases intact.
6. Temporary staging is a **last resort only** when the permanent archive cannot safely receive the approved file directly. If used, verify and transfer it to the permanent archive before changing production.
7. If verification or deployment fails, report the blocker and preserve the last working production version; never announce a release as successful prematurely.

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
