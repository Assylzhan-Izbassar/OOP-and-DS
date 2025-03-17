from Zombie import *
from Skeleton import *

class MinecraftWorld:
    def __init__(self):
        self.mobs = [
            Zombie('Zombie1', 3),
            Skeleton('Skeleton1', 3, 1)
        ]

    def spawn(self):
        for mob in self.mobs:
            mob.walk()

m1 = MinecraftWorld()
m1.spawn()
