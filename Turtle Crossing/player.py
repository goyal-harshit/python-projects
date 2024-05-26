from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Turtle")
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
        return True


