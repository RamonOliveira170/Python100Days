print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n''')

print("Welcome to the Treasure island.\nYour mission is to find the treasure.\n")

choice = input("You're at a cross road. Where do you want to go?\nType \"Left\" or \"Right\": ").capitalize()

if choice == "Right":
    print("You fell into a Hole, Game over.")

elif choice == "Left":
    print("\nYou come to a lake. There is an island in the middle of the lake.")
    choice = input("Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across: ").capitalize()

    if choice == "Swim":
        print("You got attacked by an angry trout, Game over")

    elif choice == "Wait":
            print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
            choice = input("One \"Red\", one \"Yellow\", and one \"Blue\". Which colour do you choose?: ").capitalize()

            if choice == "Yellow":
                print("\nCongratulations! You Won!")

            elif choice == "Red":
                print("\nIt's a room full of fire, Game over ")

            elif choice == "Blue":
                print("\nYou've entered the room of the beasts, Game over")

            else:
                print("\nYou choose a room that doesn't exist, Game over.")
