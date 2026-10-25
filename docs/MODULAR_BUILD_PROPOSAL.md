# Dob Defender — modular build feasibility (25 October 2026)

**Status: PROTOTYPE ONLY. Not approved as the authoritative source or production build.** No gameplay, artwork, audio, `main:index.html`, or release archive changed.

## Evidence
- Source: exact approved Alpha2.76 Sound Test 25 archive, Git blob `52352378f7fe288c52351d73b0fd4c74abc3b1aa`, 3,775,585 bytes.
- A local prototype extracts 5 inline CSS blocks, 3 inline JavaScript blocks and 46 embedded image/audio data URIs into separate text files. The main script shrinks to 122,153 bytes after media extraction.
- A small deterministic Python script replaces exact placeholder tokens with the original bytes and checks total length and `git hash-object`. Reconstructed HTML is byte-for-byte identical to the approved archive, with the same Git blob SHA.
- The prototype is a ChatGPT downloadable ZIP, not yet part of the repository. It contains `template.html`, `part_*.css`, `part_*.js`, `media_*.txt`, `manifest.json`, `build.py`. Running `python3 build.py` reconstructs `rebuilt_test.html`.
- **Limitations:** This demonstrates exact reversible packaging only. It is not a semantic JavaScript module refactor, not yet a verified production-source build, and does not prove Android runtime performance. Some individual media assets remain large. It does not reduce the final standalone HTML size.

## Recommended next controlled steps
1. Confirm the prototype rebuild SHA and JavaScript syntax locally; compare asset counts and startup behaviour against approved archive.
2. Obtain/verify exact current production `main:index.html` bytes and build a *separate* prototype from production; do not infer production bytes from a test candidate or use an old uploaded HTML.
3. Keep the current standalone HTML production model. Develop a deterministic build script and versioned source tree only after a separate architecture approval; preserve all locked artwork/gameplay.
4. Add CI checks for exact build reproducibility, script syntax, accidental placeholder tokens, version labels, media count and Git blob checks. Require explicit approval before changing production or adopting the modular source as authoritative.
5. Prefer direct verified file transfer over Google Docs Base64 bridge when supported. Delete temporary transport documents after hash verification; preserve troubleshooting records.

## Existing cleanup status
17 verified obsolete Drive transfer documents deleted on 25 October 2026. One old Alpha2.68 temporary document could not be deleted because the operation was blocked; the troubleshooting log was retained. Current GitHub production remains Alpha2.76, blob `68da879b0120364df1128848e115200deec636b6`.
