from functools import total_ordering

@total_ordering
class Product:
    def __init__(self, name, price=None):
        self._name = name
        self.__price = price

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name

    def __lt__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name < other.name

    def __str__(self):
        return self.name


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# arr = [6, 12, 4, -1, 7, 10]
# sorted_arr = sorted(arr)
#
# print(sorted_arr)
#
# print(binary_search(sorted_arr, 7))

product1 = Product("A", 100)
product2 = Product("AB", 110)
product3 = Product("BB", 105)
product4 = Product("BA", 210)
product5 = Product("BAB", 120)

products = [product1, product2, product3, product4, product5]

sorted_products = sorted(products)

for product in sorted_products:
    print(product, end=', ')

print()
name = 'BB'
target = Product(name)

idx = binary_search(sorted_products, target)
if idx == -1:
    print('Not found')
else:
    print(sorted_products[idx], idx)

# 012
# ABC
# aBC

a = 'ABC'
b = 'ABc'

if a > b:
    print(a)
elif a == b:
    print('equal')
else:
    print(b)
