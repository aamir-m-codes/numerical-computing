import sympy as sp


def newton_raphson(f, f_der, x0):
    print(f"Initial guess -> x0 = {x0}")
    for i in range(3):
        x1 = float(x0 - (f(x0) / f_der(x0)))
        print(f"n = {i}, x{i+1} = {x1}")
        x0 = x1


x = sp.Symbol("x")
expr = x + sp.sin(x)
der_expr = sp.diff(expr, x)

print(der_expr)

f = sp.lambdify(x, expr)
f_der = sp.lambdify(x, der_expr)

newton_raphson(f=f, f_der=f_der, x0=0.5)
