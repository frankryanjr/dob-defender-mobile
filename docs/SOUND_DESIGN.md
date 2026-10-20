# Dob Defender — Sound Design Register

**Status:** Planning only. No audio files are approved, generated, integrated or deployed by this document. **Baseline inspected:** Alpha2.73, main:index.html, Git blob `5dc1679fa33bcc66326215385e0d49c2f0ff4d15` (20 October 2026). Source scan found no AudioContext, HTML Audio or sound-playback calls; this is a static code scan, not runtime proof of silence.

## Purpose and rules

- One stable sound ID per *game event or sound role*, regardless of future file revisions. Code refers to IDs, never scattered literal paths.
- Filename: `DD_<ID>_<Description>_vNN.wav` (e.g. `DD_WPN_001_Laser_Fire_v01.wav`). Increment vNN when the recording or synthesis changes; keep ID unchanged. Do not overwrite approved masters.
- Categories: WPN weapons, IMP impacts, ENV environment, PWR powerups, EVT events, UI interface. Store masters in `assets/audio/{weapons,impacts,environment,powerups,events,ui}/` once approved. No empty directories or placeholder audio need be committed now.
- The machine-readable companion `docs/SOUND_MANIFEST.json` is the authoritative structured register for IDs, triggers, statuses and file references; this document is the human-readable guide. Update both together.
- Status progression: planned → candidate → approved → integrated; retired for replaced sounds. Approval of a *sound* does not approve a *production game release*.
- WAV is the archival/master target; choose compressed playback format only after checking Android compatibility, file size and quality. Record actual sample rate, channels, duration, gain, format, checksum, origin, licensing and approved revision when files exist.
- Store original masters in GitHub where practical. For standalone Android test HTML, embed runtime audio or synthesize with Web Audio; do not depend on separate local files. The manifest is documentation, not a runtime network dependency.
- No third-party recording without a documented redistribution license. Do not silently use copyrighted game audio.

## Inventory and descriptions

| ID | Title | Layperson description | Trigger / developer cue | State |
|---|---|---|---|---|
| `WPN_001` | Laser Fire | A short, crisp electronic laser pulse. | fire accepted | Planned |
| `IMP_001` | Meteor Destroyed | A sharp crack and small scattering burst. | meteor destroyed | Planned |
| `IMP_002` | Asteroid Hit | A heavy knock with fragments breaking away. | asteroid takes nonfatal hit | Planned |
| `IMP_003` | Asteroid Destroyed | A larger rocky crack and crumbling breakup. | asteroid destroyed | Planned |
| `IMP_004` | Comet Destroyed | A brittle, icy-sounding shatter. | comet destroyed | Planned |
| `IMP_005` | Ground Impact | A low thump with a brief ground rumble. | threat impacts ground | Planned |
| `IMP_006` | Dome Impact | A hollow, heavy strike against the observatory dome. | dome takes damage | Planned |
| `IMP_007` | Dome Destroyed | A structural groan and final collapse. | dome integrity reaches zero | Planned |
| `ENV_001` | Passing Car | A car approaches on a quiet road, passes with engine and tyre noise, then fades. | headlight hazard active (future feature) | Planned |
| `ENV_002` | Wind | A faint outdoor breeze in a quiet observing field. | ambient gameplay | Planned |
| `ENV_003` | Distant Thunder | A soft distant roll of thunder. | weather event (future feature) | Planned |
| `ENV_004` | Aircraft Flyover | A distant aircraft engine grows and fades. | aircraft encounter | Planned |
| `ENV_005` | Cloud Wind | A subtle gust accompanying drifting cloud. | cloud hazard (future feature) | Planned |
| `PWR_001` | Laser Sight Activated | A short electrical activation chirp. | laser sight pickup collected | Planned |
| `PWR_002` | Laser Sight Expiring | A weakening buzz with irregular flickers, then silence. | laser sight near expiry | Planned |
| `PWR_003` | GoTo Slew | A small telescope drive motor winds up and slows as it reaches target. | GoTo slew (future feature) | Planned |
| `PWR_004` | Telrad Activated | A small switch click followed by a gentle confirmation tone. | Telrad pickup (future feature) | Planned |
| `PWR_005` | Energy Restored | A bright rising electrical recharge tone. | laser energy replenished | Planned |
| `EVT_001` | Cow Rescued | A short, upbeat confirmation cue. | cow rescued | Planned |
| `EVT_002` | Cow Abducted | A rising alien tractor-beam sound ending abruptly. | cow abducted | Planned |
| `EVT_003` | UFO Approaching | A wavering, otherworldly electronic hum. | UFO appears | Planned |
| `EVT_004` | Aircraft Warning | An urgent but brief warning signal. | aircraft danger warning | Planned |
| `EVT_005` | Satellite Pass | A very restrained passing electronic shimmer. | satellite encounter (optional) | Planned |
| `UI_001` | Button Press | A soft, tactile click. | menu button activated | Planned |
| `UI_002` | Night Complete | A short optimistic victory flourish. | night-end tally begins | Planned |
| `UI_003` | Game Over | A brief descending, subdued musical sting. | final game over | Planned |
| `UI_004` | Tally Count | Quiet ticks accompanying rising or falling score. | end-of-night tally counts | Planned |
| `UI_005` | Power Warning | A discreet double warning beep. | laser energy crosses warning threshold | Planned |

## Sound specification template

- **ID / title / category:** stable reference and player-friendly label.
- **Real-world description:** what someone should hear, avoiding implementation jargon.
- **Technical direction:** timbre, attack, decay, loop/one-shot, expected duration and variations.
- **Trigger:** precise gameplay condition, including cancellation and cooldown behaviour.
- **Priority / mix:** gain, overlap limit, whether ambience ducks for warnings.
- **Asset tracking:** status, approved vNN, path, source/creator, license, file hash, actual format/duration, approval date, review notes.
- **Verification:** syntax, desktop/browser audio, Android tap-to-unlock, volume, mute, rapid-fire overlap, background/resume and offline standalone playback; distinguish observed from untested.

## Sound manager design (not yet implemented)

Use one centralized `SoundManager.play('WPN_001')`-style interface with a stable ID-to-asset mapping, master mute/volume, per-category gains, event priority, concurrency caps and repeated-shot throttling. Mobile audio must initialize/resume only after a user gesture. Handle interrupted/suspended audio contexts and page visibility. Avoid continuous playback of expensive/large samples. Sound settings must persist sensibly per browser, with silent operation if audio is unavailable.

## Approval and release procedure

1. Inventory existing Alpha2.73 events and assign IDs before creating sounds. The register above is a proposed first pass; validate exact trigger hooks when implementing.
2. Define each sound's desired character, create separately versioned candidates and audition them as a coherent pack. Do not mark candidate files approved until the user listens and approves.
3. Register approved source asset, metadata and licensing. Integrate only selected assets into a new, uniquely numbered **complete standalone HTML test**, using the verified current production baseline and the GitHub-to-local transfer procedure in `docs/WORKFLOW.md`.
4. Perform syntax/logic checks and user Android testing; iterate without publishing test gameplay to GitHub by default.
5. Only on explicit **Push to prod** for the exact approved HTML candidate, archive the immutable tested file, produce the production-label-only copy, update production and required release documents, verify Actions/Pages/live version and record user Android confirmation. No sound-documentation commit is production-game approval.

## Initial mix guidance (provisional)

Prioritize aircraft warnings, dome damage and Game Over over routine shots; duck ambience beneath important cues. Limit simultaneous repeated fire sounds, avoid startling peak levels, and provide mute and volume control. Test through phone speakers as well as headphones. Use real-world observing references sparingly: the aim is recognisable astronomical character, not physically literal sound in space.

## Open decisions

- Agree on the final list and which sounds should be audible versus intentionally silent (especially satellites and space objects).
- Choose synthesis vs recorded assets for each ID, and whether multiple randomized variants share one ID.
- Set final mixing levels only after auditioning an integrated Android build.
