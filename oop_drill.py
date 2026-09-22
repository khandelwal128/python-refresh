class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    @classmethod
    def bank_name(cls):
        return "Python Bank"

    @staticmethod
    def bank_rules():
        return "Minimum balance is 1000"

    def __str__(self):
        return f"BankAccount({self.owner}, Balance: {self.balance})"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __eq__(self, other):
        return self.owner == other.owner and self.balance == other.balance


class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest

    def deposit(self, amount):
        self.balance += amount + (amount * self.interest)

    def __str__(self):
        return f"SavingsAccount({self.owner}, Balance: {self.balance})"


class CheckingAccount(BankAccount):

    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def deposit(self, amount):
        self.balance += amount - self.fee



account1 = BankAccount("Khushi", 5000)
account2 = SavingsAccount("Khushi", 5000, 0.05)
account3 = CheckingAccount("Khushi", 5000, 50)

account1.deposit(1000)
account2.deposit(1000)
account3.deposit(1000)

print(account1)
print(account2)
print(account3)

print(repr(account1))

print(account1 == account2)

print(BankAccount.bank_name())
print(BankAccount.bank_rules())

print("Feature branch version")