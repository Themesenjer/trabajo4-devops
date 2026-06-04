from task_manager import TaskManager


def test_add_task():

    manager = TaskManager()

    manager.add_task("Tarea 1")

    assert len(manager.list_tasks()) == 1