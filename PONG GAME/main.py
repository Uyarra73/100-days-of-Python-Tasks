from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ALBI'S PONG GAME")
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.restart_game()
        scoreboard.increase_left_score()
    elif ball.xcor() < -400:
        ball.restart_game()
        scoreboard.increase_right_score()



screen.exitonclick()