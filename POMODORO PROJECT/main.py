from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    check.config(text="")
    canvas.itemconfig(timer_text, text="25:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global title_label
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break)
        title_label.config(text="Long Break!", fg=GREEN)
    elif reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work Time!", fg=RED)
    else:
        count_down(break_sec)
        title_label.config(text="Take a break!", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check

    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        check_mark = ""
        sets = math.floor(reps / 2)
        for _ in range(sets):
            check_mark += "✅"
        check.config(text=check_mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Title label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)
title_label.config(padx=5, pady=5, fg=GREEN)

# Start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2, sticky="e")
start.config(padx=5, pady=5)

# Reset button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2, sticky="w")
reset.config(padx=5, pady=5)

# Check mark
check = Label(bg=YELLOW, highlightthickness=0)
check.grid(column=1, row=3)
check.config(padx=5, pady=5, fg=GREEN)





window.mainloop()