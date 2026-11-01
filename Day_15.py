class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        return f"Hi, I'm {self.name}"

s1 = Student("Aarav", 10)
s2 = Student("Sita", 12)
print(s1.introduce())
print(s2.introduce())

class Student:
    school = "Skillshikshya"

    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks = sum(mark)

    def average(self):
        return sum(self.marks / len(self.marks))

s1 = Student("Sojan")
s1.add_mark([10, 20, 30])
print(s1.name, s1.average, s1.school)

# Task 
class Bankaccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Enter Valid Amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: Rs. {amount}")
        else:
            print("Insufficient balance!")

    def current_balance(self):
        print(f"Current Balance: Rs. {self.balance}")


account1 = Bankaccount("Ram", 5000)

account1.deposit(2000)
account1.withdraw(1500)
account1.current_balance()