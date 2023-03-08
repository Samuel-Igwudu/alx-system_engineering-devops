#!/usr/bin/python3
""" script that uses REST API """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_f = res.json()
    print("Employee {} is done with tasks".format(json_f.get('name')), end="")

    todos = '{}todos?serId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    NO_task = []
    for task in tasks:
        if task.get('completed') is True:
            NO_task.append(task)

    print("({}/{}):".format(len(NO_task), len(tasks)))
    for task in NO_task:
        print("\t {}".format(task.get("title")))
