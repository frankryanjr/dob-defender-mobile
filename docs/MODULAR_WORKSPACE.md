# Efficient modular development workspace (experimental)

This is an **internal development tool**, not a user deliverable or a change to the production game.

## What it does

`tools/modular_workspace.py` separates a verified approved standalone HTML into individual CSS/JavaScript blocks and embedded media assets. It stores exact byte slices, not reformatted source. The build command reassembles the original HTML and requires the exact Git blob SHA and byte length. The result remains a complete, offline-capable standalone HTML file.

The large embedded assets no longer need to be read/edited when working on a small JavaScript/CSS section. **This does not make the final HTML smaller or faster at runtime**, and it does not by itself automate GitHub transfer or deployment.

## Safety and scope

- Read README and the complete WORKFLOW first. Confirm current GitHub production `index.html` SHA and archive SHA.
- Before splitting, acquire the exact current production HTML bytes by the documented lossless connector transfer and verify `git hash-object` matches GitHub production. An approved archive is useful for feasibility testing but **must not substitute for current production as the next development baseline**.
- Split into a fresh working directory. The script refuses a nonempty directory or an unverified source.
- `check` verifies byte-identical reconstruction of the untouched baseline. It intentionally fails after source edits; a later candidate must instead be validated as a deliberate diff from the approved baseline, with syntax checks and a unique test version.
- Never publish the workspace or any rebuilt candidate to production without the user's explicit approval and the archive gate.
- Keep source/asset files internal. Only give the user a complete standalone HTML when user testing is required.
- No production code, game mechanics, audio or artwork are changed by adding this tooling.

## Commands

```bash
python3 tools/modular_workspace.py split /path/to/verified-index.html /tmp/dd-workspace --expected-sha <current-production-git-blob-sha>
python3 tools/modular_workspace.py check /tmp/dd-workspace
python3 tools/modular_workspace.py build /tmp/dd-workspace /tmp/dd-rebuilt.html
git hash-object /tmp/dd-rebuilt.html
```

## Status

The earlier Alpha2.76 Sound Test 25 proof of concept reconstructed 3,775,585 bytes with archive SHA `52352378f7fe288c52351d73b0fd4c74abc3b1aa`, separating 46 embedded media assets and reducing the largest JavaScript working section to about 122 KB. This was a **prototype using the approved archive**, not a production-source migration.

This checked-in tool has been added as a reusable implementation. Full end-to-end verification against the current production `index.html` and any deployment automation remains outstanding. Do not claim production modularisation is complete until those gates pass.
