#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


username = sys.argv[1]
passwd = sys.argv[2]


r = requests.get(
    "https://api.github.com/users/{}".format(username), data={"Authorization": passwd}
)

if r.status_code == 404 or r.status_code == 403:
    print("None")
else:
    user_id = r.text.split(",")[1].split(":")[1]
    print(user_id)
