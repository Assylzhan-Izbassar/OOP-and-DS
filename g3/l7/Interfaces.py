from abc import ABC, abstractmethod

class Flyable(ABC): # interface
    @abstractmethod
    def fly(self):
        pass

class Plane(Flyable):
    def fly(self):
        print(f'Plane fly')

class Bird(Flyable):
    def fly(self):
        print(f'Bird fly')


class NLO(Flyable):
    def __init__(self, plane):
        self.plane = plane

    def fly(self):
        print(f'NLO fly')



class Sky:
    flyable_objects = []

    def add_object(self, obj: Flyable):
        self.flyable_objects.append(obj)

    def print_objects(self):
        for obj in self.flyable_objects:
            obj.fly()


sky = Sky()
sky.add_object(Bird())
sky.add_object(Plane())
sky.add_object(NLO('Mars'))

sky.print_objects()