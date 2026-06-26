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
