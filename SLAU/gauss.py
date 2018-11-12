from SLAU.generate import get_matrix, get_b, get_x
import SLAU.matrix
import copy


def gauss_direct(a, b, n):
    for i in range(n):
        for j in range(i+1, n):
            m = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= a[i][k] * m
            b[j] -= b[i] * m


def gauss_reverse(a, b, n):
    x = [None for _ in range(n)]
    for i in range(n-1, -1, -1):
        s = 0.0
        for j in range(i+1, n):
            s += a[i][j]*x[j]
        x[i] = (b[i] - s) / a[i][i]
    return x


def gauss(a, b, n):
    bn = copy.copy(b)
    an = copy.deepcopy(a)
    gauss_direct(an, bn, n)
    return gauss_reverse(an, bn, n)


if __name__ == "__main__":
    n = int(input("Введите n: "))
    a = get_matrix(n)
    x = get_x(n)
    b = get_b(n, a, x)
    for i in range(n):
        print(str(a[i]) + " | "+str(b[i]))
    print("X = "+str(gauss(a, b, n)))
    print("Проверка: B = "+str(SLAU.matrix.check(a, gauss(a, b, n), n)))
