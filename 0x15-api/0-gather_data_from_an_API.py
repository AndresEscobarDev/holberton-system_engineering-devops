#!/usr/bin/python3
"""
For a given employee ID, returns
information about their TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()['name']
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    tasks = [v for v in todos if v['userId'] == int(argv[1])]
    completed = []
    for i in tasks:
        if i['completed'] is True:
            completed.append(i['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(user, len(completed), len(tasks)))
    print("\n".join("\t " + i for i in completed))
