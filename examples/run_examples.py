from src.bisection import bisection_method

root = bisection_method(1, 2, tolerance=0.05)

if root is not None:
    print(f"近似根为：{root:.4f}")
