import turtle
import random
MOVE_DISTANCE = 20

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(3, 1)

    def up(self):
        if self.ycor() + 20 > 260:
            pass
        else:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() - 20 < -260:
            pass
        else:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
