from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, num_legs):
        self.__num_legs = num_legs

    @abstractmethod
    def move(self):
        pass