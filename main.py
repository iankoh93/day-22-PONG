from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800
STARTING_X_POSITION = 350
SCORE_TO_WIN = 3
starting_speed = 0.05

screen = Screen()

game_is_on = True

screen.bgcolor("black")
screen.title("Pong! The Video Game")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.listen()
l_paddle = Paddle(-STARTING_X_POSITION)
r_paddle = Paddle(STARTING_X_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=l_paddle.down, key="s")
screen.onkey(fun=l_paddle.up, key="w")

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(starting_speed)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.hit_wall()

    if ball.distance(r_paddle) < 60 or ball.distance(l_paddle) < 60:
        if ball.xcor() > 320 or ball.xcor() < -320:
            ball.hit_paddle()
            ball.move_speed += 1

    # Detect when right paddle misses the ball
    if ball.xcor() > WIDTH / 2:
        scoreboard.l_point()
        ball.reset_position()

    # Detect when left paddle misses the ball
    if ball.xcor() < -WIDTH / 2:
        scoreboard.r_point()
        ball.reset_position()

    # Check if either player has won. (Scored 5 points)
    if scoreboard.l_score == SCORE_TO_WIN:
        game_is_on = False
        scoreboard.end_game("Left Player")
    elif scoreboard.r_score == SCORE_TO_WIN:
        game_is_on = False
        scoreboard.end_game("Right Player")


screen.exitonclick()
