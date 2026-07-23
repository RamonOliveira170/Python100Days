print("Welcome to the Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L?: ").capitalize()
pepperoni = input("Do you want pepperoni on your pizza? 'Y' or 'N': ").capitalize()
extra_cheese = input("Do you want extra cheese?: 'Y' or 'N': ").capitalize()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 4

print(f"Your total bill will be ${bill}.")
