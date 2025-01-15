from typing import List, Optional
from src.common.models import Task, PomodoroSession
from datetime import datetime

class MemoryStorage:
    def __init__(self):
        self.tasks: List[Task] = []
        self.pomodoro_sessions: List[PomodoroSession] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_tasks(self, status: Optional[str] = None) -> List[Task]:
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, task_data: dict) -> Optional[Task]:
        task = self.get_task(task_id)
        if not task:
            return None
        for key, value in task_data.items():
            setattr(task, key, value)
        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
        return task

    def add_pomodoro_session(self, session: PomodoroSession):
        self.pomodoro_sessions.append(session)

    def get_active_pomodoro(self, task_id: int) -> Optional[PomodoroSession]:
        return next(
            (session for session in self.pomodoro_sessions if session.task_id == task_id and not session.completed),
            None
        )

    def complete_pomodoro(self, session: PomodoroSession):
        session.completed = True
        session.end_time = session.end_time or datetime.now()

    def get_completed_pomodoro(self) -> List[PomodoroSession]:
        return [session for session in self.pomodoro_sessions if session.completed]
