#!/usr/bin/python3
"""
For a given employee ID, exports
information about their TODO list progress
in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    userDict = {}
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for i in users:
        user = i.get('username')
        tasks = [v for v in todos if v.get('userId') == int(i.get('id'))]
        newTasks = [{'task': v.get('title'), 'completed': v.get('completed'),
                     'username': user} for v in tasks]
        with open('todo_all_employees.json', mode='w') as f:
            userDict[i.get('id')] = newTasks
            json.dump(userDict, f)
