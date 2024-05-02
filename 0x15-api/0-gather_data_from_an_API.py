#!/usr/bin/python3
"""Returns information about user TODO progress"""

import requests
import sys


arg1 = int(sys.argv[1])
user = requests.get('https://jsonplaceholder.typicode.com/users/{}' .format(arg1)).json()
response = requests.get('https://jsonplaceholder.typicode.com/todos/')
API_data = response.json()

employee = user["name"]
completed = []
completed_task = 0
tasks = 0
for i in API_data:
    if (i["userId"] == arg1):
        tasks += 1
        if (i["completed"] == True):
            completed_task += 1
            completed.append(i["title"])
print("Employee {} is done with tasks({}/{}):".format(employee, completed_task, tasks))
for i in completed:
    print("\t {}".format(i))