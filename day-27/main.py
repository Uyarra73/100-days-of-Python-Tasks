from tkinter import *

def button_clicked():
    global my_label
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Etiqueta", font=("Courier", 16, "bold"))
# Shows the label inside the window
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

# New button
new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=30)
print(input.get())
# input.pack()
input.grid(column=3, row=2)









# Always at the end of the program
window.mainloop()