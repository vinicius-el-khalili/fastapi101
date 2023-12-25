from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    year: int

app = FastAPI()

students = {
    1: {
        "name":"John",
        "age": 0,
        "year": 2000
    }
}

# hello world

@app.get("/")
def index():
    return students

# path parameters

@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[int(student_id)]

# query parameters

@app.get("/get-by-name")
def get_student( *, name:Optional[str] = None, test: int ):
    for student_id in students:
        if (students[student_id]["name"]==name):
            return students[student_id]
    return {"Data":"Not found"}

# query + path parameters

@app.get("/get-by-name2/{student_id}")
def get_student( *, student_id: int, name:Optional[str] = None, test: int ):
    for student_id in students:
        if (students[student_id]["name"]==name):
            return students[student_id]
    return {"Data":"Not found"}

# request body and post method

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id] = student
    return students

# request body and put method

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age:  Optional[int] = None
    year: Optional[str] = None
    

@app.put("/update-student/{student_id}")
def update_student(student_id:int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student not found"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students

# delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    del students[student_id]
    return students

