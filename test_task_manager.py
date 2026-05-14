import os
import json
from task_manager import load_tasks, save_tasks, add_task, complete_task, delete_task

def test_save_and_load():
    test_tasks = [
        {
            "id": 1,
            "name": "Test task 01",
            "completed": False,
            "created": "2026-05-13 9:00:00"
        }
    ]

    save_tasks(test_tasks)

    loaded_tasks = load_tasks()

    assert len(loaded_tasks) == 1, "1 task should load"
    assert loaded_tasks[0]["name"] == "Test task 01", "Task name should match"
    assert loaded_tasks[0]["completed"] == False, "Task should not be marked complete"

    print(f"\u2713 Save and Load tasks tests passed!")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def test_add_task():
    test_tasks = []

    add_task(test_tasks, "Test task 02")

    loaded_tasks = load_tasks()

    assert len(loaded_tasks) == 1, "1 task should load"
    assert loaded_tasks[0]["id"] == 1, "Task should have ID of 1"
    assert loaded_tasks[0]["name"] == "Test task 02", "Task name should match"
    assert loaded_tasks[0]["completed"] == False, "Task should not be marked complete"
    assert loaded_tasks[0]["created"] != None, "Task should have timestamp"

    print("\u2713 Add task test passed!")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    

def test_complete_task():
    test_tasks = []

    add_task(test_tasks, "Test task 03")

    complete_task(test_tasks, 1)

    loaded_tasks = load_tasks()

    assert len(loaded_tasks) == 1, "1 task should load"
    assert loaded_tasks[0]["id"] == 1, "Task should have ID of 1"
    assert loaded_tasks[0]["name"] == "Test task 03", "Task name should match"
    assert loaded_tasks[0]["completed"] == True, "Task should be marked complete"
    assert loaded_tasks[0]["created"] != None, "Task should have timestamp"

    print("\u2713 Complete task test passed!")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def test_delete_task():
    test_tasks = []

    add_task(test_tasks, "Test task 04")
    add_task(test_tasks, "Test task 05")

    delete_task(test_tasks, 1)

    loaded_tasks = load_tasks()

    assert len(loaded_tasks) == 1, "1 task should load"
    assert loaded_tasks[0]["id"] == 2, "Remaining task should have ID of 2"
    assert loaded_tasks[0]["name"] != "Test task 04", "Remaining task name should not match deleted task"

    print("\u2713 Delete task test passed!")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def test_invalid_operations():
    test_tasks = []

    add_task(test_tasks, "Test task 06")

    loaded_tasks = load_tasks()

    complete_task(loaded_tasks, 444)

    delete_task(loaded_tasks, 444)

    print("\u2713 Invalid operations test passed!")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

if __name__ == "__main__":
    print("Running tests...\n")

    try:
        test_save_and_load()
        test_add_task()
        test_complete_task()
        test_delete_task()
        test_invalid_operations()
        print("\n\u2713 All tests passed!")
    except AssertionError as e:
        print(f"\nTest failed: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")