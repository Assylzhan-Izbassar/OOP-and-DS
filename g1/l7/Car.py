from Moveable import Moveable

class Car(Moveable):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f'{self.model} is driving...')
