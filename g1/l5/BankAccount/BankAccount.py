from abc import ABC, abstractmethod

class PositiveBalance:
    def __init__(self):
        self.name = 'balance'

    def __get__(self, instance, owner):
        print(instance)
        if instance is not None:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if instance is not None and value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'{self.name} must be positive')


class BankAccount(ABC):
    balance = PositiveBalance()

    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass


# b1 = BankAccount(balance=100)
# print(b1.balance)