#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        # Try to print the value as an integer
        print("{:d}".format(value))
        return True  # Return True if printing is successful
    except ValueError:
        # Handle the ValueError (e.g., if value is not convertible to an integer)
        print("Exception: Unknown format code 'd' for object of type '{}'".format(type(value).__name__), file=sys.stderr)
        return False  # Return False if printing fails

'''# sample test
value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
'''