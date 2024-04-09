#!/usr/bin/python3

def magic_string():
    return "BestSchool" * magic_string.calls()

magic_string.calls = lambda: getattr(magic_string, 'calls', 0) + 1
