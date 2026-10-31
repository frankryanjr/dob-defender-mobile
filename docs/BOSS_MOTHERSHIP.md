# Dob Defender — Mothership Boss Encounter (Design Specification)

**Recorded:** 31 October 2026  
**Status:** Test 1 built and Android-playtested (31 October 2026); balance and feedback revisions pending. Placeholder values only, none approved. See `docs/HANDOVER.md`. This document is a gameplay design checkpoint, not a release or test result.

## Objective and schedule

- Introduce a boss encounter **every third night** (Night 3, 6, 9, etc.).
- First test implementation is the **Night 3** mothership.
- All unaffected game mechanics, scoring, telescope artwork, music, controls, leaderboard and existing UFO behaviour must be preserved.

## Boss visual design

- The mothership must look like a **much larger version of the game's existing UFOs**, not a separate visual style.
- Initial sizing target: roughly **one-third of the playable sky width**, adjustable after actual Android gameplay/visual testing.
- Front-facing **reactor weak point**, moving or rotating, identifiable during the encounter.
- Energy shields and shield nodes are part of the encounter. Initial concept: **two shield nodes**.

## Core encounter

- The player's Dobsonian telescope **remains fixed in position**. Existing thumb/slider aiming and touch-to-fire operate as they do in normal gameplay.
- Boss has **phase-based damage**: shields must be addressed before meaningful attacks on the reactor. The reactor is a rotating/moving precision target.
- Boss may launch a limited number of attacks; timings, health, score, rewards, durations and exact fail/success conditions remain **undecided** until balanced/tested.
- Do not silently add new controls or change the telescope model.

## Technical and release constraints

- Current approved production reference: **Alpha2.80**, production `main:index.html` blob SHA `3a0b8ce5f0fc32abc950a1f68b8fd6a2e81f000b`; immutable archive `releases/Dob_Defender_Alpha2.80.html` SHA `1a4c399c361466c384f23767bedc11719cd37895`.
- Source transfer blocker resolved 31 October 2026 via direct `git clone`. Test 1 candidate built locally; no game files changed in the repository.
- Before coding: follow root README, locked WORKFLOW, GitHub baseline verification and documented lossless transfer safeguards. Resolve the transfer blocker without evading tool safety checks or using old local builds.
- Deliver a **complete standalone HTML test** for Android/gameplay review. No test publication, production push, itch.io change or release version increment without the required approval steps.

## First unverified next step

Apply user playtest feedback to Test 1 and produce Test 2 from the verified Alpha2.80 baseline.
