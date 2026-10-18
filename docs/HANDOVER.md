> **CURRENT PROCESS AUTHORITY:** [WORKFLOW.md](WORKFLOW.md) governs all new-chat onboarding, standalone HTML testing, explicit user approval, and production publishing. Historical instructions and version labels below are reference only when they conflict with WORKFLOW.md. Approved production: Alpha2.68 at branch `main`, root `index.html`. Alpha2.69 is unapproved. Do not commit or publish tests by default.

# Alpha2.68 — Integrated damage and night scoring (18 October 2026)

- Production game: root `index.html`; archived release: `releases/Dob_Defender_Alpha2.68.html`.
- Embedded approved Start Screen v1 JPEG as a data URI for standalone Android HTML use; retained approved telescope and thumb controls.
- Laser Sight rocket-junk pickup, 20-second guide, expiry fade/flicker/retraction, energy-coloured guide and shots.
- Direct dome damage: meteor 20%, asteroid 35%, comet 30%, asteroid partial 15%, split fragment 20%; ground structural damage: 5%, 9%, 8%, 4%, 5% respectively. Dome-only shake and colour-linked outline; no cracks; 1.2-second outline retraction at zero integrity.
- Independent HUD resource warning pulses (25%/10%/0%) and gain/loss flashes. Resource percentages are not score points during play.
- Comet +5, meteor +10, asteroid staged +15/25, split meteor fragments +20 total; compact numeric hit popups.
- Night Complete animated energy/dome/cow/bonus tally and Continue control. Saved cow +25 and lost cow -25 in tally; existing +50 rescue reward remains.
- **Testing:** JavaScript syntax compiled; embedded JPEG decoded (1023 × 1536); full browser execution was blocked by environment, Android/device testing outstanding. GitHub Pages deployment not yet independently verified.
- **Known limitations:** online leaderboard and sky-data functions require connectivity; local HTML gameplay itself uses embedded Start Screen art. Full scoring, collision and animation device tests are pending.

# Alpha2.7: Cow survival during tractor-beam lift (12 October 2026)

- UFO destroyed before lift begins: cow is saved as before.
- UFO destroyed during the slow tractor-beam lift: cow drops with animated kicking legs, lands safely, resumes standing, awards COW SAVED (+50) and repairs dome by 10%.
- UFO destroyed during its rapid upward escape: cow drops with kicking legs and dies in the existing red, fading SPLAT! effect. No rescue reward.
- Direct laser hit on the cow remains fatal.
- Gameplay and the locked telescope/relative steering are otherwise unchanged.
- JavaScript syntax checked; Android gameplay still needs testing.

---

# Alpha2.6 Handover Update

Latest playable candidate: `Dob_Defender_Alpha2-6.html`

Alpha2.6 changes: enforce a central telescope exclusion zone for cows; accelerate early-night pacing; vary comet nucleus/tail size (small, medium, large) and soften the curved tails; introduce occasional three-hit large asteroids with distinct large, medium and smallest stages. The 35-shot mandatory budget includes extra large-asteroid hits.

**Testing:** JavaScript parsed successfully with `node --check`. Android touch gameplay, complete wave simulations, and rendering remain to be tested.

**Preserved:** Approved telescope artwork, tap sky to fire, compact relative-swipe steering, UFO/cow interactions, ISS, aircraft warning, Starlink interference and prior releases.

---

> **Current playtest build:** Alpha2.3 (`Dob_Defender_Alpha2-1.html`), derived from Alpha2. Original Alpha1 and Alpha2 files are preserved.
> **Verification:** JavaScript syntax passed; browser runtime test blocked by environment restrictions. Awaiting Android feedback.

# Dob Defender: Project Handover and Development Log

**Project:** Dob Defender  
**Latest playable build:** Alpha2  
**Latest HTML:** `Dob_Defender_Alpha2-1.html`  
**Previous preserved baseline:** `Dob_Defender_Alpha1-2.html` (uploaded Alpha1 iteration)  
**Companion gameplay specification:** `Dob_Defender_Alpha2_Gameplay_Spec.md`  
**Last updated:** 12 October 2026  
**Status:** First playable Alpha2 prototype, browser smoke-tested, awaiting full mobile gameplay balancing

## 1. Instructions for the next developer or AI chat

Read the newest numbered HTML, this handover and the Alpha2 Gameplay Specification before editing. The latest HTML is the implementation baseline, while this handover and the specification record approved intent. Preserve prior HTML files instead of overwriting them. Never replace just a function as the final user deliverable: provide a full playable game and a downloadable standalone HTML, alongside an updated handover whenever a milestone is saved.

**Locked design:** The Obsession-style truss Dobsonian is approved artwork. Do not redesign the UTA, laser, bearing, mirror box, cradle, trusses or small scale. Preserve the aiming slider and compact translucent FIRE button. No third-party assets or runtime network dependencies. Focus on Android/mobile usability. Do not include em dashes in game-visible text.

**Important source note:** The provided Alpha1 iteration is named `Dob_Defender_Alpha1-2.html` in this project. The older historical handover referred to an emailed file `Dob_Defender_Alpha1.html`. Both references designate Alpha1-era development, but only the actual uploaded baseline was edited to create Alpha2. Do not assume the older emailed file exists in this workspace.

## 2. Current playable Alpha2 game

The player operates a small, side-on, brown truss Dobsonian telescope under a starry sky, adjusting aim with a thumb slider and shooting a green laser from its side-mounted pointer. Each level is a **NIGHT**. A four-second dusk precedes a scheduled wave of hazards. All required threats must be resolved before a five-second dawn with a four-second **SURVIVAL!** results panel. Each subsequent night starts with 100 laser energy and 100 shield. Score is cumulative. After Night 10, play continues indefinitely with a 160% maximum baseline speed and four active mandatory hazards at once.

Alpha2 replaces the historical Alpha1 lives system with a faint observatory dome. Meteors cost 20% shield, full asteroids 35%, their fragments 15%, and comets 30%. A destroyed dome makes the observatory vulnerable to one more hostile impact. Rescuing a cow restores 10 shield, including rebuilding from zero. An intact-dome bonus is only for nights with zero impacts.

FIRE is **one laser shot per tap**, costing 2 of the 100 starting energy. No auto-fire when held. Zero energy disables the laser without ending the night. Mandatory threats require no more than 35 perfect shots. Asteroids require two hits; the first halves their diameter, creates dust and increases fragment speed by 20%. Comets are slower than meteors and asteroids, with occasional harmless flybys.

UFOs: one harmless pass on Night 1, another on Night 2, then a guaranteed cow abduction attempt on Night 3. Random abduction encounters follow: at most one on Nights 4-5, two on Nights 6-8, three from Night 9. Up to three cows may independently enter, graze, kneel, sleep with Zzz, and depart. A three-second rescue window ends when the cow lifts off. Early UFO hit saves cow for +50 points and +10 shield; late hit yields comic SPLAT; an escaped abduction costs 10 energy.

An ISS pass may appear at most once a night. At 1-25 energy its selected probability is 45%, with lower odds at higher power; one successful hit restores +40 energy, capped at 100. The first ISS pass pauses for an instruction and user-tapped OK; later alerts flash twice without pausing. Friendly aircraft blink red and green. Their first appearance shows the embedded cartoon pilot warning; a hit carries a -10 extra-energy penalty. Starlink trains have 12 equally spaced lights in a straight line; destroyed satellites leave gaps, and a 35% chance second pass can return the survivors in reverse direction.

The scoring and full timing tables are in `Dob_Defender_Alpha2_Gameplay_Spec.md`. The results screen shows cows saved and accuracy at dawn; Game Over shows score, nights survived, cows saved and accuracy, with PLAY AGAIN.

## 3. Historical Alpha1 mechanics (superseded where noted)

Alpha1 started with 3 hearts, score-based levels (1 + floor(score/400)), random continuous spawning and repeated fire when held. Its old object scores were satellite 5, meteor 15, asteroid 20, comet 30 and UFO 50. Alpha2 deliberately replaced these rules with scheduled nights, shield/energy economy, single-shot taps and the approved Alpha2 point table. Use the Alpha1 code only as the preserved reference for telescope geometry, side laser origin, visual language and input-slider mathematics.

## 4. Approved telescope art — preserve unless instructed otherwise

**The telescope artwork was refined through many user screenshots and red annotations. The latest approved geometry is in the Alpha1 HTML. Do not reintroduce superseded designs.**

### Appearance

- Telescope is a **side-on stylised vector illustration** of a large wooden Obsession-type truss Dobsonian, not a conventional solid-tube telescope.
- **No astronomer/person.**
- **UTA:** short rectangular/cylindrical-looking upper cage represented in brown timber, with light brown top and bottom rings. Simple round dark focuser on its front. No black bar across the top and **no laser beam from the middle of the UTA**.
- **Green laser:** small green device vertically fixed on the UTA's right edge; green shots fire in the direction in which the whole telescope is aimed. The green tip should remain aligned to the actual firing origin.
- **Trusses:** four silver/grey poles. Two outer mostly parallel poles, plus two inward-angled poles. They form two V-like diagonal lines, **NOT an X**. Avoid crossing the middle pair.
- **Mirror box:** short wooden brown rectangular top with circular/rounded lower profile. In the final design it is intentionally compact, not a tall square box; the long truss poles connect directly to its upper edge. The large upper rectangle drawn in early versions was removed after the user marked it with an X.
- **Altitude bearing/quadrant:** a bright silver curved strip attached to the outside/front side of the moving brown mirror box, running around its rounded bottom. It must not look like a disconnected ring floating in the stationary wooden base.
- **Fixed cradle:** a narrow brown wooden box with short, minimally raised ends and an accurately circular inward U-shaped seat. It sits flat on the ground, without extra pivots, separate side rectangles or other invented hardware. The moving mirror box and its silver bearing sit **inside and behind** the fixed base's front face.
- Preserve the relative look and colors established in Alpha1. This is a deliberately simplified game vector, not a photorealistic render.

### Important mechanical model

The real Dobsonian uses two motions: altitude pivots of the optical assembly against the rocker, and azimuth rotation of the rocker on a ground board. **This game is a side-on 2D approximation of the altitude pivot only.** The user repeatedly clarified that the **wooden base/cradle remains fixed**, and the mirror box, bearing, trusses, UTA and laser must **all tilt together**.

The bearing and the wooden seat have **concentric circular geometry** so rotation cannot make the bearing drift or float away from the cradle. The center of these circles is the telescope's rotation pivot. The moving elements render first and the fixed front cradle renders last to create the proper depth and occlusion.

### Actual Alpha1 geometry (verify against accompanying HTML)

The current `.html` declares:

```js
const BR = 40;           // moving circular mirror-box/bearing radius, logical units
const CR = 43;           // fixed cradle cutout radius
const BASE_BOTTOM = 57;  // cradle floor, logical units below pivot
const BASE_TOP = 13;     // height of abbreviated upper ends
const BASE_HALF = 49;    // fixed cradle half-width
const floor = () => H - 86;
const scale = () => Math.min(.43, Math.max(.19,
  Math.min(H * .125 / 272, W * .34 / 102)));
const origin = () => ({x: W / 2, y: floor() - BASE_BOTTOM * scale()});
```

The **Alpha1 small scale is intentional** and was the latest explicit request. In the reference screenshot the user labelled A as the scope's then-current full height and B as the desired much shorter full height. The telescope was reduced to roughly 25% of the earlier on-screen height while the full-size background and controls stayed in place. Maintain that small scale unless a newer user request changes it.

The telescope function rotates all moving parts by `angle + π/2` using `canvasContext.rotate`, so straight-up (`-π/2`) corresponds to rotation zero. The mirror-box lower edge uses a circular arc based on `BR`, and the fixed base uses a circular cutout based on `CR`. Exact drawing positions, stroke widths, and order are in the HTML.

**Artwork caveat:** The compact illustration is an approved stylised representation, not mechanically rigorous CAD. If new tweaks are requested, keep the shape familiar, the silver bearing visibly attached to the mirror box, and the fixed cradle in front of the lower moving unit. Do not 'fix' the result by adding extra blocks, pivots or an oversized upper mirror box.

## 5. Alpha2 implementation and visual style

Alpha2 remains one standalone HTML canvas application with inlined CSS, JavaScript and an embedded compressed WebP of the aircraft safety popup. Canvas uses devicePixelRatio scaling, adaptive viewport dimensions and Pointer Events. The approved original `telescope()` implementation is preserved verbatim. The game has explicit title, dusk, night, tutorial, dawn and game-over states. Night objects use a capped group scheduler and segment-based laser collision test. The Moon, twinkling stars, hills, green ground and small telescope artwork remain in the original style, with the addition of a dome, cows, aircraft and ISS.

**Smoke testing:** Chromium with 390 x 844 mobile viewport and other portrait sizes, JavaScript syntax verification, pointer firing checks, tutorial OK interaction, energy and score checks, simulated wave-to-wave advancement, game-over and no-energy behaviours have been performed. See the Alpha2 specification's test section for scope. Android hardware gameplay and campaign-wide balancing have NOT yet been completed. Do not claim they have.

## 6. Known limitations and follow-up work

- Full thumb-control balancing of Nights 1-10 and endless mode is not yet validated on actual Android hardware.
- Optional event timing, small satellite hitboxes, cow rescue hitboxes and partial-dome shielding may require tuning through playtesting.
- There is no sound design, cloud high-score service, pause/settings screen, or PWA install flow.
- Current game is a first playable Alpha2 version, not a final release.
- All source changes should be assessed for regression of the exact telescope rendering, side laser origin, impact rules, accurate shot counting, pause/resume behaviour, dawn transitions and restart.

## 7. Historical design and change log

The versions below reflect the **development conversation**, not a rigorously tagged source-control history. `v9`–`v28` were iterative chat/game previews, and the only formally packaged emailed baseline is **Alpha1**.

| Stage | Summary / design decision |
|---|---|
| Initial concept | Astronomer aims Obsession-style Dobsonian; shoot meteors, comets, asteroids, UFOs and satellites with attached green laser. |
| Early gameplay | Make mobile game: thumb-angle control and tap to fire. |
| Control refinements | Switch to lower-sensitivity horizontal slider (line and ball), smaller transparent fire button, full-size screen. |
| Artwork simplification | Remove the man; shrink the telescope; use realistic Dobsonian proportions. |
| Telescope identity | Replace generic tower/tube with short brown UTA, open silver trusses, lower mirror box and rocker/base. |
| Truss corrections | Middle poles must angle inward rather than forming a large crossing X. |
| Laser correction | Laser must fire from small pointer on **side** of UTA; remove centre beam and black bar atop UTA. |
| Base corrections | Narrow, compact fixed wooden base with concave circular U-shaped seat. Remove extra rectangular pivot blocks and unnecessary wood pieces. |
| Layering corrections | Brown mirror box, bearing, trusses and UTA rotate together; stationary wooden cradle is drawn in front of lower moving components. |
| Bearing corrections | Silver curved metal altitude bearing belongs on the **front/side of the moving mirror box**, not painted into the fixed cradle or below it. |
| Mathematical correction | Establish shared centre and circular arcs for moving bearing vs fixed circular seat. |
| Mirror box refinement | Remove tall upper part of box, leave a short brown mirror box and longer poles. |
| Base height adjustment | Temporarily deepen fixed base, then trim surplus width/side heights/bottom per red annotations. |
| Approved art | User asked to **save the telescope design**; this became the reference artwork. |
| Scale corrections | User clarified A = telescope's then-current full height; B = **desired new full height**, much smaller. Final Alpha1 uses this compact size. |
| **Alpha1 — 2026-10-12** | Packaged as `Dob_Defender_Alpha1.html`, standalone playable mobile browser game; title **Dob Defender**. Alpha1 was emailed to `frankryanjr@gmail.com` with the HTML attached. |

## 8. Release tracking

| Version | Date | File | Status |
|---|---|---|---|
| Alpha1 | 2026-10-12 | `Dob_Defender_Alpha1-2.html` (uploaded baseline) | Preserved Alpha1-era file; historic Alpha1 was reported emailed under `Dob_Defender_Alpha1.html` |
| **Alpha2** | **2026-10-12** | **`Dob_Defender_Alpha2-1.html`** | Playable initial feature build, syntax and browser smoke-tested; awaiting hands-on Android balancing |

## 9. Alpha2 milestone changelog (12 October 2026)

- Added dusk and dawn cycle, fixed-sized night wave schedules, NIGHT level HUD and SURVIVAL results overlay.
- Added 100-point laser capacity with 2 points per shot and single-shot FIRE; maximum 35 mandatory accurate shots.
- Replaced Alpha1's three-heart system with 100-point protective dome, object-specific impact damage, cracks, red warnings and vulnerable final hit.
- Added full laser and dome restoration at the start of every night.
- Changed meteor, asteroid and comet speeds and scoring; introduced small 20%-faster asteroid second fragments and dust.
- Added random independent grazing, wandering and sleeping cows, plus UFO flybys and timed abduction/rescue/SPLAT outcomes.
- Added first guaranteed cow abduction on Night 3 and increasing later UFO encounter caps.
- Added ISS passes with low-energy weighted chance, +40 recharge and first-time OK tutorial, plus twice-flashing later alerts.
- Added occasional aircraft with red/green wing lights, -10 energy extra penalty and embedded illustrated first-time safety popup.
- Changed 12 detailed satellite sprites to evenly spaced Starlink-style points with a possible 35%-chance survivor-only return pass.
- Added per-target scoring, night survival/intact-dome/accuracy bonuses, complete Game Over statistics and replay.
- Kept approved Alpha1 telescope drawing function verbatim and preserved the compact mobile slider and circular FIRE control styling.
- Added game test observations, known limitations and Alpha2 specification file.

## 10. Starting prompt for a new chat

> Continue **Dob Defender** from `Dob_Defender_Alpha2-1.html`, with `Dob_Defender_Project_Handover.md` and `Dob_Defender_Alpha2_Gameplay_Spec.md`. Read all of these before development. Alpha2 is the newest playable first-build version; do not overwrite Alpha1. Preserve the exact small Dobsonian telescope, side-mounted green laser, fixed cradle, thin thumb slider and compact FIRE button. Follow the gameplay specification and changelog, avoid em dashes in all game-visible copy, check mobile pointer control, collisions, resource budgets, score, pause/tutorial behaviour, dusk/dawn and game-over/restart. After each change, provide a complete updated playable game and updated downloadable documentation.

---

**End of Alpha2 handover.**


## Alpha2.3 changes, 12 October 2026

User playtest of Alpha2 found that cows left after sleeping, early nights were too slow, the FIRE button was less convenient than tapping the sky, and aiming felt sluggish. Starlink satellites unintentionally intercepted hostile-target shots, which the user explicitly wants to keep.

Changes: sleeping cows persist until abduction or dawn; early wave density and speed increased starting from Night 1; the FIRE button was removed in favour of one tap per playfield shot; telescope tracking smoothing increased; Starlink interception preserved. Mandatory threat shot budget remains capped at 35.

Files: `Dob_Defender_Alpha2-1.html` and `Dob_Defender_Alpha2-1_Gameplay_Spec.md`. The previous Alpha2 HTML and documentation remain available. This is a playtest build rather than a fully accepted milestone. Runtime Chrome automation was blocked; JavaScript syntax was checked successfully.


## Alpha2.3 UFO movement and cow targeting update (12 October 2026)

- UFO abduction targets must be fully inside the visible playfield, with at least 23 logical pixels of clearance from the left and right edges. A cow partly entering the field is ineligible until fully visible.
- Abduction UFOs enter rapidly from above, descend vertically, visibly bank before a right-angle horizontal dash toward a cow, level out and gently bob while hovering.
- The three-second rescue window is preserved (two-second hover plus one-second beam preparation).
- If the cow is abducted, the UFO and captured cow depart rapidly straight upwards.
- Existing harmless UFO flybys, cow sleeping, scoring, dome restoration and tap-to-fire controls remain unchanged.
- Verification: JavaScript syntax checked with Node. Android gameplay and full end-to-end runtime interactions have not been verified in this update.


## Alpha2.3 adjustments (12 October 2026)

- Cows spawn entirely inside the playfield, are clamped within the full visible margin while walking, and remain visible until dawn, rescue consequences or abduction.
- ISS now crosses at a fixed high altitude (y=42 in the logical canvas), with smaller artwork and collision radius.
- Meteors have subtle random size variation and a low-intensity animated inner flame tail, retaining their original trajectories.
- Nights 1 and 2 retain an introductory UFO flyby and may additionally schedule an early cow-abduction attempt when an eligible cow is present. Night 3 guaranteed abduction is preserved.
- No changes to approved telescope geometry or tap-to-fire and aiming control design.
- Validation still required on physical Android hardware.


## Alpha2.5 relative thumb steering (12 October 2026)

- Control is 52% of screen width, left aligned 5% from the edge, up to 245px.
- Swipes steer relative to the previous target angle; thumb can lift and resume anywhere inside the control.
- Indicator tracks target bearing without jumping to the pointer position.
- 225px cumulative swipe covers the allowed telescope range.
- Sky taps still fire once; gestures on steering track do not fire.
- Previous telescope artwork and gameplay are unchanged.
- Node syntax checked; physical Android sensitivity remains to be tested.


## Alpha2.5: Cow entry and abduction collision update (2026-10-12)
- Based on Alpha2.4. Cows enter from off-screen and walk into their grazing location, never suddenly appearing at a visible edge. Cows are ineligible for abduction until fully inside the field.
- On reaching a cow the UFO proceeds immediately to lifting; the former hover and beam-delay stages have been bypassed.
- Player laser shots can strike cows. A cow hit is lost and creates a short red `SPLAT!` impact.
- Shooting a UFO after lifting has started causes the abducted cow to fall under gravity with kicking legs and then splat on the ground in a fading red impact. Before lift-off, shooting the UFO still saves the cow and restores shield.
- Existing relative swipe aiming, playfield tap-to-fire, telescope artwork, and all other systems preserved.
- JavaScript syntax checked with Node; browser and Android playtesting remain outstanding.


## Alpha2.9

- Refined comet rendering so tails are softer, fuzzier and fade more gently from the nucleus.


## Alpha2.10 (startup fix and comet tails)

- Fixed missing cow-death counter declarations that prevented the game from starting.
- Comet tails now remain straight with soft transparent falloff; curved tail geometry removed.
- Startup tested in Chromium at mobile viewport. Full Android playtesting pending.


## Alpha2.11

- Refined comet visuals to better match the supplied reference image.
- Straightened the tail and gave it a softer tapered fade from the bright nucleus.


## Alpha2.12 comet silhouette refinement

- Narrowed the straight comet tail to follow the red outline in the supplied screenshot. Removed the broad outer glow and wide mid-tail plume. The tail remains softly translucent and tapers to a fine tip, with a bright rounded nucleus. No collision or gameplay changes.


## Alpha2.13

- Refined comet rendering again to better match astrophotography references.
- Oval comet head with the brightest point toward the front.
- Tail now sprays outward and fades away.


## Alpha2.14

- Refined comet tails again so they spread more at the end and fade away more strongly.


## Alpha2.15

- Reduced comet head size.


## Alpha2.16

- Implemented telescope breakup animation on direct scope hits after dome failure.
- Added explosive outward fragments for the telescope artwork.
- Cows now panic and run out of frame when the telescope is destroyed.


## Alpha2.17: Destruction sequence timing

- Telescope fragments have gravity, remain visible, and stop at the ground.
- Surviving cows wake and run out of the playfield, including sleeping cows.
- The Game Over results appear after fragments have landed and surviving cows have escaped.
- A ten-second failsafe prevents a stalled animation from trapping the player.


## Alpha2.18

- Fixed cow panic state: all surviving cows run outward when the telescope explodes, irrespective of their previous grazing, walking, sleeping, or standing state.
- Airborne cows land and flee without incorrectly granting cow-rescue points.
- Unshielded falling enemy impacts and flying telescope debris land at the visible near horizon/ridge line rather than the bottom of the screen.
- Game Over waits for fragments to land and cows to leave, with the existing fallback timer.


## Alpha2.19 ground and cow collisions

- Fixed collision level to the flat foreground ground line, not the distant jagged mountain range.
- Telescope debris also lands on this ground level.
- Widened cow collision check at ground approach so falling threats that strike cows trigger the red splat and cow-death counter.


## Alpha2.20

- Updated cow artwork to black-and-white marked cows with ears.
- Added visible leg animation for fleeing cows.


## Alpha2.63 (14 October 2026)

- Base: uploaded Dob_Defender_Alpha2-62.html, verified internally as Alpha2.62.
- Updated start screen instructions to the three requested messages about threats, cows and aircraft.
- Changed start button from PLAY to DEFEND!.
- Added Alpha2.63 version label centred at bottom of start overlay.
- No gameplay, telescope, input, collision or scoring logic intentionally modified.
- Previous Alpha2.62 HTML retained.
- Testing: static HTML and JavaScript syntax checks; mobile browser gameplay not tested.
- Known issue: Yale BSC5 online catalogue may require connectivity or manual DEV import on some Android local-file origins.