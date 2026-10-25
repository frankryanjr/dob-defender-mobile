# Dob Defender — Open fixes

Current verified production: Alpha2.77. This document is an issue tracker, not a game-code change or release approval.

## 1. UFO abduction and cow-lost tally

- **Reported:** 25 October 2026, Android production playtest.
- **Priority:** High.
- **Symptom:** Cows visibly carried away in successful UFO abductions do not appear to increment the `Cows Lost` value shown in the end-of-night tally.
- **Documented gameplay intent:** Surviving an interrupted UFO abduction awards +50 during play, +10 dome restoration and +25 on the night-end tally; a cow lost should deduct 25 at tally. Destroying the UFO during slow lift rescues the cow; during rapid escape the falling cow dies; directly shooting the cow is fatal. Escaped abducted cows should be evaluated as lost.
- **Not yet diagnosed:** exact production `main:index.html` code paths, cow outcome state transitions, night-counter reset/snapshot and tally display. Do not assert a confirmed implementation cause.
- **First verification step:** inspect exact production Alpha2.77 SHA `ae484817ab23bb3895dca9806f957c2688827b1e` and trace state changes for successful UFO escape, rescued cow, escape-phase SPLAT and direct laser death. Check tally input and scoring exactly once for each outcome. Reproduce in isolated browser tests using in-memory instrumented production; propose minimal code fix preserving existing scoring/graphics, then deliver full test HTML for Android approval. No changes to game or production without testing and explicit release approval.

Additional issues will be appended as reported.

## 2. Cows killed by incoming impactors

- **Reported:** 25 October 2026.
- **Priority:** High; related to Issue 1.
- **Requested rule:** Every cow killed by a meteorite, asteroid, comet or other damaging incoming impactor should count as **one Cow Lost**, contributing the established -25 points in the night-end tally. The game objective is to protect all cows, not just to prevent UFO abductions.
- **Verification needed:** Determine which impactor/cow collision paths exist in Alpha2.77 and whether they currently cause cow death, visual effects, lost-cow counter updates or no interaction. Avoid adding a new collision/death mechanic without explicit design approval; if impactors already kill cows, ensure those outcomes are counted exactly once.
- **Acceptance tests:** For an impactor death, increment the current-night cows-lost count once and display the expected penalty at tally. Prevent double-counting from repeated collision frames or later state changes. Preserve existing cow rescue and UFO scoring behavior.
- **Status:** Logged; no game code changed.

## 3. Proposed cow tally redesign: night survival

- **Proposed in discussion, not yet implemented or approved for release.** Define `Cows Saved` at dawn as all cows alive at the end of the night, including any cow previously rescued from a UFO. Define `Cows Lost` as all cows killed or successfully abducted during the night (subject to verifying actual impactor collision behavior).
- Award +25 per surviving cow, -25 per lost cow in night-end tally. Retain existing immediate +50 and dome repair for successful UFO rescues. A cow must not count in both night-end columns and must be counted once per night; avoid rewarding a rescued cow twice in the tally.
- Before changing code, audit how cows spawn, depart, persist, are rescued or die in the current Alpha2.77 baseline. In particular, distinguish surviving cows that depart normally from genuinely lost cows; establish coherent per-night starting/entrant population and end-state reconciliation.
- This changes prior meaning of 'saved' from UFO rescues to all surviving cows. Requires user sign-off for gameplay and test candidate before production.

## 4. Cow population balancing proposal

- User is considering fixing cow opportunities at **3 on Night 1 and 4 on each later night** for leaderboard fairness, with arrival positions/timing and behaviour still random.
- Proposed tally remains +25 per surviving cow and -25 per lost cow; potential cow-tally swing per night is +75 to -75 on Night 1 and +100 to -100 thereafter, ignoring the existing separate +50 actual UFO rescue reward.
- **Needs code/design verification:** current game historically supports up to 3 concurrent cows. Four per night could mean 4 unique cows total rather than 4 concurrent, preserving rendering and UFO rules; inspect actual spawn logic before design changes. Ensure entrants/departures, repeated rescues and later UFO attempts don't generate more scoring opportunities than intended. No code changes or release approval.

## 5. UFO engagement from Night 1 — proposed revised progression

- **User preference (25 October 2026):** Guarantee **one actual cow-abduction attempt on Night 1** to engage players immediately; scale abduction pressure as night difficulty increases instead of waiting for the historic Night 3 guaranteed attempt.
- **Proposed initial pacing to test:** Night 1 = 1 guaranteed attempt; Night 2 = 1; Nights 3–5 = 1–2; Nights 6–8 = 2–3; Night 9 onward = 3 or more only after careful playtesting. This is a **suggested curve, not approved exact per-night counts**; adjust alongside meteor/asteroid density, flight timing and fair rescue windows.
- **Fairness/interaction with Issue 4:** proposed 3 unique cows in Night 1 and 4 per subsequent night, with at most 3 simultaneously visible. The scheduled UFO should have an eligible cow to target, should not retry indefinitely or count the same cow twice, and should provide the established rescue opportunity before escape.
- **Historical behaviour to replace if approved:** harmless flybys on early nights and an originally guaranteed Night 3 abduction, with probabilistic earlier attempts and later caps. Audit the current Alpha2.77 runtime scheduling before altering the event logic.
- **Status:** Design proposal recorded; no game changes and no production approval. First verification is current production cow/UFO spawn and encounter scheduler audit before a gameplay test candidate.
