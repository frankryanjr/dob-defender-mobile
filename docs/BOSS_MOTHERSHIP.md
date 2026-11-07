# Dob Defender — Mothership Boss Encounter (Design Specification)

**Recorded:** 31 October 2026  
**Status (updated 7 November 2026):** Night 3 mothership boss is in production (Alpha2.81). Night 6 alien boss is also in production (Alpha2.81). Balance was tuned through playtesting; see `docs/PLAYTEST_LOG.md`. The original 31 October text below is kept as design history.

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

---

## Night 6: alien boss (in production, Alpha2.81)

**Released:** 7 November 2026, from approved Test 26. Night 6 is the second boss night. It replaces the mothership's UFO scouts with aliens.

- **No UFOs during the fight.** Any UFO still abducting when the boss arrives is removed.
- **Up to three aliens** arrive at once. Each picks a standing cow, and its beam lifts that cow.
- **Tractor beam:** a solid, semi-transparent green beam from the alien's finger to the cow. It flickers and pulses. Each hit fades it a little.
- **Breaking the beam:** one laser hit on the beam breaks it (`ALIEN_BEAM_HITS = 1`). The cow falls and lands safely, which scores points and gives a shield boost if the dome is down.
- **Time limit:** a beam not broken within about 6.5 seconds (`ALIEN_LIFT_T`) takes the cow to the ship, and that cow is lost.
- **Mothership collects:** once a lifted cow passes about 55% of the way up, the mothership glides over to collect it.
- **Hitting the cow:** a lifted cow is a larger target (18 px radius, up from 13). When a beam crosses both a lifted cow and a standing cow, the lifted cow takes priority. A laser kill on a lifted cow shows a red burst in the air, not a ground splat.
- **Aliens:** they blink, grumble when a beam is broken (two alternating grumble voices), shake their fist when the cow lands, and arrive with a rising transporter sound.
- **Intro text:** "THE ALIENS ARE TAKING THE COWS", followed by the tip "SHOOT THE TRACTOR BEAMS - NOT THE COWS!"

**Night 3 status:** the mothership fight is in production from Test 24. Shooting the mothership damages it. Its defeat shows as "MOTHERSHIP DEFEATED" on the tally. Leaving without being destroyed shows "MOTHERSHIP DAMAGED". The destruction explosion was added in Test 26.

**Difficulty progression** across boss nights is not yet specified or verified. Record any decision in `docs/PLAYTEST_LOG.md` and `docs/CURRENT_STATE.md`.

