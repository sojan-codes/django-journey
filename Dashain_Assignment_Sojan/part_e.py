# E1
num = int(input("Enter a Number: "))
for i in range(1, 11):
    print(num, "X", i, "=", (num * i))

# E2
total_sum = 0
even_sum = 0
for i in range(1, 101):
    total_sum += i
    if i % 2 == 0:
        even_sum += i

print(total_sum)
print(even_sum)

# E3
user_word = input("Enter a word: ")
for i in range(0, len(user_word)):
    print(user_word[i], "->", i)

# E4
prices = {"kite": 150, "lattai": 400, "dhago": 250, "new clothes": 3500}
total = 0
for key, values in prices.items():
    print(key, ":", f"Rs {values}")
    total += values

print("Total: Rs", total)

# E5
# for i in range(1, 6):
#     print("* " * i)
#nested loop
for i in range(1, 6):
    for j in range(i):
        print("*", end = " ")
    print()

# E6
count = 10
while count > 0:
    print(count)
    if count == 1:
        print("Happy Dashain!")
    count -= 1

# E7
user_num = int(input("Enter a number:"))
total_sum = 0

while True:
    total_sum += user_num % 10
    user_num = user_num // 10
    if user_num == 0:
        break

print(total_sum)

# E8
num_set = 0
count = 0
input_list = []

while True:
    user_num = int(input("Enter a number: "))
    if user_num == 0:
        break
    input_list.append(user_num)
    count += 1

print("Count:", count)
print("Number Entered: ")
for i in input_list:
    print(i)
print("Total: ", sum(input_list))

# E9
secret = 7
attempt = 0

while True:
    num = int(input("Enter Number: "))
    attempt += 1 
    if num == secret:
        print("Correct!. Total Attempt:", attempt)
        break
    elif num > secret:
        print("Too high")
    else:
        print("Too Low")

# E10
for i in range(1, 51):
    if i % 3 == 0:
        continue
    if i > 40 and i % 7 == 0:
        break
    print(i)