from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from app.databases import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    tasks = relationship('Task', back_populates='owner')
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(255), nullable=False)
    status = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.user_id'))
    owner = relationship('User', back_populates='tasks')
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)