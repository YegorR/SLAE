from SLAU.generate import get_b, get_x, get_matrix
from math import fabs
from math import inf
from SLAU import matrix


def condition(x, x_0, n, eps):
    for i in range(n):
        if fabs(x[i]-x_0[i]) >= eps:
            return False
    return True


def iteration(a, b, n, eps):
    x_0 = [b[i]/a[i][i] for i in range(n)]
    x = [0.0 for _ in range(n)]
    count = 0
    while True:
        count += 1
        for i in range(n):
            x[i] = b[i]/a[i][i]
            for j in range(n):
                if i != j:
                    x[i] -= a[i][j] / a[i][i] * x_0[j]
        if condition(x, x_0, n, eps):
            break
        x_0 = x.copy()
        if x_0[0] == inf:
            return [inf] * n, inf
    return x, count


def zeigel(a, b, n, eps):
    x_0 = [b[i] / a[i][i] for i in range(n)]
    x = [0.0 for _ in range(n)]
    count = 0
    while True:
        count += 1
        for i in range(n):
            x[i] = b[i] / a[i][i]
            for j in range(n):
                if j < i:
                    x[i] -= a[i][j] / a[i][i] * x[j]
                elif j > i:
                    x[i] -= a[i][j] / a[i][i] * x_0[j]
        if condition(x, x_0, n, eps):
            break
        x_0 = x.copy()
        if x_0[0] == inf:
            return "inf", "inf"
    return x, count


if __name__ == "__main__":
    n = int(input("Введите n: "))
    eps = float(input("Введите eps: "))
    a = get_matrix(n)
    x = get_x(n)
    b = get_b(n, a, x)
    for i in range(n):
        print(str(a[i]) + " | " + str(b[i]))
    x, count = iteration(a, b, n, eps)
    print("X(iter) = " + str(x))
    print("Проверка: B = " + str(matrix.check(a, x, n)))
    print("Количество итераций: "+str(count))
    x, count = zeigel(a, b, n, eps)
    print("X(iter) = " + str(x))
    print("Проверка: B = " + str(matrix.check(a, x, n)))
    print("Количество итераций: " + str(count))
