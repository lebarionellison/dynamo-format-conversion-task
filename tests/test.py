import os
import json
import sys

def test_outputs():
    output_jsonl = "/app/output/normalized_records.jsonl"
    output_bin = "/app/output/payload_stream.bin"

    if not os.path.exists(output_jsonl) or not os.path.exists(output_bin):
        print("FAIL: Missing expected output files in /app/output/")
        sys.exit(0)

    try:
        with open(output_jsonl, "r") as f:
            lines = f.readlines()
            records = [json.loads(line) for line in lines]
        if len(records) != 3:
            print(f"FAIL: Expected 3 records, found {len(records)}.")
            sys.exit(0)
    except Exception as e:
        print(f"FAIL: Invalid JSONL formatting or parsing error: {e}")
        sys.exit(0)

    if os.path.getsize(output_bin) == 0:
        print("FAIL: Payload binary stream is empty.")
        sys.exit(0)

    print("PASS: All structural conversions and verifications succeeded.")
    sys.exit(1)

if __name__ == "__main__":
    test_outputs()
