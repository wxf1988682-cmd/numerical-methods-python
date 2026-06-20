def f(x):
    """
    定义要求解的函数：
    f(x) = x^2 - x - 1
    """
    return x ** 2 - x - 1


def bisection_method(a, b, tolerance=0.05, max_iterations=100):
    """
    使用二分法求方程 f(x) = 0 的近似根

    参数：
    a, b：初始区间端点
    tolerance：误差要求
    max_iterations：最大迭代次数
    """

    if f(a) * f(b) > 0:
        print("错误：区间两端函数值同号，不能使用二分法。")
        return None

    iteration = 0

    while (b - a) / 2 > tolerance and iteration < max_iterations:
        mid = (a + b) / 2

        print(f"第 {iteration + 1} 次迭代：a={a:.4f}, b={b:.4f}, mid={mid:.4f}, f(mid)={f(mid):.4f}")

        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

        iteration += 1

    return (a + b) / 2


if __name__ == "__main__":
    root = bisection_method(1, 2, tolerance=0.05)

    if root is not None:
        print(f"\n方程 x^2 - x - 1 = 0 的近似根为：{root:.4f}")
