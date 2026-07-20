from app.models.task import Task
from app.repositories.task_repository import TaskRepository


class TaskService:

    @staticmethod
    def create_task(db, task_data):

        task = Task(**task_data.model_dump())

        return TaskRepository.create(db, task)

    @staticmethod
    def get_all_tasks(db):
        return TaskRepository.get_all(db)

    @staticmethod
    def get_task(db, task_id):
        return TaskRepository.get_by_id(db, task_id)

    @staticmethod
    def delete_task(db, task_id):

        task = TaskRepository.get_by_id(db, task_id)

        if not task:
            return None

        TaskRepository.delete(db, task)

        return task