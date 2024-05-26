from turtle import Turtle
line_length = 600
dash_length = 25
gap_length = 20
dash_count = int(line_length / (dash_length + gap_length))


class Scoreboard:
    def __init__(self):
        self.score_board = Turtle()
        self.score_board.hideturtle()
        self.score_board.color("white")
        self.score_board.penup()
        self.score_board.speed("fastest")
        self.score_board.setheading(90)
        self.score_board.goto(0, -300)
        self.score_board.pendown()
        self.score_board.pensize(7)

        # Draw the dashed line
        for _ in range(dash_count):
            self.score_board.pendown()
            self.score_board.forward(dash_length)
            self.score_board.penup()
            self.score_board.forward(gap_length)

        self.score_board.penup()
        self.score_left = 0
        self.score_right = 0

        # Draw the scores
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear previous scores
        self.score_board.clear()

        # Draw the dashed line again
        self.score_board.goto(0, -300)
        self.score_board.setheading(90)
        for _ in range(dash_count + 1):
            self.score_board.pendown()
            self.score_board.forward(dash_length)
            self.score_board.penup()
            self.score_board.forward(gap_length)

        # Display the scores
        self.score_board.goto(-100, 260)
        self.score_board.write(f"{self.score_left}", align="center", font=("Arial", 24, "normal"))

        self.score_board.goto(100, 260)
        self.score_board.write(f"{self.score_right}", align="center", font=("Arial", 24, "normal"))

    def increase_left_score(self):
        self.score_left += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.score_right += 1
        self.update_scoreboard()

    def game_over(self):
        self.score_board.goto(0, 0)
        self.score_board.clear()
        self.score_board.write(f"GAME OVER : Final Score {self.score_left}  :  {self.score_right}", align="center", font=("Arial", 24, "normal"))

