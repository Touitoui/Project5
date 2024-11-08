class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insuficient balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance, "for account holder", self.account_holder)