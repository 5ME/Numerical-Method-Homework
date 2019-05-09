# -*- coding: utf-8 -*-
import numpy as np

# 牛顿插值多项式
def Newton(X, Y):
    n = np.size(X)
    D = np.zeros((n, n))
    D[:, 0] = np.transpose(Y)
    for j in range(1, n):
        for k in range(j, n):
            D[k, j] = (D[k, j-1] - D[k-1, j-1]) / (X[k] - X[k-j])
    C = D[n-1, n-1]
    for k in range(n-2, -1, -1):
        C = np.convolve(C, np.poly(X[k]))
        m = np.size(C)
        C[m-1] = C[m-1] + D[k, k]
    
    # C是包含牛顿插值多项式系数的向量，D是差商表
    return C, D

def main():
    # 输入X*
    x0 = float(input())
    # X = np.array([0.0, 1, 2, 3, 4])
    X = []
    # 输入X向量
    X.append(list(map(float, input().rstrip().split())))
    X = np.array(X)
    X = X[0]
    # Y为X的cos函数
    Y = np.cos(X)
    
    # 调用Newton函数
    C, D = Newton(X, Y)
    # 打印插值多项式
    polynomial = np.poly1d(C)
    print(polynomial)
    # 打印差商表
    print(D)

    # 计算P1(x*)
    n = np.size(C)
    result = 0
    for i in range(n):
        result = result + C[i] * x0**(n-i-1)
    # 保留6位小数
    result = round(result, 6)
    print("P" + str(i) + "(" + str(x0) + ")=" + str(result))

if __name__ == "__main__":
    main()
