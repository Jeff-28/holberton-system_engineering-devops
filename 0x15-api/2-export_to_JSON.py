#!/usr/bin/python3
"""
A script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress,
to then export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    que = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(que)
    user = response.json()
    que = que + '/todos'
    response = requests.get(que)
    todoList = response.json()
    jsList = []
    for task in todoList:
        jsList.append({'task': task.get('title'), 'completed':
                      task.get('completed'), 'username': user.get('username')})
    tasks = {}
    tasks[user.get('id')] = jsList
    with open('{}.json'.format(argv[1]), 'w') as myfile:
        myfile.write(json.dumps(tasks))
