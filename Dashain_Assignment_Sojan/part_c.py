# C1
foods = ["sel roti", "masu", "chiura", "achar"]
foods.append("dahi")
foods.insert(1, "bara")
foods.remove("achar")
print(foods)
print("Length: ", len(foods))

# C2
marks = [78, 45, 92, 66, 88, 59]
highest = marks[0]
lowest = marks[0]
total = 0
for i in marks:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i

avg = total / len(marks)
print(highest, lowest)
print("Total :", total,"\nAverage :", avg)

print("Highest:", max(marks))
print("Lowest:", min(marks))
marks.sort()
print("ascending :", marks)
marks.reverse()
print("descending : ", marks)

# C3
dashain_days = ("Ghatasthapana", "Fulpati", "Maha Ashtami", "Maha Navami", "Vijaya Dashami")
print("First Day:", dashain_days[0])
print("Last Day:", dashain_days[len(dashain_days) - 1])
print("Total number of Days:", len(dashain_days))
fulpati_exist = False
for i in dashain_days:
    if i == "Fulpati":
        fulpati_exist = True
if fulpati_exist:
    print("Yes, Fulpati exists in the Tuple.")
else:
    print("No, Fulpati Does not Exists in the Tuple.")
#Tuple is immutable so elements cannot be changed, added or removed once tuple is created.

# C4
ram_family = {"Hari", "Sita", "Gopal", "Maya"}
sita_family = {"Maya", "Bikash", "Hari", "Anju"}

print("Relatives in both families:", ram_family.intersection(sita_family))
print("All relatives:", ram_family.union(sita_family))
print("Only in ram_family:", (ram_family - sita_family))

# C5
student = {"name": "Aarav", "age": 17, "city": "Pokhara"}

student["city"] = "Kathmandu"
student["course"] = "Python"
del student["age"]
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


# C6
fruits = {
    "Apple" : "Rs 50 per Kg.",
    "Banana" : "Rs 120 per Kg.",
    "Orange" : "Rs 150 per Kg.",
    "Dragon Fruit" : "Rs 300 per Kg.",
    "Watermelon" : "Rs 220 per Kg."
}

user_fruit = input("Enter fruit Name: ")

# for i in fruits:
#         if i.lower() == user_fruit.lower():
#             print(f"{i} is",fruits[i])
#             break
# else:
#     print('Not Available.')

print(fruits.get(user_fruit.title(),"Not available"))

# C7
value = list(range(1, 11))
print(value)

value = list(range(2, 21, 2))
print(value)

value = list(range(10, 0, -1))
print(value)

value = list(range(5, 51, 5))
print(value)




