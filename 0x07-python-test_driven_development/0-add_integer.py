#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number to be added.
    b (int or float, optional): The second number to be added. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or float")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
