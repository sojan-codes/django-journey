#A1
var_str = "Sojan Buddhacharya"
print(var_str)
print(type(var_str))

var_int = 20
print(var_int)
print(type(var_int))

var_float = 20.8
print(var_float)
print(type(var_float))

var_bool = True
print(var_bool)
print(type(var_bool))

var_list = [10, 20, 30, 40, 50]
print(var_list)
print(type(var_list))

var_tuple = (10, 20, 30, 40, 50)
print(var_tuple)
print(type(var_tuple))

var_set = {10, 20, 30, 40, 50}
print(var_set)
print(type(var_set))

var_dict = {
    "Name" : "Sojan Buddhacharya",
    "Age" : 20,
    "Country" : "Nepal" 
}

print(var_dict)
print(type(var_dict))

#A2
user_age = int(input("Enter your Age:"))
print(f"You will be {user_age + 1} in Next Dashain")

#A3
kite_price = float(input("Enter the Price of One Kite: "))
kite_required = int(input("Total no of Kites required: "))
total_cost = kite_price * kite_required
print("Total Cost: ", total_cost)
print("Rounded Cost: ", int(total_cost))

#A4
#my pridiction: 55, 10, 555, 9.5, False, False, True, False
print("5" + "5")
print(5 + 5)
print("5" * 3)
print(int("7") + float("2.5"))
print(bool(0), bool(""), bool("0"), bool([]))

#A5
list_items = [1, 2, 2, 3, 3, 3]
print(list_items)

set_items = set(list_items) #Repeatable values are Removed but order is not guaranted and values are inside {} bracket
print(set_items)

tuple_items = tuple(set_items) #Made it immutable and values are inside () bracket
print(tuple_items)


