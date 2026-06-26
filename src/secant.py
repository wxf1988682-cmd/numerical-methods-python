def f(x):
    """定义要求根的函数：f(x) = x^2 - x - 1。"""
    return x ** 2 - x - 1


def secant_method(x0, x1, tolerance=0.05, max_iterations=100):
    """
    使用割线法求方程 f(x) = 0 的近似根。

    参数：
    x0：第一个初始值
    x1：第二个初始值
    tolerance：允许误差，默认是 0.05
    max_iterations：最大迭代次数，默认是 100

    返回：
    成功时返回近似根，失败时返回 None。
    """
    for iteration in range(1, max_iterations + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        # 如果两个函数值相同，分母会变成 0，无法继续计算。
        if fx1 - fx0 == 0:
            print("错误：分母为 0，无法继续迭代。")
            return None

        # 割线法公式：用两点连成的割线与 x 轴的交点作为新的近似值。
        new_x = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        print(f"iteration={iteration}, current={new_x:.4f}")

        # 当前后两次结果足够接近时，认为已经找到近似根。
        if abs(new_x - x1) < tolerance:
            return new_x

        # 更新两个点：旧的 x1 变成新的 x0，new_x 变成新的 x1。
        x0 = x1
        x1 = new_x

    print("达到最大迭代次数，未找到满足误差要求的近似根。")
    return None


if __name__ == "__main__":
    root = secant_method(1, 2)

    if root is not None:
        print(f"\n方程 x^2 - x - 1 = 0 的近似根为：{root:.4f}")
