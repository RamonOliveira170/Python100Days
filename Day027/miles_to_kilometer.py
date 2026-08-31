import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 150)
window.config(padx=30, pady=30)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 14))
is_equal_label.grid(column=0, row=2)

result_label = tkinter.Label(text="0", font=("Arial", 14))
result_label.grid(column=1, row=2)

kilometer_label = tkinter.Label(text="Km", font=("Arial", 14))
kilometer_label.grid(column=2, row=2)

def button_clicked():
    user_input = float(input.get())
    user_input *= 1.609
    result_label.config(text=round(user_input, 2))

my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=3)

window.mainloop()
