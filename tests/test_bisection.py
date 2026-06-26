import unittest

from src.bisection import bisection_method


class TestBisectionMethod(unittest.TestCase):
    def test_root_is_close_to_golden_ratio(self):
        root = bisection_method(1, 2)

        self.assertIsNotNone(root)
        self.assertAlmostEqual(root, 1.618, delta=0.05)


if __name__ == "__main__":
    unittest.main()
