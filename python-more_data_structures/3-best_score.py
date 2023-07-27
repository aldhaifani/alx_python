#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) < 1:
        return None

    keys = list(a_dictionary.keys())
    result = keys[0]
    for key in keys:
        if a_dictionary[key] > a_dictionary[result]:
            result = key
    return result
