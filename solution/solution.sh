#!/usr/bin/env bash
set -euo pipefail

WORKDIR="/app"
cd "$WORKDIR"

python3 -c '
import struct
import zlib

with open("input_bundle.dat", "rb") as f:
    raw = f.read()
'
