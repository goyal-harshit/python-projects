from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = True
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(450, 0)
l_paddle = Paddle(-450, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

time_sleep = 0.1
while game_is_on:
	time.sleep(time_sleep)
	screen.update()
	ball.move()
	scoreboard.update_scoreboard()

	# detect collision with right wall
	if ball.xcor() > 480:
		scoreboard.increase_left_score()
		time.sleep(0.5)
		ball.reset_position()
		time_sleep = 0.1

	# detect collision with left wall
	if ball.xcor() < -480:
		scoreboard.increase_right_score()
		time.sleep(0.5)
		ball.reset_position()
		time_sleep = 0.1

	# detect collision with top/bottom wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_wall()

	# detect collision with right paddle
	if ball.distance(r_paddle) < 50 and 420 < ball.xcor() < 440:
		ball.bounce_paddle()
		time_sleep *= 0.9

	# detect collision with right paddle
	if ball.distance(l_paddle) < 50 and -420 > ball.xcor() > -440:
		ball.bounce_paddle()
		time_sleep *= 0.9

	if scoreboard.score_right == 10 or scoreboard.score_left == 10:
		scoreboard.game_over()
		game_is_on = False

screen.exitonclick()
