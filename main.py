'''
Waseem Alward
Mohamed Al-omairi
restaurant_final_exam.py
'''


def menu():
    print("\tRestaurant Register\t\t\n")
    print("Dish No.\tDish Name\t\tPrice")
    print("---------\t---------\t\t------")
    print(f"1\t\t\tGang Gai\t\t$10.00")
    print(f"2\t\t\tPad Thai\t\t$8.75")
    print(f"3\t\t\tPad Cashew\t\t$9.50")
    print(f"4\t\t\tPad Prik \t\t$10.25")
    print(f"5\t\t\tPeanut Curry\t$9.50")
    print(f"6\t\t\tCurry Noodle \t$11.25")

subTotal = 0
menu()
itemNum = float(input("\nEnter the item number you want (1-6): "))
price = 0
total = 0

while itemNum == 1 or itemNum == 2 or itemNum == 3 or itemNum == 4 or itemNum == 5 or itemNum == 6:
    if itemNum == 1:
        print("You chose Gang Gai")
        price = 10
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    elif itemNum == 2:
        print("You chose Pad Thai")
        price = 8.75
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    elif itemNum == 3:
        print("You chose Pad Cashew")
        price = 9.50
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    elif itemNum == 4:
        print("You chose Pad Prik")
        price = 10.25
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    elif itemNum == 5:
        print("You chose Peanut Curry")
        price = 9.50
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    elif itemNum == 6:
        print("You chose Curry Noodle")
        price = 11.25
        itemQuantity = float(input("\nPlease enter how many: "))
        subTotal += (price * itemQuantity)
    userContinueOrder = input("Would you like another item? (Y/N)\n").lower()
    while userContinueOrder != 'Y'.lower() and userContinueOrder != "N".lower():
        print("Invalid input, please try again.\n")
        userContinueOrder = input("Would you like another item? (Y/N)\n").lower()
    if userContinueOrder == "y":
        menu()
        itemNum = float(input("\nEnter the item number you want (1-6): "))
    else:
        break
else:
    print("\nIncorrect Input, please try again.\n")

itemTotal = subTotal
age = input("Are 65 years of age or above? (Y/N)").lower()

while age != "Y".lower() and age != "N".lower():
    print("\nIncorrect input, please try again.\n")
    age = input("Are 65 years of age or above? (Y/N)").lower()
else:
    if age == 'y':
        print("\nYou are eligible for the senior discount!\n")
        discountTotal = 0.1 * subTotal
        subTotal *= 0.9
    elif age == "n":
        print("\nYou aren't eligible for the senior discount.\n")
        discountTotal = 0

tax = round((subTotal * .06), 2)
total = round((subTotal * 1.06), 2)
gCard = input("Do you have a gift card? (Y/N)\n").lower()
gCardApplied = 0

while gCard == 'Y'.lower() or gCard == 'N'.lower():
    if gCard == "y":
        gCard_amount = float(input("\nWhat is the current gift card balance? \n"))
        while 1 > gCard_amount > 1000:
            print("Invalid gift card amount, please try again.")
            gCard_amount = float(input("\nWhat is the current gift card balance? \n"))
        if 0 <= gCard_amount <= total:
            print("Gift card Applied\n")
            gCardApplied = gCard_amount
            total -= gCard_amount
            break
        elif gCard_amount >= total:
            gCard_amount -= total
            gCardApplied = total
            total = 0
            print(f"Remaining gift card balance: $ {gCard_amount:.2f}")
            break
        else:
            print("\nInvalid amount, please try again.\n ")
            gCard_amount = float(input("\nWhat is the current gift card balance? \n"))
    elif gCard == "n":
        gCard_amount = 0
        print("\nNo gift card was applied.\n")
        break
    else:
        print("Incorrect input, please try again.")
        gCard = input("\nDo you have a gift card? (Y/N)\n").lower()

print("\n\t\tBill Information")
print("----------------------------------")
print(f"Total of all items:\t\t\t${itemTotal:.2f}")
print(f"Total senior discounts:\t\t-${discountTotal:.2f}")
print(f"Taxes:\t\t\t\t\t\t+${tax:.2f}")
print(f"Subtotal:\t\t\t\t\t ${itemTotal+tax:.2f}")
print(f"Gift card amount applied:\t-${gCardApplied:.2f}")
print(f"\t\t\t\t\t\t\t-------")
print(f"\t\t\t\tBill:\t\t${total:.2f}")

file1 = open("restaurantReceipt.txt", "w")
file1.write("\n\t\tBill Information\n")
file1.write("----------------------------------\n")
file1.write(f"Total of all items:\t\t\t${itemTotal:.2f}\n")
file1.write(f"Total senior discounts:\t\t-${discountTotal:.2f}\n")
file1.write(f"Taxes:\t\t\t\t\t\t+${tax:.2f}\n")
file1.write(f"Subtotal:\t\t\t\t\t ${itemTotal+tax:.2f}\n")
file1.write(f"Gift card amount applied:\t-${gCardApplied:.2f}\n")
file1.write(f"\t\t\t\t\t\t\t------\n")
file1.write(f"\t\t\t\tBill:\t\t${total:.2f}\n")
file1.close()