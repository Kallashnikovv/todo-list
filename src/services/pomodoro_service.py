from datetime import datetime
from fastapi import Depends, HTTPException
from src.common.models import PomodoroSession
from src.storage.storage_handler import get_storage_handler

class PomodoroService:
    def __init__(self, storage=Depends(get_storage_handler)):
        self.storage = storage

    def create_pomodoro(self, task_id: int) -> PomodoroSession:
        if self.storage.get_active_pomodoro(task_id):
            raise HTTPException(status_code=400, detail="Active timer already exists for this task")
        new_timer = PomodoroSession(task_id=task_id, start_time=datetime.now(), end_time=None, completed=False)
        self.storage.add_pomodoro_session(new_timer)
        return new_timer

    def stop_pomodoro(self, task_id: int) -> PomodoroSession:
        active_timer = self.storage.get_active_pomodoro(task_id)
        if not active_timer:
            raise HTTPException(status_code=404, detail="No active timer found for this task")
        self.storage.complete_pomodoro(active_timer)
        return active_timer

    def get_pomodoro_stats(self):
        completed_sessions = self.storage.get_completed_pomodoro()
        stats = {
            "total_sessions": len(completed_sessions),
            "total_time": sum((s.end_time - s.start_time).seconds for s in completed_sessions if s.end_time),
        }
        return stats