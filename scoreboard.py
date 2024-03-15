from turtle import Turtle


class Scoreboard(Turtle):

    FONT = ("Courier", 15, "normal")

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=self.FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
