# -*- coding: utf-8 -*-
# 第二次作业 - 试值法求利率（非线性方程求解）
import math

# 年金计算函数
def f(x):
    p = 300
    n = 240
    A = 12*p*((1+x/12)**n-1)/x-500000
    return A

# a为左端点值，b为右端点值，accuracy为给定误差
def FalsePosition(a, b, accuracy):
    # 如果f(a)*f(b) > 0，此方法不适用
    if f(a)*f(b) > 0 :
        print("This method is not suitable ")
        return
    err = 100000
    n = 0
    # while循环
    while (err > accuracy):
        c = b - f(b)*(b-a) / ( f(b)-f(a) )
        if f(c) == 0:
            break
        elif f(a)*f(c) < 0:
            b = c
            c = b - f(b)*(b-a) / ( f(b)-f(a) )
        else:
            a = c
            c = b - f(b)*(b-a) / ( f(b)-f(a) )
        err = abs(f(c))
        n = n + 1
    return (n, round(c, 11))


# main函数
def main():
    left, right, accuracy = map(float, input().split())
    result = FalsePosition(left, right, accuracy)
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    main()
