# from g3.l4.UserDatabase import UserDatabase
#
#
# def my_decorator(func):
#     def wrapper():
#         print('Before calling the function')
#         func()
#         print('After calling the function')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('Hello world!')
#
# say_hello()
#
#
#
#
# class Person:
#     def __init__(self, name: str, age: int):
#         self._name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > 0:
#             self._age = value
#         else:
#             raise ValueError('Age must be positive')
#
#     def __hash__(self):
#         return hash(self.age)
#
#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self._age == other._age
#         return False
#
#
# class Account:
#     def __init__(self, balance: int):
#         self._balance = balance # Protected field!
#
#     @property
#     def balance(self): # With getter
#         return self._balance
# import math
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass # Method without realization
#
# class Dog(Animal):
#     def speak(self):
#         return 'Woof!'
#
# dog = Dog()
# print(dog.speak())
#
#
#
#
#
#
# class PositiveNumber:
#     def __init__(self, name: str):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if instance is not None:
#             return instance.__dict__[self.name]
#
#     def  __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'{self.name}s value must be positive')
#         instance.__dict__[self.name] = value
#
#
# class Product:
#     price = PositiveNumber('price')
#
#     def __init__(self, name: str, price: float):
#         self._name = name
#         self.price = price
#
# p = Product('Phone', 1000)
# print(p.price) # 1000
# p.price = -500 # ValueError: prices value must be positive
#
#
# class PositiveBalance:
#     def __init__(self, name: str):
#         self.name = name
#
#
#
# class BankAccount(ABC):
#     balance = PositiveBalance('balance')
#
#     def __init__(self, balance: float):
#         self.balance = balance
#
#     @abstractmethod
#     def withdraw(self, amount: float):
#         pass
#
#
# class SavingsAccount(BankAccount):
#     def withdraw(self, amount: float):
#         if amount > self.balance:
#             print('Insufficient balance')
#         else:
#             self.balance -= amount
#             print(f'Withdraw: ${amount}. New balance: ${self.balance}')
#
# acc = SavingsAccount(500)
# print(acc.balance)
# acc.withdraw(100) # Withdraw: $100. New balance: $400
# acc.balance = -100 # Error


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# shapes = [Circle(5), Rectangle(4, 5)]
# for shape in shapes:
#     print(shape.area()) # 78.54, 20
#
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2) # (4, 6)



# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def say_hello():
#     print('Hello')
#
# say_hello()
# # Hello
# # Hello
# # Hello

import time

def time_it(unit='s'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start

            if unit == 'ms':
                elapsed *= 1000 # converting to milliseconds

            print(f'Run time of {func.__name__}: {elapsed:.2f} {unit}')

            return result
        return wrapper
    return decorator

#
# @time_it('ms')
# def slow_function():
#     time.sleep(0.5)
#     print('Function is ended.')
#
# slow_function()
# # Function is ended.
# # Run time of slow_function: 501.71 ms


# from functools import lru_cache
#
# def cache(n):
#     def decorator(func):
#         func = lru_cache(maxsize=n)(func)
#         return func
#     return decorator
#
# @time_it('ms')
# @cache(3)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print("First call to fibonacci(15):") # ... Run time of fibonacci: 0.28 ms
# print(fibonacci(15))
#
# print("\nSecond call to fibonacci(15):") # Run time of fibonacci: 0.00 ms
# print(fibonacci(15))

# def permission_required(role):
#     def decorator(cls):
#         orig_method = cls.execute
#         def wrapper(self, *args, **kwargs):
#             if self.role != role:
#                 raise PermissionError(f'Permission denied for {self.role}!')
#             return orig_method(self, *args, **kwargs)
#
#         cls.execute = wrapper
#         return cls
#     return decorator
#
#
# @permission_required('admin')
# class AdminTask:
#     def __init__(self, role):
#         self.role = role
#
#     def execute(self):
#         print('Executing task...')
#
#
# admin = AdminTask('admin')
# admin.execute() # Executing task...
# user = AdminTask('user')
# user.execute() # PermissionError: Permission denied for user!


def log(prefix):
    def decorator(cls):
        add_method = cls.add
        def add(self, *args, **kwargs):
            print(f'{prefix}: calling {self.add.__name__} with params: {args}, {kwargs}')
            return add_method(*args, **kwargs)
        cls.add = add
        return cls
    return decorator


@log('INFO')
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

m = MathOperations()
print(m.add(1, 2))
# INFO: calling add with params: (1, 2), {}
# 3





