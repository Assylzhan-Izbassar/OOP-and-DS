"""
Person (name, height, age, weight)
name ... - fields
Beksultan - individual
"""
# Terminology:
# 1. class
# 2. instance of class
# 3. constructor

# The primary principles of OOP
# 1. Inheritance
# 2. Abstraction
# 3. Encapsulation
# 4. Polymorphism

class Person:
    def __init__(self, name, age):
        # fields of a class
        self.name = name
        self.age = age
        self.height = 0
        self.weight = 0

    # methods
    def run(self):
        print(self.name + ' is running...')

person1 = Person("Beksultan", 19)

print(person1.name)
print(person1.run())

