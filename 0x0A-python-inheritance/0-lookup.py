#!/usr/bin/python3

def lookup(obj):
    attributes_and_methods = []
    # Get the attributes and methods of the object
    for attribute in dir(obj):
        # Exclude built-in attributes and methods starting with '__'
        if not attribute.startswith('__'):
            attributes_and_methods.append(attribute)
    return attributes_and_methods
