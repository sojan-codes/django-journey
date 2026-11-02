# F1
def greet(name):
    return f"Happy Dashain, {name}!"

print(greet('Sojan'))
print(greet('Shakya'))

# F2
def area_of_rectangle(length, width):
    area = length * width
    return area

print(area_of_rectangle(10, 30))
print(area_of_rectangle(45, 25))

# F3
def is_even(n):
    return n % 2 == 0

print(is_even(2))
print(is_even(3))

# F4
def celsius_to_fahrenheit(c):
    F = c * 9/5 + 32
    return F

print("Fahrenheit :", celsius_to_fahrenheit(10))
print("Fahrenheit :", celsius_to_fahrenheit(50))

# F5
def find_max(numbers):
    max_val = numbers[0]
    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val

print("Largest Number: ", find_max([38, 29, 91, 55]))
print("Largest Number: ", find_max([89, 58, 152, 59]))

# F6
def count_vowels(text):
    text = text.lower()
    count = 0
    for i in text:
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
            count += 1
    return count
print("Vowels Count:", count_vowels("Sojan"))
print("Vowels Count:", count_vowels("Shakya"))

# F7
def calculate_dakshina(age):
    if age >= 0:
        if age >= 18:
            return 101
        elif age >= 10:
            return 501
        else:
            return 1001
    else:
        return "Invalid Age."

age = [7, 15, 25]
for i in age:
    print(f"Age: {i},", "Rs", calculate_dakshina(i))

# F8
def simple_interest(principal, rate, time = 1):
    si = (principal * time * rate) / 100
    return si

print("Simple Interest: Rs", simple_interest(10000, 5, 2))
print("Simple Interest: Rs", simple_interest(10000, 5))