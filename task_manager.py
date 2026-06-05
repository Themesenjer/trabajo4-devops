class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        self.tasks.append({
            "name": task,
            "completed": False
        })

    def complete_task(self, index):

        self.tasks[index]["completed"] = True

    def list_tasks(self):
        return self.tasks


if __name__ == "__main__":

    manager = TaskManager()

    manager.add_task("Estudiar DevOps")
<<<<<<< conflicto-b
    manager.add_task("Practicar GitHub - Version B")
=======
    manager.add_task("Practicar GitHub - Version A")
>>>>>>> main

    manager.complete_task(0)

    print(manager.list_tasks())
