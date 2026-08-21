import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = turtle.Screen()
my_screen.setup(600, 600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

my_screen.exitonclick()
