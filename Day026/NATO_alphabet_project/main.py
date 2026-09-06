import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in alphabet.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper().replace(" ", "")
    try:
        output_list = [dictionary[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
