from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()
     
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)