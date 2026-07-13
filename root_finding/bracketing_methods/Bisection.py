import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import utils.graphs as gr
import utils.input as inp


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
        raise ValueError(f"Same sign broken: f({x_l})={f_l}, f({x_r})={f_r} ")

    # Columns: [Iteration, lower bound, upper bound, mid, f(mid), interval width]
    # interval width -> abs(x_r - x_l)
    history_matrix = []

    for i in range(1, no_iter + 1):
        width = abs(x_r - x_l)
        x_m = float(x_l + x_r) / 2.0
        f_m = f(x_m)

        history_matrix.append([i, x_l, x_r, x_m, f_m, width])

        if f_m * f_l > 0:
            x_r = x_m
            f_l = f_m
        else:
            x_l = x_m

        X.append(x_m)
        Y.append(f_m)

        print(f"Iteration: {i}\t\tMid: {x_m}\t\tf(mid): {f_m}")

        if width < tol or f_m == 0.0:
            print(f"Width between intervals are {x_r} - {x_l} = {width}")
            return X, Y, history_matrix

    return X, Y, history_matrix


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
    X, Y, history_matrix = bisection(
        f=inputs["func"][1],
        x_l=inputs["low"],
        x_r=inputs["upper"],
        no_iter=inputs["iters"],
    )
    gr.scatter(x=X, y=Y, title=inputs["func"][0], x_label="x", y_label="f(x)")
