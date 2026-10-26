## 8. Alpha2.79 player-reported bugs — 26 October 2026 (open)

- **Issue A — leaderboard scores not uploaded/updated.** User reports several completed games without their score appearing or updating on the leaderboard. Report occurs during current itch.io use; not yet established whether also reproducible on GitHub Pages. Investigate score-submit call, persistence, API response/error, browser origin/storage and leaderboard refresh/pagination separately. Do not claim a cause until traced in the exact production source and tested.
- **Issue B — abducted cow reappears floating above ground.** User reports a cow that has been abducted later returns to the visible screen suspended above the ground. Trace UFO escape/rescue, cow reuse, state transitions, reset/spawn, y position and rendering across night transitions; establish whether successful abduction or interrupted rescue is involved. Expected invariant: lost cows stay lost during that night; rescued cows return to the ground.
- **Context:** GitHub main production Alpha2.79 blob `84f89682b3459577746c7678912a9b9dbcdcf4eb`, approved archive `131654b11232190f6470032f01180994bd969b1b`. User confirms itch.io game launches and plays; this does not prove online leaderboard submission functionality. No source code changed and no new candidate tested.
- **Investigation status:** mandatory README and full WORKFLOW reread; other required documentation inspected. GitHub connector metadata confirmed current production SHA; a partial `index.html` read returned metadata only, not source bytes. Before editing, follow WORKFLOW lossless full-baseline transfer and SHA gate. First unverified step: verify exact production HTML bytes and trace leaderboard submission and cow state paths. Keep GitHub Pages and itch.io production unchanged until approved.

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

## 6. User refinement — four cows from Night 1 and simultaneous UFO threats (25 Oct 2026)

- **Supersedes the earlier 3-cow Night 1 proposal:** fixed **4 unique cows from Night 1 onward** for equivalent scoring opportunity each night; up to 4 cows may need simultaneous presence/eligibility, so reassess the older 3-on-screen limit rather than silently enforcing it.
- **Night 1:** guarantee one abduction attempt for immediate engagement.
- **Later stages:** permit **two UFOs to attempt abductions simultaneously**, provided each targets a **different cow**. Do not permit both UFOs to reserve or abduct the same animal.
- Scale difficulty with night progression; exact threshold for two concurrent UFOs and counts per night require gameplay balancing. Respect the distinct cow outcomes, fair rescue window, and once-per-cow tally rules from Issues 1–5.
- **State:** accepted direction for next gameplay test design, **not implemented**, not a release approval. Inspect live Alpha2.77 spawn limit and UFO target reservation/scheduling before editing; preserve other approved behavior.

## 7. Night-end tally sound design mock — 25 October 2026

- User requested a soft ascending tone while laser/dome bars fill; fast click increments while earned points animate into the total; one bright positive ping for each green saved-cow marker; one dull negative cue for each red lost-cow marker; descending/depletion tone on score deductions.
- Built separate standalone **`Dob_Defender_Tally_Audio_Mock_1.html`** (8266 bytes) with a representative animated tally, synthesized Web Audio prototype (not original production audio), full sequence play, individual audition buttons, overall-effects-volume and animation-speed controls. Node syntax check passed. Example tally 1250 +65 +80 +75 -25 =1445. **User audition remains unverified.**
- This is a design mock only: no approved game assets/code altered, no game deployment or release approval. Next step: user listens on Android and comments on tempo/pitch/levels, then integrate approved sounds into exact verified Alpha2.77 source as full playable test candidate under WORKFLOW.

## Tally audio integration candidate — 25 October 2026

- User listened to `Dob_Defender_Tally_Audio_Mock_1.html`, said **“It's perfect push to prod”**. This approves the mock sounds/design; integration into real game has a distinct regression/device gate under WORKFLOW.
- Read SHA-verified production Alpha2.77 local exact file, Git blob `ae484817ab23bb3895dca9806f957c2688827b1e`; constructed complete standalone **`Dob_Defender_Alpha2.78_Tally_Audio_Test_1.html`**, 3,778,436 bytes, Git blob `b735913c59c1339198e08e3feee520344ca64c8f`.
- Code scope: added tiny optional Web Audio oscillator effects from approved mock at laser/dome bar fills, per saved/lost cow reveal, and score-roll additions/deductions. No scoring mechanics modified; existing game audio untouched. Inline script Node syntax check passed. Real Android/browser interaction and sound timing **not yet confirmed**. No game code published to production.
- **First unverified task:** user opens full Test 1 on Android, confirms sound timing/mix within actual game. Then, on renewed explicit release approval, archive exact candidate, verify archive SHA, derive production using label-only changes, verify Actions/Pages and device. No production publication on mock approval alone.

## Tally Audio Test 2 — louder mix, Android audition pending (25 Oct 2026)

User reports new tally sounds inaudible over production music in Test 1. Built complete local `Dob_Defender_Alpha2.78_Tally_Audio_Test_2.html` from verified Test 1 candidate blob `b735913c59c1339198e08e3feee520344ca64c8f`. Only changes: tally oscillator master gain 0.55 -> 1.75 (about 3.18x), temporary music duck to 0.06 while tally open and restore 0.20 on Continue, and Test 2 version labels. Git blob of resulting candidate `168c505247fa450a64824d6a9c706b3d82aef3ef` (3,778,569 bytes), all 3 inline scripts passed Node syntax check. No game scoring, artwork or production changed. Full Android listening and timing verification pending; do not release without test and renewed approval. First unverified step: user Android audition of Test 2, checking audible tally against music and music restoration on Continue.

## Alpha2.79 Cow/UFO Test 1 candidate — 25 October 2026

- **Exact source verified:** Current approved production Alpha2.78 `main:index.html` blob `fc0e3c618b5b5d41395a6b5f085a09300f61c1d3`, locally reassembled losslessly via four temporary Google Docs transport parts, verified `git hash-object` exact match. Do not substitute earlier versions or historical uploads.
- Built standalone `/mnt/data/Dob_Defender_Alpha2.79_Cow_UFO_Test_1.html`, 3,779,420 bytes, Git blob SHA **`6b9a7f91b47521b54bef783438dd5a0d440360e2`**. User has **not tested or approved** this candidate. No GitHub game/production files modified.
- Scoped candidate edits: fixed quota four unique cows created each night (no random extra cows); cow lost counted exactly once for SPLAT, impactor hit or successful escape; survivor tally `4 - lost`; UFO-abduction guaranteed Night 1 and escalating counts later; up to two distinct-target concurrent UFOs from Night 6; updated UFO target association for parallel encounters; preserved approved rescue +50 and dome repair, artwork, energy/dome/tally sound and other gameplay. Kept Game Over cow rescued legacy accounting for now apart from completed-night survivor totals.
- **Checks:** All three inline JavaScript blocks passed Node syntax validation. Local Chromium navigation attempted via file URL and local HTTP, but environment denied both with `net::ERR_BLOCKED_BY_ADMINISTRATOR`; **no real browser gameplay verification**. Potential behaviour/pacing needs Android user testing, including 4-cow positioning, first-night guaranteed rescue, overlapping later UFOs, score tally exactness, and Game Over. Review especially timing of simultaneous UFO target selections and cow state transitions. This is a test candidate only, not production.
- **First unverified next step:** user opens complete standalone Alpha2.79 Test 1 HTML on Android and reports cow visibility/UFO interactions and night-end result. If defects, revise and redeliver. Release only after explicit user approval and all archive/deployment gates.
