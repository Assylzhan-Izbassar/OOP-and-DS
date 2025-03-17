from typing import List

def avg(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

x = [1, 35, 'string']
y = set([1, 3, 5])

print(avg(y))

numbers: List[float] = [1., 4.5, 6.7]

print(avg(numbers))

