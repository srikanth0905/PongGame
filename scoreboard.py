from turtle import Turtle

FONT = ("Courier", 40, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-90, 240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(90, 240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.update_scoreboard()
