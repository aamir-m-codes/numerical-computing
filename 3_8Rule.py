import utils.input as inp


def rule3_8(f, a, b, points):
    n = points - 1
    h = float((b - a) / n)
    x = a
    total = f(x)
    for i in range(1, n):
        x += h
        if i % 3 == 0:
            total += 2 * f(x)
        else:
            total += 3 * f(x)

    total += f(b)
    return ((3 * h) / 8) * total


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
    result = rule3_8(
        f=inputs["func"][1], a=inputs["a"], b=inputs["b"], points=inputs["points"]
    )
    print(f"Answer: {result:.3f}")
