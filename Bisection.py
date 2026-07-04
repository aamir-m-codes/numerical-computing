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
        print("Both have same sign, so solution DNE")
        return

    for i in range(no_iter):
        x_m = float(x_l + x_r) / 2.0
        f_m = f(x_m)
        if f_m * x_r > 0:
            x_r = x_m
        else:
            x_l = x_m

        X.append(x_m)
        Y.append(f_m)

        print(f"Iteration: {i + 1}\t\tMid: {x_m}\t\tf(mid): {f_m}")

        if abs(float(x_r - x_l)) < tol or f_m == 0.0:
            print(
                f"Width between intervals are {x_r} - {x_l} = {abs(float(x_r - x_l))}"
            )
            return X, Y

    return X, Y


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
    X, Y = bisection(
        f=inputs["func"][1],
        x_l=inputs["low"],
        x_r=inputs["upper"],
        no_iter=inputs["iters"],
    )
    gr.scatter(x=X, y=Y, title=inputs["func"][0], x_label="x", y_label="f(x)")
