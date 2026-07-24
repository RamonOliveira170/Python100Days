import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

options = ["Rock", "Paper", "Scissors"]

winning_list = [["Draw!", "You Lose!", "You Win!"], ["You Win!", "Draw!", "You Lose!"],
                ["You Lose!", "You Win!", "Draw!"]]

user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
computer_option = random.randint(0, 2)

if not str(user).isdigit() or (user < "0" or user > "2"):
    print("Invalid choice! You Lose!")
else:
    print(f"You choose: \n{game_images[int(user)]}")
    print(f"Computer choose: \n{game_images[computer_option]}")
    print(winning_list[int(user)][computer_option])

'''if user_option == "Rock":

    if computer_option == "Rock":
        print("It's a Draw!")
    elif computer_option == "Paper":
        print("You Lose!")
    elif computer_option == "Scissors":
        print("You Win!")

elif user_option == "Paper":

    if computer_option == "Rock":
        print("You Win!")
    elif computer_option == "Paper":
        print("It's a Draw!")
    elif computer_option == "Scissors":
        print("You Lose!")

elif user_option == "Scissors":

    if computer_option == "Rock":
        print("You Lose!")
    elif computer_option == "Paper":
        print("You Win!")
    elif computer_option == "Scissors":
        print("It's a Draw!")

else:
    print("Invalid choice!")'''