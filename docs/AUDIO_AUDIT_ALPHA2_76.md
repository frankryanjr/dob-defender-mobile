# Alpha2.76 production audio reference audit — 25 October 2026

**Scope:** Read-only static audit of the *exact* production GitHub blob `68da879b0120364df1128848e115200deec636b6` (`main:index.html`). This is source-code evidence, not a report of completed audio playback or a deletion approval. No game code was modified.

## Findings

- **46 embedded data-URI audio entries** in `ddSoundData`; **31 have textual references outside the dictionary**, while **15 have none** and are **candidate unused clips**, not confirmed safe removals.
- Active game effects use two playback paths: `ddPlaySound(id)` for original `WPN_001` laser and `IMP_005` ground impact, and `ddTestSfx`/`ddEventSfx` for newer `DD_...` clips. The buffer loader decodes *all* dictionary entries when preparing audio, including candidates without active callers.
- Aircraft engine uses `DD_Propeller_Plane` loop via `ddSyncAircraftAudio()` when a living aircraft is in Night mode and the game is not paused; playback rate is **1.10**, envelope gain is `1.20*(.38+.62*sin(pi*progress)^1.2)`, smoothed over **.11 seconds**. `DD_Aircraft_Flyby` has no apparent caller. Aircraft warning modal invokes `DD_Aircraft_Seatbelt` at gain **.42**; hitting an aircraft invokes `DD_Aircraft_Laser_Hit` at **.52**.
- Laser `WPN_001` gain **.38**; ground impact `IMP_005` gain **.55**; general `ddPlaySound` default .5; event volumes vary per trigger. The separate background music is an **external MP3** (`audio/DobDefGame2.mp3`) set to volume **.20**, not one of these embedded clips.
- `DD_Slew_Light` is looped during active aim dragging at target gain **.16**. UFO appear hum is looped with gain ramp to **.78**; cow-abduction clip at **1.0**. `DD_Morning_Soft` is invoked by the dawn function at **.42**. Countdown tones are synthesized by oscillator and **do not use** the stored `DD_Countdown_Low/Mid/High` clips.
- No source modification or removal was made. A string-reference audit can miss dynamic naming or indirectly invoked clips; follow up with a runtime usage log during scenarios and a verified build after any proposed cleanup.

## Embedded audio inventory

Textual references count mentions *outside the embedded dictionary*. A count is not proof a game event fires in ordinary play.

| Clip key | Static usage |
| --- | --- |
| `DD_Aircraft_Seatbelt` | Referenced (1 textual mention) |
| `DD_Meteor_New` | Referenced (1 textual mention) |
| `DD_Aircraft_Warning` | No textual references found |
| `DD_Cow_Lost` | Referenced (1 textual mention) |
| `DD_Cow_Rescued` | Referenced (1 textual mention) |
| `DD_Dome_Damaged` | Referenced (1 textual mention) |
| `DD_Dome_Destroyed_Shield_Depletion` | Referenced (1 textual mention) |
| `DD_Game_Over` | Referenced (1 textual mention) |
| `DD_Laser_Energy_Depleted` | Referenced (1 textual mention) |
| `DD_Night_Complete` | No textual references found |
| `DD_Powerup_Collected` | Referenced (2 textual mentions) |
| `DD_UFO_Abducting_Cow` | Referenced (3 textual mentions) |
| `DD_UFO_Appears` | Referenced (3 textual mentions) |
| `DD_Satellite_Hit` | Referenced (1 textual mention) |
| `DD_Train_Complete` | Referenced (2 textual mentions) |
| `DD_ISS_Recharge` | Referenced (1 textual mention) |
| `DD_Laser_Restored` | Referenced (1 textual mention) |
| `DD_Meteor_Split` | Referenced (1 textual mention) |
| `DD_Meteor_Hit` | Referenced (1 textual mention) |
| `DD_Asteroid_Destroyed` | No textual references found |
| `DD_Asteroid_Damaged` | No textual references found |
| `DD_Junk_Burn` | Referenced (1 textual mention) |
| `DD_Night_Start` | No textual references found |
| `DD_Telescope_Destroyed` | Referenced (1 textual mention) |
| `DD_UI_Click` | Referenced (3 textual mentions) |
| `DD_Comet_Plut` | No textual references found |
| `DD_Telescope_Slew` | No textual references found |
| `DD_Sunsetting` | No textual references found |
| `DD_Asteroid_Tone_Low` | Referenced (1 textual mention) |
| `DD_Asteroid_Tone_Mid` | Referenced (1 textual mention) |
| `DD_Asteroid_Tone_High` | Referenced (1 textual mention) |
| `DD_Meteor_Fragment_Hit` | Referenced (1 textual mention) |
| `DD_Aircraft_Laser_Hit` | Referenced (1 textual mention) |
| `DD_Propeller_Plane` | Referenced (2 textual mentions) |
| `DD_Slew_Light` | Referenced (2 textual mentions) |
| `DD_Morning_Soft` | Referenced (1 textual mention) |
| `DD_Night_Warning` | No textual references found |
| `DD_Countdown_Low` | No textual references found |
| `DD_Countdown_Mid` | No textual references found |
| `DD_Countdown_High` | No textual references found |
| `DD_Morning_Orchestral` | No textual references found |
| `DD_Aircraft_Flyby` | No textual references found |
| `DD_UFO_Hit` | Referenced (1 textual mention) |
| `WPN_001` | Referenced (2 textual mentions) |
| `IMP_004` | No textual references found |
| `IMP_005` | Referenced (2 textual mentions) |

## Candidate unused keys (15)

- `DD_Aircraft_Warning`
- `DD_Night_Complete`
- `DD_Asteroid_Destroyed`
- `DD_Asteroid_Damaged`
- `DD_Night_Start`
- `DD_Comet_Plut`
- `DD_Telescope_Slew`
- `DD_Sunsetting`
- `DD_Night_Warning`
- `DD_Countdown_Low`
- `DD_Countdown_Mid`
- `DD_Countdown_High`
- `DD_Morning_Orchestral`
- `DD_Aircraft_Flyby`
- `IMP_004`

## Next unverified task

Instrument the SHA-verified production source **in memory only**, capture actual calls/played buffer IDs and gain values for normal and rare scenarios (aircraft, warnings, laser, impacts, dawn, countdown, UFO, satellite, etc.), and cross-check static candidates. Then propose a minimal deletion list, estimate size savings, rebuild a complete test candidate and run regressions. **Do not delete anything or publish a game candidate without the normal test/approval workflow.** Soundboard is explicitly paused until audio inventory is reconciled.
