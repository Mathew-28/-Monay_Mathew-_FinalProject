class Task:
    def __init__(self, title: str, priority: str, due_date=None):
        self.title = title
        self.priority = priority.capitalize()  # High, Medium, Low
        self.completed = False
        self.due_date = due_date # Optional: Add due date attribute

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "due_date": self.due_date # Optional: Include due date in serialization     
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["priority"], data.get("due_date")) # Optional: Pass due date to constructor
        task.completed = data["completed"]
        return task