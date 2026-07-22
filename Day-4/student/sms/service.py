# contains business logic

from .repo import save_student


def create_student(name, age):
    student = {"name": {name}, "age": {age}}
    save_student(student)
