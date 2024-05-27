from turtle import Turtle


class Scoreboard:
	def __init__(self):
		self.score_board = Turtle()
		self.score_board.color("white")
		self.score_board.penup()
		self.score_board.hideturtle()
		self.score_board.goto(0, 275)
		self.score = 0
		# Read the high score from the file
		try:
			with open("high_score.txt", "r") as file:
				self.high_score = int(file.read().strip()[-1])
		except (FileNotFoundError, ValueError):
			self.high_score = 0

	def score_increase(self):
		self.score = self.score + 1
		self.score_board.clear()
		return self.score

	def print_score(self):
		return self.score

	def print_high_score(self):
		return self.high_score

	def score_update(self):
		self.score_board.clear()
		self.score_board.goto(0, 275)
		self.score_board.write(f"Score: {self.score}    High Score = {self.high_score}", move=False, align="center", font=("Courier", 15, "normal"))

	def game_over(self):
		self.score_board.clear()
		self.score_board.goto(0, 25)
		self.score_board.write(f"GAME ENDS - High Score: {self.high_score}", move=False, align="center", font=("Courier", 15, "normal"))

	def reset_score_board(self):
		if self.score > self.high_score:
			self.high_score = self.score
			try:
				with open("high_score.txt", "w") as file:
					file.write(f"high_score = {str(self.high_score)}")
			except Exception as e:
				print(f"Error updating high score: {e}")
		self.score = 0


