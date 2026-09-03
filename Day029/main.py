import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #website = website_input.get()
    #email = email_input.get()
    #password = password_input.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
        # clear inputs
        website_input.delete(0, 999)
        password_input.delete(0, 999)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
canvas_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = tkinter.Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "UserEmail@email.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry(width=34)
password_input.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password")
password_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=58, command=save)
add_button.grid(columns=1, row=4, columnspan=3)


window.mainloop()