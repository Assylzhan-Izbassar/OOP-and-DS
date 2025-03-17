from Moveable import *

class Human(Moveable):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} is moving...')