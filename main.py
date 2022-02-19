import random
import time
import turtle
import player
import car
import scoreboard

colors = ["red", "green", "black", "yellow", "blue", "orange", "violet", "cyan", "lime"]
level_diff_mult = 1
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = player.Player()
screen.onkey(player.move, "Up")
cars = []
levelBoard = scoreboard.Scoreboard()
level = 1
timeMultiplyer = 1
gameOver = turtle.Turtle()
gameOver.goto(0, 0)
gameOver.hideturtle()
gameOver.color("black")


def genCars():
    chance = random.randint(1,6)
    if chance == 1:
        car1 = car.Car()
        car1.color(colors[random.randint(0, len(colors) - 1)])
        cars.append(car1)


game_ON = True
while game_ON:
    time.sleep(0.1 * timeMultiplyer)
    screen.update()
    genCars()
    if player.ycor() > 290:
        player.goto(player.xcor(), -270)
        level += 1
        levelBoard.writeLevel(level)
        timeMultiplyer *= 0.65
    for cart in cars:
        cart.move()
        if player.distance(cart) < 13:
            gameOver.write(arg="Game Over", font=("Arial", 13, "normal"))
            game_ON = False

screen.exitonclick()
