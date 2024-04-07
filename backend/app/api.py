from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from app.crud import CrudBase
from app.databases import get_db

crud = CrudBase
router = APIRouter()

@router.get('/')
def ping():
    return {"Pong": "Success"}

@router.get('/users/')
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db=db)

@router.post('/users/')
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.user_exists(user=user, db=db):
        return {"user already exists"}

    return crud.create_user(user=user, db=db)

@router.get('/tasks/')
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db=db)

@router.post("/users/{user_id}/tasks/")
def create_task_for_user(user_id: int, task_name: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task_name=task_name, user_id=user_id)

@router.get("/users/{user_id}/tasks")
def get_task_for_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_tasks(db=db, user_id=user_id)
