from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", font=("Arial", 16, "bold"))
        self.score.config(fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(150, 125,
                                                   text="You will see the question here",
                                                   width=280,
                                                   font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.canvas_text, fill=THEME_COLOR)
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.canvas_text, text=f"The quiz is over.You got {self.quiz.score}/10", fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def answer_true(self):
        correct_choice = self.quiz.check_answer("True")
        self.give_feedback(correct_choice)

    def answer_false(self):
        correct_choice = self.quiz.check_answer("False")
        self.give_feedback(correct_choice)

    def give_feedback(self, choice):
        if choice:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.canvas_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.canvas_text, fill="white")

        self.window.after(1000, self.get_next_question)


