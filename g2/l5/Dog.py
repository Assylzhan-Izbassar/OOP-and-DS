from Animal import Animal

class Dog(Animal):
    def __init__(self, name, num_legs=4):
        super().__init__(num_legs)
        self.__name = name

    def move(self):
        print(f'{self.__name} is moving')


dog = Dog('Barssik')
dog.move()

