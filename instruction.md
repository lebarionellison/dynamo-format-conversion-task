# Objective

An incoming telemetry and asset bundle has been deposited in `/app/input_bundle.dat`. Due to a transmission error, the file suffers from the following anomalies:
1. The global header magic bytes have been rotated by 3 bytes.
2. Individual payload blocks are wrapped in an invalid custom framing format with mismatched CRC32 footers.
3. Embedded metadata structures use mixed endianness.

Your goal is to write a processing script or sequence of terminal commands in `/app` to:
- Fully parse and correct the underlying file structure.
- Extract all valid data frames.
- Export the final reconstructed data into two mandatory outputs:
  - `/app/output/normalized_records.jsonl` (containing the parsed metadata records)
  - `/app/output/payload_stream.bin` (containing the concatenated, raw corrected binary payload)

The verifier will check the exact cryptographic checksum and structural integrity of both output files in `/app/output/`.
