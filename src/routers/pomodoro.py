from fastapi import APIRouter, Depends
from src.services.pomodoro_service import PomodoroService

router = APIRouter()

@router.post("/")
def create_pomodoro_endpoint(task_id: int, service: PomodoroService = Depends()):
    return service.create_pomodoro(task_id)

@router.post("/{task_id}/stop")
def stop_pomodoro_endpoint(task_id: int, service: PomodoroService = Depends()):
    return service.stop_pomodoro(task_id)

@router.get("/stats")
def get_pomodoro_stats_endpoint(service: PomodoroService = Depends()):
    return service.get_pomodoro_stats()
