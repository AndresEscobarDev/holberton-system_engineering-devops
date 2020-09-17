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
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    userDict = {}
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for i in users:
        user = i['username']
        tasks = [v for v in todos if v['userId'] == int(i['id'])]
        newTasks = [{'task': v['title'], 'completed': v['completed'],
                     'username': user} for v in tasks]
        with open('todo_all_employees.json', mode='w') as f:
            userDict[i['id']] = newTasks
            json.dump(userDict, f)
