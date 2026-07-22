class Bird:
    def sound(self):
        print("Some Sound")


class Sparrow(Bird):
    def sound(self):
        print("Chirp")


class Crow(Bird):
    def sound(self):
        print("Caw")


birds = [Sparrow(), Crow()]

for bird in birds:
    bird.sound()