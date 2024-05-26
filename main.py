from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    scoreboard.score_update()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.does_hit_walls():
        game_is_on = False
        scoreboard.game_over()
    # detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()
    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
print(f"Your final score is: {scoreboard.print_score()}")
