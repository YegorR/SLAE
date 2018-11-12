from random import randint


def get_matrix(n):
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i][j] = randint(0, 6) + 1.0
            else:
                a[i][j] = randint(3, 7) * 8.0
    return a


def get_x(n):
    return [randint(0, 4)-3.0 for _ in range(n)]


def get_b(n, a, x):
    b = list()
    for i in range(n):
        s = 0.0
        for j in range(n):
            s += a[i][j]*x[j]
        b.append(s)
    return b


if __name__ == "__main__":
    n = int(input("Введите n: "))
    a = get_matrix(n)
    x = get_x(n)
    b = get_b(n, a, x)
    print(a)
    print(x)
    print(b)
