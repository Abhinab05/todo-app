def add_task():
    task = input("Enter a task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")1
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i].strip()}")

def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    print("\nYour tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i].strip()}")

    num = int(input("Enter task number to delete: "))
    tasks.pop(num - 1)

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

    print("Task deleted!")

# Main Menu
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
