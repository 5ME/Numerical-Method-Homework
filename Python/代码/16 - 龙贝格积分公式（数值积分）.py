# -*- coding: utf-8 -*-
# 龙贝格积分公式（数值积分）
import numpy as np

# 待积分的函数f(x)
def f(x):
    y = (x**2 + x + 1) * np.cos(x)
    return y

# f: 被积函数
# a,b: 积分的上限和下限
# n: 行数的最大值
def romber(a, b, n, tol):
    M = 1
    h = b - a
    # err = 1
    J = 0
    R = np.zeros((n,n))
    R[0,0] = h * (f(a)+f(b)) / 2
    # while ((err>tol) and (J<n-1)):
    while ((J<n-1)):
        J = J + 1
        h = h / 2
        s = 0
        for p in range(M):
            x = a + h*(2*(p+1)-1)
            s = s + f(x)
        
        R[J,0] = R[J-1,0] / 2 + h*s
        M = 2 * M

        for K in range(J):
            R[J,K+1] = R[J,K] + (R[J,K] - R[J-1,K]) / (4**(K+1) - 1)
        # err = abs(R[J-1,J-1] - R[J,K])
    # quad = R[J,J]

    return R

def main():
    n = int(input())
    a = 0
    b = np.pi / 2
    tol = 10**-8
    
    R = romber(a,b,n,tol)
    result = R[:,0:4]   #截取前4列
    print(result)

if __name__ == '__main__':
    main()
