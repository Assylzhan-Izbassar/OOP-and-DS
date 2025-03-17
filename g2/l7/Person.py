from Moveable import *

class Person(Moveable):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def move(self):
        print(f'{self.name} is moving...')

    def __str__(self):
        return f'{self.name} {self.age} years old'