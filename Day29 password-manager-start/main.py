from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lett = [choice(letters) for nr in range (randint(8, 10)) ]
    password_symb = [choice(symbols) for nr in range (randint(2, 4)) ]
    password_num = [choice(numbers) for nr in range (randint(2, 4)) ]

    password_list = password_lett + password_symb + password_num
    shuffle(password_list)

    password ="".join(password_list)
    pass_entry.delete(0,END)
    pass_entry.insert(0, f"{password}", )
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = web_entry.get()
    email = email_entry.get()
    pass_w = pass_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": pass_w
        }
    }
    is_ok = True

    if len(website) == 0 or len(email) == 0 or len(pass_w) == 0:
        messagebox.showinfo(title = "Oops", message = "Please make sure none of the fields are empty")
        is_ok = False
    if is_ok:
        try:
            with open ("Day29 password-manager-start\data.json", mode = "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        else:
            pass
        finally:
            with open ("Day29 password-manager-start\data.json", mode = "w") as data_file:
                 json.dump(data, data_file, indent = 4)
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------------- SEARCH FOR DETAILS ------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("Day29 password-manager-start\data.json", mode = "r") as data_file:
            if len(website) == 0:
                messagebox.showinfo(title = "Oops", message = "Please make sure the field is not empty")
                return
            data_dict = json.load(data_file)           
    except:
        messagebox.showinfo(title = "Warning", message = "This file is empty")
    else:
        if website in data_dict:
            show_password = data_dict[website]["password"]
            show_email = data_dict[website]["email"]
            messagebox.showinfo(website,f"Email: {show_email}\nPassword: {show_password}")
        else:
            messagebox.showinfo(title = "Warning", message = "No details associated with this website")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)


canvas = Canvas(width = 200, height = 200)
padlock= PhotoImage(file = "Day29 password-manager-start\logo.png")
canvas.create_image(100,100, image = padlock)
canvas.grid(row = 0, column = 1)


# website Label
website_label = Label(text = "Website")
website_label.grid(row = 1, column = 0, padx = 20, pady = 2)
# Email Label
email_label = Label(text = "Email/Username")
email_label.grid(row = 2, column = 0, padx = 20, pady = 2)
# Password Label
password_label = Label(text = "Password")
password_label.grid(row = 3, column = 0, padx = 20, pady =2)


# Website_entry
web_entry = Entry(width = 21)
web_entry.grid(padx = 10, row = 1 , column = 1)
web_entry.focus()
# Email_entry
email_entry = Entry(width = 35)
email_entry.grid(padx = 10, row = 2 , column = 1, columnspan =2)
email_entry.insert(0, "angella@gmail.com")
# Website_entry
pass_entry = Entry(width = 21)
pass_entry.grid(padx = 10, row = 3 , column = 1)


# generate Password Button
gen_password = Button(text = "Generate Password", command = generate_password, width = 15, highlightthickness = 0)
gen_password.grid(row = 3, column =2, padx = 5, pady = 5)
# Add Button
add_butt = Button(text = "Add", width = 36, command = add_details)
add_butt.grid(row = 4, column =1, columnspan = 2)
# Search Button
search_butt = Button(text = "Search", command = search, width = 15)
search_butt.grid(row = 1, column = 2, padx = 5, pady = 5)

window.mainloop()