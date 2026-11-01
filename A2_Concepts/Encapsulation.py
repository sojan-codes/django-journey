# Protected
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")

    def _calculate_bonus(self):
        bonus = self._salary * 0.1
        return bonus


class Manager(
    Employee
):  # Python will automatically inherit constructor of its parent class automatically.
    def show_bonus(self):
        print(f"Bonus: {self._calculate_bonus()}")


e1 = Manager("Sojan", 50000)
e1.display_details()
e1.show_bonus()


# Private
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def __validate_amount(self, amount):
        return amount > 0

    def deposit(self, amount):
        if self.__validate_amount(amount):
            self.__balance += amount
        else:
            print("Invalid Amount.")

    def withdraw(self, amount):
        if self.__validate_amount(amount):
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Insufficient Balance.")
        else:
            print("Invalid Amount.")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Current Balance: {self.__balance}")


account = BankAccount("Sojan")
account.deposit(5000)
account.withdraw(2000)
account.display_details()
