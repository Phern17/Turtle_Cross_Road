import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

Y_FINISH_LINE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move(scoreboard.level - 1, game_is_on)

    # if turtle collides with any car
    for item in car.car_batch:
        if player.distance(item) < 22:
            scoreboard.game_over()
            game_is_on = False

    # if turtle collides with finish line
    if player.ycor() > Y_FINISH_LINE:
        scoreboard.next_level()
        player.starting_point()
        car.next_level()

screen.exitonclick()
