from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Не достаточно средств')
        self.balance -= amount
        print(f'Остаток {self.balance}')

sa = SavingAccount(1000)
sa.withdraw(100)