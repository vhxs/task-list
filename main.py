from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Task(BaseModel):
    name: str
    description: str
    keywords: list[str]
    created: datetime
    deadline: datetime
    priority: int


tasks: list[Task] = []


@app.get("/task/get_tasks")
async def get_tasks():
    return [task.model_dump() for task in tasks]


@app.post("/task/add_task")
async def add_task(task: Task):
    tasks.append(task)
