import numpy as np

def jacobi(A, B, P, delta, max1):
    N = max(B.shape)
    X = np.zeros((N, 1))
    times = 0       # 迭代次数
    # print(X)
    while True:
        for i in range(N):
            temp = 0
            for j in range(N):
                if i != j:
                    temp += P[j] * A[i][j]
            X[i] = (B[i] - temp) / A[i][i]
        err = abs(np.linalg.norm(X-P))
        relerr = err / np.linalg.norm(X)
        times += 1
        if err < delta or relerr < delta:
            break
        else:
            P = X.copy()
            
    return times-1, X

def main():
    # 输入矩阵阶数
    n = int(input())
    # 输入系数矩阵A
    matrixA = []
    for _ in range(n):
        matrixA.append(list(map(float, input().rstrip().split())))
    # 输入常数矩阵B
    matrixB = []
    for _ in range(n):
        matrixB.append(float(input()))
    # 输入初始点矩阵P
    matrixP = []
    for _ in range(n):
        matrixP.append(float(input()))

    # matrixA = np.mat(matrixA)
    matrixA = np.array(matrixA)
    # print(matrixA)
    # matrixB = np.mat(matrixB).T
    matrixB = np.transpose(np.array(matrixB))
    # print(matrixB)

    matrixP = np.transpose(np.array(matrixP))
    # print(matrixP)

    # 设置精度
    delta = 10**-9
    # 设置最大迭代次数
    max1 = 20

    times, X = jacobi(matrixA, matrixB, matrixP, delta, max1)
    print(times)
    print(X)
    

if __name__ == '__main__':
    main()