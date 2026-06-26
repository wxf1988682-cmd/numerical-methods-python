def f(x):
    """定义要求根的函数：f(x) = x^2 - x - 1。"""
    return x ** 2 - x - 1


def steffensen_method(x0, tolerance=0.05, max_iterations=100):
    """
    使用 Steffensen 迭代法求方程 f(x) = 0 的近似根。

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

        # 先计算 x + f(x)，它会用于构造 Steffensen 迭代公式。
        x_plus_fx = x + fx
        f_x_plus_fx = f(x_plus_fx)

        # Steffensen 公式的分母，分母为 0 时不能继续计算。
        denominator = f_x_plus_fx - fx
        if denominator == 0:
            print("错误：分母为 0，无法继续迭代。")
            return None

        # Steffensen 迭代公式：new_x = x - f(x)^2 / (f(x + f(x)) - f(x))。
        new_x = x - fx ** 2 / denominator

        print(f"iteration={iteration}, current={new_x:.4f}")

        # 当前后两次结果足够接近时，认为已经找到近似根。
        if abs(new_x - x) < tolerance:
            return new_x

        x = new_x

    print("达到最大迭代次数，未找到满足误差要求的近似根。")
    return None


if __name__ == "__main__":
    root = steffensen_method(1.5)

    if root is not None:
        print(f"\n方程 x^2 - x - 1 = 0 的近似根为：{root:.4f}")
