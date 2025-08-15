todo_list = []

def show_menu():
    print("\n----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print("✅ Task added.")

    elif choice == '2':
        if not todo_list:
            print("📝 No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                status = "✔ Done" if task["done"] else "❌ Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == '3':
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("❌ Invalid task number.")

    elif choice == '4':
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            deleted = todo_list.pop(task_num)
            print(f"🗑 Task '{deleted['task']}' deleted.")
        else:
            print("❌ Invalid task number.")

    elif choice == '5':
        print("👋 Exiting To-Do List App. Stay productive!")
        break

    else:
        print("⚠ Invalid choice. Try again.")
