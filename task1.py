import json
import os

# Filename where tasks will be stored
DATA_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("\n--- Your list is empty! ---")
        return

    print("\n--- Current To-Do List ---")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")
    print("-" * 25)

def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter task description: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to mark done: "))
                tasks[task_num - 1]["done"] = True
                save_tasks(tasks)
                print("Task updated!")
            except (ValueError, IndexError):
                print("Invalid number. Please try again.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter the task number to delete: "))
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed['title']}")
            except (ValueError, IndexError):
                print("Invalid number.")

        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please pick 1 through 5.")

if __name__ == "__main__":
    main()