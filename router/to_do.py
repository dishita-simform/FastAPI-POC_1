from fastapi import APIRouter, Depends, HTTPException
from db import db_task
from db.database import get_db
from schemas import TaskBase
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Create Task
@router.post("/", response_model=TaskBase)
def create_task(request: TaskBase, db: Session = Depends(get_db)):
    if not request.title or not request.description:
        raise HTTPException(status_code=400, detail="Title and Description are Required.")
    return db_task.create_task(db, request)

# Get All Tasks
@router.get("/", response_model=list[TaskBase])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db_task.get_all_tasks(db)
    if not tasks:
        raise HTTPException(status_code=404, detail="No Tasks Found.")
    return tasks

# Get Task
@router.get("/{id}", response_model=TaskBase)
def get_task(id: int, db: Session = Depends(get_db)):
    task = db_task.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {id} Not Found.")
    return task

# Update Task
@router.post("/{id}/update", response_model=TaskBase)
def update_task(id: int, request: TaskBase, db: Session = Depends(get_db)):
    task = db_task.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {id} Not Found.")
    if not request.title or not request.description:
        raise HTTPException(status_code=400, detail="Title and Description are Required.")
    return db_task.update_task(db, id, request)

# Delete Task
@router.delete("/{id}/delete")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db_task.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {id} Not Found.")
    db_task.delete_task(db, id)
    return {"detail": f"Task with ID {id} Deleted Successfully."}