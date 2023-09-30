#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    user_id = argv[1]
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

    with open(str(user_id) + "{}.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(tasks_data)
