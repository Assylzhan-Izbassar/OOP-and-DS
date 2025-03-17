from Person import *
from Car import *
from Moveable import *

class Test:
    def __init__(self):
        pass

class GTA:
    def __init__(self):
        self.objects = []

    def add_object(self, obj: Moveable):
        self.objects.append(obj)

    def print_objects(self):
        for obj in self.objects:
            obj.move()

game = GTA()
p1 = Person('Samat', 20)
car1 = Car('Toyota')
t1 = Test()


game.add_object(p1)
game.add_object(car1)
# game.add_object(t1)


game.print_objects()