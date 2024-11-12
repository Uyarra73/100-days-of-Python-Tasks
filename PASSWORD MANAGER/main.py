import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    username = user_input.get()
    password_entry = pass_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password_entry,
        }
    }

    if website and username and password_entry:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Cargar datos existentes
        except FileNotFoundError:
            data = {}  # Crear un diccionario vacío si el archivo no existe

        data.update(new_data)  # Actualizar datos con los nuevos

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)  # Guardar los datos actualizados

        web_input.delete(0, END)
        pass_entry.delete(0, END)

        messagebox.showinfo("Success!", "Your data has been saved!")
    else:
        messagebox.showwarning("Warning", "You must fill all the fields")

# ------------ FIND PASSWORD ---------- #
def find_password():
    website_name = web_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "This file doesn't exist")
    else:
        if website_name in data:
            web_user = data[website_name]["email"]
            web_password = data[website_name]["password"]
            messagebox.showinfo(website_name, f"Email: {web_user} \nPassword: {web_password}")
        else:
            messagebox.showwarning("Warning",f"The website {website_name} doesn't exist in this file")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

# Website input
web_input = Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

# Search button
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)

# User label
user = Label(text="Email/Username:")
user.grid(column=0, row=2)

# User input
user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "alberto@email.com")

# Password label
password = Label(text="Password:")
password.grid(column=0, row=3)

# Password entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Generate password button
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)

# Add button
add = Button(text="Add", width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()

