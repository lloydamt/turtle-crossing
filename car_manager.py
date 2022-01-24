from turtle import Turtle
import random
from car import Car


class Car_Manager():
    def __init__(self):
        self.cars = []
        self.speed = 0.1
        self.cars_on_screen = random.randint(10, 15)
        self.create_multiple(self.cars_on_screen)



    def create_multiple(self, cars_on_screen):
        for _ in range(cars_on_screen):
            car = Car()
            self.cars.append(car)

    def restart(self):
        extra_cars = random.randint(0, 5)
        self.create_multiple(extra_cars)
        self.speed *= 0.7





