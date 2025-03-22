import os

TASK_FILE = "tasks.txt"

def read_tasks():
    """Read tasks from the file and return them as a list."""
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def write_tasks(tasks):
    """Write the tasks list to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

