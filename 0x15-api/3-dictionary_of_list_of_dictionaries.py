#!/usr/bin/python3
"""
A script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress,
to then export data in the JSON format
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    jsDict = {}
    for user in users:
        jsList = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                jsList.append({'task': task.get('title'),
                               'completed': task.get('completed'),
                               'username': user.get('username')})
        jsDict[user.get('id')] = jsList
    with open('todo_all_employees.json', 'w') as myfile:
        myfile.write(json.dumps(jsDict))
