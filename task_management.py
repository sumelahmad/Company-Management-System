class Task:
    def __init__(self, task_id, description, deadline, status="Pending"):
        self.task_id = task_id
        self.description = description
        self.deadline = deadline
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display_task_info(self):
        return f"ID: {self.task_id}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.status}"

class TaskManagement:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def update_task(self, task_id, status=None, description=None):
        task = self.tasks.get(task_id)
        if task:
            if status:
                task.update_status(status)
            if description:
                task.description = description

    def generate_task_report(self):
        for task in self.tasks.values():
            print(task.display_task_info())
