import math

import numpy as np

def even(n):
    """The first n non-negative evenm integers as floats.

    Args:
        n (int): Number of values that will be output.

    Returns:
        numpy.array: One dimensional array starting at 0, up to the n'th even integer.
    """
    return 2.*np.arange(n)


def geometric(n, start=1.0, ratio=2.0):
    """Return the first n non-negative even numbers as floats.

    From a given start values and ratio between successivt terms, we use a list iterator
    to generate a geometric sequence.

    Args:
        n (int): Number of terms. Must be non-negative; bool is rejected.
        start (int or float): First term. Defaults to 1.0.
        ratio (int or float): Multiplier between terms. Defaults to 2.0.

    Returns:
        list: First n terms, starting with start at exponent zero.
        Empty when n is zero. Element types depend on start and ratio;
        integer arguments can produce integers.

    Raises:
        TypeError: If n is not a Python int, or is a bool.
        ValueError: If n is negative.
    
    Examples:
        >>> geometric(4)
        [1.0, 2.0, 4.0, 8.0]
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

    return [start * ratio**k for k in range(n)]


def fibonacci(n):
    """Return the first n Fibonacci numbers, starting with 0 and 1.

    Args:
        n (int): Number of terms; a non-negative Python integer, excluding bool.

    Returns:
        list: The first n terms, or an empty list when n is zero.

    Raises:
        TypeError: If n is not a Python int or is a bool.
        ValueError: If n is negative.

    Examples:
        >>> fibonacci(6)
        [0, 1, 1, 2, 3, 5]
        >>> fibonacci(0)
        []
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    values = []
    a, b = 0, 1
    for _ in range(n):
        values.append(a)
        a, b = b, a + b
    return values