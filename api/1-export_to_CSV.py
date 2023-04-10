#!/usr/bin/python3
"""
Method to given employee ID,
returns information about his/her TODO list progress
"""
from requests import get
from sys import argv
import csv

def information_employee():
    """
    Returns information about employees
    """
    id_employee = int(argv[1])
    employee_name = ""
    task_data = []

    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_one = get(url_users)
    response_two = get(url_todos)

    if response_one.status_code == 200:
        response_json_usr = response_one.json()
        response_json_tod = response_two.json()

        for user in response_json_usr:
            if (user['id'] == id_employee):
                employee_name = user['name']

                for tod in response_json_tod:
                    if tod['userId'] == id_employee:
                        task_data.append(tod)

        # Call the function to export data to CSV
        export_to_csv(id_employee, employee_name, task_data)


def export_to_csv(user_id, employee_name, task_data):
    """
    Exports the employee information to a CSV file
    """
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['User ID', 'Username', 'Task Completed Status', 'Task Title'])

        for task in task_data:
            csv_writer.writerow([user_id, employee_name, task['completed'], task['title']])

    print(f"Employee data has been exported to {filename}")

if __name__ == "__main__":
    information_employee()
