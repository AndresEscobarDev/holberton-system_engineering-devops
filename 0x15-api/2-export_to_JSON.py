#!/usr/bin/python3
"""
For a given employee ID, exports
information about their TODO list progress
in JSON format
"""

import requests
from sys import argv
import json


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json().get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    tasks = [v for v in todos if v.get('userId') == int(argv[1])]
    newTasks = [{'task': v.get('title'), 'completed': v.get('completed'),
                 'username': user} for v in tasks]
    filename = argv[1] + '.json'
    with open(filename, mode='w') as f:
        userDict = {argv[1]: newTasks}
        json.dump(userDict, f)
