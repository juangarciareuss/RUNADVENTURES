# Free-first production — phone-only

The repository retains Unreal Engine 5 as the final target. This branch adds a **genuine 3D Blender blocking scene** which renders a static image; it is NOT AAA quality and does NOT produce the complete rescue video.

## Free tools
- GitHub Actions: run Python validation within available free quota.
- Blender: open-source scene creation, scriptable in background mode.
- Google Colab: optional free compute, with non-guaranteed access to GPUs, run-time limits and potential disconnects.

## From Android using Colab
1. Open https://colab.research.google.com/ and create a notebook (normal browser UI). In a code cell, run:
```python
!apt-get -qq update
!apt-get -qq install blender
!git clone https://github.com/juangarciareuss/RUNADVENTURES.git
!cd RUNADVENTURES && blender -b -t 2 --python blender/build_savanna.py
```
2. Preview or retrieve `RUNADVENTURES/output/savanna_preview.png`. It is an intentionally basic 3D **blocking test** to validate the free pipeline—not the final video.
3. Evaluate runtime and available CPU/RAM/GPU before attempting any complex scene.
4. Upgrade visual assets with original, freely licensed landscapes, vegetation and animals. Verify every license, terms and file size.
5. Make a 10–15-second preview with animated camera and real 3D character assets only after this blocking render succeeds.

## Important limitations
- Colab is a temporary notebook, not a reliable always-on Unreal Engine workstation or free 4K60 video farm.
- Installing Blender and downloading dependencies can take time; free resource limits and versions vary.
- This repo does not provision cloud GPUs and does not contain licensed animal models or finished cinema-quality shots.
- Never store access tokens in notebooks or GitHub commits.
- Free-first target = **prove a 3D render can be generated with zero infrastructure spend**. The cinematic art-quality target remains unchanged.
