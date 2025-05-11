from sqlalchemy.orm import Session
from db.models import DbTask
from schemas import TaskBase

def create_task(db:Session, request:TaskBase):
    new_task = DbTask(
        id=request.id,
        title=request.title,
        description=request.description,
        completed=request.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks(db:Session):
    return db.query(DbTask).all()

def get_task(db:Session, id:int):
    return db.query(DbTask).filter(DbTask.id == id).first()

def update_task(db:Session, id:int, request:TaskBase):
    task = db.query(DbTask).filter(DbTask.id == id)
    task.update({
        'title': request.title,
        'description': request.description,
        'completed': request.completed
    })
    db.commit()
    return 'Task Updated'

def delete_task(db:Session, id:int):
    task = db.query(DbTask).filter(DbTask.id == id)
    task.delete(synchronize_session=False)
    db.commit()
    return 'Task Deleted'