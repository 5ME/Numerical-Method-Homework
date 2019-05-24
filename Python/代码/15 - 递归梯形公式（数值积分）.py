# -*- coding: utf-8 -*-
# 递归梯形公式（数值积分）
import numpy as np

# 待积分的函数f(x)
def f(x):
    y = 1 / x
    return y

# f: 被积函数
# a,b: 积分的上限和下限
# n: 迭代次数
def rctrap(a, b, n):
    M = 1
    h = b - a
    T = np.zeros((n+1,1))
    T[0,0] = h * (f(a)+f(b)) / 2
    for j in range(n):
        M = 2 * M
        h = h / 2
        s = 0
        for k in range(int(M/2)):
            x = a + h*(2*(k+1)-1)
            s = s + f(x)
        T[j+1,0] = T[j,0]/2 + h*s
    # T是递归梯形公式序列
    return T

def main():
    a, b, n = map(int, input().split())
    result = rctrap(a, b, n)
    print(result)

if __name__ == '__main__':
    main()
