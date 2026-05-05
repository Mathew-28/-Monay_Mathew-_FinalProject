"""Entry point for the To-Do List CLI application. Handles the main menu loop and user interaction."""

from manaber import TaskManager
from colorama import init, Fore, Style
init(autoreset=True)  # auto resets color after each print

def get_valid_priority():
    while True:
        priority = input("Enter priority (High, Medium, Low): ").capitalize()
        if priority in TaskManager.PRIORITY_ORDERS:
            return priority
        print("Invalid priority! try again.")

def get_valid_index(task_manager):
    while True:
        try:
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(task_manager.tasks):
                return index
            else:
                print("Out of bounds.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return None
        
def main():
    manager= TaskManager()

    while True:
        print(Fore.CYAN + "\n==== TO-DO LIST ====")
        print(Fore.YELLOW + "1. Add Task")    
        print(Fore.YELLOW + "2. View Tasks")
        print(Fore.YELLOW + "3. Mark Task as Done")
        print(Fore.YELLOW + "4. Delete Task") 
        print(Fore.YELLOW + "5. Sort by Due Date") 
        print(Fore.YELLOW + "6. Exit")   

        choice = input("Choose an option: ")    

        if choice == "1":
            title = input("Task Title: ").strip()
            if not title:
                print(Fore.RED + "Title cannot be empty!")
                continue    
            priority = get_valid_priority()
            due_date = input("Due Date (YYYY-MM-DD) or press Enter to skip: ").strip()
            if not due_date:
                due_date = None
            manager.add_task(title, priority, due_date)
            print(Fore.GREEN + "Task added successfully!")

        elif choice == "2":
            manager.list_tasks()    
        elif choice == "3":
            task = manager.list_tasks()  # Get sorted tasks
            if task:
                index = get_valid_index(manager)
                if index is not None:
                    manager.mark_done(index)
        elif choice == "4":
            task = manager.list_tasks()  # Get sorted tasks
            if task:
                index = get_valid_index(manager)
                if index is not None:
                    manager.delete_task(index)
        elif choice == "5":
            manager.list_tasks_by_date()
        elif choice == "6":
            manager.save_tasks()  # Ensure tasks are saved before exiting
            print(Fore.MAGENTA + "Saved tasks. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option! Please try again.")

if __name__ == "__main__":
    main()
