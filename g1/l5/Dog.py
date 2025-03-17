from Animal import Animal

class Dog(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(weight)
        self._name = name

    @property
    def name(self):
        return self._name

    def eat(self): # перезапись метода
        print(f'{self.name} кушает косточку')


dog1 = Dog('Барбос', 24)
dog1.eat()