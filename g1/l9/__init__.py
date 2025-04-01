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
        return True if self.name.find(other.name) != -1 else False

    def __str__(self):
        return self.name

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def products_filter(products, target):
    result = []

    for product in products:
        if product == target:
            result.append(product)

    return result

li = [1, 86, 12, 34, 35, 15]

print(linear_search(li, 34))


p1 = Product('A B', 100)
p2 = Product('B', 105)
p3 = Product('C A', 110)

products = [p1, p2, p3]
name = "A"
target = Product(name)

filtered_product = products_filter(products, target)

for product in filtered_product:
    print(product, end=', ')