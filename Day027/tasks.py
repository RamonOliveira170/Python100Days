import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

my_label = tkinter.Label(text="A am a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New config")
my_label.config(padx=50, pady=50)


def button_clicked():
    print("I got clicked")
    #my_label["text"] = "Button got clicked!"
    my_label.config(text=input.get())

my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)
print(input.get())

window.mainloop()
