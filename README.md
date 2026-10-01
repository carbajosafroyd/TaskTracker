# Task Tracker CLI

A simple command-line task tracker written in Python.

The application stores tasks in a local `tasks.json` file and supports adding, updating, deleting, listing, and changing the status of tasks.

Project URL: https://roadmap.sh/projects/task-tracker

## Requirements

- Python 3
- No external libraries

## Getting Started

Open PowerShell in the project directory:

```powershell
cd C:\Python\Projects\Beginner\TaskTracker
```

Run the application with:

```powershell
python task_tracker.py <command>
```

The `tasks.json` file is created automatically when the first task is added.

## Commands

### Add a task

```powershell
python task_tracker.py add "Buy groceries"
```

Example output:

```text
Task added successfully (ID: 1)
```

### List all tasks

```powershell
python task_tracker.py list
```

### List tasks by status

```powershell
python task_tracker.py list todo
python task_tracker.py list in-progress
python task_tracker.py list done
```

Example output:

```text
1: Buy groceries [todo]
```

### Update a task

```powershell
python task_tracker.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```powershell
python task_tracker.py delete 1
```

### Mark a task as in progress

```powershell
python task_tracker.py mark-in-progress 1
```

### Mark a task as done

```powershell
python task_tracker.py mark-done 1
```

## Task Properties

Each task contains:

- `id`: A unique numeric identifier
- `description`: The task description
- `status`: `todo`, `in-progress`, or `done`
- `createdAt`: The date and time when the task was created
- `updatedAt`: The date and time when the task was last updated

## Storage

Tasks are stored in `tasks.json` in the project directory. The file is created automatically if it does not exist.

Example:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2026-10-01T10:00:00.000000",
        "updatedAt": "2026-10-01T10:00:00.000000"
    }
]
```

## Error Handling

The application displays helpful messages when:

- A command is missing required arguments
- A task ID is not a number
- A task cannot be found
- An invalid task status is provided
- The JSON file contains invalid data
