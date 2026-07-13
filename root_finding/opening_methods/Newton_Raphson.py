import utils.input as inp


def newton_raphson(f, d_f, start, n):
    x = start
    for i in range(n):
        x = x - (f(x) / d_f(x))

    return x


if __name__ == "__main__":
    schema = [
        {
            "name": "diff",
            "prompt": "Enter f(x): ",
            "type": "diff",
        },
        {
            "name": "start",
            "prompt": "Enter X0 (default 0.0): ",
            "type": "float",
            "default": 0.0,
        },
        {
            "name": "n",
            "prompt": "Enter iterations (default 100): ",
            "type": "int",
            "default": 100,
        },
    ]

    inputs = inp.user_input(schema=schema)
    result = newton_raphson(
        f=inputs["diff"][1],
        d_f=inputs["diff"][3],
        start=inputs["start"],
        n=inputs["n"],
    )
    print(f"Result: {result:.3f}")
