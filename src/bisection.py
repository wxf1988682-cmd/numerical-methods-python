def f(x):
    """
    定义要求根的函数。
    这里要求解的是方程 x^2 - x - 1 = 0。
    """
    return x ** 2 - x - 1


def bisection_method(a, b, tolerance=0.05, max_iterations=100):
    """
    使用二分法求方程 f(x) = 0 的近似根。

    参数：
    a, b：初始区间的左右端点
    tolerance：允许误差，默认是 0.05
    max_iterations：最大迭代次数，默认是 100

    返回：
    成功时返回近似根，失败时返回 None。
    """
    if f(a) * f(b) > 0:
        print("错误：区间两端函数值同号，不能使用二分法。")
        return None

    for iteration in range(1, max_iterations + 1):
        mid = (a + b) / 2

        print(f"iteration={iteration}, current={mid:.4f}")

        if f(mid) == 0 or (b - a) / 2 <= tolerance:
            return mid

        # 根据函数值的符号，保留仍然包含根的半个区间。
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    print("达到最大迭代次数，未找到满足误差要求的近似根。")
    return None


if __name__ == "__main__":
    root = bisection_method(1, 2)

    if root is not None:
        print(f"\n方程 x^2 - x - 1 = 0 的近似根为：{root:.4f}")
