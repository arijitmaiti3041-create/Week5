from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass
class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")
    def calculate_interest(self):
        rate = 0.05
        interest = self.__balance * rate
        print("Interest:", interest)
account = SavingsAccount("Arijit", 10000)
print("Account Holder:", account.name)
print("Initial Balance:", account.get_balance())
account.deposit(2000)
print("Updated Balance:", account.get_balance())
account.calculate_interest()
