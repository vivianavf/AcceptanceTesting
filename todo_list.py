import os
import json

# todo_manager.py
class TodoManager:
    def __init__(self, file_path='todolist.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, name, description=''):
        task = {'name': name, 'status': 'Pending', 'description': description}
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            print(f"- {task['name']} ({task['status']})")

    def mark_completed(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            task = self.tasks[task_id - 1]
            task['status'] = 'Completed'
            self.save_tasks()
            print("Marked as completed.")
        else:
            print("Invalid task ID.")

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
    
    def show_task_count(self):
        print(f"Total number of tasks: {len(self.tasks)}")

    def show_completed_tasks(self):
        completed_tasks = [task['name'] for task in self.tasks if task['status'] == 'Completed']
        print("Completed tasks:")
        for task in completed_tasks:
            print(f"- {task}")

def main():
    todo_list_manager = TodoManager()

    # Main loop
    while True:
        print("\nTo-Do List Manager:")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Show total number of tasks")
        print("6. Show completed tasks")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            todo_list_manager.add_task(name, description)
        elif choice == "2":
            todo_list_manager.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list_manager.mark_completed(task_id)
        elif choice == "4":
            todo_list_manager.clear_tasks()
        elif choice == "5":
            todo_list_manager.show_task_count()
        elif choice == "6":
            todo_list_manager.show_completed_tasks()
        elif choice == "0":
            todo_list_manager.save_tasks()
            print("Exiting program. Your to-do list has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()