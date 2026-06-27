# numerical-methods-python

![Python Tests](https://github.com/wxf1988682-cmd/numerical-methods-python/actions/workflows/python-tests.yml/badge.svg)

## 项目简介

本项目是一个用于学习数值分析方法与 Python 编程的练习项目，主要实现常见的非线性方程求根算法。

项目以方程：

```text
x^2 - x - 1 = 0
```

为主要示例，分别使用不同数值方法求解该方程的近似根。

通过本项目，可以练习 Python 函数定义、循环结构、条件判断、模块导入、单元测试，以及 GitHub 项目管理的基本流程。

## 已实现算法

目前已经实现以下数值方法：

* 二分法 Bisection Method
* 牛顿迭代法 Newton Method
* 割线法 Secant Method
* Steffensen 迭代法

## 算法简介

### 1. 二分法 Bisection Method

二分法是一种常见的非线性方程求根方法。

如果函数 f(x) 在区间 [a, b] 上连续，并且 f(a) 与 f(b) 异号，那么该区间内至少存在一个实根。二分法通过不断取区间中点，将有根区间逐步缩小，直到满足误差要求。

### 2. 牛顿迭代法 Newton Method

牛顿迭代法是一种利用函数值和导数信息求解非线性方程近似根的方法。

该方法从一个初始值出发，根据函数在当前点的切线与 x 轴的交点不断更新近似根。牛顿法通常收敛较快，但需要计算导数，并且对初始值有一定要求。

### 3. 割线法 Secant Method

割线法是一种不需要显式求导的非线性方程求根方法。

它利用两个初始点构造割线，并用割线与 x 轴的交点作为新的近似根。割线法可以看作是牛顿法的一种变形，适合在导数不方便计算时使用。

### 4. Steffensen 迭代法

Steffensen 迭代法是一种加速迭代方法，常用于提高简单迭代的收敛速度。

它通过构造加速公式，使迭代过程在一定条件下更快接近方程的根。本项目中使用 Steffensen 方法求解同一个非线性方程，并与其他方法进行对比。

## 项目结构

```text
numerical-methods-python/
├── README.md
├── .gitignore
├── examples/
│   └── run_examples.py
├── src/
│   ├── bisection.py
│   ├── newton.py
│   ├── secant.py
│   └── steffensen.py
└── tests/
    ├── test_bisection.py
    ├── test_newton.py
    ├── test_secant.py
    └── test_steffensen.py
```

## 运行环境

本项目使用 Python 编写，不依赖第三方库。

建议使用：

```text
Python 3.8 或以上版本
```

## 运行方式

在项目根目录下，可以运行统一示例文件：

```bash
python examples/run_examples.py
```

也可以单独运行某一个算法文件，例如：

```bash
python src/bisection.py
python src/newton.py
python src/secant.py
python src/steffensen.py
```

## 运行测试

本项目使用 Python 标准库 `unittest` 编写基础测试。

在项目根目录下运行：

```bash
python -m unittest discover tests
```

如果测试通过，会看到类似输出：

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
## 自动测试


本项目已配置 GitHub Actions 自动测试流程。

每次向 `main` 分支提交代码时，GitHub Actions 会自动运行以下命令：

```bash
python -m unittest discover tests
```

如果测试全部通过，GitHub Actions 页面会显示绿色对勾。

当前测试内容包括：

- 二分法测试
- 牛顿迭代法测试
- 割线法测试
- Steffensen 迭代法测试


## 示例结果

不同方法求解方程：

```text
x^2 - x - 1 = 0
```

得到的近似根都应接近：

```text
1.618
```

由于不同算法的迭代方式和误差控制不同，最终输出结果可能略有差异。例如：

```text
二分法：1.6250
牛顿迭代法：1.6181
割线法：1.6190
Steffensen 迭代法：1.6189
```

这些结果都在允许误差范围内。

## 学习收获

通过本项目，我主要练习了：

1. Python 函数定义与模块化编程；
2. while 循环、条件判断和数值迭代过程；
3. 二分法、牛顿法、割线法、Steffensen 法等数值方法；
4. 使用 `examples/` 编写统一运行示例；
5. 使用 `unittest` 编写基础单元测试；
6. 使用 `.gitignore` 忽略 Python 缓存文件；
7. 使用 Git 进行版本管理；
8. 使用 GitHub 保存和展示项目；
9. 使用 Codex 辅助生成、修改和检查代码。

## 后续计划

后续可以继续扩展以下内容：

* 增加简单迭代法 Fixed-point Iteration
* 增加更多非线性方程示例
* 增加算法收敛次数对比
* 增加误差变化过程记录
* 使用 GitHub Actions 实现自动测试
* 整理为更规范的 Python 包结构

```
```
