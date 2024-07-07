from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    id_: int
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
