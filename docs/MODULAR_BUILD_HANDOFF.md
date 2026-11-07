# Dob Defender — Modular build handoff

**Purpose:** let any AI or platform (Claude, ChatGPT or another) work on the game without loading the whole 3.8 MB HTML file at once. This document is the method. The split tool lives in `tools/modular_workspace.py`. The archived files in `releases/` are the source of truth.

**Status (7 November 2026):** verified. The archived Test 26 file (`releases/Dob_Defender_Alpha2.80_Mothership_Boss_Test_26.html`, blob `398334335c90e4062141445ff6eaf3ebfdd955bb`) splits into 10 pieces and rebuilds byte for byte. Its game-logic piece matches the working copy used for the released build. So the source is recoverable from GitHub at any time. No separate source folder is needed.

## 1. Why the split exists
The standalone game HTML is about 3.8 MB. Most of that is base64-encoded sounds and images. A chat can't read or rewrite a file that size in one go, and earlier attempts broke it into several partial files that were hard to reassemble. The split avoids that: each piece is small enough to read, edit and check on its own, and a script puts them back together.

## 2. The three parts of a split
| Part | What it is | Example |
|---|---|---|
| `template.html` | The page skeleton with **tokens** where each script or style block was. | `@@DOB_BLOCK_006@@` |
| `blocks/block_NNN.js` / `.css` | The `<script>` and `<style>` contents, in document order. The game logic is `block_006.js`, about 160 KB. | `blocks/block_006.js` |
| `assets/media_NNN.txt` | Base64 `data:` URIs (sounds and images) pulled out of the blocks. | `assets/media_001.txt` |
| `manifest.json` | Format version, the source blob SHA and byte count, and the list of tokens with their file paths. | |

Rebuilding replaces each token with the contents of its file. Nothing else is changed.

## 3. Split an approved file
Get the file from GitHub (for example, the archive for the current production build, `releases/Dob_Defender_Alpha2.81.html`, or the approved test archive). Then run:

```
python3 tools/modular_workspace.py split releases/Dob_Defender_Alpha2.80_Mothership_Boss_Test_26.html workspace --expected-sha 398334335c90e4062141445ff6eaf3ebfdd955bb
```

- `--expected-sha` must be the Git blob SHA of the file you split. The tool refuses any other file.
- The workspace folder must be new or empty.
- The tool runs a `check` automatically. A PASS means the rebuilt output is byte-identical to the original.

## 4. Build from an unedited split
```
python3 tools/modular_workspace.py build workspace rebuilt.html
```
This works only while the blocks are unchanged.

## 5. Edit and build (the normal case)
1. Split the current archive into a new empty workspace (step 3).
2. Edit only the block files you need. Use grep or read line ranges in `block_006.js`. Don't load the whole file at once.
3. Build with the script below. **Don't use `build` after editing**: its check compares against the original file, so it always refuses an edited workspace.

```python
# build_edited.py: join the pieces, verify every token, write a new file. Never overwrites.
import json, pathlib, re, sys
ws, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
assert not out.exists(), "output exists"
m = json.loads((ws / "manifest.json").read_text(encoding="utf-8"))
result = (ws / "template.html").read_bytes()
for group in ("blocks", "media"):
    for part in m[group]:
        token = part["token"].encode()
        assert result.count(token) == 1, token
        result = result.replace(token, (ws / part["path"]).read_bytes())
assert not re.search(rb"@@DOB_(BLOCK|MEDIA)_", result), "unresolved token"
out.write_bytes(result)
print(len(result), "bytes written to", out)
```

## 6. Checks before any test or release
- **Script syntax:** extract every inline `<script>` (no `src=`) from the built file and run `node --check` on each. Don't check only the last one.
- **Smoke test:** load the built file in headless Chrome at 390×844 with no page errors. Then exercise the change.
- **Hash record:** record the byte count and Git blob SHA (`git hash-object file`) for any candidate.

## 7. Pitfalls we hit
- **Line comments in game script:** a `//` comment at the end of a long line comments out the rest of that line, which can break the whole script. Use `/* … */` for inline comments.
- **Undeclared variables in test code:** `page.evaluate` runs in its own scope. Declare variables with `const` or `let`.
- **Stale browser cache:** test links need a new `?v=` number. Check the served version, not just the link.
- **Splitting a dirty file:** only split an approved file with its expected SHA. Never split a hand-edited copy and call it approved.

## 8. Where things go
- Test builds: `tests/` on `main` and `dev`, labelled UNAPPROVED / TEST BUILD (see `docs/WORKFLOW.md` §4A).
- Production: only after explicit approval, following `docs/WORKFLOW.md` §4 and `docs/RELEASE_CHECKLIST.md`. The production file is derived from an archived copy with only the label changes.
- Playtest reports and the decisions they led to: `docs/PLAYTEST_LOG.md`.
