from Moveable import *

class Car(Moveable):
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f'{self.model} is moving...')

    def __str__(self):
        return self.model