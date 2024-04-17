#!/usr/bin/python3

def inherits_from(obj, a_class):
    # Check if obj is an instance of a class that is a subclass of a_class
    return isinstance(obj, type) and issubclass(obj, a_class)
