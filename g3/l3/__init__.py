from Animal import Animal
from Cat import Cat

a1:Animal = Animal('Бобик', 3)
a1.eat()
# a2: Cat = Animal('Мурка', 10)
# a2.eat()
cat = Cat('Мурка', 10, eating_habit=['рыбку', 'вискас', 'мясо'])
cat2 = Cat('Барсик', 3, 'Оранжевый')
cat.eat()
cat.eat('Вискас')
print(cat.name, cat.age)
# print(cat.color)

print(cat2.name, cat2.age)
print(cat[1])
print(cat(51))
print(len(cat)) # длина кошки -> возраст кошки
print(repr(cat))
print(cat + cat2)
# cat_copy = eval(cat.__repr__())
# print(cat_copy)
# eval(cat2.__repr__())