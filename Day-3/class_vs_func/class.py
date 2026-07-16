class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


student = Student("gokila", 20)

student.display()

# State
#   +      => Now class makes sense
# Behavior
