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
        new_task["id"] = max(task["id"] for task in tasks) + 1
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

def complete_task(tasks, task_id):
    found = False
    for task in tasks:
        if task['id'] == task_id:
            found = True
            task['completed'] = True
            print(f'Task {task_id} marked complete!')
            save_tasks(tasks)
            return
    if found == False:
        print(f'Error: Task {task_id} not found')

def delete_task(tasks, task_id):
    if len(tasks) == 0:
        print('No tasks found')
    found = False
    for task in tasks:
        if task['id'] == task_id:
            found = True
            tasks.remove(task)
            print(f'Task {task_id} removed')
            save_tasks(tasks)
            return
    if found == False:
        print(f'Error: Task {task_id} not found')

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command', help="Available commands")

    # List subcommand
    parser_list = subparsers.add_parser("list", help="View all tasks")

    # Add task subcommand
    parser_add = subparsers.add_parser("add", help="Add new task")
    parser_add.add_argument("task_name", type=str, help="Name of new task")

    # Complete task command
    parser_complete = subparsers.add_parser("complete", help="Mark task as completed")
    parser_complete.add_argument("task_id", type=int, help="ID of task to mark as completed")

    # Delete task command
    parser_delete = subparsers.add_parser("delete", help="Delete task")
    parser_delete.add_argument("task_id", type=int, help="ID of task to delete")

    # Parse arguments
    args = parser.parse_args()

    if args.command == "list":
        # Call the view_tasks method
        tasks = load_tasks()
        view_tasks(tasks)
    elif args.command == "add":
        # Call the add_tasks method
        tasks = load_tasks()
        add_task(tasks, args.task_name)
    elif args.command == "complete":
        # Call the complete_task method
        tasks = load_tasks()
        complete_task(tasks, args.task_id)
    elif args.command == "delete":
        # Call the delete_task method
        tasks = load_tasks()
        delete_task(tasks, args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()