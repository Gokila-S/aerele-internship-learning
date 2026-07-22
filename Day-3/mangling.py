class Student:
    def __init__(self):
        self.__password = "123"

student = Student()
print(student._Student__password) #Accessing private variable using name mangling
print(student.__password)
