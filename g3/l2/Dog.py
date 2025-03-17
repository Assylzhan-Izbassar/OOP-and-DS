class Dog:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    @staticmethod
    def calling():
        print('Куча, куча')

    def __str__(self) -> str:
        return f'Dog is {self.get_name()}'


dog1 = Dog('Бобби')
print(dog1.get_name())

Dog.calling()

print(dog1)