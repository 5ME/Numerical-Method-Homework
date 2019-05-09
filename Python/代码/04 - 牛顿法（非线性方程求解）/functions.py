# -*- coding: utf-8 -*-
import math

# 函数f
def f(t):
    e = math.exp(1)
    y = 9600 * (1-e**(-t/15.0)) - 480*t
    return y

# 函数f的导数df
def df(t):
    e = math.exp(1)
    dy = 640 * (e**(-t/15.0)) - 480
    return dy

# 函数r
def r(t):
    e = math.exp(1)
    x = 2400 * (1-e**(-t/15.0))
    return x

# 函数r的导数dr
def dr(t):
    e = math.exp(1)
    dr = 160 * (e**(-t/15.0))
    return dr

# 牛顿迭代法
def newton(p0, delta, eps):
    err = 1.0
    relerr = 1.0
    max = 100000    # 最大迭代次数
    k = 0   # 迭代次数计数
    while (err>delta) and (relerr>delta) and (k<max):
        p1 = p0 - f(p0) / df(p0)
        err = abs(p1-p0)
        relerr = 2 * err / (abs(p1)+delta)
        p0 = p1
        # print(err, relerr)
        # print(p0, r(p0))
        # print()
        k = k+1
    return (p0, r(p0))

