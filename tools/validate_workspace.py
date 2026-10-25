#!/usr/bin/env python3
"""Read-only modular workspace validation. Requires Python 3 and Node.js."""
import argparse
import base64
import binascii
import json
import re
import subprocess
import sys
from pathlib import Path

URI = re.compile(rb'data:(?:image|audio)/[a-zA-Z0-9.+-]+(?:;[a-zA-Z0-9=+\\-]+)*;base64,([A-Za-z0-9+/=]+)')
MARKERS = ('laser', 'meteor', 'asteroid', 'comet', 'aim', 'pointer',
           'score', 'collision', 'audio', 'telescope')

def validate(root, markers=False):
    manifest = json.loads((root / 'manifest.json').read_text())
    if manifest.get('format') != 1:
        raise ValueError('Unsupported workspace manifest')
    template = (root / 'template.html').read_bytes()
    blocks = manifest['blocks']
    media = manifest['media']
    if len({e['token'] for e in blocks + media}) != len(blocks) + len(media):
        raise ValueError('Duplicate manifest tokens')
    combined = bytearray(template)
    js_count = 0
    for block in blocks:
        token = block['token'].encode()
        if template.count(token) != 1:
            raise ValueError('Missing or duplicate template token')
        path = Path(block['path'])
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Unsafe manifest path')
        raw = (root / path).read_bytes()
        combined.extend(raw)
        if path.suffix == '.js':
            script = re.sub(rb'^<script\b[^>]*>', b'', raw, count=1, flags=re.I)
            script = re.sub(rb'</script\s*>\s*$', b'', script, count=1, flags=re.I)
            result = subprocess.run(['node', '--check', '--input-type=commonjs'],
                                    input=script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode:
                raise ValueError('JavaScript syntax failed in ' + str(path) +
                                 ': ' + result.stderr.decode(errors='replace')[-250:])
            js_count += 1
    for item in media:
        token = item['token'].encode()
        if combined.count(token) != 1:
            raise ValueError('Missing or duplicate media token')
        path = Path(item['path'])
        if path.is_absolute() or '..' in path.parts:
            raise ValueError('Unsafe manifest path')
        raw = (root / path).read_bytes()
        match = URI.fullmatch(raw)
        if not match:
            raise ValueError('Malformed data URI: ' + str(path))
        try:
            decoded = base64.b64decode(match.group(1), validate=True)
        except binascii.Error as exc:
            raise ValueError('Invalid Base64: ' + str(path)) from exc
        if not decoded:
            raise ValueError('Empty asset: ' + str(path))
    if markers:
        text = bytes(combined).lower()
        missing = [m for m in MARKERS if m.encode() not in text]
        if missing:
            raise ValueError('Missing source markers: ' + ', '.join(missing))
    print(f'PASS: {js_count} JS syntax checks; {len(media)} decoded assets; token checks; markers={markers}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('workspace', type=Path)
    parser.add_argument('--source-markers', action='store_true')
    args = parser.parse_args()
    try:
        validate(args.workspace, args.source_markers)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print('FAIL:', exc, file=sys.stderr)
        sys.exit(1)
