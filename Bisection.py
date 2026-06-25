import math
import sympy as sp
import utils.graphs as gr


def bisection(f, x_l, x_r, no_iter, tol=0.1):
    X = []
    Y = []

    X.append(x_l)
    X.append(x_r)

    f_l = f(x_l)
    f_r = f(x_r)

    Y.append(f_l)
    Y.append(f_r)

    if f_l * f_r > 0:
        print("Both have same sign, so solution DNE")
        return

    for i in range(no_iter):
        if abs(float(x_r - x_l)) < tol:
            print(
                f"Width between intervals are {x_r} - {x_l} = {abs(float(x_r - x_l))}"
            )
            return X, Y
        x_m = float(x_l + x_r) / 2.0
        f_m = f(x_m)
        if f_m * x_r > 0:
            x_r = x_m
        else:
            x_l = x_m

        X.append(x_m)
        Y.append(f_m)

        print(f"Iteration: {i + 1}\t\tMid: {x_m}\t\tf(mid): {f_m}")

    return X, Y


def user_input():
    x_sym = sp.symbols("x")
    while True:
        user_input = input("Enter function f(x): ")

        try:

            sym_exp = sp.sympify(user_input)
            f = sp.lambdify(x_sym, sym_exp, modules=["math", "sympy"])

            x_l = float(input("Enter lower bound: "))
            x_r = float(input("Enter upper bound: "))
            no_iter = int(input("Enter iterations (default: 1000): ").strip() or 1000)
            return sym_exp, f, x_l, x_r, no_iter

        except Exception as e:
            print(f"Invalid mathematical expression")


if __name__ == "__main__":
    sym_exp, f, x_l, x_r, no_iter = user_input()
    X, Y = bisection(f=f, x_l=x_l, x_r=x_r, no_iter=no_iter)
    gr.scatter(x=X, y=Y, title=sym_exp, x_label="x", y_label="f(x)")
