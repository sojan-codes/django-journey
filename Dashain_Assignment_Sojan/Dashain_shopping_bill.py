menu_items = {
    "Rice": [750, 1],
    "Biscuit": [200, 1],
    "Current Noodle": [50, 1],
    "Beer": [345, 1],
    "Coke": [250, 1],
    "Dairy Milk": [150, 1],
    "Peanuts": [100, 1],
}


def menu():
    print("*******Menu*******")
    for key, value in menu_items.items():
        print(key, "| Qty: ", value[1], "| Price: ", value[0])


def total_bill(cart):
    total = 0
    final = 0
    dashain_discount = 0.10
    print("\n*******itemised bill*******")
    for key, value in cart.items():
        print(
            "Item:", key, "| Quantity:", value[1], "| Sub Total:", (value[0] * value[1])
        )
    for value in cart.values():
        total += value[0] * value[1]
    if total > 5000:
        final = f"\nTotal Bill Amount: Rs {total - (total * dashain_discount)} with Dashain Discount@10%"
    else:
        final = f"\nTotal Bill Amount: Rs {total}"
    return final


menu()
cart_items = {}
print("\n*******Add to Cart*******")
while True:
    print("\n--Shop--")
    cus_item = input("Enter The Item: ")
    if cus_item.strip().title() == "Done":
        print(total_bill(cart_items))
        break
    if not menu_items.get(cus_item.strip().title(), False):
        print("\nItem not Available.")
        continue
    try:
        item_quantity = int(input("Enter the Quantity: "))
        if item_quantity <= 0:
            print("Enter Valid Quantity.")
            continue
    except:
        print("\nEnter Valid Quantity.")
        continue

    for item in menu_items.keys():
        if cart_items.get(cus_item.strip().title(), False):
            cart_items[cus_item.strip().title()][1] += item_quantity
            break
        if cus_item.strip().title() == item:
            cart_items[cus_item.strip().title()] = [menu_items[item][0], item_quantity]
            break
    else:
        print("\nItem not available.")
    print("\n--Cart Items--")
    for key, value in cart_items.items():
        print(f"Item: {key}, Qty: {value[1]}")
