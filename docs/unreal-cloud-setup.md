# RunAdventures — Unreal cloud setup (not provisioned)

## Current stage
This repository contains Unreal project configuration, a manifest-driven camera trajectory CSV generator, CI tests and design documentation. **There is no provisioned GPU, imported 3D environment or completed Unreal-rendered video yet.**

## Cloud workstation
1. Choose a **Windows machine with NVIDIA GPU**, adequate VRAM and storage, and an interactive remote desktop solution that works in Android browser. Check the Unreal Engine hardware requirements and cloud provider quota before buying hours.
2. Install the matching Unreal Engine version from the Epic Games launcher (currently configured for 5.5, pin a tested version before production).
3. Clone the GitHub repo and open `unreal/RunAdventures.uproject` to create project metadata.
4. Add licensed Fab/Marketplace/environment and animal assets **outside the code repository**. Store asset inventory, versions and licensing evidence in cloud object storage.
5. Generate camera trajectory CSV:
   `python scripts/build_camera_path.py --episode episodes/001-pilot.json --output output/camera.csv`
6. Implement UE Editor Sequencer importing of the CSV to a CineCameraActor transform track. Camera coordinates are in centimeters (x forward; z up), with 60 frames/second.
7. Create first level using professional savanna landscape, photorealistic lighting and foliage assets, then set up Movie Render Queue (start 720p before 4K).
8. Upload outputs to cloud storage, inspect first frames and sample full clip, then shut down and **deallocate** VM to avoid hourly charges.

## Security and budget
- No cloud accounts, servers, API keys, remote access or bills were created by these repository commits.
- Require explicit approval before creating billable resources.
- Place hard budget alerts and an idle-shutdown mechanism before long rendering.
- Use GitHub Actions only for data tests, not UE 4K rendering.
- Do not expose an unprotected RDP port; use a reputable authenticated remote access method.

## Next task for Codex
Implement an Unreal Python Sequencer camera importer and verify its APIs **inside the configured Unreal version**, then save a sample level sequence. A bare CSV is not a playable level or movie.
