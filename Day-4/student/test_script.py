from sms.repo import get_students
from sms.api import add_student

name = input("Enter name: ")
age = int(input("Enter age: "))
add_student(name, age)

students = get_students()
print("Students:", students)