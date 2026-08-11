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
    """returns a random account from data"""
    return data[random.randint(0, len(data) - 1)]
    #return random.choice(data)


def compare(option_A, option_B):
    """compare 2 accounts and return the position B account if user got it right,
     if wrong, return 0 to close the game"""
    try:
        user_option = input("Who has more followers? Type \"A\" or \"B\": ").lower().strip()
    except ValueError or None:
        print("Invalid input, Type only \"A\" or \"B\"")

    if (user_option == "a" and option_A["follower_count"] > option_B["follower_count"]) \
            or (user_option == "b" and option_B["follower_count"] > option_A["follower_count"]):
        print("You're right!\n")
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
    while option_A == option_B:
        option_B = new_term()

    print(f"Compare A: {option_A["name"]}. a {option_A["description"]}, from {option_A["country"]}")
    print(art.vs)
    print(f"Compare B: {option_B["name"]}. a {option_B["description"]}, from {option_B["country"]}")

    new_option = compare(option_A, option_B)

    if new_option == 0:
        print("Game over!")
        print(f"Score: {score}")
        running = False

    else:
        score += 1
        option_A = new_option
