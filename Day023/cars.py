import random
import turtle
turtle.colormode(255)
STARTING_MOVE_SPEED = 5
MOVE_INCREMENT = 10

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

class Cars():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_SPEED

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-240, 240))
            new_car.color(random_color())
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
