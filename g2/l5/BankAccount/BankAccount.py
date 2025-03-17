from abc import ABC, abstractmethod


class PositiveBalance:
    def __init__(self):
        self.name = 'balance'

    def __get__(self, instance, owner):
        return instance.__dict__[self.name] if instance is not None else 0

    def __set__(self, instance, value):
        if value < 0:
            raise AttributeError('Balance cannot be negative')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class BankAccount(ABC):
    balance = PositiveBalance()

    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float):
        pass

class SavingAccount(BankAccount):
    def withdraw(self, amount: float):
        if amount > self.balance:
            raise Exception('Not enough balance')
        self.balance -= amount
        print(f'The remaining balance is: {self.balance}')


acc = SavingAccount(500)
print(acc.balance)
acc.withdraw(100)
acc.balance = -100
print(acc.balance)