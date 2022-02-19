import time
import turtle
import random


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(100,290), random.randint(-230, 230))

    def move(self):
        self.backward(20)
