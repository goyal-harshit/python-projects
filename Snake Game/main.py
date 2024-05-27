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


def end_game():
    snake.erase_snake()
    scoreboard.game_over()
    screen.update()
    global game_is_on
    game_is_on = False


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# if we want to end the game
screen.onkey(end_game, "Escape")

game_is_on = True
while game_is_on:
    scoreboard.score_update()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.does_hit_walls():
        scoreboard.reset_score_board()
        time.sleep(0.5)
        snake.reset_snake()
    # detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()
    # detect collision with self
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            scoreboard.reset_score_board()
            time.sleep(0.5)
            snake.reset_snake()

screen.exitonclick()
print(f"High score is: {scoreboard.print_high_score()}")
