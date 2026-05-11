import json
import os
import datetime as dt

# Task Object Structure
# {
#   "id": 001 #three digit integer
#   "name": "Task objective" #string
#   "completed": False #boolean
#   "created": "2026-05-01 09:00:00" #timestamp
# }

# Task List Structure
# [
#   {task1 dictionary}
#   {task2 dictionary}
#   {task3 dictionary}
# ]

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as tasklist:
            contents = json.load(tasklist)
            return contents
    else:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as tasklist:
        json.dump(tasks, tasklist, indent=2)

def add_task(tasks, task_name):
    # Create new task dictionary item
    new_task = {}
    if len(tasks) == 0:
        new_task["id"] = 1
    else:
        max_id = 0
        for task in tasks:
            if task["id"] > max_id:
                max_id = task["id"]
        new_task["id"] = max_id + 1
    new_task["name"] = task_name
    new_task["completed"] = False
    new_task["created"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add new task to tasklist
    tasks.append(new_task)

    # Save updated tasklist to JSON file
    save_tasks(tasks)

    # Print confirmation message
    print("New task added!")

def view_tasks(tasks):
    if len(tasks) == 0:
        print('No tasks found')
    else:
        print(f'{"#":3}{"ID":3}  {"Task":20}{"Status":5}')
        print("-" * 35)
        count = 1
        for task in tasks:
            id = task["id"]
            name = task["name"]
            status = task["completed"]
            if status:
                status = "DONE"
            else:
                status = "----"
            print(f'{count:<3}{id:0>3}  {name:20}{status:5}')
            count += 1


if __name__ == "__main__":
    tasks = load_tasks()
    view_tasks(tasks)