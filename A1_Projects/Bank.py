class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Amount Deposited: {amount}"
        else:
            return "Enter valid amount!"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

    def with_balance(self):
        return f"Current Balance: {self.balance}"


u1 = BankAccount("Sojan")

print(u1.deposit(12000))
print(u1.withdraw(500))
print(u1.with_balance())