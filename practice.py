user_num = int(input("Enter a number: "))

def check(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n

for i in range(user_num + 1):
    print(check(i))

    