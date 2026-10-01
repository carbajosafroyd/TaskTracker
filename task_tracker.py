import os
import json
import sys
from datetime import datetime

def commands():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py add \"task description\"")
            return

        description = sys.argv[2]
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py update <id> \"new description\"")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        description = sys.argv[3]
        update_task(task_id, description)
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete <id>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        delete_task(task_id)
    
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py mark-in-progress <id>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        change_task_status(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py mark-done <id>")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Task ID must be a number.")
            return

        change_task_status(task_id, "done")
    
    elif command == "list":
        status = None

        if len(sys.argv) >= 3:
            status = sys.argv[2]

            valid_statuses = ["todo", "in-progress", "done"]

            if status not in valid_statuses:
                print("Invalid status. Use: todo, in-progress, or done")
                return

        list_tasks(status)

    else:
        print("Unknown command")

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []

    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON.")
        return []

def list_tasks(status=None):
    tasks = load_tasks()

    if status is not None:
        tasks = [task for task in tasks if task["status"] == status]

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f'{task["id"]}: {task["description"]} [{task["status"]}]')
        
def add_task(description):
    tasks = load_tasks()

    if len(tasks) == 0:
        next_id = 1
    else:
        next_id = tasks[-1]["id"] + 1

    current_time = datetime.now().isoformat()

    task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }

    tasks.append(task)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Task added successfully (ID: {next_id})")

def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task updated successfully (ID: {task_id})")
            return

    print(f"Task not found (ID: {task_id})")
    
def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task deleted successfully (ID: {task_id})")
            return

    print(f"Task not found (ID: {task_id})")

def change_task_status(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()

            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"Task status updated successfully (ID: {task_id})")
            return

    print(f"Task not found (ID: {task_id})")

def main():
    
    commands()
    
if __name__ == "__main__":
    main()