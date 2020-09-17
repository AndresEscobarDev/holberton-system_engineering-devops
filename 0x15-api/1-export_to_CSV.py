#!/usr/bin/python3
"""
For a given employee ID, exports
information about their TODO list progress
in CSV format
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()['username']
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    tasks = [v for v in todos if v['userId'] == int(argv[1])]
    filename = argv[1] + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for t in tasks:
            writer.writerow([argv[1], user, t['completed'], t['title']])
