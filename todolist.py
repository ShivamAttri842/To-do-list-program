import json
import os

class TodoList:
    FILE_NAME = 'todo_list.json'

    def __init__(self):
        self.todo_list = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, 'r') as file:
                    self.todo_list = json.load(file)
            except json.JSONDecodeError:
                print("Error loading tasks. File might be corrupted.")
                self.todo_list = []

    def save_tasks(self):
        """Save tasks to a file."""
        try:
            with open(self.FILE_NAME, 'w') as file:
                json.dump(self.todo_list, file, indent=4)
        except IOError:
            print("Error saving tasks. Please check file permissions.")

    def show_menu(self):
        """Display the menu options."""
        print("\n--- To-Do List Menu ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Mark Task as Not Done")
        print("6. Edit Task")
        print("7. Sort Tasks")
        print("8. Exit")

    def view_list(self):
        """Display the current tasks in the to-do list."""
        if not self.todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.todo_list, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{idx}. {task['task']} - {status}")

    def add_task(self):
        """Add a new task to the to-do list."""
        task = input("Enter the task you want to add: ").strip()
        if task:
            self.todo_list.append({'task': task, 'done': False})
            print(f"'{task}' has been added to your list.")
            self.save_tasks()
        else:
            print("Task cannot be empty.")

    def remove_task(self):
        """Remove a task from the to-do list."""
        self.view_list()
        try:
            task_num = int(input("Enter the task number you want to remove: ")) - 1
            if 0 <= task_num < len(self.todo_list):
                removed_task = self.todo_list.pop(task_num)
                print(f"'{removed_task['task']}' has been removed from your list.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_done(self):
        """Mark a task as done."""
        self.view_list()
        try:
            task_num = int(input("Enter the task number you want to mark as done: ")) - 1
            if 0 <= task_num < len(self.todo_list):
                self.todo_list[task_num]['done'] = True
                print(f"'{self.todo_list[task_num]['task']}' has been marked as done.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_not_done(self):
        """Mark a task as not done."""
        self.view_list()
        try:
            task_num = int(input("Enter the task number you want to mark as not done: ")) - 1
            if 0 <= task_num < len(self.todo_list):
                self.todo_list[task_num]['done'] = False
                print(f"'{self.todo_list[task_num]['task']}' has been marked as not done.")
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def edit_task(self):
        """Edit an existing task."""
        self.view_list()
        try:
            task_num = int(input("Enter the task number you want to edit: ")) - 1
            if 0 <= task_num < len(self.todo_list):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    self.todo_list[task_num]['task'] = new_task
                    print(f"Task has been updated to '{new_task}'.")
                    self.save_tasks()
                else:
                    print("Task description cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def sort_tasks(self):
        """Sort tasks by status or name."""
        print("\nSort by:")
        print("1. Status (Done/Not Done)")
        print("2. Name")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            self.todo_list.sort(key=lambda x: x['done'])
        elif choice == '2':
            self.todo_list.sort(key=lambda x: x['task'])
        else:
            print("Invalid choice.")
            return
        self.save_tasks()
        print("Tasks have been sorted.")

    def exit_program(self):
        """Confirm before exiting."""
        confirm = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm == 'y':
            print("Exiting the To-Do list. Have a productive day!")
            self.save_tasks()
            return True
        return False

    def run(self):
        """Main function to run the to-do list application."""
        while True:
            self.show_menu()
            choice = input("Choose an option (1-8): ")

            if choice == '1':
                self.view_list()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.mark_done()
            elif choice == '5':
                self.mark_not_done()
            elif choice == '6':
                self.edit_task()
            elif choice == '7':
                self.sort_tasks()
            elif choice == '8':
                if self.exit_program():
                    break
            else:
                print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    TodoList().run()