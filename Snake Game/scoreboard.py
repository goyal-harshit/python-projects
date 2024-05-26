from turtle import Turtle


class Scoreboard:
	def __init__(self):
		self.score_board = Turtle()
		self.score_board.color("white")
		self.score_board.penup()
		self.score_board.hideturtle()
		self.score_board.goto(0, 275)
		self.score = 0

	def score_increase(self):
		self.score = self.score + 1
		self.score_board.clear()
		return self.score

	def print_score(self):
		return self.score

	def score_update(self):
		self.score_board.clear()
		self.score_board.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 15, "normal"))

	def game_over(self):
		self.score_board.clear()
		self.score_board.goto(0, 0)
		self.score_board.write(f"GAME OVER - Final Score: {self.score}", move=False, align="center", font=("Courier", 15, "normal"))
