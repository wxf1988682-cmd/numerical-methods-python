import unittest

from src.steffensen import steffensen_method


class TestSteffensenMethod(unittest.TestCase):
    def test_root_is_close_to_golden_ratio(self):
        root = steffensen_method(1.5)

        self.assertIsNotNone(root)
        self.assertAlmostEqual(root, 1.618, delta=0.05)


if __name__ == "__main__":
    unittest.main()
