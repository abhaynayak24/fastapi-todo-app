from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas
from datetime import datetime

class CrudBase:

    @classmethod
    def get_all_users(cls, db: Session):
        try:
            return db.query(models.User).all()
        except Exception as err:
            return err
    
    @classmethod
    def get_users_by_id(cls, db: Session, user_id: int):
        try:
            return db.query(models.User).filter(models.User.user_id == user_id).first()
        except Exception as err:
            return err
    
    @classmethod
    def user_exists(cls, db: Session, user: models.User):
        try:
            return db.query(models.User).filter(models.User.username == user.username).exists().scalar()
        except Exception as err:
            return False

    @classmethod
    def get_all_tasks(cls, db: Session):
        try:
            return db.query(models.Task).all()
        except Exception as err:
            return err
    
    @classmethod
    def get_tasks_by_id(cls, db: Session, task_id: int):
        try:
            return db.query(models.Task).filter(models.Task.task_id == task_id).first()
        except Exception as err:
            return err
    
    @classmethod
    def get_user_tasks(cls, db: Session, user_id: int):
        return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

    @classmethod
    def create_user(cls, db: Session, user: schemas.UserCreate):
        try:
            db_user = models.User(username=user.username, password=user.password)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except Exception as err:
            return err
    
    @classmethod
    def create_task(cls, db: Session, task_name: schemas.TaskCreate, user_id: int):
        db_task = models.Task(task_name=task_name.task_name, owner_id=user_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task