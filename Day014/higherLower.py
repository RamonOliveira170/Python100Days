import random
import art
from game_data import data

"""
name = data[random.randint(0, len(data) - 1)]["name"]
follower_count = data[random.randint(0, len(data) - 1)]["follower_count"]
description = data[random.randint(0, len(data) - 1)]["description"]
country = data[random.randint(0, len(data) - 1)]["country"]
"""


def new_term():
    return data[random.randint(0, len(data) - 1)]


def compare(option_A, option_B):
    try:
        user_option = input("Who has more followers? Type \"A\" or \"B\": ").lower().strip()
    except ValueError or None:
        print("Invalid input, Type only \"A\" or \"B\"")

    if user_option == "a" and option_A["follower_count"] > option_B["follower_count"]:
        print("You got it!")
        return option_A

    elif user_option == "b" and option_B["follower_count"] > option_A["follower_count"]:
        print("You got it!")
        return option_B

    else:
        print("Sorry you guessed it wrong")
        return 0

print(art.logo)
score = 0
option_A = new_term()
running = True

while running:
    option_B = new_term()

    print(f"Compare A: {option_A["name"]}.{option_A["follower_count"]} {option_A["description"]}, from {option_A["country"]}")
    print(art.vs)
    print(f"Compare B: {option_B["name"]}.{option_B["follower_count"]} {option_B["description"]}, from {option_B["country"]}")

    new_option = compare(option_A, option_B)

    if new_option == 0:
        print("Game over!")
        print(f"Score: {score}")
        running = False

    else:
        score += 1
        option_A = new_option
