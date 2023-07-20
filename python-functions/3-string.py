#!/usr/bin/python3
def reverse_string(string):
    length = len(string)
    rev_string = ""
    for i in range(length - 1, -1, -1):
        rev_string += string[i]
    return rev_string
