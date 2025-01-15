from fastapi import FastAPI
from src.routers import tasks, pomodoro

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(pomodoro.router, prefix="/pomodoro", tags=["Pomodoro"])
