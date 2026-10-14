# Production pipeline — implementation specification

## Key distinction
The viewer receives a **linear pre-rendered YouTube video**, with gameplay-like HUD and timed events. Codex authors code and configuration; Unreal Engine running on a cloud GPU generates the actual visuals. Neither a Codex environment nor this repository should claim that rendering was completed without an MP4 and inspection.

## Shot design
Use the timeline in `episodes/001-pilot.json`. Unreal Sequencer shot tracks should align precisely with beat boundaries; use a single camera and smoothly eased translations, avoiding cuts or excessive head bob.

## Render requirements (targets; not currently validated)
- 3840x2160 resolution at 60fps (30s = 1800 frames)
- Movie Render Queue with a fixed camera path and reproducible lighting
- Linear footage with 5 beats: hook, pursuit, safe exercise stop, rescue reward, transition
- Audio synchronization and game HUD compositing
- Generate a cheap 720p preview first, then a final 4K render only after review

## Asset requirements
Use licensed high-quality Unreal-compatible African savanna foliage, cliffs, rocks and original animal models/animations. Record license and provenance. No Disney IP. High-quality assets and creative art direction are prerequisites for a premium result.

## Cloud GPU implementation
Provision a Windows GPU VM with adequate NVIDIA VRAM and Unreal version matching the project. Install Unreal Engine, renderer prerequisites and FFmpeg. Keep credentials in cloud secrets. Clone/pull repository. Import licensed assets stored separately in object storage. Trigger an Unreal headless or scripted Movie Render Queue render; upload artifacts to cloud storage. **Stop and deallocate the instance when idle**. No VM has been provisioned yet.

## Quality acceptance
Human review of actual 10–15 second Unreal renders for cinematic realism, animal fidelity, POV comfort, smooth pacing, clear objective, optional exercise safety and satisfying visual feedback. Expand to 30 seconds only if accepted; expand to 30 minutes later.

## Start commands
```bash
python scripts/validate_episode.py episodes/001-pilot.json
```

## Next engineering task for Codex
Implement an Unreal Engine 5 project scaffold, Sequencer and camera-path generator driven by the episode JSON, and a Movie Render Queue job definition. Scripts must be idempotent and explain which steps need an Unreal installation. Do not substitute a 2D video prototype.
