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
