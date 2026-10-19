import unittest
from main import countInBand


class TestCountInBand(unittest.TestCase):
    def test_sample_one(self):
        scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]
        self.assertEqual(countInBand(scores, 42, 58), 6)

    def test_no_scores_in_band(self):
        scores = [35, 42, 42, 50, 58, 58, 58, 63, 71, 88]
        self.assertEqual(countInBand(scores, 90, 100), 0)

    def test_duplicate_edges(self):
        self.assertEqual(countInBand([10, 10, 10, 20, 20, 30, 30], 10, 20), 5)

    def test_single_value_range(self):
        self.assertEqual(countInBand([5, 5, 5, 6, 7], 5, 5), 3)

    def test_full_range(self):
        self.assertEqual(countInBand([0, 0, 25, 100, 100], 0, 100), 5)


if __name__ == "__main__":
    unittest.main()
