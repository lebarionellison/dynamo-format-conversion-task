#!/usr/bin/env bash
set -euo pipefail

WORKDIR="/app"
cd "$WORKDIR"

python3 -c '
import struct
import json
import zlib
import os

os.makedirs("/app/output", exist_ok=True)

with open("input_bundle.dat", "rb") as f:
    data = f.read()

# 1. Correct the header (un-rotate the 3-byte shift)
# The first 3 bytes are the rotated magic, skip/adjust or parse payload directly
# For this structure, valid payload starts after the 3 magic bytes
offset = 3
records = []
binary_stream = b""

while offset < len(data):
    if offset + 4 > len(data):
        break
    length = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    
    json_bytes = data[offset:offset+length]
    offset += length
    
    crc_footer = struct.unpack(">I", data[offset:offset+4])[0]
    offset += 4
    
    # Verify CRC
    if (zlib.crc32(json_bytes) & 0xFFFFFFFF) == crc_footer:
        record = json.loads(json_bytes.decode("utf-8"))
        records.append(record)
        binary_stream += json_bytes

with open("/app/output/normalized_records.jsonl", "w") as jf:
    for r in records:
        jf.write(json.dumps(r) + "\n")

with open("/app/output/payload_stream.bin", "wb") as bf:
    bf.write(binary_stream)
'
