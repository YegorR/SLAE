import SLAU.gauss
from SLAU.generate import get_matrix
from math import inf


def inverse_matrix(a, n):
    rev = [[0.0] * n for _ in range(n)]
    for i in range(n):
        b = [0.0 for _ in range(n)]
        b[i] = 1.0
        x = SLAU.gauss.gauss(a, b, n)
        for j in range(n):
            rev[j][i] = x[j]
    return rev


def multi_matrix(a, b, n):
    c = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j];
    return c


def check(a, x, n):
    if inf in x:
        return [inf] * n
    b = [0.0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i] += a[i][j] * x[j]
    return b


if __name__ == "__main__":
    n = int(input("Введите n: "))
    a = get_matrix(n)
    for i in range(n):
        print(a[i])
    print("Обратная матрица")
    rev = inverse_matrix(a, n)
    for i in range(n):
        print(rev[i])
    print("Проверка, A*A^-1: ")
    E = multi_matrix(a, rev, n)
    for i in range(n):
        print(E[i])
