from Mob import Mob

class Zombie(Mob):
    def attack(self):
        return self.damage_score + 4

    def walk(self):
        print('Zombie: walking')