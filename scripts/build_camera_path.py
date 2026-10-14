#!/usr/bin/env python3
"""Create deterministic 60fps POV camera coordinates from an episode manifest.

Outputs a camera.csv for ingestion by Unreal Sequencer tooling; not a render.
Distances use centimeters, times are exact frame multiples.
"""
import argparse
import csv
import json
import math
from pathlib import Path

RUN_SPEED_CM_S = 230.0
EYE_HEIGHT_CM = 170.0
FRAME_RATE = 60

def sample_camera(data, fps=FRAME_RATE):
    duration = data["duration_seconds"]
    beats = data["beats"]
    walk_cm = 0.0
    result = []
    for frame in range(duration * fps + 1):
        time_s = frame / fps
        beat = next((b for b in beats if b["start"] <= time_s < b["end"]), beats[-1])
        is_running = beat["type"] in ("run", "transition")
        # Exact frame integration; stop and exercise do not move the virtual camera.
        if frame and is_running:
            walk_cm += RUN_SPEED_CM_S / fps
        # Gentle side-to-side curvature without sharp turns.
        x_cm = walk_cm
        y_cm = 75.0 * math.sin(walk_cm / 1400.0)
        z_cm = EYE_HEIGHT_CM
        # Avoid exaggerated head bob and artificial camera rolls for comfort.
        yaw = math.degrees(math.atan2(75.0 / 1400.0 * math.cos(walk_cm / 1400.0), 1.0))
        result.append((frame, round(time_s, 6), round(x_cm, 3),
                       round(y_cm, 3), round(z_cm, 3), 0.0, round(yaw, 4), 0.0,
                       beat["type"]))
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episode", default="episodes/001-pilot.json")
    parser.add_argument("--output", default="output/camera.csv")
    args = parser.parse_args()
    data = json.loads(Path(args.episode).read_text(encoding="utf-8"))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(("frame","time_s","x_cm","y_cm","z_cm","pitch_deg","yaw_deg","roll_deg","beat"))
        writer.writerows(sample_camera(data))
    print(f"Wrote {data['duration_seconds'] * FRAME_RATE + 1} frames to {output}")

if __name__ == "__main__":
    main()
