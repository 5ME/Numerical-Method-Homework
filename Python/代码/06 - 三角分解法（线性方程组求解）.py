import numpy as np
from scipy.linalg import lu

def main():
    # 输入矩阵阶数
    n = int(input())
    # 输入矩阵A
    matrixA = []
    for _ in range(n):
        matrixA.append(list(map(float, input().rstrip().split())))
    # 输入矩阵B
    matrixB = []
    for _ in range(n):
        matrixB.append(float(input()))

    # matrixA = np.mat(matrixA)
    matrixA = np.array(matrixA)
    # print(matrixA)
    # matrixB = np.mat(matrixB).T
    matrixB = np.transpose(np.array(matrixB))
    # print(matrixB)

    # LU分解
    P, L, U = lu(matrixA)
    # print(L)
    # print(U)
    temp = np.eye(n)
    LU_result = L - temp + U
    print(LU_result)

    # 解方程组
    solution = np.linalg.solve(matrixA, matrixB)
    solution = np.mat(solution)
    print(solution.T)

if __name__ == '__main__':
    main()