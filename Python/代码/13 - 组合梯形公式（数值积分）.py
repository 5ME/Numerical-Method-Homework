# -*- coding: utf-8 -*-
# 组合梯形公式（数值积分）
import numpy as np

# 待积分的函数f(x)
def f(x):
    y = 2 + np.sin(2*np.sqrt(x))
    return y

# f: 被积函数
# a,b: 积分的上限和下限
# M: 等距子区间的数量
def traprl(a, b, M):
    h = (b-a) / M
    s = 0
    for k in range(1,M):
        x = a + h*k
        s = s + f(x)
    s = h * (f(a) + f(b)) / 2 + h*s
    
    return s

def main():
    a, b, M = map(int, input().split())
    result = traprl(a, b, M)
    print("%.8f" % result)

if __name__ == '__main__':
    main()
