def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append({"task": task, "done": False})
            print("Task added!")

        elif choice == "2":
            print("\nTasks: ")
            for i, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

        elif choice == "3":
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
