import struct
import json
import zlib

def build_asset():
    # 1. Create sample structured telemetry records
    records = [
        {"id": 1, "sensor": "thermal_core_0", "status": "nominal", "val": 42.5},
        {"id": 2, "sensor": "thermal_core_1", "status": "warning", "val": 89.1},
        {"id": 3, "sensor": "power_rail_a", "status": "nominal", "val": 12.0}
    ]
    
    # 2. Package into raw binary stream with shifted magic bytes (simulation of transmission corruption)
    raw_payload = b""
    for r in records:
        json_bytes = json.dumps(r).encode('utf-8')
        # Frame format: [Length: 4 bytes big endian][JSON payload][CRC32: 4 bytes]
        length_header = struct.pack(">I", len(json_bytes))
        crc = zlib.crc32(json_bytes) & 0xFFFFFFFF
        crc_footer = struct.pack(">I", crc)
        raw_payload += length_header + json_bytes + crc_footer

    # Apply intentional rotation/corruption to the global header magic bytes (shift by 3 bytes)
    magic = b"DYN" # Original magic
    corrupted_magic = magic[3:] + magic[:3] # Rotated
    
    complete_bundle = corrupted_magic + raw_payload

    with open("/app/input_bundle.dat", "wb") as f:
        f.write(complete_bundle)

if __name__ == "__main__":
    build_asset()
