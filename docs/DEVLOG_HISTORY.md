# Dob Defender — Development History

*Public-facing overview | Updated 27 October 2026*

Dob Defender began as an idea for a mobile arcade game combining amateur astronomy, a Dobsonian telescope, science fiction and the arcade games that inspired its creator. The player aims a telescope-mounted green laser at incoming threats, protects the observatory, and tries to save the cows. This is a development timeline, not a list of every internal test build.

**Read the detailed history:** [Project History and Production Tracker](PROJECT_HISTORY.md). For version-by-version changes, also see the [Changelog](CHANGELOG.md). Dates and approvals below follow current GitHub evidence, supplemented by earlier preserved chat and handover records.

| Date | Milestone | What changed |
| --- | --- | --- |
| **11–12 Oct 2026** | The concept and first prototypes | A touch-controlled Dobsonian telescope versus meteors, asteroids, comets and other sky threats; green laser firing and arcade scoring. |
| **12 Oct** | Telescope design locked; Alpha1 | Numerous artwork iterations (early v9–v28 previews) produced the compact brown truss telescope, silver bearings and trusses, side-mounted laser pointer, and slider/fire controls. Alpha1 used lives and score-based levels. |
| **12 Oct** | Alpha2 changes the game | Replaced conventional levels with dusk-to-dawn **Nights**; introduced scheduled attacks, dome integrity, finite laser energy, cow rescues/abductions, ISS recharge, Starlink and the aircraft safety warning. |
| **12–14 Oct** | Gameplay development | Adjusted early difficulty, aiming and touch behavior, cow/UFO movement, comet trails, impacts and destruction effects. The astronomy setting and approved telescope art stayed central. |
| **14 Oct** | Alpha2.63 title presentation | Clear instructions, DEFEND! start action and centered version label. |
| **15 Oct** | GitHub and online rankings | Source/version history moved into GitHub. Alpha2.64–2.67 introduced nickname registration, Supabase-backed worldwide scores, and repairs to the initial deployment. |
| **16 Oct** | Start Screen v1 approved | Finished title artwork selected and preserved for subsequent releases. |
| **18 Oct** | Alpha2.68–2.69 scoring and night flow | Dome damage, Laser Sight power-up, richer space debris, animated night-end scoring and a persistent Game Over screen. |
| **19 Oct** | Alpha2.70–2.73 refinements | Corrected dome destruction and score popups, improved leaderboard navigation and phone layouts, reshaped final results, and rebalanced waves, power-ups and laser energy. |
| **23–25 Oct** | Alpha2.74–2.78 sound design | Added, selected and mixed laser, impact, UFO, aircraft, telescope and interface sounds, plus background music and score-tally audio. |
| **25 Oct** | Alpha2.79 expanded world | Start-screen **Nights Defended Worldwide** indicator; four cows, revised saved/lost tally, more UFO abductions and dual abductors from later nights. |
| **26 Oct** | Alpha2.80 bug fixes | Prevented already-abducted cows from remaining visible in midair; made game-over leaderboard submission status and retry handling clearer. Approved and committed to GitHub production. |

## Beyond the code

The project also involved selecting and preserving artwork, making original design and sound decisions, repeated Android playtests, recording rejected ideas, establishing a strict test-and-approval release process, and preparing the game for public playtesting on itch.io. Some ideas required many test versions before being approved; test numbers must not be confused with published versions.

## For future itch.io devlogs

Use this overview as a stable introduction. Each new devlog can highlight **what changed**, **why it changed**, **what players should notice**, and **what still needs feedback**. Refer back to the [detailed development history](PROJECT_HISTORY.md), [changelog](CHANGELOG.md), and [development handover](HANDOVER.md) before claiming a release, fix or test result.

The repository is the source of truth. GitHub production and the separately uploaded itch.io game may be on different versions. A commit, Pages deployment, Android test and itch.io upload are distinct milestones.
