from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight

    def eat(self, food=None):
        if food is not None:
            print(f'{self._name} eats {food}')
        else:
            print(f'{self._name} is eating something.')

    def __repr__(self):
        return f'Cat({self._name!r}, {self.get_age()!r}, {self.weight!r})'


cat1 = Cat('Murka', 10, 15)
# print(cat1.name)
# print(cat1.weight)
# print(cat1.get_age())
cat1.eat()
# print(cat1)
print(repr(cat1))

cat2 = eval(repr(cat1))

print(cat2)


cat1.eat(['viskas', 'fish'])
# cat1.sleep()