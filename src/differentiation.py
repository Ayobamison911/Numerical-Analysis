def forward_difference(f, x, h):
    """
    Forward Difference:
    f'(x) ≈ (f(x + h) - f(x)) / h
    """
    if h == 0:
        raise ValueError("Step size h cannot be zero")
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h):
    """
    Backward Difference:
    f'(x) ≈ (f(x) - f(x - h)) / h
    """
    if h == 0:
        raise ValueError("Step size h cannot be zero")
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h):
    """
    Central Difference:
    f'(x) ≈ (f(x + h) - f(x - h)) / (2h)
    (Most accurate)
    """
    if h == 0:
        raise ValueError("Step size h cannot be zero")
    return (f(x + h) - f(x - h)) / (2 * h)
