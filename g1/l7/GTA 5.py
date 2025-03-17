from Human import *
from Car import *

class GTA5:
    def __init__(self):
        self.moveable = []

    def add_moveable(self, item):
        self.moveable.append(item)

    def print_moveable(self):
        for item in self.moveable:
            item.move()


game_instance = GTA5()

h1 = Human('Ербол')
c1 = Car('Германия', 'Mercedes')

game_instance.add_moveable(h1)
game_instance.add_moveable(c1)

game_instance.print_moveable()