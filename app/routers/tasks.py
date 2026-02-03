from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import TaskCreate,TaskUpdate,TaskResponse
from app.models import User, Task
from  app.utils.dependencies import get_current_user

tasks_router = APIRouter()


@tasks_router.post("/erstell_task",response_model=TaskResponse)
def task_erstellen(task:TaskCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):

   new_task = Task(
        title=task.title,
        description = task.description,
        completed=False,
        user_id=current_user.id
    )
   db.add(new_task)
   db.commit()
   db.refresh(new_task)

   return new_task

@tasks_router.get("/get_all_tasks", response_model=List[TaskResponse])
def get_tasks(db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks

@tasks_router.get("/get_task/{id}", response_model=TaskResponse)
def get_task(id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id,Task.user_id == current_user.id).first()
    if not task :
        raise HTTPException(status_code=400,detail="Task not found")
    return task


@tasks_router.put("/put_task/{id}", response_model=TaskResponse)
def put_task(id:int,task_update:TaskUpdate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id,Task.user_id == current_user.id).first()
    if not task :
        raise HTTPException(status_code=400,detail="Task not found")

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed

    db.commit()
    db.refresh(task)
    return task


@tasks_router.delete("/delete_task/{id}")
def delete_task(id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == id,Task.user_id == current_user.id).first()
    if not task :
        raise HTTPException(status_code=400,detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
