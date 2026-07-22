class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})" #Dev-friendly o/p

student = Student("Gokila", 20)

print(student)