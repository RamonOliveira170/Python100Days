import turtle
from snake import Snake
import time

my_screen = turtle.Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up,"Up" )
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right,"Right" )
my_screen.onkey(snake.left,"Left" )

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

my_screen.exitonclick()
