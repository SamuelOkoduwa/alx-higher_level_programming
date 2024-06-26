#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

'''# Sample test
def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, length):
    try:
        for i in range(length):
            print(my_list[i])
        return length
    except IndexError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
'''