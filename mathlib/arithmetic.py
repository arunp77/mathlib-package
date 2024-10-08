def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The sum of the two numbers.

    Examples:
    >>> add(5, 3)
    8
    >>> add(2.5, 1.5)
    4.0
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first.

    Parameters:
    a (float or int): The number to be subtracted from.
    b (float or int): The number to subtract.

    Returns:
    float or int: The result of subtracting b from a.

    Examples:
    >>> subtract(10, 4)
    6
    >>> subtract(2.5, 0.5)
    2.0
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float or int): The first number.
    b (float or int): The second number.

    Returns:
    float or int: The product of the two numbers.

    Examples:
    >>> multiply(4, 3)
    12
    >>> multiply(2.5, 4)
    10.0
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second.

    Parameters:
    a (float or int): The numerator.
    b (float or int): The denominator.

    Returns:
    float: The result of dividing a by b.

    Raises:
    ValueError: If the denominator (b) is zero.

    Examples:
    >>> divide(8, 2)
    4.0
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(x, y):
    """
    Raise x to the power of y.

    Parameters:
    x (float or int): The base.
    y (float or int): The exponent.

    Returns:
    float or int: The result of x raised to the power of y.

    Raises:
    ValueError: If either x or y is not a numeric type.

    Examples:
    >>> power(2, 3)
    8
    >>> power(5, 0)
    1
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both x and y must be numeric types.")
    return x ** y


#----------------- doctest ------------------
# # mathlib/arithmetic.py

# # ... [existing code] ...

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
