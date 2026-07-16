#contains business logic

from repo import save_student 

def create_student(name,age):
    student = {f"name": {name} , "age": {age}}
    save_student(student)