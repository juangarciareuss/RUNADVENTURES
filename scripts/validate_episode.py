#!/usr/bin/env python3
"""Validate the timing and basic safety of a linear RunAdventures episode."""
import json
import sys
from pathlib import Path

def validate(data):
    errors = []
    beats = data.get("beats", [])
    duration = data.get("duration_seconds")
    if not isinstance(duration, int) or duration <= 0:
        errors.append("duration_seconds must be a positive integer")
    if data.get("format") != "linear_prerendered_video":
        errors.append("format must be linear_prerendered_video")
    if not beats:
        errors.append("At least one beat is required")
    previous_end = 0
    for index, beat in enumerate(beats):
        start, end = beat.get("start"), beat.get("end")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            errors.append(f"Beat {index}: start/end must be numeric")
            continue
        if start != previous_end:
            errors.append(f"Beat {index}: expected start {previous_end}, got {start}")
        if end <= start:
            errors.append(f"Beat {index}: end must be greater than start")
        if beat.get("type") == "exercise_stop" and "stop" not in beat.get("visual", "").lower():
            errors.append(f"Beat {index}: exercise must explicitly stop virtual camera")
        previous_end = end
    if isinstance(duration, int) and previous_end != duration:
        errors.append(f"Timeline ends at {previous_end}s, expected {duration}s")
    return errors

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("episodes/001-pilot.json")
    errors = validate(json.loads(path.read_text(encoding="utf-8")))
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        sys.exit(1)
    print(f"OK: {path} timeline and basic constraints valid")
