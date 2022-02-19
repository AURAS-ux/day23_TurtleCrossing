import turtle


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.color("black")
        self.setheading(90)
        
    def move(self):
        self.forward(20)
