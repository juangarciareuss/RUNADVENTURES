# RunAdventures – Instructions for Codex

You are working on RunAdventures, a premium, original first-person exercise-adventure video production system.

## Non-negotiables
- The viewer **jogs in place on the floor**, not on a treadmill. Maintain a smooth, comfortable POV camera.
- Use Unreal Engine 5 for the final 3D world and Movie Render Queue for output; never substitute simple generated 2D animations and claim AAA quality.
- You may generate scaffolding/scripts without a GPU but never claim a rendered scene was produced or tested unless the output exists and was inspected.
- Video playback is not interactive: no real-time motion sensing or collecting items through the YouTube player. Collectables in the first version are timed narrative events.
- Exercises (e.g., squats, reaching, optional side steps) happen only after the running motion has stopped. Avoid sudden lateral jumps or twisting while running. Include an accessible skip/low-impact path.
- Build an original African-inspired environment; no Disney characters, names, logo, exact shots or music.
- Keep cost controls and stop-on-idle on cloud infrastructure; never embed cloud credentials.
- Do not commit heavy proprietary 3D assets, binary build output or generated videos into Git. Document their storage and licenses.
- Prefer small testable changes with clear README instructions.

## First implementation
1. Create a JSON schema for episode definitions: metadata, biomes, route segments, encounters, collectibles, movement prompts, safe stops and audiovisual cues.
2. Add a valid sample Episode 001 manifest and Python tests for its consistency.
3. Document the GPU/cloud render setup without provisioning paid services without user approval.
4. Create a minimal Unreal automation plan and scripts that can be validated without a local engine installation.
5. Mark all visual/render claims as *planned* until verified.

## Definition of done: first real render
A real cloud GPU workstation runs Unreal Engine and outputs a continuous 10–15 second first-person run in a photorealistic African-inspired savanna scene. Keep the actual MP4 and screenshots outside Git; document settings and result.

## Repository conventions
- docs/: architecture, gameplay and setup
- episodes/: JSON episode manifests
- schemas/: schemas
- scripts/: tooling and validations
- unreal/: Unreal project and automation (as available)
- infrastructure/: IaC and deployment guides
