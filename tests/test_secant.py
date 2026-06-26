import unittest

from src.secant import secant_method


class TestSecantMethod(unittest.TestCase):
    def test_root_is_close_to_golden_ratio(self):
        root = secant_method(1, 2)

        self.assertIsNotNone(root)
        self.assertAlmostEqual(root, 1.618, delta=0.05)


if __name__ == "__main__":
    unittest.main()
