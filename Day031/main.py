import tkinter
import random
import pandas

TIMER = 3000
BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}

try:
    words_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/Spanish-words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = words_data.to_dict(orient="records")

current_card = {}


def is_known():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    flashcard_canvas.itemconfig(card_background, image=flashcard_front_image)
    current_card = random.choice(words_to_learn)
    flashcard_canvas.itemconfig(card_title, text="Spanish", fill="black")
    flashcard_canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    flip_timer = window.after(TIMER, flip_card)


def flip_card():
    flashcard_canvas.itemconfig(card_background, image=flashcard_back_image)
    flashcard_canvas.itemconfig(card_title, text="English", fill="white")
    flashcard_canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIMER, flip_card)

flashcard_front_image = tkinter.PhotoImage(file="./images/card_front.png")
flashcard_back_image = tkinter.PhotoImage(file="./images/card_back.png")
flashcard_canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
card_background = flashcard_canvas.create_image(400, 263, image=flashcard_front_image)
flashcard_canvas.config(bg=BACKGROUND_COLOR)
card_title = flashcard_canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = flashcard_canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
flashcard_canvas.grid(column=0, row=0, columnspan=2)

yes_button_image =tkinter.PhotoImage(file="./images/right.png")
yes_button = tkinter.Button(image=yes_button_image, highlightthickness=0, command=is_known)
yes_button.grid(column=0, row=1)

no_button_image = tkinter.PhotoImage(file="./images/wrong.png")
no_button = tkinter.Button(image=no_button_image, highlightthickness=0, command=next_card)
no_button.grid(column=1, row=1)

next_card()
window.mainloop()
