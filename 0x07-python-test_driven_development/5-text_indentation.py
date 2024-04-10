#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    lines = []
    current_line = ''

    for char in text:
        current_line += char
        if char in special_chars:
            lines.append(current_line.strip())
            current_line = ''

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)
        print()