"""

"""
class Car:
    wheels = 4

    def __init__(self, color, model, size = 3):
        self._color = color
        self.model = model
        self.__size = size

    def get_color(self):
        return self._color

    def get_size(self):
        return self.__size / 10

    def __repair_fuel(self):
        print(self.model, "fuel is repaired")

car1 = Car('white', 'Toyota')

print(car1.get_color())
print(car1.get_size())
print(car1.__repair_fuel())