#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    a = sentence[0] if length > 0 else None
    t = (len(sentence), a)
    return t
