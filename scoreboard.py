import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.color("black")
        self.write(arg=f"Level:{1}", font=("Arail", 20, "bold"))

    def writeLevel(self, level):
        self.clear()
        self.write(arg=f"Level:{level}", font=("Arail", 20, "bold"))
