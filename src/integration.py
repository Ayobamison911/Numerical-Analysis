
def trapezoidal_rule(f, a, b, n):
    """
    Approximates the integral of f from a to b
    using the Trapezoidal Rule with n subintervals.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        total += f(a + i * h)

    return h * total


def simpsons_rule(f, a, b, n):
    """
    Approximates the integral of f from a to b
    using Simpson's 1/3 Rule.

    n must be a positive even integer.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n, 2):
        total += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        total += 2 * f(a + i * h)

    return (h / 3) * total
