# -*- coding: utf-8 -*-
import functions

def main():
    p0, delta, epsilon = map(int, input().split())
    # y = functions.f(p0)
    # print(y)
    delta = 10**(-delta)
    epsilon = 10**(-epsilon)
    time = functions.newton(p0, delta, epsilon)
    print("%.5f" % time[0])
    print("%.5f" % time[1])

if __name__ == '__main__':
    main()