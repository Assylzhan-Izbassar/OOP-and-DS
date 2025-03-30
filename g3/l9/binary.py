import bisect
import time

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price

    def __hash__(self):
        return hash(self.price)

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price

    def __str__(self):
        return self.name + ' ' + str(self.price)

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

# arr = [-2, 4, 0, 2, 2, 10, 40, 12]
# arr = sorted(arr)

p1 = Product("A", 1)
p2 = Product("B", 2)
p3 = Product("C", 3)
p4 = Product("D", 4)
p5 = Product("D", 4)
p6 = Product("D", 4)
p7 = Product("D", 4)

products = [p1, p2, p3, p4, p5, p6, p1, p2, p4, p3]
pivot = Product('target', 2)

products = sorted(products, key=lambda p: p.price)
# print(arr)

# print(bisect.bisect_left(arr, 2))

for p in products:
    print(p, end=' ')

print()
print(binary_search(products, pivot))