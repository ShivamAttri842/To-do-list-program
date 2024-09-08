To-Do List Application
This is a simple yet functional To-Do List application implemented in Python. The application allows users to manage their tasks by providing a range of features, including viewing, adding, removing, editing, and sorting tasks. It also supports marking tasks as done or not done.

Features
View To-Do List: Displays all tasks with their status (Done/Not Done).
Add Task: Allows users to add a new task to the list.
Remove Task: Provides the ability to remove a task from the list.
Mark Task as Done: Marks a selected task as completed.
Mark Task as Not Done: Marks a selected task as incomplete.
Edit Task: Allows users to update the description of an existing task.
Sort Tasks: Sorts tasks either by status or alphabetically by task name.
Exit Program: Confirms before exiting and saves the current state of the tasks.
Error Handling
The application includes robust error handling to manage various potential issues:

File Errors: Handles errors related to file reading and writing, including permissions and I/O errors.
JSON Parsing Errors: Catches issues with JSON decoding if the file is corrupted.
Invalid User Input: Gracefully handles invalid task numbers and non-numeric input.

Requirements
Python 3.x
No external libraries are required; only built-in modules are used.

Clone the repository to your local machine:
git clone https://github.com/yourusername/todo-list.git

Run the application:
python todo_list.py
Follow the on-screen menu to manage your tasks.

File Structure
todo_list.py: The main Python script containing the implementation of the To-Do List application.
todo_list.json: (Automatically created) The file where tasks are saved and loaded.
