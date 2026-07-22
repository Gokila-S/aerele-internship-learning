class Student:

    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

s1 = Student(1)
s2 = Student(1)

print(s1 == s2)