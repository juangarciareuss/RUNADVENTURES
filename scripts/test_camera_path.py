"""Built-in unittest tests; run: python -m unittest discover -s scripts -p 'test_*.py'"""
import json
from pathlib import Path
import unittest
from build_camera_path import sample_camera

ROOT = Path(__file__).resolve().parents[1]

class CameraPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.episode = json.loads((ROOT / "episodes/001-pilot.json").read_text(encoding="utf-8"))
        cls.frames = sample_camera(cls.episode)

    def test_length_and_time(self):
        self.assertEqual(len(self.frames), 1801)
        self.assertEqual(self.frames[0][0], 0)
        self.assertEqual(self.frames[-1][1], 30.0)

    def test_stationary_exercise(self):
        # Virtual motion is frozen during exercise and reward (15s to 27s).
        f = self.frames
        self.assertEqual(f[15 * 60][2:5], f[21 * 60][2:5])
        self.assertEqual(f[21 * 60][2:5], f[26 * 60][2:5])

    def test_consistent_height_and_no_roll(self):
        self.assertTrue(all(p[4] == 170.0 and p[7] == 0.0 for p in self.frames))

    def test_run_moves_forward(self):
        self.assertGreater(self.frames[14 * 60][2], self.frames[5 * 60][2])

if __name__ == "__main__":
    unittest.main()
