# numerical-methods-python

## 项目简介

本项目是一个用于学习数值分析方法的 Python 项目，主要用于实现和理解常见的数值计算算法。

目前已经实现：

- 二分法求解非线性方程

## 已实现算法

### 1. 二分法 Bisection Method

二分法是一种常见的非线性方程求根方法。

如果函数 f(x) 在区间 [a, b] 上连续，并且 f(a) 与 f(b) 异号，那么该区间内至少存在一个实根。二分法通过不断取区间中点，将有根区间逐步缩小，直到满足误差要求。

本项目中求解的方程为：

```text
x^2 - x - 1 = 0
```

目前已经实现：

- 二分法求解非线性方程
- 牛顿迭代法求解非线性方程

## 项目结构

```text
numerical-methods-python/
├── README.md
├── .gitignore
├── src/
│   └── bisection.py
└── examples/
    └── run_examples.py
```

## 运行方式

在项目根目录下运行：

```bash
python src/bisection.py
```

或者运行示例文件：

```bash
python examples/run_examples.py
```

## 示例输出

```text
第 1 次迭代：a=1.0000, b=2.0000, mid=1.5000, f(mid)=-0.2500
第 2 次迭代：a=1.5000, b=2.0000, mid=1.7500, f(mid)=0.3125
第 3 次迭代：a=1.5000, b=1.7500, mid=1.6250, f(mid)=0.0156

方程 x^2 - x - 1 = 0 的近似根为：1.6250
```

## 后续计划

后续计划继续实现以下数值计算方法：

- 牛顿迭代法
- Steffensen 迭代法
- 割线法
- 简单迭代法
- 线性方程组迭代法

## 学习收获

通过本项目，我练习了：

1. Python 函数定义；
2. while 循环和条件判断；
3. 二分法的基本思想；
4. GitHub 仓库创建与代码提交；
5. README 项目文档编写；
6. 本地开发与远程仓库同步流程。