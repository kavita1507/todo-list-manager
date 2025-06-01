def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added.")

def remove_task(index):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Removed: {removed.strip()}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks yet.")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List Manager")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter your task: ")
            add_task(task)
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Enter a valid number.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")
