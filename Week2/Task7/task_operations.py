from file_handler import read_tasks, write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)

def remove_task(task_number):
    tasks = read_tasks()
    try:
        tasks.pop(task_number - 1)  # Assuming 1-based indexing
        write_tasks(tasks)
    except IndexError:
        print("Error: Task number out of range.")

def update_task(task_number, new_task):
    tasks = read_tasks()
    try:
        tasks[task_number - 1] = new_task
        write_tasks(tasks)
    except IndexError:
        print("Error: Task number out of range.")

def view_tasks():
    tasks = read_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")
