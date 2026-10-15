# Alpha2.64 handover — online leaderboard

Based on Alpha2.63; approved Dobsonian design and gameplay retained.

## New features
- Nickname-only player registration, with browser-local identity and random secret.
- Global top-50 leaderboard from Supabase.
- Only the player's highest score is stored, with night reached.
- Nickname changes retain player identity and score.
- Game Over submits the score.

## Backend
Supabase project: Dob Defender, region eu-west-1.
Edge Function: dob-leaderboard.
Database: dd_players, dd_rate_limits.
The service-role key stays server-side. Browser identity can be lost by clearing storage. This casual leaderboard is not cheat-proof.

## Validation and known issues
Supabase migration succeeded; Edge Function deployed active; HTML committed to GitHub. Android gameplay, browser network calls and automated syntax workflow have not yet been verified.
Earlier handover: docs/HANDOVER.md. Earlier build preserved: Alpha2.63.
