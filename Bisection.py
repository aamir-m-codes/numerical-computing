import math


def bisection(f, x_l, x_r, no_iter):
    f_l = f(x_l)
    f_r = f(x_r)
    if f_l * f_r > 0:
        print("Both have same sign, so solution DNE")
        return

    for i in range(no_iter):
        x_m = float(x_l + x_r) / 2.0
        f_m = f(x_m)
        if f_m * x_r > 0:
            x_r = x_m
        else:
            x_l = x_m

        print(f"Iteration: {i + 1}\t\tSolution: {x_m}")


def f(x):
    return x + math.sin(x)


x_l = -1
x_r = 10
no_iter = 5

bisection(f=f, x_l=x_l, x_r=x_r, no_iter=no_iter)
