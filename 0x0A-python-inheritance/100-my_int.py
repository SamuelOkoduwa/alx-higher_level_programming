#!/usr/bin/python3
"""Defines a MyInt class that inherits from int."""


class MyInt(int):
    """Represents a rebel integer."""

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)
