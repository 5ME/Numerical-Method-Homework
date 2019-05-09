# -*- coding: utf-8 -*-
import numpy as np

# 最小二乘多项式拟合
# 构造M阶最小二乘多项式，拟合N个数据点
# X是1×n横坐标向量，Y是1×n纵坐标向量，M是最小二乘多项式的次数
def lspoly(X, Y, M):
    n = np.size(X)
    F = np.zeros((n, M+1))
    for k in range(M+1):
        F[:,k] = np.transpose(X)**k
    # 公式(25)求解系数矩阵 F'FC = F'Y
    A = np.transpose(F).dot(F)
    B = np.transpose(F).dot(np.transpose(Y))
    C = np.linalg.solve(A, B)
    C = np.flipud(C)
    # C是多项式的系数列表

    return C

def main():
    # X = np.array([-3, 0, 2, 4])
    # Y = np.array([3, 1, 1, 3])
    # M是最小二乘多项式的次数，这里拟合的是抛物线设为2
    M = 2
    # 输入数据点个数
    n = int(input())
    X = []
    Y = []
    # 输入数据点
    for _ in range(n):
        xtemp, ytemp = map(float, input().split())
        X.append(xtemp)
        Y.append(ytemp)
    X = np.array(X)
    Y = np.array(Y)

    C = lspoly(X, Y, M)
    print(C)

    # 拟合结果
    result = C[0] * X**2 + C[1] * X + C[2]
    # print(result)
    # 误差（norm2范数，即欧式距离）
    # error = np.linalg.norm(result - Y)
    error = np.sqrt(np.sum(np.square(result - Y)))
    error = round(error, 7)
    print(error)

if __name__ == "__main__":
    main()
