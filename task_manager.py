import json
import os
import datetime as dt
import argparse

def load_tasks():
    """
    Load list of tasks from the JSON file

    Returns:
        List of task dictionaries, or empty list if file doesn't exist
    """
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as tasklist:
            contents = json.load(tasklist)
            return contents
    else:
        return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file

    Arguments:
        List of task dictionaries to save
    """
    with open("tasks.json", "w") as tasklist:
        json.dump(tasks, tasklist, indent=2)

def add_task(tasks, task_name):
    """
    Add new task to list of tasks and save to JSON file

    Arguments:
        List of task dictionaries to add to
        Name/description of new task
    """
    # Check for empty string
    if task_name.strip() == "":
        print("Error: Input required.")
        return
    # Create new task dictionary item
    new_task = {}
    if len(tasks) == 0:
        new_task["id"] = 1
    else:
        # Generate next available ID
        new_task["id"] = max(task["id"] for task in tasks) + 1
    new_task["name"] = task_name
    new_task["completed"] = False
    new_task["created"] = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add new task to tasklist
    tasks.append(new_task)

    # Save updated tasklist to JSON file
    save_tasks(tasks)

    # Print confirmation message
    print(f"New task added - {task_name}")

def view_tasks(tasks):
    """
    View formatted list of tasks

    Arguments:
        List of task dictionaries to display
    """
    # Check for empty list
    if len(tasks) == 0:
        print("Error: No tasks found.")
    else:
        print(f'{"#":4}{"ID":3} | {"Tasks":25}')
        print("-" * 35)
        count = 1
        for task in tasks:
            id = task["id"]
            name = task["name"]
            status = task["completed"]
            if status:
                status = "[\u2713]"
            else:
                status = "[ ]"
            print(f"{count}.  {id:0>3} | {name:20}{status:^5}")
            count += 1

def complete_task(tasks, task_id):
    """
    Mark task from list as complete and save to JSON file

    Arguments:
        List of task dictionaries
        ID of task to be marked complete
    """
    # Check for invalid integer input
    if task_id <= 0:
        print("Error: Task ID must be positive, non-zero integer.")
        return
    found = False
    for task in tasks:
        if task["id"] == task_id:
            found = True
            task["completed"] = True
            print(f"Task with ID {task_id} marked complete.")
            save_tasks(tasks)
            return
    if found == False:
        print(f"Error: Task with ID {task_id} not found. Use \'list\' to see all tasks.")

def delete_task(tasks, task_id):
    """
    Delete task from list and save to JSON file

    Arguments:
        List of task dictionaries
        ID of task to be deleted
    """
    # Check for invalid integer input
    if task_id <= 0:
        print("Error: Task ID must be positive, non-zero integer.")
        return
    # Check for empty list
    if len(tasks) == 0:
        print("Error: No tasks found.")
        return
    found = False
    for task in tasks:
        if task["id"] == task_id:
            found = True
            tasks.remove(task)
            print(f"Task with ID {task_id} removed.")
            save_tasks(tasks)
            return
    if found == False:
        print(f"Error: Task with ID {task_id} not found. Use \'list\' to see all tasks.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

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