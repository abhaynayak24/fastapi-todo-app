from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    tasks: list

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    task_name: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    task_id: int
    owner: str
    owner_id: int
    status: bool

    class Config:
        orm_mode = True