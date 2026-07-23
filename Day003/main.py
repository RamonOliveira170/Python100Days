print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride")

    age = int(input("What is your age?: "))
    bill = 0

    if age <= 12:
        print("The ticket will cost $5")
        bill += 5
    elif age <= 18:
        print("The ticket will cost $7")
        bill += 7
    elif age >= 45 and age <= 55:
        print("The tickte will be free!")
        bill += 0
    else:
        print("The ticket will cost $12")
        bill += 12

    want_photos = input("Do you want to have a photo take? 'Y' (3$)/ 'N': ").capitalize()

    if want_photos == "Y":
        bill += 3

    print(f"The total bill will be ${bill}")

else:
    print("You cannot ride")

number_to_check = int(input("What is the number you want to check?: "))

if number_to_check % 2 == 0:
    print(f"{number_to_check} is even!")
elif number_to_check % 2 != 0:
    print(f"{number_to_check} is odd!")