from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if not snake.wall():
        game_is_on = False
        score.game_over()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()