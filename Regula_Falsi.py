"""
Regula Falsi (False Position) method is the bracketing (bisection) method
but with some geometry intelligence
"""

import utils.input as inp


def regula_falsi(f, a, b, max_iter, tol=0.1):
    f_a = f(a)
    f_b = f(b)

    if f_a * f_b > 0:
        raise ValueError(f"Same sign broken: f({a})={f_a}, f({b})={f_b}")

    prev_c = a

    for i in range(1, max_iter + 1):
        c = ((a * f_b) - (b * f_a)) / (f_b - f_a)
        f_c = f(c)

        print(f"Iteration: {i}\t\tf({a}) = {f_a}\t\tf({b}) = {f_b}\t\tf({c}) = {f_c}")

        if abs(f_c) < tol or abs(c - prev_c) < tol or f_c == 0.0:
            print(f"Convergence achieved at iteration {i} and Root = {c}")
            return

        if f_a * f_c > 0:
            a = c
            f_a = f_c
        else:
            b = c
            f_b = f_c

        prev_c = c


if __name__ == "__main__":
    schema = [
        {
            "name": "func",
            "prompt": "Enter function f(x): ",
            "type": "func",
        },
        {
            "name": "low",
            "prompt": "Enter lower bound: ",
            "type": "float",
        },
        {
            "name": "upper",
            "prompt": "Enter upper bound: ",
            "type": "float",
        },
        {
            "name": "iters",
            "prompt": "Enter iterations (default: 100): ",
            "type": "int",
            "default": 100,
        },
    ]

    inputs = inp.user_input(schema=schema)
    regula_falsi(
        f=inputs["func"][1],
        a=inputs["low"],
        b=inputs["upper"],
        max_iter=inputs["iters"],
    )
