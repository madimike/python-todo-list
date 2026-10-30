def todo_app():
    tasks = []

    print("Welcome to your Personal To-Do List!")

    while True:
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Exit")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            if len(tasks) == 0:
                print("Your list is currently empty!")
            else:
                print("\nYour Tasks:")
                for i in range(len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")

        elif choice == "2":
            new_task = input("What task would you like to add? ")
            tasks.append(new_task)
            print(f"'{new_task}' has been added!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    todo_app()