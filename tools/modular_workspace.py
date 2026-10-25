#!/usr/bin/env python3
"""Dob Defender lossless development workspace. No production publication.

Usage:
  python tools/modular_workspace.py split approved.html workspace --expected-sha GIT_BLOB_SHA
  python tools/modular_workspace.py build workspace rebuilt.html
  python tools/modular_workspace.py check workspace

Works on the exact bytes of a verified approved HTML file. Keep the original
source unchanged. Assets are external only in the *working* directory; build
re-embeds everything into one standalone HTML with SHA verification.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

BLOCK_RE = re.compile(rb"<(?:style|script)\b[^>]*>[\s\S]*?</(?:style|script)\s*>", re.I)
MEDIA_RE = re.compile(rb"data:(?:audio|image)/[a-zA-Z0-9.+-]+(?:;[a-zA-Z0-9=+\-]+)*;base64,[A-Za-z0-9+/=]+")
TOKEN_RE = re.compile(rb"@@DOB_(?:BLOCK|MEDIA)_[0-9]{3}@@")


def git_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def split(source, workspace, expected):
    original = source.read_bytes()
    actual = git_sha(original)
    if actual != expected:
        raise ValueError(f"Source is not the expected approved file: {actual} != {expected}")
    if not original.rstrip().lower().endswith(b"</html>"):
        raise ValueError("Source has no complete closing HTML tag")
    if workspace.exists() and any(workspace.iterdir()):
        raise ValueError("Workspace must be new/empty; refusing to overwrite")
    workspace.mkdir(parents=True, exist_ok=True)
    blocks, media = [], []
    template = bytearray()
    last = 0
    for index, match in enumerate(BLOCK_RE.finditer(original), 1):
        token = f"@@DOB_BLOCK_{index:03d}@@".encode()
        block = match.group()
        template.extend(original[last:match.start()])
        template.extend(token)
        block_data = bytearray()
        prev = 0
        for asset in MEDIA_RE.finditer(block):
            media_token = f"@@DOB_MEDIA_{len(media)+1:03d}@@".encode()
            media_name = f"assets/media_{len(media)+1:03d}.txt"
            block_data.extend(block[prev:asset.start()])
            block_data.extend(media_token)
            (workspace / "assets").mkdir(exist_ok=True)
            (workspace / media_name).write_bytes(asset.group())
            media.append({"token": media_token.decode(), "path": media_name})
            prev = asset.end()
        block_data.extend(block[prev:])
        suffix = "css" if block.lower().startswith(b"<style") else "js"
        name = f"blocks/block_{index:03d}.{suffix}"
        (workspace / "blocks").mkdir(exist_ok=True)
        (workspace / name).write_bytes(block_data)
        blocks.append({"token": token.decode(), "path": name})
        last = match.end()
    template.extend(original[last:])
    if not blocks:
        raise ValueError("No script/style blocks found")
    (workspace / "template.html").write_bytes(template)
    manifest = {"format": 1, "source_git_sha": actual, "source_bytes": len(original),
                "blocks": blocks, "media": media}
    (workspace / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Split: {len(blocks)} blocks, {len(media)} assets; source {len(original)} bytes; SHA {actual}")
    check(workspace)


def rebuild(workspace):
    manifest = json.loads((workspace / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("format") != 1:
        raise ValueError("Unsupported manifest format")
    result = (workspace / "template.html").read_bytes()
    for group in ("blocks", "media"):
        for part in manifest[group]:
            token = part["token"].encode()
            if result.count(token) != 1:
                raise ValueError(f"Missing or duplicate token: {token!r}")
            result = result.replace(token, (workspace / part["path"]).read_bytes())
    if TOKEN_RE.search(result):
        raise ValueError("Unresolved workspace placeholder")
    return result, manifest


def check(workspace):
    result, manifest = rebuild(workspace)
    actual = git_sha(result)
    if len(result) != manifest["source_bytes"] or actual != manifest["source_git_sha"]:
        raise ValueError(f"Build differs from original approved source: {len(result)} bytes; SHA {actual}")
    print(f"PASS: byte-identical build ({len(result)} bytes; SHA {actual})")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("split")
    s.add_argument("source", type=Path)
    s.add_argument("workspace", type=Path)
    s.add_argument("--expected-sha", required=True)
    b = sub.add_parser("build")
    b.add_argument("workspace", type=Path)
    b.add_argument("output", type=Path)
    c = sub.add_parser("check")
    c.add_argument("workspace", type=Path)
    args = parser.parse_args()
    if args.command == "split":
        split(args.source, args.workspace, args.expected_sha)
    elif args.command == "check":
        check(args.workspace)
    else:
        data = check(args.workspace)
        if args.output.exists():
            raise ValueError("Output already exists; refusing to overwrite")
        args.output.write_bytes(data)
        print(f"Built: {args.output}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
