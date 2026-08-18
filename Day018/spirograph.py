import turtle
import random
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("blue")
leonardo.speed(0)

for _ in range(72):
    leonardo.circle(100)
    leonardo.left(5)
    leonardo.color(random_color())


my_screen = turtle.Screen()
my_screen.exitonclick()