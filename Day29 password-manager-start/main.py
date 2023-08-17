from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
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
    
    if len(website) == 0 or len(email) == 0 or len(pass_w) == 0:
        messagebox.showinfo(title = "Oops", message = "Please make sure none of the fields are empty")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(website,f"These are the details you entered\n Email: {email}\n Password: {pass_w}\n Is it Ok to save?")
    
    if is_ok:
        web_entry.delete(0,END)
        pass_entry.delete(0,END)
        with open ("User_details", mode = "a") as file:
            file.write(f"{website}|{email}|{pass_w}\n")
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)



canvas = Canvas(width = 200, height = 200)
padlock= PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = padlock)
canvas.grid(row = 0, column = 1)



# website Label
website_label = Label(text = "Website")
website_label.grid(row = 1, column = 0)
# Email Label
email_label = Label(text = "Email/Username")
email_label.grid(row = 2, column = 0)
# Password Label
password_label = Label(text = "Password")
password_label.grid(row = 3, column = 0)




# Website_entry
web_entry = Entry(width = 35)
web_entry.grid(row = 1 , column = 1, columnspan =2)
web_entry.focus()
# Email_entry
email_entry = Entry(width = 35)
email_entry.grid(row = 2 , column = 1, columnspan =2)
email_entry.insert(0, "angella@gmail.com", )
# Website_entry
pass_entry = Entry(width = 21)
pass_entry.grid(row = 3 , column = 1)



# generate Password Button
gen_password = Button(text = "Generate Password", command = generate_password)
gen_password.grid(row = 3, column =2)
# Add Button
add_butt = Button(text = "Add", width = 36, command = add_details)
add_butt.grid(row = 4, column =1, columnspan = 2)


window.mainloop()