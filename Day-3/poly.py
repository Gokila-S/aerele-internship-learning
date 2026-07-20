class FlyingSuperhero:
    def fly(self):
        return "Flying with superpowers!"

class Airplane:
    def fly(self):
        return "Flying with jet engines!"

# showcases Duck Typing and Polymorphism
def launch_into_sky(object_that_can_fly):
    print(object_that_can_fly.fly())

launch_into_sky(FlyingSuperhero()) 
launch_into_sky(Airplane())        