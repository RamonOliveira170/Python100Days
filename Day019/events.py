import turtle

michelangelo = turtle.Turtle()
michelangelo.shape("turtle")
myscreen = turtle.Screen()

def move_forward():
    michelangelo.forward(20)

def turn_left():
    michelangelo.left(20)

def turn_right():
    michelangelo.right(20)

def move_back():
    michelangelo.back(20)

def clear():
    michelangelo.clear()

def home():
    michelangelo.penup()
    michelangelo.home()
    michelangelo.pendown()

myscreen.listen()
myscreen.onkey(key="w", fun=move_forward)
myscreen.onkey(key="a", fun=turn_left)
myscreen.onkey(key="d", fun=turn_right)
myscreen.onkey(key="s", fun=move_back)
myscreen.onkey(key="c", fun=clear)
myscreen.onkey(key="space", fun=home)
myscreen.exitonclick()

