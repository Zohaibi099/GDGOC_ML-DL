def read_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    try:
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
