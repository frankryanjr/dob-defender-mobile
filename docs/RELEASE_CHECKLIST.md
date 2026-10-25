# Dob Defender — release and transfer checklist

Use together with [WORKFLOW.md](WORKFLOW.md). This is a tracking aid; WORKFLOW remains authoritative.

## Before development
- [ ] Read current README, WORKFLOW, PROJECT_HISTORY, HANDOVER, GAMEPLAY, CHANGELOG, DEVELOPMENT and approved artwork notes.
- [ ] Fetch current `main:index.html` and latest approved archive metadata; resolve any mismatch.
- [ ] Check for an already verified local production copy (matching Git blob SHA).
- [ ] If not present, transfer using the proven lossless method, splitting Base64 through temporary Drive documents only if needed.
- [ ] Record local byte count, `git hash-object`, GitHub blob SHA and temporary Drive document IDs.

## Candidate testing (Stage A)
- [ ] Make requested changes in a separately named full standalone HTML candidate.
- [ ] Confirm unaffected artwork/gameplay and offline assets remain intact.
- [ ] Run JavaScript syntax and other applicable tests; note untested Android behaviour.
- [ ] Provide downloadable HTML; no unapproved production or archive changes.
- [ ] Record user's explicit approval and exact candidate file/hash.

## Production (Stage B — explicit approval required)
- [ ] Re-check GitHub state for interrupted/already completed release.
- [ ] Archive exact approved candidate under new `releases/Dob_Defender_AlphaX.Y.html`.
- [ ] Fetch archive and verify its blob SHA **exactly** matches approved candidate.
- [ ] Derive production only from verified archive, with documented version-label changes.
- [ ] Diff against archive: no unintended gameplay, artwork or audio changes.
- [ ] Update `main:index.html`; fetch and verify production SHA.
- [ ] Update README, PROJECT_HISTORY, HANDOVER, CHANGELOG, DEVELOPMENT and relevant gameplay notes.
- [ ] Check Actions, Pages deployment and live HTML/version separately.
- [ ] Ask user to confirm Android playability; do not conflate with automated tests.

## Cleanup and handover
- [ ] Delete only verified obsolete temporary transfer documents, not troubleshooting records.
- [ ] Preserve exact release archive, source, and historical documentation.
- [ ] Record completed steps, hashes, commit, deployment status, Android status and unresolved items.
- [ ] If blocked, first search historical successful workarounds and record what was actually tried.

## Alpha2.76 checkpoint — 25 October 2026
- Approved candidate: Alpha2.76 Sound Test 25.
- Archive: `releases/Dob_Defender_Alpha2.76.html`; blob `52352378f7fe288c52351d73b0fd4c74abc3b1aa`.
- Production: `main:index.html`; blob `68da879b0120364df1128848e115200deec636b6`.
- Production commit: `521e842f65284b4663cbb7430ce80b3fd9dc229b`.
- Deployment/live-page/Android checks: track separately; do not infer from commit.
- Temporary Google Drive audit: 19 title-matching transfer/troubleshooting documents, reported aggregate sizes 5,497,612 bytes; deletion not yet performed.
