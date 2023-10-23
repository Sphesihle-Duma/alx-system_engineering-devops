#!/usr/bin/python3
""" A script that uses the API to make a request and return data """

if __name__ == "__main__":
    import csv
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
    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode="w", newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todo_list:
            csv_writer.writerow([
                str(emp_id),
                str(emp_name),
                str(task["completed"]),
                task['title']
                ])
        print(f"Data has been exported to {csv_filename}")
