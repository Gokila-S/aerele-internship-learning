#If our class stores only data and has no behavior, we can use a dataclass to reduce boilerplate code. 
#A dataclass automatically generates special methods like __init__().
from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:int

    def introduce(self): #It can have methods as well
        print(f"My name is {self.name}")

s1 = Student("Gokila",20)
s2 = Student("Kaviya",19)

print(s1.name)
print(s2.age)

s1.introduce()
s2.introduce()