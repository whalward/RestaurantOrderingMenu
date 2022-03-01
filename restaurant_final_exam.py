'''
Waseem Alward
Cis - 125 - 72
restaurant_final_exam.py
'''

def menu ():
    print("\tRestaurant Register\t\t\n")
    print("Dish No.\tDish Name\t\tPrice")
    print("---------\t---------\t\t------")
    print(f"1\t\tGang Gai\t\t$10")
    print(f"2\t\tPad Thai\t\t$8.75")
    print(f"3\t\tPad Cashew\t\t$9.50")
    print(f"4\t\tPad Prik \t\t$10.25")
    print(f"5\t\tPeanut Curry\t\t$9.50")
    print(f"6\t\tCurry Noodle \t\t$11.25")

subTotal = 0

while True:
    menu()
    A= float(input("\nEnter the item number you want (1-6): "))
    P = 0
    total = 0
    
    if A == 1:
        print("Gang Gai")
        P = 10
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
    elif A == 2:
        print("Pad Thai")
        P = 8.75
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
    elif A == 3:
        print("Pad Cashew")
        P = 9.50
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
        break
    elif A == 4:
        print("Pad Prik")
        P = 10.25
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
    elif A == 5:
        print("Peanut Curry")
        P = 9.50
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
    elif A == 6:
        print("Curry Noodle")
        P = 11.25
        B = float(input("\nPlease enter how many: "))
        subTotal += (P*B)
        order = input("Would you like another item? (Y/N)").lower()
        if order == "n":
            break
    else:
        print("\nIncorrect Input, please try again.\n")

itemTotal = subTotal

while True:
    age = input("Are you the 65 y/o or above? (Y/N)").lower()
    if age == 'y':
        print("You chose yes")
        discountTotal = 0.1 * subTotal
        subTotal *= 0.9
        break
    elif age == "n":
        print("You chose No.")
        discountTotal = 0
        break
    else:
        print("Incorrect input, please try again.")
        
total = round((subTotal * 1.06),2)

tax = round((subTotal * .06),2)

gCard = input("Do you have a giftcard? (Y/N)").lower()

while True:
    if gCard == "y":
        while True:
            gCard_amount = float(input("How much money would you like to apply from the card? "))
            if gCard_amount >= 0 and gCard_amount <= subTotal:
                print("Giftcard Applied")
                total -= gCard_amount
                break
            else:
                print("Invalid amount, please try again. ")
        break            
    elif gCard == "n":
        gCard_amount = 0
        break
    else:
        print("Incorrect input, please try again.")
        
print("\n\tBill Information")
print("----------------------------")
print(f"Total of all items:\t\t${itemTotal}")
print(f"Total senior discounts:\t\t-${discountTotal}")
print(f"Taxes:\t\t\t\t+${tax}")
print(f"Gift card amount applied:\t-${gCard_amount}")
print(f"\t\t\t\t-----")
print(f"\t\tBill:\t\t${round(total,2)}")






