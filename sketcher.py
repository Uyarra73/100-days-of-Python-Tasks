from turtle import Turtle, Screen

albi = Turtle()
screen = Screen()

def move_forward():
    albi.forward(10)

def move_backward():
    albi.backward(10)

def rotate_right():
    albi.right(10)

def rotate_left():
    albi.left(10)

def restart():
    albi.clear()
    albi.penup()
    albi.home()
    albi.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")
screen.onkey(restart, "c")
screen.exitonclick()