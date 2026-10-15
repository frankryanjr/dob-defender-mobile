# Alpha2.66 — Versioned score history

- Each score submission now stores the exact game version, score, night reached and submission timestamp in `public.dd_score_history`.
- The player's highest score also retains the version in `public.dd_players.best_version`.
- Existing verified screenshot result for Stargazerman (7,525, Night 9) is attributed to Alpha2.65.
- Historical submissions allow future version-based rankings and seasons without changing the current global leaderboard.
- Supabase Edge Function `dob-leaderboard` version 2 accepts `version` in score submissions.
- Older clients that omit version cannot submit a score; upgrade to Alpha2.66.
- JavaScript syntax compiled successfully. Live Android score submission still requires verification.

## Future seasons
A season identifier can later be added to the history table or mapped from submission timestamps; the historical data is preserved.
