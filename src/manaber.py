"""TaskManager module for managing a collection of Task objects, including loading, saving, sorting, and displaying tasks."""

import json
import os   
from task import Task
from colorama import Fore, Style

class TaskManager:
    PRIORITY_ORDERS = {"High": 1, "Medium": 2, "Low": 3}    

    def __init__(self,):
        self.filename = os.path.join(os.path.dirname(__file__), "..", "data", "tasks.json")
        self.tasks = [] 
        self.load_tasks()   

    def add_task(self, title, priority, due_date=None):
        if priority.capitalize() not in self.PRIORITY_ORDERS:
            raise ValueError("Invalid priority! Use High, Medium, or Low.")
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()  # Save after adding a task

    def list_tasks(self):
        if not self.tasks:
            print(Fore.RED + "No tasks found.")
            return None
        
        sorted_tasks = sorted(self.tasks, key=lambda t: self.PRIORITY_ORDERS[t.priority])

        for i, task in enumerate(sorted_tasks, 1):
            status_color = Fore.GREEN if task.completed else Fore.RED
            status = "✓" if task.completed else "✗"
            print(f"{Fore.CYAN}{i}. {status_color}[{status}] {Fore.WHITE}{task.title} {Fore.YELLOW}({task.priority}) {Fore.BLUE}- Due: {task.due_date if task.due_date else 'No due date'}{Style.RESET_ALL}")

        return sorted_tasks  #important fix
    
    def list_tasks_by_date(self):
        if not self.tasks:
            print(Fore.RED + "No tasks found.")
            return None
        
        sorted_tasks = sorted(self.tasks, key=lambda t: (t.due_date is None, t.due_date or ""))

        for i, task in enumerate(sorted_tasks, 1):
            status_color = Fore.GREEN if task.completed else Fore.RED
            status = "✓" if task.completed else "✗"
            print(f"{Fore.CYAN}{i}. {status_color}[{status}] {Fore.WHITE}{task.title} {Fore.YELLOW}({task.priority}) {Fore.BLUE}- Due: {task.due_date if task.due_date else 'No due date'}{Style.RESET_ALL}")

        return sorted_tasks  #important fix
    
    def mark_done(self, index):
        try:
            self.tasks[index].mark_done()
        except IndexError:
            print("Invalid task number!")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Deleted task: {removed.title}")
        except IndexError:
            print("Invalid task number!")

    def save_tasks(self):
        dir_name = os.path.dirname(self.filename)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(self.filename, "w") as f: 
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
