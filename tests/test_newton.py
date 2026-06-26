import unittest

from src.newton import newton_method


class TestNewtonMethod(unittest.TestCase):
    def test_root_is_close_to_golden_ratio(self):
        root = newton_method(1.5)

        self.assertIsNotNone(root)
        self.assertAlmostEqual(root, 1.618, delta=0.05)


if __name__ == "__main__":
    unittest.main()
