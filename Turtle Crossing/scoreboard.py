from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score_board = Turtle()
        self.score_board.color("white")
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.goto(-250, 275)
        self.level = 0

    def score_increase(self):
        self.level = self.level + 1

    def print_score(self):
        return self.level

    def score_update(self):
        self.score_board.clear()
        self.score_board.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.score_board.clear()
        self.score_board.goto(0, 0)
        self.score_board.write(f"GAME OVER - Final Score: {self.level}", move=False, align="center", font=FONT)
