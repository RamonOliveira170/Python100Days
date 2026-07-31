import random

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["orange", "strawberry", "grape", "apple", "tomato", "potato", "starfruit", "watermelon"]
chosen_word = random.choice(word_list)
user_lives = 6
correct_letters = []
placeholder = ""
used_letters = []
tries = 0
game_over = False

for position in range(len(chosen_word)):
    placeholder += "_"

print(logo)
print(stages[6])

while not game_over:
    display = ""
    guess = input("Guess a letter: ").lower()[0]

    if guess in correct_letters:
        print(f"You've already guessed \"{guess}\"")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

            if letter not in used_letters:
                tries += 1
                used_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        if guess not in used_letters:
            tries += 1
            used_letters.append(guess)
            user_lives -= 1

    print(stages[user_lives])

    print(display)

    print(f"Used letters: {used_letters}")

    if user_lives < 1:
        print("-" * 80)
        print(f"You lose, the word was \"{chosen_word}\"!")
        game_over = True

    if "_" not in display:
        print("-" * 80)
        print("You win!!!")
        game_over = True

print(f"{tries} tries")
print("-"*80)
