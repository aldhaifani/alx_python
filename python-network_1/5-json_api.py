#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


try:
    q = sys.argv[1]
except IndexError:
    q = ""

r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

if len(r.text) == 0:
    print("No result")
else:
    try:
        body = eval(r.text)
        print(r.text)
        print("[{}] {}".format(body['id'], body['name']))
    except (SyntaxError, NameError):
        print("Not a valid JSON")
