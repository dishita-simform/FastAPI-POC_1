from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class DbTask(Base):
    __tablename__ = "to-do"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    description=Column(String)
    completed=Column(Boolean)