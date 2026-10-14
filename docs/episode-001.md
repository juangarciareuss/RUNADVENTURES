# Episode 001 — Rescue the Five Cubs

**Status:** design only; not implemented or rendered.

## Format
- 30-minute target, first-person continuous cinematic jogging adventure
- 4K / 60fps target, subject to performance and rendering budget
- Viewer jogs in place; no treadmill
- Original African-inspired environments and animal characters
- No actual movement detection on YouTube

## Story
Five lion cubs have been separated and guarded by a pack of hyenas. The runner explores five connected environments to find them and reunite the family. Each rescue is a scripted cinematic milestone with an optional safe stationary exercise.

| Order | Time window | Biome | Rescue moment |
|---|---|---|---|
| 1 | 00:00–06:00 | Golden savanna | Stop, shallow squat, reach gently forward |
| 2 | 06:00–12:00 | Waterfall forest | Stop, controlled step, squat, reach |
| 3 | 12:00–18:00 | Echo canyon | Stop, hold shallow squat briefly, reach |
| 4 | 18:00–24:00 | Shadowlands | Stop, look around while standing, squat, reach |
| 5 | 24:00–30:00 | Stone fortress | Stop, squat, reach, then resume jogging once standing |

Each event must have a clear visual/audio cue, a brief run-down, a stable stationary scene, an optional low-impact alternative, and an on-screen progress change from 0/5 to 5/5. Animal interactions are cinematic events rather than tracked physical actions.

## First real prototype
10–15 seconds of forward camera motion along an original savanna path, rendered in Unreal Engine on a cloud GPU. No fake placeholder footage. Review camera comfort, image realism, consistency, motion and budget before introducing animals.

## Content and licensing
Build original names, characters, story beats, set dressing, sound and music. Record provenance and licensing for each imported 3D asset.

## Next design questions
- Camera head-bob intensity and virtual jog speed
- Stationary exercise pause duration
- Animal animation licensing and quality
- GPU rendering cost per minute

## Gameplay-like video direction — no viewer input required
The final work is a **scripted YouTube video**, not a playable game. It should nevertheless create a strong **illusion of game progression** through consistent HUD, visible missions, a 0/5 cub tracker, objective markers, sound cues, collectible discoveries and elaborate rescue animations.

### Core viewing loop
1. **Hook (first 5 seconds):** spectacular savanna vista, visible hyena threat and the headline objective 'Rescue 5 cubs'.
2. **Jogging exploration:** continuous first-person path with clearly telegraphed environmental reveals and new sights.
3. **Encounter:** hints of a cub, hyenas, a small environmental hazard or clue; audio changes to raise anticipation.
4. **Exercise checkpoint:** the on-screen hero slows and comes to a full stop; an optional controlled squat/reach or stationary action is shown with a clear countdown.
5. **Scripted rescue and reward:** a cub reacts and runs to safety, progress increases from N/5 to N+1/5, a short triumphant stinger plays, and a unique reward is revealed.
6. **Return to jogging:** the camera resumes smoothly toward a recognizable next landmark.

### Visual treatment
- Cinematic African-inspired landscapes with consistent realism and distinct memorable landmarks.
- Disciplined, game-quality HUD: compact objective, 5-cub indicator, optional distance/time marker, location title on transitions; no intrusive or constantly flashing icons.
- Carefully staged wildlife with original realistic lion cubs and hyenas. Animals must never look like 2D stickers.
- Pacing built for at-home jogging in place: transitions from run to exercise stop must be gradual; no sudden turns, camera shakes, or simulated falls.
- A linear video has no branching or input validation; every rescue happens on the timeline whether the viewer follows the movement or not. Do not misrepresent this.

### Creative quality gate
Before scaling to long-form, produce a complete 20–30 second **gameplay-like slice** with visible objective, cinematic run, a unique encounter, stationary guided movement and satisfying visual reward. Test readability and visual excitement on a phone and large screen; revise until the slice feels substantially more compelling than generic scenic running footage.
