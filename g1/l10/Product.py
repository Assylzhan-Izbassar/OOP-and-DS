from functools import total_ordering

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) - 1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

@total_ordering
class Product:
    def __init__(self, name, price):
        self._name = name
        self.__price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self.__price

    def __hash__(self):
        return hash(self.price)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return False

    def __str__(self):
        return f'{self.name} {self.price}'

p1 = Product('A', 110)
p2 = Product('AB', 130)
p3 = Product('AC', 105)
p4 = Product('AD', 120)

catalog = [p1, p2, p3, p4]
sorted_catalog = quick_sort(catalog)

for item in sorted_catalog:
    print(item)