# Dob Defender — gameplay reference

**Current release:** Alpha2.64. **First retained build:** Alpha2.17.

## Player profiles and leaderboard

Players register a unique nickname once per browser. A locally stored player identity supports nickname changes and automatic submission of the best score on Game Over. The global leaderboard shows up to 50 top scores and night reached. Clearing browser data loses the locally stored identity; internet access is required for registration and score submission.

## Objective

Defend your observatory from incoming meteorites, asteroids and comets. Save cows. Do not shoot aircraft. Survive each night until dawn.

## Touch controls

- Relative left/right swipe on centred aiming slider rotates telescope.
- Tap slider or sky to fire one shot.
- Pause button suspends gameplay.
- DEV panel offers testing tools, including jumping to a selected night, restarting and importing Yale BSC5 data.

## Systems to preserve

- Approved Dobsonian telescope silhouette and laser origin.
- Laser energy and recharge/cost; dome health; score; nights and restarts.
- Meteors/asteroids/comets, UFO cow abduction, aircraft warnings, ISS and Starlink encounters.
- Astronomical sky field and Yale Bright Star Catalogue support with local caching/import.
- Mobile-first responsive layout and thumb-operated controls.

## Scope

This is a concise reference, not a complete reverse-engineered mechanics specification. Consult the playable HTML and historical handover for precise constants, schedules, scoring and collision behaviour. When there is a discrepancy, the latest approved HTML is authoritative.
