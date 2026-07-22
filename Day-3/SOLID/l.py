class Animal:
    def speak(self):
        print("Animal Sound")


class Dog(Animal):
    def speak(self):
        print("Bark")

animal = Dog()
animal.speak()