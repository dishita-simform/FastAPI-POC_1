from sqlalchemy.orm import Session
from db.models import Task
from schemas import TaskBase
from fastapi import HTTPException

def create_task(db: Session, request: TaskBase):
    # Ensure due_date is a valid Python date object
    new_task = Task(
        title=request.title,
        description=request.description,
        completed=request.completed,
        due_date=request.due_date  # Use the default date format (YYYY-MM-DD)
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db: Session):
    tasks = db.query(Task).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="No Tasks Found.")
    return tasks

def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task With ID {task_id} Not Found.")
    return task

def update_task(db: Session, task_id: int, request: TaskBase):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} Not Found.")
    task.title = request.title
    task.description = request.description
    task.completed = request.completed
    task.due_date = request.due_date  # Use the default date format (YYYY-MM-DD)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} Not Found.")
    db.delete(task)
    db.commit()
    return {"detail": f"Task with ID {task_id} Deleted Successfully."}