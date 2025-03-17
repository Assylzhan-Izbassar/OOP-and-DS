from abc import ABC, abstractmethod

class Mob(ABC):
    def __init__(self, name, damage_score):
        self.name = name
        self.damage_score = damage_score

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def walk(self):
        pass