import utils.input as inp


def rule1_3(f, a, b, points):
    n = points - 1
    h = float((b - a) / n)
    x = a
    total = f(x)

    for i in range(1, n):
        x += h
        if i % 2 != 0:
            total += 4 * f(x)
        else:
            total += 2 * f(x)

    total += f(b)
    return (h / 3) * total


if __name__ == "__main__":
    schema = [
        {
            "name": "func",
            "prompt": "Enter f(x): ",
            "type": "func",
        },
        {
            "name": "a",
            "prompt": "Enter lower limits: ",
            "type": "float",
        },
        {
            "name": "b",
            "prompt": "Enter higher limits: ",
            "type": "float",
        },
        {
            "name": "points",
            "prompt": "Enter points: ",
            "type": "int",
        },
    ]
    inputs = inp.user_input(schema=schema)
    result = rule1_3(
        f=inputs["func"][1], a=inputs["a"], b=inputs["b"], points=inputs["points"]
    )
    print(f"Answer: {result:.3f}")
