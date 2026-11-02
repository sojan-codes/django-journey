#B1
user_fname = input('Enter your Name: ')
print(user_fname.upper())
print(user_fname.lower())
print(user_fname.title())
print(len(user_fname))

#B2
greeting = "Happy Dashain to you and your family"
greet_list = greeting.split()
first_word = greet_list[0]
last_word = greet_list[len(greet_list) - 1]

print("First Word:", first_word,"\nLast Word:", last_word)
print("The first 5 characters:", greeting[:5])
print("The last 6 characters:", greeting[-6:])
print("Reversed sentence:", greeting[::-1])

#B3
user_sentence = input("Enter a Sentence: ")
print("Count:", (user_sentence.lower()).count('a'))

#B4
msg = "   Vijaya Dashami ko hardik shubhakamana   "
msg = msg.strip()
print(msg)
msg = msg.replace("hardik","dherai")
print(msg)
items = msg.split()
print("Word Count:", len(items))

#B5
user_word = input("Enter a Word: ")
rev_word = user_word[::-1]
isPalindrome = False
if user_word.lower() == rev_word.lower():
    isPalindrome = True

print("Is Palindrome? :", isPalindrome)

#B6
user_email = input("Enter your Email:")
count = 0
for i in user_email:
    if i == "@":
        count += 1

if count == 1:
    email_detail = user_email.split("@")
    username_part = email_detail[0]
    domain_part = email_detail[1]

    print("Username:", username_part)
    print("Domain:", domain_part)
else:
    print("There should be only one @")




