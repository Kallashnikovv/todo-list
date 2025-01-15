from fastapi import APIRouter, Depends
from src.common.schemas import TaskCreate, TaskUpdate
from src.services.task_service import TaskService

router = APIRouter()

@router.post("/")
def create_task_endpoint(task: TaskCreate, service: TaskService = Depends()):
    return service.create_task(task.title, task.description)

@router.get("/")
def get_tasks_endpoint(status: str = None, service: TaskService = Depends()):
    return service.get_tasks(status)

@router.get("/{task_id}")
def get_task_endpoint(task_id: int, service: TaskService = Depends()):
    return service.get_task(task_id)

@router.put("/{task_id}")
def update_task_endpoint(task_id: int, task_update: TaskUpdate, service: TaskService = Depends()):
    return service.update_task(task_id, task_update.title, task_update.description, task_update.status)

@router.delete("/{task_id}")
def delete_task_endpoint(task_id: int, service: TaskService = Depends()):
    return service.delete_task(task_id)