import turtle
import turtle_crossing
import time
import cars
import scoreboard

my_screen = turtle.Screen()
my_screen.tracer(0)

player = turtle_crossing.Turtle_Crossing()

my_screen.setup(600, 600)
my_screen.bgcolor("white")
my_screen.listen()
my_screen.onkey(player.move_up, "w")
my_screen.onkey(player.move_down, "s")

scoreboard = scoreboard.Scoreboard()
car_manager = cars.Cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()

my_screen.exitonclick()
