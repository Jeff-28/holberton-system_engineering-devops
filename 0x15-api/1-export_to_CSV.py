#!/usr/bin/python3
"""
A script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress,
to then export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    que = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    response = requests.get(que)
    user = response.json()
    que = que + '/todos'
    response = requests.get(que)
    todoList = response.json()

    with open('{}.csv'.format(argv[1]), 'w', newline="") as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for toDo in todoList:
            obj = [toDo.get('userId'), user.get('username'),
                   toDo.get('completed'), toDo.get('title')]
            writer.writerow(obj)
