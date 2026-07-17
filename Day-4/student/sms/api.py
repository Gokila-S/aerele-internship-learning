#Acts as the interface between the outside world and business logic

from .service import create_student

def add_student(name, age):
    create_student(name, age)