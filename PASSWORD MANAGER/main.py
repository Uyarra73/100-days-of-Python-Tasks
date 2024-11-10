from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # new_list = [expression for item in iterable if condition]
    password_list += [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    pass_entry.delete(0, END)
    pass_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

    #print(f"Your password is: {generated_password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    username = user_input.get()
    password_entry = pass_entry.get()

    if website and username and password_entry:
        is_ok = messagebox.askokcancel(title=website, message=f"Do you really want to save these data? \nUsername: {username}\nPassword: {password_entry}\n")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"Website: {website} | Username: {username} | Password: {password_entry} \n")

            web_input.delete(0, END)
            user_input.delete(0, END)
            pass_entry.delete(0, END)

            messagebox.showinfo("Success! Your data have been saved!")
    else:
        messagebox.showwarning("You must fill all the fields")

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

#Website input
web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

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
add = Button(text="Add", width=36,  command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()