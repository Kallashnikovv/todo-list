from fastapi import Depends, HTTPException
from src.common.models import Task
from src.storage.storage_handler import get_storage_handler

class TaskService:
    def __init__(self, storage=Depends(get_storage_handler)):
        self.storage = storage

    def create_task(self, title: str, description: str = None) -> Task:
        if any(t.title == title for t in self.storage.get_tasks()):
            raise HTTPException(status_code=400, detail="Task title must be unique")
        new_task = Task(id=len(self.storage.get_tasks()) + 1, title=title, description=description, status="TODO")
        self.storage.add_task(new_task)
        return new_task

    def get_tasks(self, status: str = None) -> list[Task]:
        return self.storage.get_tasks(status)

    def get_task(self, task_id: int) -> Task:
        task = self.storage.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def update_task(self, task_id: int, title: str = None, description: str = None, status: str = None) -> Task:
        task = self.storage.get_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if title and any(t.title == title for t in self.storage.get_tasks() if t.id != task_id):
            raise HTTPException(status_code=400, detail="Task title must be unique")
        updated_task = self.storage.update_task(task_id, {"title": title, "description": description, "status": status})
        return updated_task

    def delete_task(self, task_id: int) -> Task:
        task = self.storage.delete_task(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task