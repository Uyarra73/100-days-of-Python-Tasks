from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MIN_VERTICAL_DISTANCE = 50


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        y_position = random.randint(-250, 250)
        while self.is_valid_position(y_position):
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280, y_position)
            self.cars.append(new_car)

    def is_valid_position(self, y_position):
        for car in self.cars:
            if abs(car.ycor() - y_position) < MIN_VERTICAL_DISTANCE:
                return False
        return True

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
