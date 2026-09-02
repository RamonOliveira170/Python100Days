import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, my_timer
    window.after_cancel(my_timer)
    reps = 0
    check_mark.config(text="")
    title_label.config(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 50))
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    #If it's the 8th repetition
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED, background=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    #If it's the 2/4/6th repetition
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK, background=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    #If it's the 1/3/5/7th repetition
    else:
        title_label.config(text="Work", fg=GREEN, background=YELLOW)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import math
def count_down(count):
    global reps, my_timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = tkinter.Label()
check_mark.grid(column=1, row=3)

window.mainloop()
