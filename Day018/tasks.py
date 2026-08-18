from turtle import Screen, Turtle
import random

michelangelo = Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")

for _ in range(4):
    michelangelo.forward(100)
    donatello.forward(100)

    michelangelo.right(90)
    donatello.left(90)

start = michelangelo.pos()

while True:
    break
    michelangelo.forward(200)
    michelangelo.left(170)
    if michelangelo.distance(start) < 1:
        break


donatello.left(45)

for _ in range(10):
    donatello.forward(10)
    donatello.penup()
    donatello.forward(10)
    donatello.pendown()

donatello.home()
donatello.clear()
michelangelo.clear()

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "pink"]

def draw_shape(sides):
    shape = 360 / sides
    for _ in range(sides):
        michelangelo.forward(100)
        michelangelo.right(shape)
        michelangelo.color(random.choice(colors))

for shape in range(3, 11):
    draw_shape(shape)

def random_direction():
    direction = random.randint(0, 1)
    if direction == 0:
        donatello.left(random.randint(0, 360))
    else:
        donatello.right(random.randint(0, 360))

for _ in range(20):
    donatello.forward(50)
    random_direction()

screen = Screen()
screen.exitonclick()
