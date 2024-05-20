#!/usr/bin/python3

""" Returns employee information using REST api """

import requests
REST_API = "https://jsonplaceholder.typicode.com"


def get_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress for a given ID.

    Args:
    employee_id: The integer ID of the employee.
    """
    url = f"{REST_API}/todos?userId={employee_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        todos = response.json()

        completed_tasks = sum(1 for task in todos if task.get("completed"))
        total_tasks = len(todos)

        user_response = requests.get(f"{REST_API}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get("name", "Unknown")

        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        if completed_tasks > 0:
            for task in todos:
                if task.get("completed"):
                    print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving data: {e}")

        if __name__ == "__main__":
            if len(sys.argv) > 1:
                try:
                    employee_id = int(sys.argv[1])
                    get_todo_progress(employee_id)
                except ValueError:
                    print("Please provide a valid integer employee ID.")
                else:
                    print("Usage: python script.py <employee_id>")
