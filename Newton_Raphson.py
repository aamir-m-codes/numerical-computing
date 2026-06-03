def newton_raphson(f, d_f, start, n):
    x = start
    for i in range(n):
        x = x - (f(x) / d_f(x))

    return x


def f(x):
    return x**2 - 4


def d_f(x):
    return 2 * x


start = 3
n = 4
print(newton_raphson(f, d_f, start, n))
