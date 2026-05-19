def trapezoidal(f, a, b, points):
    n = points - 1
    h = float((b - a) / n)
    x = a
    total = f(x)

    for i in range(1, n):
        x += h
        total += 2 * f(x)

    total += f(b)
    return (h / 2) * total


def f(x):
    return x / (1 + x**2)


a = 0
b = 2
points = 5
result = trapezoidal(f=f, a=a, b=b, points=points)
print(f"Answer: {result:.3f}")
