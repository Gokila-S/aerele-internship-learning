#Only handles user interaction

from sms.api import add_student
from sms.repo import get_students

name = input("Enter name: ")
age = int(input("Enter age: "))

add_student(name, age)

students = get_students()
print("Students:", students)