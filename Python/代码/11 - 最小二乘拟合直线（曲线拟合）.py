# -*- coding: utf-8 -*-
import numpy as np

# 最小二乘法拟合曲线
def lsline(X, Y):
    xmean = np.mean(X)
    ymean = np.mean(Y)
    sumx2 = (X - xmean).dot(np.transpose(X - xmean))
    sumxy = (Y - ymean).dot(np.transpose(X - xmean))
    A = sumxy / sumx2
    B = ymean - A * xmean
    # A为拟合直线x系数，B为常数项
    return A, B

def main():
    # X = np.array([-1, 0, 1, 2, 3, 4, 5, 6])
    # Y = np.array([10, 9, 7, 5, 4, 3, 0, -1])

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

    A, B = lsline(X, Y)
    A = round(A, 7)
    B = round(B, 7)
    # A为拟合直线x系数，B为常数项
    print("y=" + str("%.7f" % A) + "x+" + str("%.7f" % B))

    # 拟合结果
    result = A * X + B
    # 误差（norm2范数，即欧式距离）
    # error = np.linalg.norm(result - Y)
    error = np.sqrt(np.sum(np.square(result - Y)))
    error = round(error, 7)
    print(error)

if __name__ == "__main__":
    main()
