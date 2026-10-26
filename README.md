**Latest development checkpoint (26 October 2026):** Alpha2.80 Bugfix Test 1 standalone local candidate built from SHA-verified Alpha2.79; fixes dead abducted cow rendering and adds retry/persistence for failed leaderboard submissions. Browser startup and JS syntax pass; Android and live leaderboard submission pending. Production unchanged. See `docs/HANDOVER.md`.

**Verification update (25 October 2026):** User confirms Alpha2.79 live deployment and successful Android verification. This is user-reported verification; independent assistant-side live HTTP/Actions checks have not been rerun. Production remains Alpha2.79; see `docs/HANDOVER.md`.

**Current production (25 October 2026): Alpha2.79.** Approved Test 7 archived at `releases/Dob_Defender_Alpha2.79.html` (SHA `131654b11232190f6470032f01180994bd969b1b`); `main:index.html` SHA `84f89682b3459577746c7678912a9b9dbcdcf4eb`, production commit `0925ddac00764ce6fa71ff061d40954e96c41f25`. Only title/version labels differ from the exact approved test. Actions, Pages live-served version and Android confirmation pending. See `docs/HANDOVER.md`.

**Local development checkpoint (25 October 2026):** Alpha2.79 Cow Tally Test 2 is a local, **unapproved and uncommitted** standalone test candidate derived from GitHub-verified Alpha2.78 and the locally created worldwide-counter test. Four starting cows, night-end saved/lost census and guaranteed early abduction scheduling are included. Two simultaneous abductors are **not implemented**. Three/gameplay plus auxiliary scripts syntax-checked, Android/browser not verified. Production remains Alpha2.78. See top of `docs/HANDOVER.md`.\n\n**Development test checkpoint (25 October 2026):** Alpha2.79 Cow/UFO Nights Defended Test 4 is ready for Android testing. Standalone HTML: `Dob_Defender_Alpha2.79_Cow_UFO_Nights_Defended_Test_4.html`, 3,780,736 bytes, Git blob SHA `1adeb31800f6a3d5f2ecb1e333821981f0da686c`. It carries the cow/UFO test changes and adds a globe badge that sums final-night values from the leaderboard response. Current database total: 157 nights across 27 accepted score submissions; endpoint limit is 50 records, then the badge shows a `+` lower-bound marker. Three inline JS syntax checks pass; browser/Android testing pending. **Production remains Alpha2.78** SHA `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`. See top of `docs/HANDOVER.md`.

**Current production:** **Alpha2.78** (approved Tally Audio Test 2, 25 October 2026), `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`; exact approved test archived in [`releases/Dob_Defender_Alpha2.78.html`](releases/Dob_Defender_Alpha2.78.html) SHA `168c505247fa450a64824d6a9c706b3d82aef3ef`. User confirmed tally audio sounded correct and requested production. New score-tally sounds and temporary music ducking only; open cow scoring changes not included.

# Dob Defender — Project entry point

Mobile browser game: Dobsonian telescope defence. **GitHub is the source of truth.** This file is intentionally short to minimise conversation-context usage.

**Mandatory blocker recovery (all chats):** If any task hits a blocker, reread current README/WORKFLOW and search the GitHub handovers, development history and relevant archived procedures for already-proven workarounds; attempt applicable documented solutions before declaring a blocker or involving the user. See WORKFLOW §2A.

## New development chat — required startup

1. Read this short README.
2. Read **[docs/WORKFLOW.md](docs/WORKFLOW.md) in full**. It is the locked, authoritative development, testing, approval and production procedure. This requirement is unchanged.
3. Follow the WORKFLOW onboarding instructions to inspect the current approved game, specifications, handover and development history. **Inspect required sources internally; do not reproduce their full contents in conversation output.** After initial mandatory inspection, retrieve only task-relevant sections.
4. For current efficiency work, read **[docs/EFFICIENCY_HANDOVER.md](docs/EFFICIENCY_HANDOVER.md)** and **[docs/MODULAR_WORKSPACE.md](docs/MODULAR_WORKSPACE.md)**. Resume at the first unverified step.
5. Give concise status updates; keep large HTML, Base64, media and internal artifacts out of conversation output.
6. **Before requesting large game HTML**, read the documented proven lossless transfer procedure and size limits in `docs/WORKFLOW.md` and its archived transfer sections. Plan the verified chunked route first; do not attempt an oversized single-file fetch/Doc transfer and only investigate the proven method after failure.
7. **Checkpoint automatically at every milestone:** before starting the next meaningful development step, commit a concise, verified handover to GitHub recording what passed, what failed or remains untested, exact references and the first unverified next task. Keep README current-state pointers in sync. Do this without waiting for the user to request documentation; see WORKFLOW §5. This is documentation permission, not game publication permission.

**Context warning:** The user repeatedly encountered a “maximum conversation length” warning shortly after starting chats. Reducing document/tool output is a mitigation, not a verified fix. Avoid fetching large blobs until needed; never substitute an older uploaded HTML for the current production baseline.

## Current state — verify against GitHub at startup

- Latest known production release: **Alpha2.76** (25 October 2026).
- Last observed production `main:index.html` blob SHA: `68da879b0120364df1128848e115200deec636b6`. **Recheck before development.**
- **Decision (25 October 2026):** the modular development and automated testing infrastructure is **MVP-complete / sufficient for now**. Freeze further tooling optimisation unless a concrete development need or failure requires it. **Next phase: game development and player feedback**, using the existing tests.
- **Verified 25 October 2026:** exact production source (3,775,528 bytes, SHA `68da879b0120364df1128848e115200deec636b6`) was reconstructed and checked; modular `split/check/build` passed (8 blocks, 46 assets), and static validation and four deliberate negative cases passed. Consult the latest efficiency handover for exact evidence.
- **Next unverified task:** build and verify browser-driven gameplay smoke tests where supported (aim/fire, start screen, collisions/scoring, audio, rendering); clearly distinguish browser automation from Android/device verification. Improve the lossless transfer route without weakening SHA checks.
- No gameplay changes or production publication are authorised by this handover. Explicit user approval is required for production.

## Documentation map — open when relevant

| Document | Purpose |
| --- | --- |
| [WORKFLOW](docs/WORKFLOW.md) | **Mandatory full read** of concise locked policy; detailed procedures linked on demand |
| [EFFICIENCY_HANDOVER](docs/EFFICIENCY_HANDOVER.md) | Current task, completed work, unresolved steps and context-saving rules |
| [MODULAR_WORKSPACE](docs/MODULAR_WORKSPACE.md) | Modular source design and validation |
| [HANDOVER](docs/HANDOVER.md) | Current game handover; consult as required by workflow |
| [GAMEPLAY](docs/GAMEPLAY.md) | Mechanics and approved gameplay specification |
| [CHANGELOG](docs/CHANGELOG.md) | Release changes |
| [DEVELOPMENT](docs/DEVELOPMENT.md) | Development details |
| [PROJECT_HISTORY](docs/PROJECT_HISTORY.md) | Historical decisions and prior work |
| [Start screen handover](docs/Start_Screen_v1_Handover.md) | **Historical, task-specific reference**; not a standing current-work priority |
| [Archived full WORKFLOW](docs/archive/WORKFLOW_FULL_2026-10-25.md) | Detailed historical procedures; read relevant sections before operations, not at every startup |
| [Archived full README](docs/archive/README_FULL_2026-10-25.md) | Previous 29.5k-character README preserved intact, including old release summaries, transfer procedures and legacy notes |

Older release headings in the archived README, including “Current production — Alpha2.69/Alpha2.70,” are **historical statements**, not current status. Consult them only for relevant history.

## Non-negotiable safeguards

- Do not begin code changes until mandatory GitHub onboarding and exact production-source verification are complete.
- Preserve approved gameplay, artwork and controls unless explicitly changed.
- Handle internal source transfers, builds, scripts and archives yourself; involve the user only for decisions, gameplay testing or approval.
- Deliver complete standalone playable HTML for user testing.
- Do not publish unapproved builds or promote production without explicit approval.
- Verify release archive integrity and deployment before providing a production play link.

**Suggested first message for new chats:** “Read the Dob Defender root README and follow its mandatory GitHub onboarding internally, keeping outputs concise. Resume from the first unverified task in the efficiency handover.”
