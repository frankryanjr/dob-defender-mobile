# DOB DEFENDER — AUTHORITATIVE DEVELOPMENT & RELEASE WORKFLOW

**Status: LOCKED.** This short document is the authoritative, mandatory startup and release policy. GitHub is the source of truth: [frankryanjr/dob-defender-mobile](https://github.com/frankryanjr/dob-defender-mobile). Do not start development until onboarding is complete.

## 1. Mandatory startup — every new development chat

1. Read root [README](../README.md) and **this entire WORKFLOW**.
2. Retrieve and inspect the current handover, specifications and history: [HANDOVER](HANDOVER.md), [GAMEPLAY](GAMEPLAY.md), [CHANGELOG](CHANGELOG.md), [DEVELOPMENT](DEVELOPMENT.md), [PROJECT_HISTORY](PROJECT_HISTORY.md). Inspect the [start-screen handover](Start_Screen_v1_Handover.md) when required by current work or to resolve relevant historical context; it is not automatically the current development objective.
3. Check current production `main:index.html`, latest approved release archive, exact version and Git blob SHAs. Resolve conflicting claims using current GitHub evidence, not old headings, uploads or conversation memory.
   - **Large-file preflight is mandatory:** before retrieving production HTML bytes, read the proven lossless retrieval recipe in the archived workflow (“PROVEN LOSSLESS” / “VERIFIED GITHUB-TO-LOCAL”) and the latest efficiency handover's transfer findings. First obtain SHA/length metadata; then choose a bounded, chunked transfer with per-part limits and final byte-count/Git-blob-SHA verification. Never trial an oversized single payload or temporary document first and only consult the established procedure after it fails.
4. For modular/efficiency work, read [EFFICIENCY_HANDOVER](EFFICIENCY_HANDOVER.md) and [MODULAR_WORKSPACE](MODULAR_WORKSPACE.md), and resume at the first unverified task.
5. **Keep full source contents inside tool execution**, not conversation output. Report concise SHA/status/conflict summaries. Read historical details or long procedures on demand.

The complete pre-restructure workflow is preserved at [archive/WORKFLOW_FULL_2026-10-25.md](archive/WORKFLOW_FULL_2026-10-25.md). Its detailed procedures remain authoritative where this short policy refers to them. Consult the relevant archived section **before performing that operation**; it is not a mandatory full startup read.

## 2. Founding principle — minimum user involvement

The assistant handles source retrieval, transfer, builds, validation, documentation and internal artifacts. Do not ask the user to download/re-upload internal ZIPs, run scripts, copy Base64, or act as a file courier. Ask the user only for decisions, genuine gameplay/visual testing, access actions that only they can perform, or explicit production approval. Deliver a complete standalone playable HTML for user tests.

Before declaring a tooling blocker, consult documented historical solutions and attempt supported alternatives. Do not repeat failed methods without a reason.

## 3. Exact baseline and development

- **GitHub production is the baseline.** Obtain exact current `main:index.html` bytes and blob SHA. Large-file `fetch_file` may return metadata without content: use the verified GitHub blob → Base64 → temporary Google Doc → export → local decode route, or another demonstrably lossless method. The detailed transfer recipe and safeguards are in the [archived workflow](archive/WORKFLOW_FULL_2026-10-25.md) under “PROVEN LOSSLESS” and “VERIFIED GITHUB-TO-LOCAL”.
- Verify complete HTML, byte count and `git hash-object` against the current GitHub blob SHA **before editing**. Keep untouched verified baseline and a separately named working copy.
- Preserve all unrelated approved artwork, mechanics, controls, audio, leaderboard and behaviour. Make minimal scoped edits and unique candidate versions. Validate syntax/assets/relevant regression checks; distinguish static checks from real browser/Android testing.
- Never substitute an old uploaded HTML, previous candidate or approved archive for current production source.

## 4. Two-stage delivery and approval — non-negotiable

**Stage A: Development and user testing (default).** Produce a complete downloadable standalone HTML. A GitHub-hosted test is allowed only with the user's explicit authorisation, at a separate versioned `tests/` path, with integrity verification. Test authorisation does not authorise production.

**Stage B: Production release (only after explicit user approval).** Record exact approved candidate/version/SHA and actual test results. Transfer the **exact approved HTML** to a new immutable versioned `releases/` archive and verify archive SHA matches the approved candidate. **Hard stop on mismatch.** Derive production from that verified archive, changing only necessary, documented test-version labels; inspect diff for unintended gameplay changes. Update `main:index.html` and release documentation only after these gates.

Verify commit, GitHub Actions, Pages deployment and live-served version independently where possible. Do not conflate a successful write with deployment or user Android confirmation. Provide production play link only after deployment verification; disclose unverified checks.

Detailed archive and release procedures, including label-only production promotion, traceability, cache/version safeguards and transfer methods, remain in the [archived workflow](archive/WORKFLOW_FULL_2026-10-25.md). **Read relevant sections before any release.**

## 5. Documentation, precedence and handover

Record candidate and release versions, exact source/test/archive/production SHAs, user approval, checks, label-only diff, deployment status, unresolved issues and next step. Retain historical release archives. Keep handover current.

Priority: explicit user instruction and this locked workflow; current verified GitHub production and approved artifact; current specifications/handover; older documentation and historical files. If a requirement conflicts or GitHub is unavailable, stop and explain rather than guessing.

## 6. Efficient operating rules

- Fetch and inspect mandatory documents without printing their entire bodies into the chat. Read large historical or technical procedures only for the task at hand.
- Do not echo large HTML, embedded media or Base64 chunks in tool results. Use bounded internal operations, hashes and short summaries.
- Keep reusable modular components, scripts, temporary transfers and validation logs internal; rebuild complete standalone HTML when testing requires it.
- If context limits interrupt work, update GitHub handover with the **first unverified step** and resume in a new chat.
- Efficiency work does not permit bypassing source verification, user testing, approval or release checks.

**Detailed historical reference:** [Complete workflow before restructuring](archive/WORKFLOW_FULL_2026-10-25.md). The archive is preserved intact; this document changes *when* detailed sections must be read, not the safeguards they impose.
