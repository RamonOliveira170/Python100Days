import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_input.delete(0, 999)

    #nr_letters = random.randint(8, 10)
    #nr_symbols = random.randint(2, 4)
    #nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    #for char in password_list:
    #  password += char

    password_input.insert(0, password)
    pyperclip.copy(password)

def search_account():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data_accounts = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Alert", message="No Data file found.")
    else:
        try:
            if data_accounts[website]:
                messagebox.showinfo(title=website,
                                    message=f"Email: {data_accounts[website]["email"]}\n"
                                            f"Password: {data_accounts[website]["password"]}")
        except KeyError:
            messagebox.showinfo(title="Alert",
                                message=f"No details for {website} exists.!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Alert!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="User info", message=f"These are the details entered: \n"
                                                                  f"Email: {email}\n"
                                                                  f"Password: {password}\n"
                                                                  f"It is ok to save?")
        if is_ok:
            json_dictionary = {website: {"email": email,
                                         "password": password}}
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except(FileNotFoundError, json.decoder.JSONDecodeError):
                with open('data.json', 'w') as data_file:
                    json.dump(json_dictionary, data_file, indent=4)
            else:
                data.update(json_dictionary)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
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

website_input = tkinter.Entry(width=34)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")
website_input.focus()

search_button = tkinter.Button(text="Search", command=search_account)
search_button.grid(column=2, row=1, sticky="wens")

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "UserEmail@email.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry(width=34)
password_input.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=58, command=save_account)
add_button.grid(columns=1, row=4, columnspan=3)

window.mainloop()
