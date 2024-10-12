import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x= -200
y= -150

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    turtles.append(new_turtle)
    y += 60
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You win! The winner is {turtle.pencolor()} turtle")
            else:
                print(f"You loose! The winner is {turtle.pencolor()} turtle")

screen.listen()
screen.exitonclick()