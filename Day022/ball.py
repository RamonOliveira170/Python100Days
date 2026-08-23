import turtle
import random
RANDOM_DIRECTION = random.choice([10, -10])

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = RANDOM_DIRECTION
        self.y_move = RANDOM_DIRECTION
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self, direction):
        self.goto(0, 0)
        self.move_speed = 0.1
        if direction == "left":
            self.y_move = random.choice([10, -10])
            self.bounce_x()
        elif direction == "right":
            self.y_move = random.choice([10, -10])
            self.bounce_x()
