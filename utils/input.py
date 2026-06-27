import sympy as sp


def user_input(schema):
    inputs = {}
    for i in schema:
        if i["type"] == "int":
            inp = int(input(i["prompt"]).strip() or i.get("default") or 0)
            inputs[i["name"]] = inp
        elif i["type"] == "float":
            inp = float(input(i["prompt"]).strip() or i.get("default") or 0.0)
            inputs[i["name"]] = inp

        elif i["type"] == "str":
            inp = input(i["prompt"]).strip() or i.get("default") or ""
            inputs[i["name"]] = inp

        elif i["type"] == "func" or i["type"] == "diff":
            x_sym = sp.symbols("x")
            while True:
                inp = input(i["prompt"])

                try:
                    sym_exp = sp.sympify(inp)
                    f = sp.lambdify(x_sym, sym_exp, modules=["math", "sympy"])
                    inputs.setdefault(i["name"], []).append(sym_exp)
                    inputs[i["name"]].append(f)

                    if i["type"] == "diff":
                        der_expr = sp.diff(sym_exp, x_sym)
                        f_der = sp.lambdify(x_sym, der_expr, modules=["math", "sympy"])
                        inputs[i["name"]].append(der_expr)
                        inputs[i["name"]].append(f_der)

                    break
                except Exception as e:
                    print(f"Invalid mathematical expression")

    return inputs


def AXB_input():
    A = [[0.0 for _ in range(3)] for _ in range(3)]
    B = [0.0 for _ in range(3)]

    print("~~~ Input Ax=B ~~~")
    print("Enter A:-")

    for i in range(3):
        for j in range(3):
            A[i][j] = float(input(f"Enter element A[{i}][{j}]: "))

    print("Enter B:-")
    for i in range(3):
        B[i] = float(input(f"Enter element B[{i}]: "))

    iters = int(input("Enter number of iterations (default 100): ").strip() or 100)
    return iters, A, B
