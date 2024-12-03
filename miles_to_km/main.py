from tkinter import *


def miles_to_km():
    global input
    miles = float(input.get())
    km = miles * 1.609
    label3.config(text=str(km))

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20, bg="#33485c")

input = Entry(width=15)
input.insert(END, string="0")
input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()