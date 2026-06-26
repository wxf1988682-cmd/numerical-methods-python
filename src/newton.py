def f(x):
    """定义要求根的函数：f(x) = x^2 - x - 1。"""
    return x ** 2 - x - 1


def derivative_f(x):
    """定义函数 f(x) 的导数：f'(x) = 2x - 1。"""
    return 2 * x - 1


def newton_method(x0, tolerance=0.05, max_iterations=100):
    """
    使用牛顿迭代法求方程 f(x) = 0 的近似根。

    参数：
    x0：迭代的初始值
    tolerance：允许误差，默认是 0.05
    max_iterations：最大迭代次数，默认是 100

    返回：
    成功时返回近似根，失败时返回 None。
    """
    x = x0

    for iteration in range(1, max_iterations + 1):
        fx = f(x)
        derivative = derivative_f(x)

        # 导数为 0 时不能做除法，因此无法继续迭代。
        if derivative == 0:
            print("错误：导数为 0，无法继续迭代。")
            return None

        # 牛顿迭代公式：新值 = 当前值 - 函数值 / 导数值。
        new_x = x - fx / derivative

        print(f"iteration={iteration}, current={new_x:.4f}")

        # 当前后两次结果足够接近时，认为已经找到近似根。
        if abs(new_x - x) < tolerance:
            return new_x

        x = new_x

    print("达到最大迭代次数，未找到满足误差要求的近似根。")
    return None


if __name__ == "__main__":
    root = newton_method(1.5)

    if root is not None:
        print(f"\n方程 x^2 - x - 1 = 0 的近似根为：{root:.4f}")
