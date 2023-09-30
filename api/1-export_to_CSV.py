#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import requests
from sys import argv
import csv


def export_to_CSV(user_id):
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()["name"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    tasks_data = []

    for task in tasks:
        tasks_data.append(
            [
                str(user_id),
                employee_name,
                task["completed"],
                task["title"],
            ]
        )

    with open(str(user_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tasks_data)


if __name__ == "__main__":
    export_to_CSV(argv[1])
