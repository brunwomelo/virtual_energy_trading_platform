from fastapi import FastAPI
from app.routers import user

app = FastAPI()

app.include_router(user.router, prefix="/api/v1", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
