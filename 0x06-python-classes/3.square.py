#!/usr/bin/python3

"""The class square"""
class Square:
    """The instance of the class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    """The method"""
    def area(self):
        return self.__size ** 2
