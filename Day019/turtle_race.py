import turtle
import random

is_race_on = False
colors = ["blue", "red", "yellow", "green", "purple", "orange"]
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []

myscreen = turtle.Screen()
myscreen.setup(width=500, height=400)

user_bet = myscreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-240, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You lose, the winner was the {winning_color} turtle")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

myscreen.exitonclick()
