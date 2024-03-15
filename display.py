from turtle import Screen, Turtle


class Display:

    FONT = ("Courier", 15, "normal")

    def __init__(self):
        self.screen = Screen()
        self.screen_setup()
        self.screen.listen()

        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()

    def screen_setup(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Mamba Game")
        self.screen.tracer(0)

    def update_screen(self):
        self.screen.update()

    def on_key_pressed(self, snake):
        self.screen.onkeypress(lambda: snake.set_heading(90), "Up")
        self.screen.onkeypress(lambda: snake.set_heading(270), "Down")
        self.screen.onkeypress(lambda: snake.set_heading(180), "Left")
        self.screen.onkeypress(lambda: snake.set_heading(0), "Right")

    def game_over(self):
        self.game_over_turtle.color("white")
        self.game_over_turtle.write("GAME OVER!", align="center", font=self.FONT)

    def exit_on_click(self):
        self.screen.exitonclick()
