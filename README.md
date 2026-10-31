**Current development status (31 October 2026):** See **[docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)** for the concise production baseline, active Night 3 boss test, verification gaps and single next action. The detailed handover remains in [docs/HANDOVER.md](docs/HANDOVER.md). Historical release checkpoints belong in the handover/changelog, not as competing current-state claims here.

# Dob Defender — Project entry point

Mobile browser game: Dobsonian telescope defence. **GitHub is the source of truth.** This file is intentionally short to minimise conversation-context usage.

**Mandatory blocker recovery (all chats):** If any task hits a blocker, reread current README/WORKFLOW and search the GitHub handovers, development history and relevant archived procedures for already-proven workarounds; attempt applicable documented solutions before declaring a blocker or involving the user. See WORKFLOW §2A.

## New development chat — required startup

1. Read this short README.
2. Read **[docs/WORKFLOW.md](docs/WORKFLOW.md) in full**. It is the locked, authoritative development, testing, approval and production procedure. This requirement is unchanged.
3. Read **[docs/CURRENT_STATE.md](docs/CURRENT_STATE.md)** for the short checkpoint, then follow the WORKFLOW onboarding instructions to inspect the current approved game, specifications, handover and development history. **Inspect required sources internally; do not reproduce their full contents in conversation output.** After initial mandatory inspection, retrieve only task-relevant sections.
4. For current efficiency work, read **[docs/EFFICIENCY_HANDOVER.md](docs/EFFICIENCY_HANDOVER.md)** and **[docs/MODULAR_WORKSPACE.md](docs/MODULAR_WORKSPACE.md)**. Resume at the first unverified step.
5. Give concise status updates; keep large HTML, Base64, media and internal artifacts out of conversation output.
6. **Before requesting large game HTML**, read the documented proven lossless transfer procedure and size limits in `docs/WORKFLOW.md` and its archived transfer sections. Plan the verified chunked route first; do not attempt an oversized single-file fetch/Doc transfer and only investigate the proven method after failure.
7. **Checkpoint automatically at every milestone:** before starting the next meaningful development step, commit a concise, verified handover to GitHub recording what passed, what failed or remains untested, exact references and the first unverified next task. Keep README current-state pointers in sync. Do this without waiting for the user to request documentation; see WORKFLOW §5. This is documentation permission, not game publication permission.

**Context warning:** The user repeatedly encountered a “maximum conversation length” warning shortly after starting chats. Reducing document/tool output is a mitigation, not a verified fix. Avoid fetching large blobs until needed; never substitute an older uploaded HTML for the current production baseline.

## Current state — verify against GitHub at startup

- **Latest documented approved production:** Alpha2.80, `main:index.html` Git blob `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`. Recheck exact GitHub state before development.
- **Active development:** unapproved local Night 3 Mothership Boss Test 1; first next step is Android gameplay feedback before Test 2.
- **Canonical concise restart checkpoint:** [CURRENT_STATE](docs/CURRENT_STATE.md). See it for candidate SHA, pending checks and precise resumption instructions.
- Modular development and testing tooling is sufficient for now. Do not pursue tooling optimisation without a concrete need.
- No game code change or production publication is authorised by this documentation. Explicit user approval remains mandatory.

## Documentation map — open when relevant

| Document | Purpose |
| --- | --- |
| [CURRENT_STATE](docs/CURRENT_STATE.md) | Short verified restart status and first unverified next action |
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

**Suggested first message for new chats:** “Read the Dob Defender root README and follow its mandatory GitHub onboarding internally, keeping outputs concise. Resume from the single first unverified task in docs/CURRENT_STATE.md, while following WORKFLOW in full.”
