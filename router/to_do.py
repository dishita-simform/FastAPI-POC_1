from fastapi import APIRouter, Depends
from db import db_task
from db.database import get_db
from schemas import TaskBase
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

#Create Task
@router.post("/", response_model=TaskBase)
def create_task(request: TaskBase, db: Session = Depends(get_db)):
    return db_task.create_task(db, request)

#Get All Tasks
@router.get("/", response_model=list[TaskBase])
def get_all_tasks(db: Session = Depends(get_db)):
    return db_task.get_all_tasks(db)

#Get Task
@router.get("/{id}", response_model=TaskBase)
def get_task(id: int, db: Session = Depends(get_db)):
    return db_task.get_task(db, id)

#Update Task
@router.post("/{id}/update")
def update_task(id: int, request: TaskBase, db: Session = Depends(get_db)):
    return db_task.update_task(db, id, request)

#Delete Task
@router.delete("/{id}/delete")
def delete_task(id: int, db: Session = Depends(get_db)):
    return db_task.delete_task(db, id)