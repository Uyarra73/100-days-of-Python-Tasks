import turtle
from turtle import Turtle, Screen
import random

color_list= [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]

turtle.colormode(255)
albi = Turtle()
albi.hideturtle()
albi.penup()
albi.speed("fastest")

def random_color():
    color = random.choice(color_list)
    return color

x = -turtle.window_width() // 2 + 150
y = -turtle.window_height() // 2 + 100
albi.goto(x, y)

for _ in range(10):
    for _ in range(10):
        albi.dot(20, random_color())
        albi.forward(50)
        y += 5
    albi.goto(x, y)

screen = Screen()
screen.exitonclick()



