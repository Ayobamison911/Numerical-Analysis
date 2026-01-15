def newton_forward_difference_table(y_values):
    """
    Constructs the forward difference table.

    y_values: list of y corresponding to x_0, x_0 + h, ...
    Returns a list of lists where table[i][j] is Δ^j y_i
    """
    n = len(y_values)
    table = [[0] * n for _ in range(n)]

    # First column is y values
    for i in range(n):
        table[i][0] = y_values[i]

    # Calculate forward differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table


def evaluate_newton_forward(x0, h, table, x_target):
    """
    Evaluates the Newton Forward Difference polynomial at x_target.

    P(x) = y_0 + uΔy_0 + (u(u−1)/2!)Δ²y_0 + ...
    where u = (x − x0) / h
    """
    u = (x_target - x0) / h
    n = len(table)
    y_pred = table[0][0]

    u_term = 1
    factorial = 1

    for j in range(1, n):
        u_term *= u - (j - 1)
        factorial *= j
        y_pred += (u_term * table[0][j]) / factorial

    return y_pred


def evaluate_newton_forward_third(x0, h, table, x_target):
    """
    Newton Forward Difference Interpolation
    Using ONLY up to 3rd forward difference.

    f(x)= f(x0)
          + uΔf(x0)
          + u(u-1)/2! Δ²f(x0)
          + u(u-1)(u-2)/3! Δ³f(x0)

    where u = (x - x0)/h
    """

    u = (x_target - x0) / h

    f0 = table[0][0]

    # Protect in case user provides fewer than 4 values
    term1 = table[0][1] if len(table[0]) > 1 else 0
    term2 = table[0][2] if len(table[0]) > 2 else 0
    term3 = table[0][3] if len(table[0]) > 3 else 0

    result = (
        f0
        + u * term1
        + (u * (u - 1) / 2) * term2
        + (u * (u - 1) * (u - 2) / 6) * term3
    )

    return result
