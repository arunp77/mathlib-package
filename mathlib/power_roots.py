def power(base, exp):
    """
    Compute the power of a base raised to an exponent.

    Parameters:
    base (float or int): The base number.
    exp (float or int): The exponent to which the base is raised.

    Returns:
    float: The result of raising the base to the exponent.

    Examples:
    >>> power(2, 3)
    8
    >>> power(5, 2)
    25
    >>> power(9, 0.5)
    3.0
    """
    return base ** exp

def sqrt(x):
    """
    Compute the square root of a number.

    Parameters:
    x (float or int): The number to find the square root of.

    Returns:
    float: The square root of the number.

    Raises:
    ValueError: If x is negative.

    Examples:
    >>> sqrt(4)
    2.0
    >>> sqrt(9)
    3.0
    >>> sqrt(0)
    0.0
    """
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return x ** 0.5

def cbrt(x):
    """
    Compute the cube root of a number.

    Parameters:
    x (float or int): The number to find the cube root of.

    Returns:
    float: The cube root of the number.

    Examples:
    >>> cbrt(8)
    2.0
    >>> cbrt(27)
    3.0
    >>> cbrt(-27)
    -3.0
    """
    if x < 0:
        return -(-x) ** (1/3)
    return x ** (1/3)

