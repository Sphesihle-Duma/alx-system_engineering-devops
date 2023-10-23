#!/usr/bin/python3
""" A script that uses the API to make a request and return data """

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    emp_id = sys.argv[1]

    api_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(api_url)
    employee_data = response.json()
    emp_name = employee_data["name"]

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    res_todos = requests.get(todo_url)
    todo_list = res_todos.json()

    completed_tasks = [task for task in todo_list if task["completed"]]
    num_c_tasks = len(completed_tasks)
    total = len(todo_list)
    print(f"Employee {emp_name} is done with tasks({num_c_tasks}/{total}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
