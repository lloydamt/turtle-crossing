from turtle import Screen
from player import Player
import time
from car_manager import Car_Manager
from level import Level
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car_Manager()
level = Level()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(car_manager.speed)
    for car in car_manager.cars:
        car.move()
        if car.xcor() < -300:
            car.create_car()

        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()

    if player.ycor() > 280:
        player.refresh()
        car_manager.restart()
        level.level_up()







screen.exitonclick()