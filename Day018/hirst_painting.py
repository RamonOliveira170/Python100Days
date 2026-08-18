import turtle
from extract_color import color_list
import random
turtle.colormode(255)

michelangelo = turtle.Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")
michelangelo.penup()
michelangelo.setheading(225)
michelangelo.forward(300)
michelangelo.setheading(0)
michelangelo.speed(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    michelangelo.dot(20, random.choice(color_list))
    michelangelo.forward(50)

    if dot_count % 10 == 0:
        michelangelo.setheading(90)
        michelangelo.forward(50)
        michelangelo.setheading(180)
        michelangelo.forward(500)
        michelangelo.setheading(0)

michelangelo.hideturtle()
my_screen = turtle.Screen()
my_screen.exitonclick()
