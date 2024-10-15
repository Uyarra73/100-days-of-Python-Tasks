from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.current_heading = 0
        self.head = self.squares[0]
        self.tail = self.squares[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend_snake(self):
        self.add_square(self.tail.position())


    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(20)

    def set_heading(self, heading):
        self.current_heading = heading

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def wall(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x >= 290 or x <= -290 or y >= 290 or y <= -290:
            return False
        return True



