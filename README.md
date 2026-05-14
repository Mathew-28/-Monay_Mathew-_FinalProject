# To-Do List CLI

A command-line to-do list application built with Python. Manage your tasks with priority levels, due dates, and persistent storage — all from the terminal.

## Features

- Add tasks with a title, priority level, and optional due date
- View tasks sorted by priority (High, Medium, Low)
- View tasks sorted by due date
- Mark tasks as complete
- Delete tasks
- Tasks are automatically saved and loaded from a local JSON file

## Requirements

- Python 3.12+
- [colorama](https://pypi.org/project/colorama/)

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python src/main.py
```

You will be presented with a menu:

```
==== TO-DO LIST ====
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Sort by Due Date
6. Exit
```

### Adding a Task

Select option `1` and provide:
- **Task Title** — a short description of the task
- **Priority** — `High`, `Medium`, or `Low`
- **Due Date** — in `YYYY-MM-DD` format (optional, press Enter to skip)

### Viewing Tasks

- Option `2` lists tasks sorted by **priority**
- Option `5` lists tasks sorted by **due date**

Each task displays its completion status, title, priority, and due date.

### Marking a Task as Done

Select option `3`, view the task list, then enter the task number to mark it complete.

### Deleting a Task

Select option `4`, view the task list, then enter the task number to delete it.

### Exiting

Select option `6` to save all tasks and exit.

## Data Storage

Tasks are saved automatically to `data/tasks.json`. They are loaded back when the app starts, so your tasks persist between sessions.

## Project Structure

```
<LastName_FirstName>_FinalProject/
├── README.md            # Project overview, features, and setup guide
├── requirements.txt     # External dependencies
├── src/                 # All Python source files
│   ├── main.py          # Entry point and menu logic
│   ├── manaber.py       # TaskManager class (add, list, sort, save, load)
│   └── task.py          # Task class and serialization
└── data/                # Persistent task storage
    └── tasks.json       # Auto-generated task file
```

## Demo

YouTube URL: https://youtu.be/Bd4kfzS5z60demo
