from task_manager import TaskManager


def test_add_task():

    manager = TaskManager()

    manager.add_task("Tarea 1")

    assert len(manager.list_tasks()) == 1


def test_complete_task():

    manager = TaskManager()

    manager.add_task("DevOps")

    manager.complete_task(0)

    assert manager.list_tasks()[0]["completed"] is True