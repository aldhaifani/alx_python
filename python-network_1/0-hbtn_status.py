#!/usr/bin/python3
"""
A module that fetches and prints data from a url
"""
import requests

r = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("	- type: {}".format(type(r.text)))
print("	- content: {}".format(r.text))
