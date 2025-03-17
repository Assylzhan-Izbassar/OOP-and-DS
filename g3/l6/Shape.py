from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} с площадью {self.area()}'


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    # def __str__(self):
    #     return f'Rectangle(width={self.width}, height={self.height})'


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    # def __str__(self):
    #     return f'Circle(radius={self.radius})'

def calc_area(s):
    for shape in shapes:
        # print('Площадь', shape, shape.area())
        print(shape)
    # print(shape.area())

shapes = [Circle(2), Rectangle(2, 4), Circle(5)]
calc_area(shapes)