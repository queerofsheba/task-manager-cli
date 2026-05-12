import json
import os
import datetime as dt
import argparse

# Task Object Structure
# {
#   "id": 1 #integer
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

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # List subcommand
    parser_list = subparsers.add_parser("list", help="View all tasks")

    # Add task subcommand
    parser_add = subparsers.add_parser("add", help="Add task")
    parser_add.add_argument("task_name", type=str, help="Name of new task")

    # Parse arguments
    args = parser.parse_args()

    print(f"Command received: {args.command}")  # DEBUG

    if args.command == "list":
        print("Calling view_tasks...")  # DEBUG
        # invoke the view_tasks method
        tasks = load_tasks()
        print(f"Loaded {len(tasks)} tasks")  # DEBUG
        view_tasks(tasks)
    elif args.command == "add":
        print(f"Calling add_task with: {args.task_name}")
        # invoke the add_tasks method
        tasks = load_tasks()
        add_task(tasks, args.task_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()