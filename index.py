from fastapi import FastAPI
from routes.student import student_router

app = FastAPI()
app.include_router(student_router)


@app.get("/")
def index():
    return {"message": "Hello World"}
