#Only handles user interaction

from api import add_student
from repo import get_students

name = input("Enter name: ")
age = int(input("Enter age: "))

add_student(name, age)

students = get_students()
print("Students:", students)