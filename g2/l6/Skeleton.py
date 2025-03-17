from Mob import Mob

class Skeleton(Mob):
    def __init__(self, name, damage_score, bow):
        super().__init__(name, damage_score)
        self.bow = bow

    def attack(self):
        return self.damage_score + 6

    def walk(self):
        print('Skeleton: walking')


