def bisection(f, a, b, tol=1e-6, max_iter=50):
    """
    Bisection Method with iteration table.
    Returns: root, iterations
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    iterations = []

    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fa = f(a)
        fc = f(c)

        iterations.append({
            "iter": i,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc
        })

        if abs(fc) < tol or abs(b - a) / 2 < tol:
            return c, iterations

        if fa * fc < 0:
            b = c
        else:
            a = c

    return (a + b) / 2.0, iterations


def newton_raphson(f, df, x0, tol=1e-6, max_iter=50):
    """
    Newton-Raphson Method with iteration table.
    Returns: root, iterations
    """
    iterations = []
    x = x0

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero. Newton-Raphson fails.")

        x_new = x - fx / dfx

        iterations.append({
            "iter": i,
            "x": x,
            "f(x)": fx,
            "x_next": x_new
        })

        if abs(x_new - x) < tol:
            return x_new, iterations

        x = x_new

    return x, iterations
