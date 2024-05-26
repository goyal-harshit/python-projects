import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    scoreboard.score_update()
    screen.update()
    time.sleep(0.1)
    player.move()
    if player.reset_position():
        scoreboard.score_increase()


screen.exitonclick()
print(f"Your final score is: {scoreboard.print_score()}")
