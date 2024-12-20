from turtle import Turtle
import time

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.ball_speed = 0.01


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def restart_game(self):
        print("You missed the ball")
        self.goto(0, 0)
        self.ball_speed = 0.01
        self.bounce_x()







