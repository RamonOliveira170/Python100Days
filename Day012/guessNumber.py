import random
import art

EASY_LEVEL_TURNS = 8
HARD_LEVEL_TURNS = 5

def check_numbers(random_number, user_lives):
    while user_lives > 0:
        print(f"You have {user_lives} tries remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess != random_number:
            user_lives -= 1
            if user_guess > random_number:
                print("Too high")
            else:
                print("Too low")
            if user_lives == 0:
                print(f"Game over! The number was \"{random_number}\"")

        elif user_guess == random_number:
            print(f"You got it! the number was {random_number}")
            print(f"You still had {user_lives} tries!")
            user_lives = 0


def number_guessing(difficulty="easy"):
    random_number = random.randint(1, 100)
    user_lives = EASY_LEVEL_TURNS
    if difficulty == "easy":
        check_numbers(random_number, user_lives)

    if difficulty == "hard":
        user_lives = HARD_LEVEL_TURNS
        check_numbers(random_number, user_lives)

    if input("Do you want to play again? Type \"yes\" or \"no\": ").lower() == "yes":
        print("\n" * 20)
        number_guess_game()
    else:
        print("Closing...")


def number_guess_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\": ").lower().strip()

    if difficulty == "easy":
        number_guessing("easy")
    elif difficulty == "hard":
        number_guessing("hard")
    else:
        print("Easy mode by default")
        number_guessing()

number_guess_game()
