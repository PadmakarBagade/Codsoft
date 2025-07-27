import json
import os

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
            return

        print("\n--- Your To-Do List ---")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['title']}")
        print("-----------------------\n")

    def mark_task_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                todo_list.mark_task_complete(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                task_num = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()