from typing import List

def avg(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)

nums = [4.0, 3.0, 6.0]
print(avg(nums))

"""
Метод который суммирует два числа
"""
def calculate(a: int, b: int):
    return a + b


def calculate_2(**kwargs: int):
    return kwargs["a"] + kwargs["b"]

x = 4
y = 7

print(calculate(x, y))

x = '4'
y = '7'

print(calculate(x, y))
