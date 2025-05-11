from fastapi import FastAPI
from router import to_do
from db.database import engine
from db.models import Base

app = FastAPI()

app.include_router(to_do.router)

@app.get("/")
def root():
    return {"message": "Welcome to the To-Do API!"}

Base.metadata.create_all(bind=engine)