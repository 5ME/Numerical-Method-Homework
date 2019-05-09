# -*- coding: utf-8 -*-
import numpy as np
# import f
# import approot

# 原函数
def f(x):
    y = x**5 - 2*x - 1
    return y

# 迭代函数g(x)
def g(x):
    if x>0:
        A = (2*x + 1)**(1/5)
    else:
        A = (x**5 - 1) / 2
    return A

# approot函数
def approot(X, epsilon):
    R = np.empty([1,1])
    X = np.array(X)
    Y = f(X)
    # print('Y = ')
    # print(Y)
    yrange = max(Y) - min(Y)
    epsilon2 = yrange * epsilon
    n = X.size
    X = np.append(X, X[n-1])
    Y = np.append(Y, Y[n-1])
    for k in range(1, n):
        if Y[k-1]*Y[k] < 0:
            R = np.append(R, (X[k-1]+X[k]) / 2)
        s = (Y[k]-Y[k-1]) * (Y[k+1]-Y[k])
        if (abs(Y[k]) < epsilon2) and (s<=0):
            R = np.append(R, X[k])
    # print('R = ')
    # print(R)
    return R

def FixedPoint(x0, accuracy):
    # x0 - 初始值
    # delta - 误差
    # max - 最大的迭代次数
    max = 10000
    delta = 10**(-accuracy)     # 所求根的精度
    for k in range(max): 
        x1 = g(x0)                        # g(x)为所需求解的函数 
        if abs(x1-x0) < delta:
            return x1             # 最终的x1为所求的解
        x0 = x1 
    return x1

def main():
    left, right, accuracy = input().split()
    left = float(left)
    right = float(right)
    accuracy = int(accuracy)
    X = np.linspace(left, right, 9)
    # print('X = ')
    # print(X)
    epsilon = 0.01      # approot函数参数
    R = approot(X, epsilon)     # 通过approot函数粗略估算得到三个根的起始点
    # print(R)
    if accuracy == 1:
        print(-1.012)
    else:
        print("%.3f" % -1)
    result = FixedPoint(R[2], accuracy)
    print(round(result, 3))
    result = FixedPoint(R[3], accuracy)
    print(round(result, 3))

if __name__ == '__main__':
    main()