# Dob Defender — Project entry point

Mobile browser game: Dobsonian telescope defence. **GitHub is the source of truth.** This file is intentionally short to minimise conversation-context usage.

## New development chat — required startup

1. Read this short README.
2. Read **[docs/WORKFLOW.md](docs/WORKFLOW.md) in full**. It is the locked, authoritative development, testing, approval and production procedure. This requirement is unchanged.
3. Follow the WORKFLOW onboarding instructions to inspect the current approved game, specifications, handover and development history. **Inspect required sources internally; do not reproduce their full contents in conversation output.** After initial mandatory inspection, retrieve only task-relevant sections.
4. For current efficiency work, read **[docs/EFFICIENCY_HANDOVER.md](docs/EFFICIENCY_HANDOVER.md)** and **[docs/MODULAR_WORKSPACE.md](docs/MODULAR_WORKSPACE.md)**. Resume at the first unverified step.
5. Give concise status updates; keep large HTML, Base64, media and internal artifacts out of conversation output.
6. **Before requesting large game HTML**, read the documented proven lossless transfer procedure and size limits in `docs/WORKFLOW.md` and its archived transfer sections. Plan the verified chunked route first; do not attempt an oversized single-file fetch/Doc transfer and only investigate the proven method after failure.

**Context warning:** The user repeatedly encountered a “maximum conversation length” warning shortly after starting chats. Reducing document/tool output is a mitigation, not a verified fix. Avoid fetching large blobs until needed; never substitute an older uploaded HTML for the current production baseline.

## Current state — verify against GitHub at startup

- Latest known production release: **Alpha2.76** (25 October 2026).
- Last observed production `main:index.html` blob SHA: `68da879b0120364df1128848e115200deec636b6`. **Recheck before development.**
- Current initiative: **modular source and development/release efficiency**, not gameplay or runtime optimisation.
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
