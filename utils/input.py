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

        elif i["type"] == "func":
            x_sym = sp.symbols("x")
            while True:
                inp = input(i["prompt"])

                try:
                    sym_exp = sp.sympify(inp)
                    f = sp.lambdify(x_sym, sym_exp, modules=["math", "sympy"])
                    inputs.setdefault(i["name"], []).append(sym_exp)
                    inputs[i["name"]].append(f)
                    break
                except Exception as e:
                    print(f"Invalid mathematical expression")

    return inputs
