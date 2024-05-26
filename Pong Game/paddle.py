from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, x_cor, y_cor):
		super().__init__()
		self.shape("square")
		self.penup()
		self.speed("fastest")
		self.setheading(90)
		self.color("white")
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.goto(x_cor, y_cor)

	def up(self):
		if self.ycor() < 250:
			self.forward(20)

	def down(self):
		if self.ycor() > -250:
			self.forward(-20)

	def reset_position(self, x_cor, y_cor):
		self.goto(x_cor, y_cor)
