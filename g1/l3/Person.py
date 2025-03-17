class Person: # базовый класс
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def introduce(self, name, age=None):
        if age:
            print(f'Your name is {name} and you {age} years old, right?')
        else: print(f'Your name is {name}, right?')
