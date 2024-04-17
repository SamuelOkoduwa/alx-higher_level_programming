#!/usr/bin/python3
"""Defines a function add_attribute that adds a new attribute to an object."""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        attr_name (str): The name of the attribute.
        attr_value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
