from functools import total_ordering

@total_ordering
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.name < other.name

    def __str__(self):
        return self.name


p1 = Product('p1', 1)
p2 = Product('p2', 2)
p3 = Product('p3', 3)

arr = [p1, p2, p3]
# target = Product('target', 2)
target = Product('p1', 10)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i, arr[i]

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


print(linear_search(arr, target))

import bisect
#
# arr = [1, 3, 5, 7, 10, 10, 10, 10, 10]
# target = 10
print(binary_search(arr, target))
# print(bisect.bisect_right(arr, target))

print('Finished')