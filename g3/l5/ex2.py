# Дискрипторы
class PositiveNumber:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.attr_name]

    def __set__(self, instance, value):
        if value < 0:
            raise AttributeError(f"{self.attr_name} не должно быть меньше нуля!")
        else:
            instance.__dict__[self.attr_name] = value


class Product:
    price = PositiveNumber('price')

    def __init__(self, name, price):
        self._name = name
        self.__price = price


p = Product('iPhone', 999)
p.price = -599

print(p.price)