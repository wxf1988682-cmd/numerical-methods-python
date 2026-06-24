import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.bisection import bisection_method
from src.newton import newton_method
from src.secant import secant_method
from src.steffensen import steffensen_method


def print_header(method_name):
    print("\n" + "=" * 50)
    print(method_name)
    print("Solving equation: x^2 - x - 1 = 0")
    print("=" * 50)


def print_result(root):
    if root is None:
        print("Result: this method did not find an approximate root.")
    else:
        print(f"Result: approximate root = {root:.4f}")


def main():
    tolerance = 0.05

    print("Numerical methods examples")
    print("Target equation: x^2 - x - 1 = 0")
    print(f"Tolerance: {tolerance}")

    print_header("1. Bisection Method")
    print("Initial interval: [1, 2]")
    root = bisection_method(1, 2, tolerance=tolerance)
    print_result(root)

    print_header("2. Newton Method")
    print("Initial guess: x0 = 1.5")
    root = newton_method(1.5, tolerance=tolerance)
    print_result(root)

    print_header("3. Secant Method")
    print("Initial guesses: x0 = 1, x1 = 2")
    root = secant_method(1, 2, tolerance=tolerance)
    print_result(root)

    print_header("4. Steffensen Method")
    print("Initial guess: x0 = 1.5")
    root = steffensen_method(1.5, tolerance=tolerance)
    print_result(root)


if __name__ == "__main__":
    main()
