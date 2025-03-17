from abc import ABC, abstractmethod

class Animal(ABC): # абстрактный класс
    def __init__(self, weight):
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @abstractmethod
    def eat(self):
        pass

# a1 = Animal(20)
# print(a1.weight)