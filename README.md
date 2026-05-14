# Task Manager CLI

A command-line task manager tool built with Python. Manage your tasks efficiently 
from the terminal with persistent JSON storage.

## Features

+ Add tasks with assigned IDs and automatic timestamps
+ View all tasks in formatted list
+ Mark tasks as complete
+ Delete tasks by ID
+ Persistent storage with JSON
+ Input validation and error handling
+ Clean, user-friendly command-line interface

## Installation

### Prerequisites

+ Python 3.7 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/queerofsheba/task-manager-cli.git
cd task-manager-cli
```

2. No additional dependencies needed! This project uses only Python standard library.

## Usage

### Add new tasks
```bash
python3 task_manager.py add "Get cape."
python3 task_manager.py add "Wear cape."
python3 task_manager.py add "Fly."
```

### View all tasks
```bash
python3 task_manager.py list
```

### Mark a task as complete
```bash
python3 task_manager.py complete 1
```

### Delete a task
```bash
python3 task_manager.py delete 2
```

### Get help
```bash
python3 task_manager.py --help
python3 task_manager.py add --help
```

## What I Learned

Through building this CLI tool, I practiced:
+ Python fundamentals
+ CLI development
+ Data persistence
+ Testing
+ Git workflow
+ Documentation

## Author

Jade Goodwin-Carter | Software Engineering Student

+ Portfolio: [queerofsheba.github.io/dev_portfolio](https://queerofsheba.github.io/dev_portfolio)
+ GitHub: [@queerofsheba](https://github.com/queerofsheba)
+ LinkedIn: [jadegoodwin](https://linkedin.com/in/jadegoodwin)

## License

This project is open-source and available under the [MIT License](License)

If you found this project helpful, consider giving it a star!