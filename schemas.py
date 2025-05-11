from pydantic import BaseModel

class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    class Config:
        from_attributes = True