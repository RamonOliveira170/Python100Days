import tkinter
import random
import json
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"

words_data = pandas.read_csv("./data/Spanish-words.csv")
words_to_learn = words_data.to_dict(orient="records")


def next_card():
    current_card = random.choice(words_to_learn)
    flashcard_canvas.itemconfig(card_title, text="Spanish")
    flashcard_canvas.itemconfig(card_word, text=current_card["Spanish"])


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flashcard_front_image = tkinter.PhotoImage(file="./images/card_front.png")
flashcard_canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
flashcard_canvas.create_image(400, 263, image=flashcard_front_image)
flashcard_canvas.config(bg=BACKGROUND_COLOR)
card_title = flashcard_canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = flashcard_canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
flashcard_canvas.grid(column=0, row=0, columnspan=2)

yes_button_image =tkinter.PhotoImage(file="./images/right.png")
yes_button = tkinter.Button(image=yes_button_image, highlightthickness=0, command=next_card)
yes_button.grid(column=0, row=1)

no_button_image = tkinter.PhotoImage(file="./images/wrong.png")
no_button = tkinter.Button(image=no_button_image, highlightthickness=0)
no_button.grid(column=1, row=1)

next_card()
window.mainloop()
