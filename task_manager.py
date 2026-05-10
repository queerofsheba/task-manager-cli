import json
import os

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
        json.dump(tasks, tasklist, indent=3)

# Test load_tasks and save_tasks functions
if __name__ == "__main__":
    # Test load
    tasks = load_tasks()
    print("Loaded tasks:", tasks)
       
    # Test save with dummy data
    test_task = {"id": 1, "name": "Test task", "completed": False}
    tasks.append(test_task)
    save_tasks(tasks)
    print("Saved tasks")
       
    # Load again to verify
    tasks = load_tasks()
    print("Loaded tasks after save:", tasks)