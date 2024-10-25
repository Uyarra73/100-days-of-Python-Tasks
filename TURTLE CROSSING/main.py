import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TOP_POSITION = (0, 280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        car_manager.generate_car()

    car_manager.move_cars()

    for car in car_manager.cars:
        if car.xcor() < -320:
            car_manager.cars.remove(car)

        if  car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()         
            
    if player.distance(TOP_POSITION) < 10:
        player.start_position()
        car_manager.speed_up()
        scoreboard.increase_score()



screen.exitonclick()