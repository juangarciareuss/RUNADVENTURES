# RunAdventures

**RunAdventures** is an original, cinematic exercise-adventure experience designed for running in place while watching a first-person video on YouTube.

## Vision
Create high-quality continuous 3D adventures, with physical movement cues, collectables and story-driven missions. Viewers jog in place, not on a treadmill. Videos are pre-rendered and **cannot detect viewers' movements**; all movement prompts are timed and optional.

## Episode 001: Rescue the Five Cubs
An original African savanna and jungle world. Five lion cubs have been taken by hyenas. Traverse five connected biomes: golden savanna, waterfall forest, echo canyon, shadowlands, and stone fortress.

## Creative and safety constraints
- Original characters, world design, music and story; do not copy Disney's *The Lion King* characters, shots or soundtrack.
- Camera: human-height first-person jogging path; smooth forward motion without abrupt turns.
- Safety: jog in place in a clear, stable area, away from objects. Before squats, reaches or side steps, transition to a stationary safe segment; movements are optional.
- Strive for photorealistic quality with Unreal Engine 5. Do not pass off 2D placeholders as final scenes.
- Validate one continuous 10–15 second real 3D render before expanding.
- Do not commit Unreal DerivedDataCache, Intermediate, Saved, rendered videos, paid assets or secrets.

## Technical direction
- Unreal Engine 5, sequencer and Movie Render Queue for high-quality offline output.
- Python for data validation, procedural definitions and render orchestration.
- GitHub for code and design docs; a separately provisioned cloud Windows GPU workstation for Unreal and rendering.
- Codex handles repository code and scripts, but its hosted environment is not the GPU render machine.

## Milestones
1. Data schemas, camera and episode design.
2. Provision and verify a cloud Windows GPU environment.
3. Build the first savanna scene with licensed assets.
4. Render and review 10–15 seconds of continuous POV jogging.
5. Add original hyena/cub models and a guided, stationary rescue.
6. Extend to the five biomes and a 30-minute episode.

See [AGENTS.md](AGENTS.md) and [episode design](docs/episode-001.md).
