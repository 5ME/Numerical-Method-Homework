# -*- coding: utf-8 -*-
# 第一次作业 - 二分法求利率（非线性方程求解）
import math

def f(x):
    p=300
    n=240
    A=12*p*((1+x/12)**n-1)/x-500000
    return A

def regula(a, b, accuracy):
    delta = 0.5 * 10**(-accuracy)
    n = math.floor( (math.log(b-a) - math.log(delta))*1.0 / math.log(2) )
    if f(a) * f(b) > 0 :
        print("ya,yb are not suitable ")
        return
    for k in range(1000000):
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a)*f(c) < 0:
            b = c
            c = (a + b) / 2
        else:
            a = c
            c = (a + b) / 2
        err = abs(b - a) / 2
        if err < delta:
            break
    # print(k+1)
    return (n, round(c, accuracy+1))

def main():
    left, right, accuracy = input().split()
    left = float(left)
    right = float(right)
    accuracy = int(accuracy)
    result = regula(left, right, accuracy)
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    main()

