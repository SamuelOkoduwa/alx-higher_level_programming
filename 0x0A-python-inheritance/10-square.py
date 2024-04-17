#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Returns the string representation of the Square."""
        return f"[Square] {self.__size}/{self.__size}"
