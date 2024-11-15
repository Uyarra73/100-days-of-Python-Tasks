from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = ("Ariel", 40, "italic")
WORD = ("Ariel", 60, "bold")

random_entry = {}
random_french_word = ""

try:
    word_list = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pd.read_csv("data/french_words.csv")

words_dictionary = word_list.to_dict(orient="records")

# --- SHOW WORD FUNCTION --- #
def show_word():
    global random_entry, flip_timer, random_french_word
    if words_dictionary:
        window.after_cancel(flip_timer)
        random_entry = random.choice(words_dictionary)
        random_french_word = random_entry["French"]
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=random_french_word, fill="black")
        canvas.itemconfig(create_image, image=card_front)

        # --- APPLY IMAGE CHANGE --- #
        flip_timer = window.after(3000, change_image)
    else:
        canvas.itemconfig(title, text="Congratulations!", fill="black")
        canvas.itemconfig(word, text="You learned all the words", fill="black")
        canvas.itemconfig(create_image, image=card_front)

# --- CHANGE IMAGE FUNCTION --- #
def change_image():
    english_word = random_entry["English"]
    canvas.itemconfig(create_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")

# --- COMBINED FUNCTION TO SHOW A NEW WORD AND SAVE THE PREVIOUS ONE --- #
def show_and_save():
    if random_entry in words_dictionary:
        words_dictionary.remove(random_entry)
        new_data = pd.DataFrame(words_dictionary)
        new_data.to_csv("data/words_to_learn.csv", index=False)
    show_word()


# ---- SET UP WINDOW ---- #
window = Tk()
window.title("FR - EN FLASHCARDS")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, change_image)

# --- SET UP CANVAS --- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front =PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
create_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=LANGUAGE)
word = canvas.create_text(400, 263, text="", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)

# --- BUTTONS --- #
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=show_and_save)
check_button.grid(column=1, row=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=show_word)
cross_button.grid(column=0, row=1)

show_word()



window.mainloop()
