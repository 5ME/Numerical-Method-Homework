# -*- coding: utf-8 -*-
import numpy as np

def Lagran(X, Y):
    w = np.size(X)
    n = w - 1
    L = np.zeros((w, w))
    for k in range(n+1):
        V = 1
        for j in range(n+1):
            if k != j:
                V = np.convolve(V, np.poly(X[j])) / (X[k] - X[j])
        L[k, :] = V
    C = Y.dot(L)
    # C为插值多项式系数矩阵；L为拉格朗日系数多项式矩阵
    return C, L

def main():
    # 输入X*
    x0 = float(input())
    # X = np.array([0.0, 1.2])
    # X = np.array([0.0, 0.6, 1.2])
    # X = np.array([0.0, 0.4, 0.8, 1.2])
    X = []
    # 输入X向量，表示区间
    X.append(list(map(float, input().rstrip().split())))
    X = np.array(X)
    X = X[0]
    # Y为X的cos函数
    Y = np.cos(X)
    # print(X)
    # print(Y)
    
    # 调用Lagran函数
    C, L = Lagran(X, Y)
    # 插值多项式系数矩阵
    print(C)
    # 拉格朗日系数多项式矩阵
    print(L)

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
