from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class TaskBase(BaseModel):
    # id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    completed: bool = False
    due_date: date

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, value: date):
        if value < date.today():
            raise ValueError("Due Date can Only be Set for Future Dates.")
        return value

    class Config:
        from_attributes = True