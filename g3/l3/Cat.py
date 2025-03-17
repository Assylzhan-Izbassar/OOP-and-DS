from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color=None, eating_habit=None):
        super().__init__(name, age)
        if color:
            self.color = color
        if eating_habit:
            self.eating_habit = eating_habit

    def eat(self, food='Рыбка'):
        print(f'{self.name} кушает {food}')

    def __repr__(self):
        return f'Cat(name={self.name!r}, age={self.age!r})'

    def __getitem__(self, idx):
        if idx >= 0 and idx < len(self.eating_habit):
            return self.eating_habit[idx]
        else:
            return self.eating_habit[-1]

    def __call__(self, calories):
        if calories < 0 or calories > 50:
            return f'{self.name} не кушает это'
        else:
            return f'{self.name} обожает кушать'

    def __str__(self):
        return f'{self.name}'

    """
    длина объекта
    """
    def __len__(self):
        return self.age

    """
    перегрузка оператора +
    """
    def __add__(self, other):
        # return Cat(other.name + self.name, 1)
        return self.age + other.age