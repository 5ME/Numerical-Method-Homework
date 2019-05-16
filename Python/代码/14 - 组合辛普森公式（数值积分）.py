# -*- coding: utf-8 -*-
# 组合辛普森公式（数值积分）
import numpy as np

# 待积分的函数f(x)
def f(x):
    y = 2 + np.sin(2*np.sqrt(x))
    return y

# f: 被积函数
# a,b: 积分的上限和下限
# M: 等距子区间的数量
def simprl(a, b, M):
    h = (b-a) / (2*M)
    s1 = 0
    s2 = 0
    
    for k in range(1,M+1):
        x = a + h*(2*k-1)
        s1 = s1 + f(x)
    
    for k in range(1,M):
        x = a + h*2*k
        s2 = s2 + f(x)
    
    s = h * (f(a) + f(b) + 4*s1 + 2*s2) / 3
    
    return s

def main():
    a, b, M = map(int, input().split())
    result = simprl(a, b, M)
    print("%.8f" % result)

if __name__ == '__main__':
    main()
