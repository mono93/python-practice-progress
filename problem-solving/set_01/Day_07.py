"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

FILE_NAME = "tasks.txt"

def add_task(task):
    if task.strip() == "":
        print("Error: Task cannot be empty.")
    else:
        task_list = load_tasks()
        print(task_list)
        task_list.append({"task": task, "status": "not_done"})
        print(task_list)
        save_tasks(task_list)

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Your task list is empty.")
    else:
        print("Your Tasks:\n")
        for index, task in enumerate(tasks, start=1):
            status_symbol = "✔" if task["status"] == "done" else "✘"
            print(f"{index}. {task['task']} || {status_symbol}")


def mark_task_completed(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = "done"
        save_tasks(tasks)
    else:
        print("Error: Invalid task number.")


def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
    else:
        print("Error: Invalid task number.")

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}||{task['status']}\n")

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("||")
                tasks.append({'task': task, 'status': status})
    return tasks


def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit \n")

        choice = input("choose an option: ")

        try:
            if int(choice) & 1 <= int(choice) <= 5:
                if choice == "1":
                    task = input("Enter the task you want to add: ")
                    add_task(task)
                elif choice == "2":
                    view_tasks()
                elif choice == "3":
                    task_number = int(
                        input("Enter the task number to mark as completed: "))
                    mark_task_completed(task_number)
                elif choice == "4":
                    task_number = int(
                        input("Enter the task number to delete: "))
                    delete_task(task_number)
                elif choice == "5":
                    print("Exiting the Task List Manager. Goodbye!")
                    break
            else:
                print("Error: Please choose a valid option (1-5).")
                break

        except ValueError:
            print("Error: That is not a valid integer.")
            break

main()
