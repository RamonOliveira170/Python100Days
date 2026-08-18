import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

raphael = turtle.Turtle()
raphael.shape("turtle")
raphael.color("red")
raphael.pensize(5)
raphael.speed(10)
colours = ["blue", "red", "yellow", "green", "purple", "black"]
directions = [0, 90, 180, 270]

for _ in range(200):
    raphael.forward(30)
    raphael.setheading(random.choice(directions))
    #raphael.color(random.choice(colours))
    raphael.color(random_color())

my_screen = turtle.Screen()
my_screen.exitonclick()
