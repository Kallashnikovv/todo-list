import json
from typing import List, Optional
from datetime import datetime
from src.common.models import Task, PomodoroSession

class FileStorage:
    def __init__(self, file_path: str = "storage.json"):
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data.get("tasks", [])]
                self.pomodoro_sessions = [PomodoroSession(**session) for session in data.get("pomodoro_sessions", [])]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
            self.pomodoro_sessions = []

    def _save_data(self):
        data = {
            "tasks": [task.dict() for task in self.tasks],
            "pomodoro_sessions": [session.dict() for session in self.pomodoro_sessions],
        }
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_task(self, task: Task):
        self.tasks.append(task)
        self._save_data()

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
        self._save_data()
        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self._save_data()
        return task

    def add_pomodoro_session(self, session: PomodoroSession):
        self.pomodoro_sessions.append(session)
        self._save_data()

    def get_active_pomodoro(self, task_id: int) -> Optional[PomodoroSession]:
        return next((s for s in self.pomodoro_sessions if s.task_id == task_id and not s.completed), None)

    def complete_pomodoro(self, session: PomodoroSession):
        session.completed = True
        session.end_time = session.end_time or datetime.now()
        self._save_data()

    def get_completed_pomodoro(self) -> List[PomodoroSession]:
        return [s for s in self.pomodoro_sessions if s.completed]