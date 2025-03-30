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

    def __str__(self):
        return self.name + ' ' + str(self.price)


def linear_search(arr, target):
    idx = []
    for i, item in enumerate(arr):
        if item == target:
            print(item, target, 'I am here')
            idx.append(i)
    return idx if len(idx) > 0 else -1


# arr = [1, 5, 19, 2, 5, -1, 2]
# target = 2

p1 = Product("A", 1)
p2 = Product("B", 2)
p3 = Product("C", 3)
p4 = Product("D", 4)
p5 = Product("D", 4)
p6 = Product("D", 4)
p7 = Product("D", 4)

products = [p1, p2, p3, p4, p5, p6, p1, p2, p4, p3]
pivot = Product('target', 2)
# pivot = p3

start = time.time()
print(linear_search(products, pivot))
end = time.time()

print(end - start)