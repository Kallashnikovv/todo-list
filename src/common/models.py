from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

class PomodoroSession(BaseModel):
    task_id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    completed: bool
    