
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

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 30))  # Output: 2





from functools import total_ordering

@total_ordering
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return (self.name, self.price) == (other.name, other.price)

    def __lt__(self, other):
        return (self.name, self.price) < (other.name, other.price)

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"


def binary_search(products, target):
    left, right = 0, len(products) - 1
    while left <= right:
        mid = (left + right) // 2
        if products[mid] == target:
            return mid
        elif products[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found







arr = [1, 2, 3, 4, 5, 5, 5, 6, 7]
L, R = 5, 5





def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 25, 30, 45, 50]
print(linear_search(arr, 30))  # Output: 2










class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"


def linear_search(products, target: Product):
    for i, product in enumerate(products):
        if product == target:
            return i  # Returns the index of the found element
    return -1  # Element not found





import bisect
arr = [1, 3, 5, 7, 9]
print(bisect.bisect_left(arr, 6))  # Output: 3
print(bisect.bisect_right(arr, 6)) # Output: 3


import bisect
from typing import List, Optional

# class Product:
#     def __init__(self, id: int, name: str, price: float):
#         self.id = id
#         self.name = name
#         self.price = price
#
#     def __eq__(self, other):
#         if isinstance(other, Product):
#             return self.price == other.price and self.name == other.name
#         return False
#
#     def __hash__(self):
#         return hash((self.name, self.price))
#
#     def __lt__(self, other):
#         return self.price < other.price


class ProductCatalog:
    def __init__(self, products: List[Product]):
        self.products = products

    def linear_search_by_name(self, target_name: str) -> Optional[Product]:
        """Линейный поиск продукта по названию"""
        for product in self.products:
            if product.name == target_name:
                return product
        return None

    def binary_search_by_price(self, target_price: float) -> Optional[Product]:
        """Бинарный поиск продукта по цене (список должен быть отсортирован)"""
        sorted_products = sorted(self.products)  # Использует __lt__ для сортировки
        index = bisect.bisect_left(sorted_products, Product(0, "", target_price))

        if index < len(sorted_products) and sorted_products[index].price == target_price:
            return sorted_products[index]
        return None

    def add_product(self, product: Product):
        """Добавление нового продукта"""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Удаление продукта"""
        self.products.remove(product)


# # Пример использования
# products = [
#     Product(1, "Laptop", 1200),
#     Product(2, "Mouse", 25),
#     Product(3, "Keyboard", 45),
#     Product(4, "Monitor", 300)
# ]
#
# catalog = ProductCatalog(products)
#
# print(catalog.linear_search_by_name("Mouse"))  # Линейный поиск
# print(catalog.binary_search_by_price(300))  # Бинарный поиск
