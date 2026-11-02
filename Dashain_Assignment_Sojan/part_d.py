# D1
user_number = int(input("Enter a Number: "))

if user_number > 0:
    print('positive.')
elif user_number < 0:
    print('negative.')
else:
    print('The number is Zero.')

# D2
user_number = int(input("Enter a Number: "))

if user_number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# D3
user_grade = int(input("Enter your Marks(out of 100): "))
val = "Grade:"
if user_grade >= 0 and user_grade <= 100:
    if user_grade > 89:
        print(val, "A+")
    elif user_grade > 79:
        print(val, "A")
    elif user_grade > 69:
        print(val, "B+")
    elif user_grade > 59:
        print(val, "B")
    elif user_grade > 49:
        print(val, "C")
    else:
        print(val, "Fail")
else:
    print("Invalid Marks")

# D4
user_year = int(input("Enter a year: "))
if (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
    print(user_year, "is leap year.")
else:
    print(user_year, "is not leap year.")

# D5
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is largest.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is largest.")
else:
    print(num3, "is largest.")

# D6
passenger_age = int(input("Enter your age: "))
val = "Bus fare:"
if passenger_age >= 0:
    if passenger_age >= 60:
        print(val, "Rs 600")
    elif passenger_age > 12:
        print(val, "Rs 1000")
    elif passenger_age > 4:
        print(val, "Rs 500")
    else:
        print(val, "Free")
else:
    print("Invalid Age.")

# D7
username = "admin"
password = "dashain2083"

user_name = input("Enter Username: ")
user_password = input("Enter Password: ")

if user_name == username:
    if user_password == password:
        print("Login successful.")
    else:
        print("Wrong password.")
else:
    print("User not found.")


