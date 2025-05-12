from sqlalchemy import Column, Integer, String, Boolean, func, Date
from db.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    due_date = Column(Date)