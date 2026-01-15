def absolute_error(true_value, approx_value):
    """
    Returns Absolute Error:
    |True - Approx|
    """
    return abs(true_value - approx_value)


def relative_error(true_value, approx_value):
    """
    Returns Relative Error:
    |True - Approx| / |True|
    """
    if true_value == 0:
        raise ValueError("True value cannot be zero for relative error.")
    return abs(true_value - approx_value) / abs(true_value)


def percentage_error(true_value, approx_value):
    """
    Returns Percentage Error:
    ( |True - Approx| / |True| ) * 100
    """
    return relative_error(true_value, approx_value) * 100
