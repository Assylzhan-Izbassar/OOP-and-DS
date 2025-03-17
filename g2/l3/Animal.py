class Animal:
    def __init__(self, name, age):
        self._name = name # protected field
        self.__age = age # private field

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def eat(self):
        print('Animal is eating')

    def sleep(self):
        print('Animal is sleeping')
