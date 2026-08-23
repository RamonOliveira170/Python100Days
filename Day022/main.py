import turtle
import time
import paddle
import ball
import scoreboard

my_screen = turtle.Screen()
my_screen.setup(800, 600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

ball = ball.Ball()
right_paddle = paddle.Paddle((360, 0))
left_paddle = paddle.Paddle((-360, 0))
scoreboard = scoreboard.Scoreboard()

my_screen.listen()
my_screen.onkey(left_paddle.up,"w" )
my_screen.onkey(left_paddle.down, "s")
my_screen.onkey(right_paddle.up,"Up" )
my_screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(right_paddle) < 30 and ball.xcor() > 330 or ball.distance(left_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position("left")
        scoreboard.increase_score("left")

    if ball.xcor() < -380:
        ball.reset_position("right")
        scoreboard.increase_score("right")

my_screen.exitonclick()
