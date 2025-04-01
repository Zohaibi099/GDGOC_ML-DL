from task_operations import add_task, remove_task, update_task, view_tasks

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task description: ")
            add_task(task)
        elif choice == '2':
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to update: "))
                new_task = input("Enter the new task description: ")
                update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
