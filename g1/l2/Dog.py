class Dog:
    feet = 4

    def __init__(self, name): # конструктор
        self.name = name

    def __str__(self) -> str: # toString
        return f'Dog named by {self.name}, with {self.feet} feet!'

    def bark(self):
        self.name = [1, 2, 3]
        print(f'{self.name} говорит Гав!')


dog1 = Dog('Рекс')

print(type(dog1.name))

# print(dog1.bark())

# print(type(dog1.name))

print(dog1)
