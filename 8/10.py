class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class TaskView:
    def show_task(self, task):
        print(f"Задача {task.id}: {task.title}")


class TaskController:
    def __init__(self):
        self.tasks = []
        self.view = TaskView()

    def add_task(self, title):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)


controller = TaskController()
controller.add_task("Утро")
controller.add_task("День")

for task in controller.tasks:
    controller.view.show_task(task)
