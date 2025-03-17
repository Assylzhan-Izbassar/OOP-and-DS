from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model):
        self._model = model

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print(f'{self._model} движется')


# v = Vehicle('BMW')
c = Car('BMW')
c.drive()