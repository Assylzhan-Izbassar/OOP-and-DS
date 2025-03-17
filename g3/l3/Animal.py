class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} кушает')

    def __str__(self):
        return f'{self.name}, ему/ей {self.age} лет'