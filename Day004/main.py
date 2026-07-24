import random
import my_module

random_integer = random.randint(1 ,10)

print(random_integer)
print(my_module.my_favourite_number)

random_number_0_to_1 = random.random() * 10 #0 inclusive but 1 not included

print(random_number_0_to_1)

random_float = random.uniform(1, 10)

print(random_float)

choice = input("\nChoose 'Head' or 'Tails': ").capitalize()
coin = random.randint(0, 1)

if coin == 1 and (choice == "Tails" or choice == "Heads"):
    coin = "Heads"
    if coin == choice:
        print(f"{coin}. You win")
    else:
        print(f"{coin}. You Lose")

elif coin == 0 and (choice == "Tails" or choice == "Heads"):
    coin = "Tails"
    if coin == choice:
        print(f"{coin}. You win")
    else:
        print(f"{coin}. You Lose")

else:
    print("Wrong choice")