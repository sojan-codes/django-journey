# X1
for i in range(1, 51):
    if (i % 3 == 0) and (i % 5 == 0 ):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        
# X2
def is_prime(n):
    count = 0
    if n <= 0 or n == 0:
        print("Invalid Number")
    else: 
        for val in range(1, n + 1):
            if n % val == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False

for i in range(1, 101):
    if is_prime(i):
        print(f"{i} is Prime.")
    else:
        print(f"{i} is Not Prime")
        

        
# X3
user_sentence = input("Enter a Sentence: ")
word_split = user_sentence.split()
word_set = set(word_split)

word_dict = {}
for val in word_set:
    count = word_split.count(val)
    word_dict[val] = count

print(word_dict)

# X4
first = 0
last = 1

count = 0
while count < 15:
    print(first, end = " ")
    first, last = last, first + last
    count += 1


    


