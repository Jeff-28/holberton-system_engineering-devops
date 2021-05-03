#!/usr/bin/python3
"""
A script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    que = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(que)
    user = response.json()
    que = que + '/todos'
    response = requests.get(que)
    todoList = response.json()
    tasksDone = 0
    titleList = []
    for toDo in todoList:
        for key, value in toDo.items():
            if key == 'completed' and value is True:
                tasksDone += 1
                titleList.append(toDo.get('title'))
    print('Employee {} is done with tasks({}/{}):\
            '.format(user.get('name'), tasksDone, len(todoList)))
    for title in titleList:
        print('\t{}'.format(title))
