class Dog:
    def __init__(self, name): # contractor
        self.__name = name

    def get_name(self):
        return self.__name + ' is a dog'

    def set_name(self, name):
        if (name != ''): # validation
            self.__name = name

    def __str__(self): # to_string()
        return self.get_name()

    @staticmethod
    def bark():
        print('bark')

dog1 = Dog('Rex')
dog2 = Dog('Akzhol')
dog1.set_name('')

print(dog1.bark())
print(Dog.bark())

# print(dog1.get_name())
