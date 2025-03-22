from file_handler import read_tasks, write_tasks

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print(f"Task '{task}' added successfully.")


def remove_task(task_number):
    tasks = read_tasks()
    
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            write_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def update_task(task_number, new_task):
    tasks = read_tasks()

    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = new_task
            write_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    tasks = read_tasks()
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")
