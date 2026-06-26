import numpy as np
import utils.input as inp


def jcobi_method(A, b, x0=None, tol=1e-10, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    new_x = np.zeros(n)

    for k in range(max_iter):
        for i in range(n):
            sum = 0.0

            for j in range(n):
                if i != j:
                    sum += A[i][j] * x[j]

            new_x[i] = (b[i] - sum) / A[i][i]

        if np.linalg.norm(new_x - x, ord=np.inf) < tol:
            return new_x, k + 1

        x[:] = new_x
    return x, max_iter


if __name__ == "__main__":
    A, b = inp.AXB_input()

    answer, iters = jcobi_method(A, b)

    print(f"Answer: {answer}")
    print(f"iter: {iters}")
